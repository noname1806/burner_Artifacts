# TextMe — findings

Reviewer ask (IMF R2): where interception fails due to genuine hardening (PairIP /
Play Integrity), *name the mechanism per app and report it as a finding* rather than
leaving a blank. This is that characterization for TextMe.

Two data points:
- **v3.54.0** — installed on the rooted x86_64 API-31 emulator, dynamic launch attempted
  (crash observed). Historical lab note, retained below.
- **v3.55.0** — APKPure universal XAPK, decompiled 2026-07-24 (`textMeapk/`). Full static
  characterization; **corrects two claims from the earlier draft** (backend host and
  "certificate pinning"). Package `com.textmeinc.textme`, versionCode `355000004`.

---

## v3.55.0 static analysis (evidence-backed, 2026-07-24)

Tools: `aapt` dump (segfaulted on the PairIP-manipulated manifest — a finding in itself),
`apktool` (failed on PairIP "sparsely packed" resource table), **androguard 3.4.0a1**
(parsed manifest + binary XML resources successfully), JADX source tree.

### App / SDK profile
- `minSdkVersion = 32`, `targetSdkVersion = 35`, `compileSdk = 36`.
  → **Will not install on the API-31 (Android 12) emulator** — same barrier class as
  TextFree (`INSTALL_FAILED_OLDER_SDK`). Needs API ≥ 32.
- `native-code: arm64-v8a, armeabi-v7a, x86, x86_64` — **all four ABIs present**, and
  `libpairipcore.so` + `liblinphone.so` ship for **x86_64 too**. (So the v3.54.0 x86_64
  crash was *not* a missing-library issue; corrects the earlier "arm64-only" impression.)
- **VoIP engine = Linphone/mediastreamer**: `liblinphone.so`, `libmediastreamer2.so`,
  `libortp.so`, `libsrtp2.so`, `libmswebrtc.so`, `libbctoolbox.so`, `libmsaaudio.so`,
  `libmssilk.so`. Telephony perms `MANAGE_OWN_CALLS`, `FOREGROUND_SERVICE_PHONE_CALL`,
  `FOREGROUND_SERVICE_MICROPHONE`, `RECORD_AUDIO` → SIP-based calling via ConnectionService.
- Heavy ad/attribution stack: AppLovin, Vungle, BidMachine, PubNative/HyBid, Verve/NextGen,
  Smaato, MobileFuse, Giphy; AppsFlyer; Firebase Crashlytics.

### Hardening — PairIP (full code-virtualization, not just licensing)
- **`android:name="com.pairip.application.Application"`** is the app's Application class —
  PairIP owns process startup. `com.pairip.licensecheck.LicenseActivity` also registered.
- PairIP class set in DEX: `VMRunner` (native `Object executeVM(byte[] vmCode, Object[])`
  in `libpairipcore.so`), `VmDecryptor`, `SignatureCheck` (APK-signature / anti-repackaging
  check), `StartupLauncher`, `InitContextProvider`, `licensecheck/{LicenseClient,
  LicenseActivity, LicenseContentProvider, LicenseResponseHelper, ...}`.
- **~22 extension-less, randomly-named `assets/` blobs** (e.g. `assets/26Aniqm78pgwTP1c`)
  = the encrypted VM bytecode that `VMRunner.executeVM` runs. 20 `classes*.dex`. This is
  PairIP **method virtualization**: real logic is lifted into a custom bytecode executed
  inside the native VM → static devirtualization is research-grade, out of scope.
- **App is NOT debuggable** (`android:debuggable` unset → false), so the NSC
  `debug-overrides` user-CA trust path (below) does **not** apply to the release build.

### Second integrity layer — Firebase App Check via Play Integrity
- Manifest registers `FirebaseAppCheckPlayIntegrityRegistrar` (+ `FirebaseAppCheckRegistrar`,
  `...KtxRegistrar`). App Check is **backed by the Play Integrity API** → server-side
  attestation that the request comes from a genuine, Play-installed, unmodified app on a
  non-compromised device. This gates the *server*, and would also resist off-device token
  replay; it does not by itself block on-device TLS interception.

