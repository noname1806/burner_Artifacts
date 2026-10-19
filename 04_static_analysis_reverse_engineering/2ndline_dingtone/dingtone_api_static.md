# 2ndLine / Dingtone (`me.number.app.im`) — STATIC API surface

Source: static string analysis of the base APK, **v2.6.1** (APKPure XAPK,
`me.number.app.im`, 5 dex, ~396k strings), downloaded 2026-07-28 because the app
was no longer installed on emulator-5554 and we never pulled it during the live
session. Method: raw ASCII-string scan of `classes*.dex` for URL hosts, REST path
fragments, and the socket command enum (`extract_apis.py` in `dingtone_apk/`).
Retrofit/OkHttp routes live as literal strings, so this recovers the **declared**
surface (superset of the 6 endpoints seen in the runtime Frida window).

Cross-check: the runtime capture (see `2ndline_findings.md`) observed
`dt-apigatewayv2.dt-pn1.com` serving `/config/client`, `/plan/...`,
`/plan/subscription/getBurnInfo`, `/telosWeb/number/ad/sub/detail`, and
`dt-apigateway-log.dt-pn1.com` serving `/report/log/async`. All of those reappear
in the static set, so provenance is consistent; static adds the rest.

## Architecture (the important finding)

Dingtone splits its backend into **two transports**:

1. **HTTP/REST gateways** — account/number/billing/config business logic.
   Hosts seen statically:
   - `dt-apigatewayv2.dt-pn1.com`  (main REST gateway — runtime-confirmed)
   - `apigateway.dt-dn1.com:9230`  (config/log gateway; **cleartext `http://`** on port 9230)
   - `gateway.funblocks.io`        (alternate config host: `/config/client`)
   - `dt-apigateway-log.dt-pn1.com` (telemetry: `/report/log/async`)
2. **Proprietary socket/binary protocol** — messaging, SMS, calls, login,
   registration, contacts, groups, presence. Carried over the Dingtone edge PoP
   servers, NOT REST: `*.dingtone.co` (`usca10`, `usva00`, `sg60`, `jptyo50`,
   `au80`, `ie70`, `brsp20`, `cn30`.dingtone.co) and `es0/es1.gsedge.net`.
   Commands are the `DTRESTCALL_TYPE_*` enum (46 values) + `MESSAGE_TYPE_*` /
   `MSG_TYPE_*` push constants.

=> **Confirms the earlier caveat: message/SMS/call *content* is not retrievable
over REST** — it is a socket protocol. The REST gateway exposes account, number
lifecycle, burn state, billing, and config. This is a genuine static-analysis
finding, not an inference.

Auth (runtime-confirmed): REST endpoints authenticate by `userId` + `deviceId`
**query parameters only**, no bearer/Authorization header. Both are device-resident.

---

## REST endpoints (static)

### Config / auth-switch
- `GET /config/client`                      — per-client/account config (also on dt-dn1 + funblocks)
- `/auth/grayswitch`                         — feature/gray-release flags

### Number lifecycle (private second number)
- `/number/query/list`                       — list numbers on the account
- `/number/areacode/getAreaCode`             — area-code catalog
- `/number/lock` , `/number/unlock`          — reserve / release a number during purchase
- `/pstn/getRandomNumber`                    — offered numbers pool
- `/pstn/getAreaCode`                         — PSTN area codes
- `/pstn/getNumberCountries`                 — country availability
- `/pstn/getNumberPrice` , `/pstn/v2/getNumberPrice`  — pricing
- `/pstn/phone/query/regcredit`              — registration credit check
- `/pstn/share/getPrivateNumber`             — private-number provisioning
- `/pstn/share/PayPortoutCredits`            — number port-out payment
- `/pstn/share/orderVoiceMail`               — order voicemail service
- `/pstn/feedback`                            — number feedback

