# 2ndLine ("2nd Line", me.number.app.im — Dingtone engine, v2.6.2)

**Naming note for the paper:** the installed app labelled "2nd Line" is package
`me.number.app.im`, built on the **Dingtone** engine (launcher activity
`MainDingtone`; DB `Dingtone.db`). This is distinct from TextNow's 2ndLine
(`com.enflick.android.tn2ndline`). The manuscript must state exactly which "2ndLine"
was analysed; our results are for the Dingtone-based app. Active lab line:
(225) 300-6923, valid until 2026-07-20; userId `215506997933319`.

## TLS interception DEFEATED (paper had only "partial")

Using the Frida BoringSSL hook (`tools/net_capture.py`, plaintext at
`SSL_read`/`SSL_write` in libjavacrypto.so/libssl.so), full plaintext was recovered
despite pinning — upgrading the paper's "partially feasible" to complete visibility.

### Undocumented cloud API surface (host `*.dt-pn1.com`)

Gateway `dt-apigatewayv2.dt-pn1.com`:
- `GET /config/client?...&userId=215506997933319`
- `GET /plan/query/number/getSubList?userId=…&deviceId=And.<hex>.number`
- `GET /plan/query/upgrade/product?userId=…&deviceId=…`
- `GET /plan/subscription/getBurnInfo?userId=215506997933319`   ← burn-state endpoint
- `GET /telosWeb/number/ad/sub/detail?userId=…&deviceId=…`
Logging gateway `dt-apigateway-log.dt-pn1.com`: `POST /report/log/async`.

### Key forensic finding — weak cloud auth (no bearer token)

The Dingtone cloud endpoints authenticate via **`userId` + `deviceId` query
parameters only** — no Authorization/bearer header was observed in any request. Both
identifiers are recoverable from the device (`userId 215506997933319`, `deviceId
And.80140f8be7e8b17260028dbd893359e2.number`). Token-scoped cloud acquisition is
therefore **even more trivial than Burner/Hushed** (no token minting/refresh needed):
possession of the device-resident userId+deviceId suffices to query the account's
cloud API. (Real-time messaging likely rides a Dingtone socket channel, not REST;
message-content REST endpoints did not appear in this window and are follow-up work.)

## On-device artifacts (logical acquisition) — unencrypted `Dingtone.db` (55 tables)

No encryption (contrast Hushed). Forensically relevant tables:
- `dt_message` (content, senderId, msgId, conversationId, msgState) — SMS/chat bodies
- `dt_conversation`, `last_access_conversation_table` — threads
- `history_call`, `history_call_participant`, `pstn_call_records` — call logs
- `pstn_call_recordings`, `pstn_call_recording_anchors` (recordingId, targetPhoneNum,
  filePath, signLifeTime) — **call-recording references (cloud-retrievable)**
- `sms_gateway_cache_ex` (targetPhoneNumber, privatePhoneNumber, gateway ids)
- `phoneNumberInfo`, `dupcd_phonenumber`, `BlockedInboundSms` (content, fromNumber)
Other DBs: area_code.db, dt_event.db, billing.db, ads.db, superofferwall.db, gif.db.

## Table 2 cells (Dingtone 2ndLine)

- Device-resident SQLite DBs: ● ; Database encrypted at rest: ○ (plaintext)
- Undocumented API observed: ● (dt-pn1.com gateway mapped)
- Cloud data acquisition: ● — and auth is weaker (device-resident userId+deviceId,
  no bearer token)
- Method: TLS interception ● **feasible via Frida SSL hook** (was △ partial in prior draft)
