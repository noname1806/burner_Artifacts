# Burner — case study artifacts (Section 6)

Device databases and screenshots for the controlled Burner case study. Every account, number,
message, and conversation here was **created by the research team** on devices we control; the
scenario (a mock drug-sale negotiation) is fabricated for the study. These are not real
suspects or victims. Phone numbers are masked to their area code and exchange (last four
digits `XXXX`); account and line identifiers are replaced with placeholder UUIDs. The SQLite
databases remain valid (`PRAGMA integrity_check` = ok) after masking.

```
case_study/
├── case1_final_analysis/        Case 1 — UI-deleted threads (messages still on device)
│   ├── com.adhoclabs.burner.messages.db
│   └── burnerDatabase.db
├── case2_before_burn/           Case 2 — device state BEFORE the number burn
│   ├── com.adhoclabs.burner.messages.db
│   └── burnerDatabase.db
├── case2_after_burn/            Case 2 — device state AFTER the number burn
│   ├── com.adhoclabs.burner.messages.db
│   └── burnerDatabase.db
└── screenshots/                 UI and database evidence
    ├── 225802_text.png, 225586_text.png              pre-deletion conversations (Fig. 3)
    ├── deleted_message_recovered_01.png, _02.png     messages recovered after UI deletion (Fig. 5)
    ├── case_study_2_before_burner_01.png             two numbers created before burn (Fig. 6a)
    ├── case_study_2_after_burner_01.png              single active number after burn (Fig. 6b)
    └── case_study_2_database_after_burn.png          DbMessage rows kept for the burned burnerId (Fig. 6c)
```

## What the databases show
- **`com.adhoclabs.burner.messages.db`** — tables `DbMessage` (id, burnerId, contactId,
  dateCreated, direction, type, state, text) and `DbConversation`. Message rows survive both
  UI deletion (Case 1) and a full number burn (Case 2); after a burn, rows keyed to the burned
  `burnerId` remain on device.
- **`burnerDatabase.db`** — tracks the active burner lines. After a burn it lists only the
  still-active line, while the message store above still holds the burned line's messages.

## How to reproduce the case-study result
```bash
# Case 1: deleted messages still present on device
sqlite3 case1_final_analysis/com.adhoclabs.burner.messages.db \
  "SELECT dateCreated, direction, contactId, text FROM DbMessage ORDER BY dateCreated;"

# Case 2: compare the active lines before vs after the burn ...
sqlite3 case2_before_burn/burnerDatabase.db   "SELECT * FROM BurnerEntity;"
sqlite3 case2_after_burn/burnerDatabase.db    "SELECT * FROM BurnerEntity;"
# ... while the burned line's messages persist in the message store
sqlite3 case2_after_burn/com.adhoclabs.burner.messages.db \
  "SELECT DISTINCT burnerId FROM DbMessage;"
```
Converting `dateCreated` (Unix epoch milliseconds) gives the timeline shown in the paper.
