# TextFree — findings (com.pinger.textfree, "Text Free: Second Phone Number", Pinger Inc, 50M+)

TextFree is the fully-hardened endpoint of the 5-app spectrum. On the study emulator it
could not be run; we characterize it statically and name every barrier precisely
(reviewer ask: name the mechanism, don't leave a blank).

## Install barrier (emulator, API 31) — plain and documented

- Google Play shows *"This app is available only for your other devices"* for the
  emulator, while it installed TextMe, Hushed, and 2ndLine — i.e. the exclusion is
  TextFree-specific.
- Direct sideload of the AAB split set (`adb install-multiple`) gives the concrete
  cause: **`INSTALL_FAILED_OLDER_SDK: Requires newer sdk version #32 (current version
  is #31)`**. TextFree requires **minSdk 32 (Android 12L)**; the emulator is API 31.
- The distributed bundle ships an **arm64-v8a** split only (no x86_64), so it is also
  ABI-incompatible with the x86_64 emulator.
- **We therefore do not over-attribute the store block to attestation:** the
  proximate, verified cause is minSdk/ABI. (Attestation is a *runtime* barrier, below.)

## Static hardening profile — heaviest in the sample

From `base.apk` DEX (`apk/textfree_base.apk`):
- **PairIP** VM code protection: `com/pairip` ×48, `com.pairip.VMRunner` ×12,
  `licensecheck` ×31.
- **Play Integrity + DroidGuard** attestation: `PlayIntegrity` ×36, `integrity` ×155,
  `DroidGuard` ×1.
- **Firebase App Check** (`firebaseappcheck.googleapis.com`).
- **FingerprintJS** commercial device fingerprinting / anti-fraud (`api.fpjs.io`,
  `eu.api.fpjs.io`, `ap.api.fpjs.io`).
- Extensive ad-tech / data-broker footprint (Smaato, InMobi, Rubicon, Taboola, Vungle,
  AppLovin, Moloco, Rokt, OpenX, BidMachine, LiveRamp `rlcdn.com`, Amazon `a2z`
  advertising) — relevant to the app's data-sharing surface.

## Dynamic-analysis path (future work)

Running TextFree requires an **API ≥ 32, arm64** environment:
- not the physical Samsung S10+ (SM-G975U1): it runs Android 12 (API 31), below minSdk 32;
- a fresh rooted API ≥ 32 emulator.
On such a device or emulator, TextFree would still face **PairIP + Play Integrity/DroidGuard + App Check +
FingerprintJS** at runtime, which on a rooted/instrumented device is expected to block
launch or attest-fail (cf. TextMe's PairIP SIGSEGV). Dynamic acquisition and API
mapping are thus bounded and reported, not claimed.

## Longitudinal note

The prior draft cited TextFree as PairIP + Play-Integrity attestation. The current
release confirms this and adds **Firebase App Check + FingerprintJS**, and raises the
floor to **minSdk 32** — a continued hardening trajectory that supports the
"structural, moving-target" framing rather than a transient bug.

## Table 2 cells

TextFree device/network/cloud (dynamic) = **△ not-feasible (minSdk 32 on study
emulator; PairIP + Play Integrity + App Check + FingerprintJS at runtime)** — a named
boundary, explicitly distinct from ○ observed-absent. Static profile = ● reported.
