# Hushed — paper-ready write-up (FSIDI revision)

Drop-in text for the Hushed portions of the manuscript, grounded entirely in the
reproduced lab evidence (v5.31.0, emulator-5554 Android 12, rooted). Prose is kept
plain and specific (reviewers flagged "overblown" phrasing in the prior draft).

---

## 4.2 Hushed: findings (rewrite)

Hushed stores its primary application state in an SQLCipher-encrypted GreenDAO
database, `databases/hushed-encrypted.db` (the prior draft's `hushed.db` is a
misnomer). Static analysis with androguard/JADX resolved the database
password-derivation routine to a single method,
`com.hushed.base.repository.database.DBEncryptionUtil.getInstallationPassword(
SharedPreferences)`, invoked from `DBEncryptionUtil.initialize(...)` when the
GreenDAO helper opens the database through the SQLCipher `SupportFactory`.

The routine derives the passphrase deterministically from two recoverable inputs
(Figure X). On first launch the app generates a random installation identifier with
`UUID.randomUUID()` and **persists it in clear text** to
`shared_prefs/com.hushed.release_preferences.xml` under the key `KEY_DB_INFO_STORE`.
On every subsequent open it reads that UUID back, concatenates it with the fixed
package string `com.hushed.release`, computes a SHA-1 digest over the UTF-8 bytes,
takes the first 16 digest bytes, and maps each byte into the printable ASCII range
via `(b & 0xFF) mod 94 + 33`, yielding a 16-character passphrase (returned as a
`char[]` and passed directly to SQLCipher).

Because both inputs are recoverable under logical acquisition — the UUID from plain
shared-preferences and the package name from the manifest — the passphrase is
reconstructable offline, with no network interaction and no server-side secret.
We reproduced this on a fresh acquisition: UUID
`096c899c-d74c-4fde-bd80-323dcbc05cd9` yields passphrase `V,rFJ92N9HfC;'V[`, which
opens `hushed-encrypted.db` (SQLCipher 4; page size 4096; KDF PBKDF2-HMAC-SHA512 with
256,000 iterations; page HMAC-SHA512). The decrypted database exposes 15 tables,
including `accounts`, `numbers`, `conversations`, `events` (messages), `contacts`,
and `blocked_numbers`. Our released tool `hushed_decrypt.py` performs the full
derivation and decryption from a device image.

This behaviour is architectural rather than an incidental defect: the app *chooses*
to derive the key from a client-recoverable identifier so the database can be opened
without user interaction on every launch. Tightening it would require a design change
(e.g. binding the key to a Keystore-held secret), not a bug fix.

## 4.2.x Persistence after UI deletion (new subsection; RQ1)

We measured what a user-initiated deletion actually removes, using a
capture→decrypt→diff protocol: force-stop the app, acquire `/data/data/com.hushed.release`
with a per-file hash manifest, decrypt `hushed-encrypted.db`, and diff table contents
before and after the action.

Deleting a single message through the UI (long-press → delete → confirm) removed the
corresponding row from the `events` table (13 → 12 rows). The row was **hard-deleted**:
no soft-delete flag was set, and a byte-level search of the entire post-deletion
acquisition — every database, write-ahead log, journal, cache and preference file —
found no residue of the message text.

To test for lower-level residue we decrypted every 4 KB page of the SQLCipher database
in place (AES-256-CBC with the per-page IV, without repacking) and searched freelist
and unallocated space (`sqlcipher_carve.py`). As a control, the same carver recovered
the message from the *pre*-deletion image (physical page 24) with its record context
intact, confirming the method detects residual records when present. After deletion the
message was absent from every page. The cause is that SQLCipher enforces
`PRAGMA secure_delete = ON`, which zero-overwrites freed cell content
(`freelist_count = 0` after the operation).

Consequently, for Hushed a message removed through the UI is **not recoverable from the
device**. This is consistent with our cloud observation (Section 6): token-scoped
collection did not return bodies for deleted items either. Hushed single-message
deletion is therefore effectively destructive — a marked contrast with Burner, whose
plaintext SQLite store retains deleted message rows on disk (Section 4.1). The
forensically durable Hushed artifacts are instead the **linkage/metadata** that survive
deletion (conversation and account context) and the **burned-line event rows** discussed
below; blanket "message content persists" claims do not hold for Hushed at the single-
message level.

---

## Revised Table 2 (Hushed column) + legend

Split the overloaded symbol so a method limitation is not reported as an app property:

- ● observed and validated
- ◐ partially observed / limited evidence
- ○ **observed absent** (property tested for and not present)
- △ **not feasible in this study** (method could not reach it — a limitation, not a result)
- N/A not applicable (feature absent)

| Forensic property | Hushed | change vs prior draft |
|---|---|---|
| Explicit burn-number feature | ● | — |
| Device-resident SQLite DBs | ● | — |
| Database encrypted at rest | ● | — |
| Offline DB decryption feasible | ● | reproduced; exact params reported |
| **Message content persists after UI deletion** | **○** | **corrected — was overclaimed; secure_delete zeroes it** |
| Linkage/metadata persists after UI deletion | ● | new, explicit |
| Artifacts persist after number burn | △ | not reproduced here (needs active line) |
| **Auth tokens recoverable on device** | **◐** | **refined — Firebase installation state yes; messaging token is Keystore-wrapped, not offline-recoverable (cf. Burner ●, plaintext)** |
| Undocumented API observed | ● | — |
| Cloud data acquisition | ◐ | — |

---

## Figure X — caption

> **Figure X.** Reverse-engineered Hushed database key derivation
> (`DBEncryptionUtil.getInstallationPassword`, decompiled from
> `com.hushed.release` v5.31.0). A per-install UUID generated with
> `UUID.randomUUID()` and stored in clear text in shared-preferences
> (`KEY_DB_INFO_STORE`) is concatenated with the package name, hashed with SHA-1,
> and the first 16 bytes are mapped into printable ASCII to form the 16-character
> SQLCipher passphrase. Both inputs are recoverable by logical acquisition, making
> offline decryption deterministic.

(Use the Java reconstruction in `hushed_key_derivation.md`, or a JADX screenshot of
the named method, as the figure body.)

---

## Reviewer-response crosswalk (Hushed items)

| Reviewer point | Venue | Addressed by |
|---|---|---|
| Hushed password derivation "too vague"; give concrete RE / JADX figure | DFRWS R2 | Named class+method, first-run UUID generation, Figure X, exact SQLCipher params |
| "Need more detail to assess/reproduce" the derivation | DFRWS R2 | Released `hushed_decrypt.py`; worked example reproduced on fresh image |
| Confusing mod-94 / "Base94" derivation | DFRWS R1 | Plain-language explanation (map bytes to ASCII 33–126) |
| Complementary Hushed script missing from repo | IMF R3 | `hushed_decrypt.py` + `sqlcipher_carve.py` released |
| "Courtroom-ready/hash-manifest" not in code | IMF R2 | Capture harness now emits per-file hash manifest + bundle hash |
| Missing table / duplicate paragraph / `hushed.db` naming in 4.2 | DFRWS R1/R2 | 4.2 rewritten; DB corrected to `hushed-encrypted.db` |
| Table 2 conflates "not observed" vs "not feasible" | IMF R2 | New 5-symbol legend; Hushed cells corrected |
| "Is this just a patchable bug?" | DFRWS R1 | Framed as architectural (deterministic key from recoverable inputs, by design) |