### Plans / subscriptions / **burn**
- `/plan/query/number/getSubList`            — number subscriptions (runtime-confirmed)
- `/plan/query/upgrade/product`              — upgrade products (runtime-confirmed)
- `/plan/query/productinfos`                 — product catalog
- `/plan/query/open/freeTry`                 — free-trial eligibility
- `/plan/subscription/getBurnInfo`           — **burn-state** of a line (runtime-confirmed)
- `/telosWeb/subscription/burn`              — **execute burn** on a subscription/number
- `/telosWeb/cancel/subscribe/info`          — cancellation info
- `/telosWeb/number/ad/sub/detail`           — ad-supported sub detail (runtime-confirmed)

### Billing / payments
- `/billing/gpiab/createOrder`               — Google Play in-app-billing order create
- `/billing/gpiab/deliver`                   — deliver purchased entitlement
- `/billing/user/checkIn/v3`                 — daily check-in
- `/billing/user/getCheckInHst` , `/billing/user/getCheckInLvl/v3`
- `/dtpay/api/v1/trade/create` , `/trade/status` , `/trade/verify`   — Dingtone-pay trades
- `/dtpay/subscription/v2/deliver` , `/dtpay/subscription/v2/restore`
- `/v2/purchase`                              — generic purchase

### Rewards / social / support
- `/point/summary` , `/point/gradeinfo`      — loyalty points
- `/lottery/userTaskStatus`                  — task/lottery status
- `/invite/config` , `/gwebsvr/support/invite` — invite flow
- `/campaign/ad` , `/campaign/localpush`     — campaigns / local push

### Telemetry
- `POST /report/log/async`                   — async client logging (runtime-confirmed)
- `/log`                                      — logging

---

## Socket command family (`DTRESTCALL_TYPE_*`, 46 values) — NOT REST

Messaging/identity/telephony live here (over `*.dingtone.co`). Forensically
relevant commands:

- Identity/session: `LOGIN`, `LOGOUT_CMD`, `REGISTER`, `REGISTER_DEVICE`,
  `ACTIVATE_DEVICE`, `REGISTER_EMAIL`, `ACTIVATE_EMAIL`, `ACTIVATION`,
  `DEACTVIE_SELF`, `DEACTVIE_OTHERS`, `GET_DEVICELIST`, `UPLOAD_SIM_INFO`
- Messaging: `MESSAGE`, `MESSAGE_CHAT`
- SMS: `GET_SMS_GATEWAY`  (maps to the on-device `sms_gateway_cache_ex` table)
- Voice: `ORDER_VOICEMAIL`
- Contacts/social: `SEARCH_USER(S)`, `DELETE_CONTACT`, `REQ_FREIENDLIST` [sic],
  `QUERY_PUBLIC_ID`, `SET_PRESENCE`, `POST_MYPOSITION`, `BLOCK_SEARCH_ME`
- Groups: `GROUP_ADD_USER`, `GROUP_DEL_USER`, `GROUP_ADD_CMD`, `GROUP_DEL_CMD`,
  `GROUP_REST_USER`, `GROUP_REST_CMD`, `QUIT_GROUP`
- Money/subs: `GET_MY_BALANCE`, `QUERY_RATE_INFO`, `GIFT_SEND`, `GP_SUBS_STATUS`,
  `VERIFY_GP_SUBS`, `GP_VERIFY_RETRY`, `GET_COUPON_LIST`, `REWARD_AD`
- Invite: `GET_INVITE_LINK`, `SUPPORT_INVITE`, `SEND_TO_INVITEE`, `SHARE_SOCIAL`
- Generic: `COMMON_CMD`, `COMMON_RESTCALL`

## Ethics note
Same disclosure question as the Burner/Hushed endpoint table: these are
undocumented backend routes. If Table 5 endpoints are published, decide whether to
publish the Dingtone set too; consider listing route *categories* + the burn-state
endpoint (the forensically load-bearing one) rather than the full billing/pay list.
