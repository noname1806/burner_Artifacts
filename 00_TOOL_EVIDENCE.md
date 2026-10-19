# Tool → evidence map (paper §3, "Released toolkit and data")

Every tool listed in §3 must have an entry here. Tools without evidence are not listed in the paper.

| Tool (toolkit folder) | Evidence of use | Location | Public / restricted |
|---|---|---|---|
| Hardening scan (`01-hardening-scan`) | Scan report for Hushed 5.31.0 | `04_static_analysis_reverse_engineering/hardening_scan_reports/com_hushed_release.{json,md}` | Public |
| Hashed logical acquisition (`02-acquire`) | `appdata.tar`, `appdata.tar.sha256`, `manifest.sha256`, `meta.txt` for Hushed A00, A08 before/after, orch baseline; 2ndLine A00 | Originals: `99_RESTRICTED_DO_NOT_SHARE/`; sanitized: `02_device_acquisitions_sanitized/` | Sanitized public |
| SQLCipher decryption of Hushed (`04-decrypt-hushed`) | `hushed-decrypted.db` for A00 and A08 before | `02_device_acquisitions_sanitized/hushed/` (sanitized) | Sanitized public; key-derivation tool public (after vendor disclosure) |
| TLS capture beneath pinning (`07-network-capture`) | Sanitized Frida `SSL_read`/`SSL_write` captures, Hushed and 2ndLine | `03_network_traffic_sanitized/{hushed,2ndline}_frida_ssl/` | Public |
| Orchestrator + UI driving (`11-orchestrator`, `10-ui-helper`) | `orch_baseline_20260718_023858`; number-collection logs and step screenshots | `02_device_acquisitions_sanitized/hushed/orch_baseline_*`; `99_RESTRICTED_DO_NOT_SHARE/number_corpus_original/collection_*/track/` | Mixed |
| BFCC (`08-cloud-client-bfcc`) | Burner cloud exports | `99_RESTRICTED_DO_NOT_SHARE/burner/cloud_exports_bfcc/` | Restricted. **Gap:** no `.manifest.json` files, although §5 says every export writes one |
| BurnerCheck (`09-identify-burnercheck`) | Evaluation corpus, scripts and outputs | `06_number_corpus_burnercheck/` | Public (masked) |

**Not listed in the paper (no saved output):** `03-db-diff`, `05-carve-deleted`, `06-extract-prefs`. The Hushed events 13 → 12 result is still reproducible from the before/after decrypted databases.

