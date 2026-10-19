# 4.3 2ndLine (Dingtone): findings — paper-ready subsection

Written to match the 4.1 (Burner) / 4.2 (Hushed) style; plain, specific phrasing.

---

## 4.3 2ndLine (Dingtone): findings

The application labelled "2nd Line" in our sample is package `me.number.app.im`,
built on the Dingtone calling/messaging engine (launcher activity `MainDingtone`,
primary store `Dingtone.db`); it is distinct from TextNow's similarly named
`com.enflick.android.tn2ndline`, and we report results for the Dingtone-based app
that our market survey returned. Unlike Hushed, 2ndLine stores application state in
an **unencrypted** SQLite database, and unlike TextMe/TextFree it runs normally under
instrumentation, so both device and network layers were fully accessible.

**On-device artifacts.** Logical acquisition of `/data/data/me.number.app.im/`
recovered `Dingtone.db` (55 tables) with no encryption at rest. Message bodies and
thread state persist in `dt_message` (content, `senderId`, `msgId`, `conversationId`,
`msgState`) and `dt_conversation`; call activity persists in `history_call`,
`history_call_participant`, and `pstn_call_records`. Notably, `pstn_call_recordings`
and `pstn_call_recording_anchors` retain references to server-side call recordings
(`recordingId`, `targetPhoneNum`, `filePath`, `signLifeTime`), and
`sms_gateway_cache_ex` links the private (second) number to target numbers and the
SMS gateway used. Auxiliary databases (`area_code.db`, `dt_event.db`, `billing.db`,
`ads.db`) provide supporting context.

**Network and cloud interface.** TextMe-style pinning prevented proxy interception in
the prior study; here we obtained full plaintext by hooking the TLS primitives
(`SSL_read`/`SSL_write`) beneath the pinning layer, without patching the APK
(Section 3). Authenticated traffic resolves to a Dingtone API gateway,
`dt-apigatewayv2.dt-pn1.com`, exposing endpoints for client configuration
(`/config/client`), the account's number list (`/plan/query/number/getSubList`),
subscription and upgrade state (`/plan/query/upgrade/product`,
`/telosWeb/number/ad/sub/detail`), and line burn state
(`/plan/subscription/getBurnInfo`); a second host (`dt-apigateway-log.dt-pn1.com`)
receives asynchronous logging.

**Authentication observation (forensically relevant).** In all observed requests the
account was identified by a `userId` and a `deviceId` supplied as URL query
parameters, with no bearer token or `Authorization` header. Both identifiers are
recoverable from the device (`userId` and the `deviceId` string
`And.<hex>.number`). Consequently, cloud queries for a seized account require only
device-resident identifiers — a weaker binding than the refresh-token exchange used by
Burner and Hushed, and one that makes token-scoped collection correspondingly simpler.
Real-time message delivery appears to use a separate Dingtone socket channel rather
than these REST endpoints; enumerating message-content endpoints on that channel is
left as follow-up work, and we do not claim to have mapped the full API surface.

**Summary.** 2ndLine (Dingtone) contributes the plaintext-storage, weak-cloud-binding
point of the comparison: message, call, and recording references sit unencrypted on
the device, and the cloud account is addressable using only device-resident
identifiers.
