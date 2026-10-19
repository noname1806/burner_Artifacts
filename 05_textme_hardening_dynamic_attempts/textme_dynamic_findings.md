# TextMe 3.55.0 — dynamic analysis + on-device storage (2026-07-24)

Environment built this session: Android Studio AVD **TextMe_API33** (google_apis/x86_64,
Android 13 / API 33; created because TextMe minSdk=32 blocks the API-31 lab emulator),
booted `-writable-system`, `adb root` + remount, **mitmproxy CA installed into the system
trust store** (`/system/etc/security/cacerts/c8750f0d.0`), TextMe installed via
`install-multiple` (base + config.x86_64 + xxhdpi + en), emulator routed through host
`mitmdump` (10.0.2.2:8080). Evidence in `captures/textme_api33/` (textme.flows, mitm.log,
drive.log, pairip_bypass.js, license_dialog.png).

## Result 1 — TLS interception SUCCEEDS (no certificate pinning: confirmed dynamically)
On the first, uninstrumented launch the app reached its network layer and mitmproxy
decrypted its HTTPS in cleartext, **confirming the static finding that TextMe does not pin**.
Captured to the real backend `api.textme-app.com`:

- `POST /api/register-device/` — request headers include a full device fingerprint and a
  **per-request signature**: `X-T: <64-hex SHA-256>`, `X-TIMESTAMP`, `X-CLIENT-VERSION: 3.55.0`,
  `X-BUNDLE-ID: com.textmeinc.textme2.android`, `X-DEVICE-*` (manufacturer/brand/model/sdk/
  build-id), `X-CARRIER: T-Mobile; cc=US; mnc=260; mcc=310`, `X-TZ: America/Chicago`,
  `X-CONNECTIVITY: WIFI`. Body: `device_uid`, `device_token` (FCM push token),
  `android_id`, `google_ad_id`, `device_model`, `carrier=...`.
- `POST /api/app-settings/` — same header scheme.
- **Server edge (`Server: awselb/2.0`) returned HTTP 403** to both. Cause undetermined from
  one run (candidates: AWS WAF rule, the `X-T` signature check, or attestation) — NOT
  attributed to App Check (no `X-Firebase-AppCheck` header was present; the App Check
  endpoint was never called in the captured window). Do not overclaim.
- Also observed: `firebaseinstallations.googleapis.com/.../go-text.me:textme-gplus`,
  firebase remote-config (fireperf), app-measurement, crashlytics settings, AppsFlyer,
  c2dm/register3.

Interpretation: the interception barrier for TextMe is **not** TLS pinning. A system-store
MITM CA reads its API traffic as soon as the app runs.

## Result 2 — PairIP defeats dynamic instrumentation (login unreachable)
Without Frida the app runs to the PairIP **license gate** and exits gracefully:
`LicenseClient` binds `com.android.vending` licensing service →
`LicenseCheckException: Licensing service could not process request` (sideloaded APK is not
a Play-licensed purchase; `BIND_EXPRESS_INTEGRITY_SERVICE` also "not found" on this image)
→ `LicenseActivity` shows *"Something went wrong — Check that Google Play is enabled…"*
(screenshot `license_dialog.png`) → `System.exit`.

Attempted bypass (`pairip_bypass.js`: no-op `LicenseClient.handleError` + block
`LicenseActivity.exitApp`/`System.exit`/`Runtime.exit`/`Process.killProcess`). **Defeated:**
the moment Frida attached, `libpairipcore.so` crashed the process before the Java hooks even
installed — `Fatal signal 11 (SIGSEGV), code 2 (SEGV_ACCERR), fault addr 0x…7f7000, #00
…libpairipcore.so (offset 0x14bc000)`, process uptime 2s. This is the **same native
SIGSEGV signature as the v3.54.0 crash** → PairIP's anti-instrumentation tamper-response,
not a license or a TLS issue. (After the Frida session, relaunches kept SIGSEGV-ing in
libpairipcore.so; reboot needed to clear the state.) Consequence: no account can be
provisioned under instrumentation on the emulator, so **logged-in / post-auth traffic is
not reachable** here.

## Result 3 — On-device storage (logical acquisition of /data/data/com.textmeinc.textme)
State = **pre-login** (no account provisioned, per Result 2).

- **All databases are plaintext `SQLite format 3` — NO SQLCipher / no on-device encryption.**
  (Contrast Hushed, which is SQLCipher-encrypted.) Present DBs are **all third-party
  analytics/ad SDKs**: Batch (`LocalCampaignsSQLTracker.db`, `ba_tr.db`), `mixpanel`,
  Firebase `google_app_measurement_local.db`, `com.google.android.datatransport.events`.
- **No first-party TextMe messaging database exists yet** (no conversations/messages/
  contacts store) — it is created only after account/number provisioning.
- **Cleartext first-party identifiers already persisted pre-login (all recoverable):**
  - `shared_prefs/device_id.xml.xml` → `device_id = 6503a3ca-8867-37da-83c6-f402a5bca105`
    (== the `device_uid` sent to `api.textme-app.com`).
  - `shared_prefs/FCM.xml` → full FCM push registration token.
  - `files/PersistedInstallation.*.json` → Firebase Installation ID + `AuthToken` (JWT) +
    `RefreshToken`, in the clear.
  - `shared_prefs/textme_prefs.xml` → `first_launch_timestamp`.
  - Jetpack DataStore present (`files/datastore/`) but pre-auth holds only Firebase session data.

### Does TextMe delete permanently, or is data recoverable?
**Not testable on the emulator** for messages/contacts: PairIP blocks account provisioning,
so there is no user content to create/delete/carve. What IS established: TextMe's on-device
store is **unencrypted plaintext SQLite**, so once messaging data is written post-login it
would sit in the clear — making both recovery and deletion-residue carving **feasible in
principle** (unlike Hushed's SQLCipher). Demonstrating the actual delete-persistence
behavior requires a **Play-licensed install on non-instrumented arm64/API≥32 hardware**
(the lab S10+ runs Android 12 / API 31 and does not qualify), where PairIP's license check passes and no Frida is attached.

## Paper impact (Table 2 / §4.4)
- Device-storage encryption: TextMe = **plaintext SQLite (no SQLCipher)** — a concrete
  comparative point vs Hushed.
- "Undocumented API observed": now **● observed live** — `api.textme-app.com`
  `/api/register-device/`, `/api/app-settings/`, with signed-request scheme (`X-T`). Add to
  Appendix Table 5.
- Message deletion-persistence & cloud acquisition: remain **△ not-feasible**, named
  mechanism = **PairIP native anti-instrumentation (SIGSEGV) + Play license gate blocking
  account provisioning on the emulator** (distinct from cert pinning; distinct from ○ absent).
