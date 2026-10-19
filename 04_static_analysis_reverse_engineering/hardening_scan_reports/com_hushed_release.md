# Forensic workflow report: com.hushed.release

- Acquisition: `captures\com.hushed.release\orch_baseline_20260718_023858\appdata.tar`  (SHA-256 `08e5755af0925d53...`)
- Databases: 4 (1 encrypted, 3 plaintext)
  - plaintext: `databases/google_app_measurement_local.db`
  - ENCRYPTED: `databases/hushed-encrypted.db`
  - plaintext: `databases/maelstrom.db`
  - plaintext: `databases/afpurchases.db`

## Outcome-schema template (complete per action)

| action | device (created/persist/removed) | network | cloud |
|---|---|---|---|
| register |  |  |  |
| obtain number |  |  |  |
| send SMS |  |  |  |
| receive SMS |  |  |  |
| delete message |  |  |  |
| delete thread |  |  |  |
| burn number |  |  |  |
| logout |  |  |  |

## Next (interactive) steps
1. For each action: `ui.py` to drive it, `capture.sh` before/after, `dbdiff.py` (decrypt first with the app's key-derivation plugin if encrypted).
2. Network: `net_capture.py <pkg>` to map the API beneath pinning.
3. Cloud: replay the recovered credential read-only; log every request.

> Note: hardening detected — record blocked observations as △ (not feasible) with the named mechanism.
