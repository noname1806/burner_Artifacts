# Network Traffic / API Inventory — Burner, 2ndLine, Hushed

Consolidated from the project's captures and static analysis. Covers the three
service-burn apps requested. Data provenance per app differs — stated inline.

Source files:
- `dataset_release/public/02_network_traffic/2ndline_frida_ssl/*.http.jsonl` (Frida SSL_read/SSL_write)
- `dataset_release/public/02_network_traffic/hushed_frida_ssl/*.http.jsonl` (Frida SSL_read/SSL_write)
- `BFCC-4F35/analysis.py`, `paper.txt` Table 5, `paper_evidence/2ndline_findings.md`

---

## 1. Burner (Ad Hoc Labs — `com.adhoclabs.burner`)

**Capture status:** No network capture on disk (listed as NOT FOUND in
`dataset_release/README_FIRST.md`, §4.1 / Table A.4). Endpoints below are from the
BFCC client code and paper Table 5 — statically mapped / read-only validated, not
from an on-disk pcap.

**Auth model:** Firebase refresh token (from `shared_prefs/com.google.firebase.auth.FIREBASE_USER.xml`)
→ exchanged at `securetoken.googleapis.com` for an ID token → sent as `Authorization: Bearer <id_token>`.

| Method | Host | Path | Function |
|---|---|---|---|
| POST | `securetoken.googleapis.com` | `/v1/token?key=<firebase_key>` | Exchange refresh token → ID token |
| GET | `phoenix.burnerapp.com` | `/v3/user/{USER_ID}/burners` | List all burner lines (current + historical) |
| GET | `phoenix.burnerapp.com` | `/v3/user/{USER_ID}/subscriptions` | List subscriptions |
| GET | `phoenix.burnerapp.com` | `/v2/user/{USER_ID}/conversations?page=&pageSize=` | List conversation threads |
| GET/POST/DELETE | `phoenix.burnerapp.com` | `/v2/user/{USER_ID}/burners/{burner_id}/conversations/{conv_id}/messages` | Read / send / delete messages in a thread |
| GET | `phoenix.burnerapp.com` | `/v2/user/{USER_ID}/sip-registration` | SIP/VoIP registration params |

---

## 2. 2ndLine (Dingtone engine — `me.number.app.im`, v2.6.2)

**Capture status:** Full plaintext captured via Frida BoringSSL hook despite pinning.
36 request + 36 response HTTP/1.1 messages in the public export. This is the only app
with first-party API traffic captured to disk.

**Auth model:** `userId` + `deviceId` query parameters only — **no bearer/Authorization
header observed**. Both recoverable from the device (`Dingtone.db`). Weakest cloud auth
of the three.

**First-party API — gateway `dt-apigatewayv2.dt-pn1.com`:**

| Method | Path | Function |
|---|---|---|
| GET | `/config/client?cc=US&newer=1&appVersion=2.6.2&appType=69&osType=2&userId=&group=common` | Client config |
| GET | `/plan/query/number/getSubList?userId=&deviceId=` | Subscribed numbers list |
| GET | `/plan/query/upgrade/product?userId=&deviceId=` | Upgrade products |
| GET | `/plan/subscription/getBurnInfo?userId=` | **Burn-state endpoint** |
| GET | `/telosWeb/number/ad/sub/detail?userId=&deviceId=` | Ad/subscription detail |

**Logging gateway `dt-apigateway-log.dt-pn1.com`:** `POST /report/log/async`

**Note:** message-content REST endpoints did not appear in this capture window; real-time
messaging likely rides a Dingtone socket channel, not REST (follow-up work).

**Third-party SDK traffic observed:** `graph.facebook.com` (FB SDK gatekeepers/activities),
`app.adjust.com/event`, `firebaselogging.googleapis.com`, `firebaselogging-pa.googleapis.com`,
`fundingchoicesmessages.google.com`.

---

## 3. Hushed (`com.hushed.release`, v5.31.0)

**Capture status:** First-party API calls rode HTTP/2, so they are NOT in the parsed
plaintext export — the Hushed capture on disk is **SDK traffic only**. First-party
endpoints below are from paper Table 5 (statically mapped / read-only validated).

**Auth model:** Firebase Installations + Google OAuth sign-in chain → Hushed Access Token.
Replayed tokens enable off-device read-only collection.

**First-party API (from Table 5, not from on-disk capture):**

| Method | Host | Path | Function |
|---|---|---|---|
| POST | `gk.production.hushed.com` | `/users/signin/google` | Exchange Google OAuth/ID token → Hushed Access Token |
| GET | `api.production.hushed.com` | `/v1/users/{userId}/phones` | Active + historical phone numbers + timestamps |
| GET | `api.production.hushed.com` | `/v1/users/{userId}/items` | Message bodies, call logs, attachments (timestamp query) |
| POST | `firebaseinstallations.googleapis.com` | `/v1/projects/affinityclick.com.../installations` | Register client as valid Firebase installation |

**Third-party SDK traffic actually captured (plaintext, HTTP/1.1):**

| Method | Host | Path |
|---|---|---|
| POST | `sdk.iad-01.braze.com` | `/api/v3/data`, `/api/v3/content_cards/sync` |
| POST | `aj0zur.launches.appsflyersdk.com` | `/api/v6.17/androidevent?app_id=com.hushed.release` |
| POST | `firebaseremoteconfigrealtime.googleapis.com` | `/v1/projects/{ID}/namespaces/firebase:streamFetchInvalidations` |
| GET | `www.gstatic.com` | `/recaptcha/verify_key/orcas/prod/android/verify_key.txt` |
| POST | `www.recaptcha.net` | `/recaptcha/api3/mri` |

---

## Summary matrix

| | Burner | 2ndLine | Hushed |
|---|---|---|---|
| First-party API captured to disk | ✗ (not found) | ✓ plaintext (Frida) | ✗ (HTTP/2, SDK only) |
| Auth mechanism | Firebase refresh → Bearer ID token | userId+deviceId query params (no token) | Google OAuth → Hushed Access Token |
| Primary API host | `phoenix.burnerapp.com` | `dt-apigatewayv2.dt-pn1.com` | `api.production.hushed.com` |
| Burn/delete endpoint | `DELETE .../messages` | `GET /plan/subscription/getBurnInfo` | — |
| TLS interception | (static map only) | defeated pinning via Frida | SDK plaintext; first-party HTTP/2 |
