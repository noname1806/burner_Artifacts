# Hushed encrypted-DB key derivation — reverse-engineering evidence

Reproduced end-to-end on Hushed **v5.31.0** (APK `apk/hushed_5.31.0.apk`), fully offline.
Answers DFRWS-USA Review 2's request for a concrete JADX-level account of the
derivation and reproducibility of the recovered password.

## Where the logic lives (for the JADX figure)

Open the APK in JADX and navigate to:

    Class : com.hushed.base.repository.database.DBEncryptionUtil
    Method: char[] getInstallationPassword(SharedPreferences)     ← derivation
    Caller: DBEncryptionUtil.initialize(DaoMaster$DevOpenHelper, SharedPreferences)
            → opens the GreenDAO (org.greenrobot.greendao) database via SQLCipher

DEX map (v5.31.0): `getInstallationPassword` + `KEY_DB_INFO_STORE` + `SHA-1` are in
classes4.dex; the SQLCipher `SupportFactory` / `net.sqlcipher` / `passphrase` open
path is in classes3.dex. Raw smali of the method: `DBEncryptionUtil_getInstallationPassword.smali`.

## Faithful Java reconstruction (verified against the smali)

```java
// com.hushed.base.repository.database.DBEncryptionUtil
char[] getInstallationPassword(SharedPreferences prefs) {
    String uuid = prefs.getString("KEY_DB_INFO_STORE", null);
    if (uuid == null) {                       // first run: mint + persist
        uuid = UUID.randomUUID().toString();
        prefs.edit().putString("KEY_DB_INFO_STORE", uuid).apply();
    }
    byte[] digest = MessageDigest.getInstance("SHA-1")
                       .digest((uuid + "com.hushed.release").getBytes("UTF-8"));
    char[] pw = new char[16];
    for (int i = 0; i < 16; i++)
        pw[i] = (char) (((digest[i] & 0xFF) % 94) + 33);  // map to ASCII 33..126
    return pw;                                 // used directly as SQLCipher passphrase
}
```

## Forensic significance (why this is structural, not a patchable bug)

1. **The passphrase input is recoverable by design.** The per-install UUID is not
   a secret: it is generated with `UUID.randomUUID()` and **written back to
   plaintext shared-prefs** (`com.hushed.release_preferences.xml` →
   `KEY_DB_INFO_STORE`). Any logical acquisition of `/data/data/com.hushed.release`
   yields it.
2. **The derivation is deterministic and self-contained** — UUID + a hard-coded
   package string → SHA-1 → fixed byte→char map. No server secret, no
   hardware-backed key, no user input. Given the prefs file, the key is
   reconstructable offline on any machine.
3. Together these make offline decryption a property of the *architecture*
   (client-side deterministic key derivation from recoverable inputs), which
   supports the "structural persistence, not incidental bug" framing (task #5).

## Verified decryption parameters (SQLCipher)

| Parameter | Value |
|---|---|
| cipher_version | SQLCipher 4.x |
| cipher_page_size | 4096 |
| kdf_iter | 256000 |
| cipher_kdf_algorithm | PBKDF2_HMAC_SHA512 |
| cipher_hmac_algorithm | HMAC_SHA512 |

Worked example (lab install): UUID `096c899c-d74c-4fde-bd80-323dcbc05cd9`
→ passphrase `V,rFJ92N9HfC;'V[` → decrypts `databases/hushed-encrypted.db`
(15 tables). Tool: `tools/hushed_decrypt.py`.

## Paper corrections surfaced

- Encrypted DB is `hushed-encrypted.db`, **not** `hushed.db` (as stated in the draft).
- Password is returned as a **char[]**, not a String; used directly as the SQLCipher passphrase.
- Name the exact prefs key (`KEY_DB_INFO_STORE`) and class/method, replacing the
  draft's vague "installation UUID in shared preferences plus an app/build identifier."