### Network posture — **NO certificate pinning** (corrects prior "cert pinning" claim)
`res/xml/network_security_config.xml` (recovered via androguard AXML; JADX/aapt failed on it):
```
<base-config cleartextTrafficPermitted="false"/>          <!-- no trust-anchors override, no pin-set -->
<debug-overrides> trust-anchors: system + user </debug-overrides>   <!-- debug builds only; app not debuggable -->
<domain-config cleartextTrafficPermitted="true">
   go-text.me, textme-store-assets.s3.amazonaws.com,
   textme-www-assets.s3.amazonaws.com, localhost, 127.0.0.1
</domain-config>
```
- **There is no `<pin-set>` anywhere**, and app code constructs **no OkHttp
  `CertificatePinner`** (only OkHttp's own library classes reference the type; no
  `.certificatePinner(...)` / `CertificatePinner.Builder().add(...)` in first-party code).
- Net effect: API traffic is ordinary TLS validated against the **system trust store**.
  A CA installed in the **system** store (the lab's Magisk system-CA + HTTP Toolkit setup)
  **would intercept** `api.textme-app.com` — *if the app can be launched*. The interception
  barrier is therefore **not pinning**; it is (1) minSdk-32 install gate on the API-31
  emulator and (2) PairIP integrity/virtualization + Play-Integrity App Check on a
  rooted/tampered environment.

### Backend map (recovered from `res/values/strings.xml` — **not** `web.textmeup.com`)
| Purpose | Host |
|---|---|
| Production API | `api.textme-app.com` (HTTPS/443) |
| "ECR" API | `api-ecr.textme-app.com` |
| Staged rollout | `srp.textme-app.com` |
| QA | `qa.textme-app.com`, `qa-ecr.textme-app.com`, `qa-py3.textme-app.com` |
| Dev | aliased to production hostname |
| Firebase project | `go-text.me:textme-gplus` |
| Firebase RTDB | `https://go-text-me-textme-gplus.firebaseio.com` |
| Firebase app id / sender | `1:137745609594:android:efc263516c4d5567` / `137745609594` |
| Firebase Web API key (embedded) | `AIzaSyDI...[REDACTED]` |
| Assets | `textme-{www,store}-assets.s3.amazonaws.com` |
| Support | `go-text.me` (Zendesk) |

(`go-text.me` is the brand / Firebase-project / support domain — the prior draft's
`web.textmeup.com` was the wrong first-party API host. The `qa-py3` name hints the
backend migrated to a Python-3 stack.)

---

## v3.54.0 dynamic note (historical lab data — retained)

- On launch (`…SplashActivity`) the process **deterministically crashed** before UI:
  `Fatal signal 11 (SIGSEGV), code 2 (SEGV_ACCERR)`, top frame
  `…/split_config.x86_64.apk!libpairipcore.so` (+0x78e14), identical fault address across
  repeated launches.
- Root-detection ruled out as sole cause: Magisk present but **Zygisk disabled**; adding
  the package to the Magisk DenyList did not change the crash → consistent with a PairIP
  native-VM failure on the x86_64 emulator, not a simple root check.
- Given v3.55.0's minSdk-32 gate, this crash path is now moot on API-31 anyway — the app
  no longer installs there.

---

## Path forward (future work / physical device)
- A physical **arm64 / API ≥ 32** device is the right target (not the Samsung S10+ SM-G975U1, which runs Android 12 / API 31):
  the app installs, and since there is **no cert pinning**, a system-store MITM CA should
  capture `api.textme-app.com` traffic — **provided** PairIP's integrity/signature check
  and Play-Integrity App Check tolerate the environment (unrooted device preferred; root
  hiding may still trip PairIP).
- PairIP VM devirtualization is out of scope.
- Static analysis fully characterizes endpoints/manifest/permissions/hardening (this file).

## Table 2 cell
TextMe "Undocumented API observed" / "Cloud data acquisition" = **△ not feasible in this
study**, named mechanism = **PairIP code-virtualization + Play-Integrity App Check +
minSdk-32 install gate** (explicitly *not* certificate pinning, and distinct from ○
observed-absent).
