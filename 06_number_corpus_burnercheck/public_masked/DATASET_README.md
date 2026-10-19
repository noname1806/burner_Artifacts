# Dataset: Not All "Burners" Burn — Android burner-app forensics

Supporting data for the FSIDI manuscript *Not All "Burners" Burn: A Forensic Analysis of Android
Burner Apps*. All accounts, lines and conversations were created by the researchers on a rooted
Android 12 (API 31) emulator, plus an Android 13 (API 33) emulator for TextMe. No third-party users'
messages are included.

## Contents

| Folder | What it is | Supports |
|---|---|---|
| `01_device_acquisitions/hushed/A00_clean_baseline_*` | Hushed 5.31.0, decrypted SQLCipher store after first sync | §4.2, Table 3 |
| `01_device_acquisitions/hushed/A08_before_delete_*`, `A08_after_delete_*` | Hushed decrypted store immediately before and after a single-message UI deletion | §4.2 secure-delete result (events 13 → 12; deleted text present in the before-file bytes, absent from the after-file bytes) |
| `01_device_acquisitions/hushed/orch_baseline_*` | Hash manifest and metadata only (orchestrator run) | §3 workflow |
| `01_device_acquisitions/2ndline/A00_baseline_*` | 2ndLine (Dingtone engine) 2.6.2, `Dingtone.db` | §4.3, Table 3 |
| `original_manifest.sha256`, `original_appdata.tar.sha256`, `original_meta.txt` | Per-file SHA-256 manifest and bundle hash of the **unsanitized** acquisition | chain of custody |
| `02_network_traffic/hushed_frida_ssl/` | Plaintext captured beneath TLS (Frida hooks on `SSL_read`/`SSL_write`), parsed into HTTP/1.1 messages | §3 network layer, §4.2 |
| `02_network_traffic/2ndline_frida_ssl/` | As above, for 2ndLine; includes the REST gateway `dt-apigatewayv2.dt-pn1.com` | §4.3, Table A.4 |
| `02_network_traffic/textme_api33_mitmproxy/` | TextMe 3.55.0 traffic captured with mitmproxy (system CA, no pinning), plus the PairIP license-gate screenshot | §4.4 |
| `03_number_corpus/app_numbers_2508.masked.csv` | 2,508 app-issued numbers looked up with Twilio Lookup v2 (line type, carrier) and NANPA prefix records. 2,458 have a collection record (Burner 503, Hushed 450, 2ndLine 505, TextMe 500, TextFree 500) and are the positives used in the paper; 50 Hushed rows without a collection record are excluded | RQ2, §5.1 |
| `03_number_corpus/hushed_documented_450.record_ids.txt` | `record_id`s of the 450 Hushed numbers documented in the collection log | §5.1 positives |
| `03_number_corpus/labeled_611_with_negatives.masked.csv` | Twilio and NANPA results for an earlier lookup batch. Its 372 conventional rows are the negatives; the 225 app-issued rows and 14 rows with no Twilio result (11 trial-account rate-limit errors, 3 empty replies) are not used | §5.1 negatives |
| `03_number_corpus/negatives_known_contacts_372.record_ids.txt` | `record_id`s of the 372 negatives: numbers belonging to known contacts of the research team, each confirmed by the team as the contact's own conventional line. The contact record itself is restricted | §5.1 negatives |
| `03_number_corpus/evaluate_public.py` | Reproduces the §5.1 main table (100 positives per app, seed 2026, plus the 372 negatives) and per-app recall on all 2,458 positives, with 95% Wilson intervals; writes `confusion_matrices.json` | §5.1 tables |
| `03_number_corpus/validation/balanced_subsample.py` | Repeats the per-app draw 1,000 times to show the result does not depend on the seed | §5.1 robustness |
| `03_number_corpus/validation/validate_burnercheck.py` | Leave-one-app-out test of the carrier rule and the exact-carrier sensitivity check | §5.1 robustness |

Run `python 03_number_corpus/evaluate_public.py` to reproduce the identification metrics. Each script's
output is saved next to it (`*_OUTPUT.txt`).

Ground truth is assigned by provenance only: positives are numbers we obtained from the apps, and
negatives are known contacts. No label is derived from a classifier's output.

## Sanitization (and why)

The raw data contains live credentials for the test accounts, inputs to Hushed's database key, and
phone numbers. Phone numbers from these services are recycled and reassigned to members of the
public, and the negative set consists of real people's numbers. We therefore applied the following:

- **Phone numbers:** the line number (last four digits) is replaced with `XXXX`. The NPA and NXX are
  kept so that NANPA prefix lookups remain reproducible. `record_id` is a keyed HMAC of the full
  number, so records can be joined against the unmasked list available to reviewers.
- **Credentials and identifiers:** refresh, ID, FCM and installation tokens, API keys, account
  IDs, device IDs, the 2ndLine `userId`/`deviceId` pair, emails and referral codes are replaced.
- **Hushed databases:** masking uses same-length byte replacement across the whole file, so page
  layout, freelist and unallocated space are preserved. Carving and secure-delete results therefore
  remain reproducible. Every file passes `PRAGMA integrity_check` (see `integrity.json`).
  **The encrypted database and the key-derivation inputs are not published** (see "Restricted
  material").
- **`Dingtone.db`:** the app had synced the emulator's device address book (574 contacts belonging
  to third parties) into `local_user` and `local_user_data`. These tables are emptied, the profile
  image is removed, identifiers are masked, and the file is vacuumed.
- **Network traffic:** streams are parsed into HTTP messages and gzip bodies are decompressed. JSON
  values under sensitive keys, sensitive headers, query parameters and path IDs are replaced with
  `[REDACTED]` or `{ID}`. **Binary bodies (protobuf or media), brotli bodies, websocket payloads and
  any bytes that are not HTTP/1.1 (for example HTTP/2 HPACK frames) are withheld.** They cannot be
  reliably scanned for identifiers. Byte counts and original SHA-256 values are kept, and
  `parse_summary.json` lists the withheld bytes per file. Hushed's own API calls were carried over
  HTTP/2, so the Hushed export consists mostly of SDK traffic and responses.
- **Omitted entirely:** `shared_prefs`, `files/`, `cache/`, MMKV stores and WebView data. These hold
  tokens and SDK identifiers, and the paper's findings do not depend on them.

`REDACTION_LOG.csv` (shipped next to this folder) counts every redaction by location and rule.

## Restricted material (available to reviewers and verified law enforcement on request)

The following are withheld from public release: the original `appdata.tar` acquisitions, the
encrypted Hushed store and its key inputs, the raw Frida and mitmproxy captures, the unmasked number
lists, the known-contact record behind the negative set, and the number-collection screenshots. They are held by the authors and shared under a
confidential link with the editor and reviewers. The Hushed key-derivation and decryption tool is
published in the toolkit after coordinated disclosure to the vendor; the key inputs of our test
accounts are not.

## Licence

CC BY 4.0 for the data and MIT for the scripts, unless the authors state otherwise.
