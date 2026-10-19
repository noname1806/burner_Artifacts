# Burner — network / cloud API traffic (sanitized)

Burner (Ad Hoc Labs, `com.adhoclabs.burner`) was **not** captured with a passive TLS proxy
like the other apps. Its cloud API rides HTTPS to `phoenix.burnerapp.com`, and we mapped and
exercised that surface directly using a Firebase token recovered during device acquisition.
This folder is the sanitized record of that traffic.

```
burner_network/
├── cloud_responses/     JSON returned by the Burner REST API, collected by BFCC (read-only)
│   ├── *.burners.json          lines on the account (id, number, settings, entitlements)
│   ├── *.conversations.json    conversation/message rows
│   ├── *.messages.json         message bodies
│   ├── *.subscriptions.json    subscription state
│   ├── *.sip.json              SIP registration parameters
│   └── *.bundle.json           combined export
└── api_mapping/         direct API probing and static endpoint extraction
    ├── burner_phoneNumbers_*.json / .headers.json / .log.txt   one request/response (401)
    ├── burner_scan.md          mapped endpoints and findings
    ├── urls.csv                URLs extracted from the APK
    ├── sdks.csv, permissions.csv   SDKs and permissions from the APK
```

## Endpoints observed (base `https://phoenix.burnerapp.com`)
| Method | Path | Returns |
|---|---|---|
| GET | `/v3/user/{USER_ID}/burners` | lines on the account |
| GET | `/v2/user/{USER_ID}/conversations` | conversation threads |
| GET/POST/DELETE | `/v2/user/{USER_ID}/burners/{burner_id}/conversations/{conv_id}/messages` | message history |
| GET | `/v2/user/{USER_ID}/sip-registration` | SIP/VoIP parameters |
| GET | `/v2/user/{USER_ID}/phoneNumbers?areaCode=&numberType=` | available numbers (needs auth) |
| POST | `https://securetoken.googleapis.com/v1/token` | exchange refresh token → ID token |

Authentication is a Firebase refresh token (recovered from
`shared_prefs/com.google.firebase.auth.FIREBASE_USER.xml`) exchanged for a short-lived ID
token that the endpoints accept as a Bearer token.

## Sanitization
All accounts, numbers, and messages were created by the research team on devices we control;
no third-party content is present. In this release:
- **User and line identifiers** (`userId`, `burnerId`, message `id`, UUIDs) are replaced with
  `00000000-0000-0000-0000-0000000000NN` placeholders, consistently across files.
- **Phone numbers** keep the area code and exchange (NPA-NXX) and have the last four digits
  replaced with `XXXX`.
- **Bearer/ID tokens and API keys** are removed (`[REDACTED_TOKEN]`); `keys.csv` from the raw
  capture is not included.
- Message **text** is kept because it is researcher-authored test content.

The unredacted originals, including tokens and full numbers, are held by the authors and
shared with reviewers and verified law-enforcement agencies on request.
