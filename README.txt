===============================================================================
NOT ALL "BURNERS" BURN - EVIDENCE ARTIFACTS
Supporting material for the manuscript "Not All Burners Burn: A Forensic
Analysis of Android Burner Apps"
===============================================================================

PURPOSE
This folder holds the evidence behind the paper's findings, organised so that a
reviewer can trace each result back to the file it came from and check that the
files have not changed. All accounts, numbers, lines and conversations were
created by the research team on devices we control. No third party's data is
included in the shareable folders. Folders 01 through 15 are shareable
(sanitised where noted). Folder 99 is restricted and must not be shared.


HOW TO VERIFY FILE INTEGRITY
1. Open ARTIFACT_INVENTORY.txt. It lists, for every file, the size in bytes,
   the SHA-256 hash, and the path.
2. To check one file on Windows PowerShell:
      Get-FileHash -Algorithm SHA256 "01_app_versions\APK_VERSIONS.csv"
   On Linux or macOS:
      sha256sum 01_app_versions/APK_VERSIONS.csv
3. Compare the printed hash against the hash in ARTIFACT_INVENTORY.txt for the
   same path. If they match, the file is intact.
4. 00_TOOL_EVIDENCE.md maps each tool named in the paper (Section 3) to the
   evidence file that shows it was used.


WHAT EACH FOLDER CONTAINS

01_app_versions
   The exact app versions and runtime environment the results come from.
   APK_VERSIONS.csv lists each app and the version analysed. The runtime file
   records the emulator and OS used during capture.

02_device_acquisitions_sanitized
   Logical acquisitions of the device, after masking. Covers Hushed (a clean
   baseline, and the before and after states of a single-message deletion) and
   2ndLine (a baseline). Each acquisition keeps its original SHA-256 manifest so
   the masked copy can be tied back to the untouched original. integrity.json
   records that every database still passes an SQLite integrity check.

03_network_traffic_sanitized
   Network traffic for the three apps that could be intercepted, after masking.
   2ndLine and Hushed were captured below TLS with a Frida hook and are parsed
   into HTTP messages (the .http.jsonl files). TextMe was captured with
   mitmproxy. parse_summary.json records how many messages were parsed and how
   many bytes were withheld because they were not plain HTTP.

04_static_analysis_reverse_engineering
   What static analysis of the app packages found. Includes the 2ndLine
   (Dingtone) API extraction, the hardening scan reports, the Hushed
   key-derivation write-up and the recovered method, and the TextMe and TextFree
   findings and manifests.

05_textme_hardening_dynamic_attempts
   Evidence that dynamic analysis of TextMe was blocked by its hardening. The
   license-gate screenshot, the Frida script that was tried, and a write-up of
   the crash inside the PairIP native library.

06_number_corpus_burnercheck
   The number identification study (BurnerCheck). Contains:
   - collection_scripts: how the numbers were gathered from each app.
   - public_masked: the masked corpus, the scoring script, the expected output,
     and the redaction log and hash list.
   - evaluation_597_labeled: the earlier labelled set and its scoring.
   - validation: the balanced-sample and classifier validation scripts and
     their saved outputs.
   Running the scoring script reproduces the precision, recall, specificity and
   F1 figures reported in Section 5.1.

07_burner_network_sanitized
   Burner's cloud API traffic, after masking. Burner was not captured with a
   passive proxy; its API was mapped and exercised directly. cloud_responses
   holds the JSON the Burner server returned. api_mapping holds the direct API
   probe, the endpoint scan, and the URLs and SDKs extracted from the package.
   Identifiers and the last four digits of phone numbers are masked.

08_case_study_burner_figures
   The figures used in the Section 6 case study: the conversation screenshots,
   the recovered-message screenshots, the before and after burn screenshots, and
   the methodology and use-case diagrams.

09_bfcc_cloud_client
   The Burner Forensics Cloud Client source, its README, and its architecture
   diagram. BFCC performs read-only-by-default cloud collection and writes
   hashed, Merkle-rooted evidence manifests.

10_ui_action_screenshots
   Screenshots of the app actions referenced in the paper, mainly the Hushed
   delete and burn steps, plus launch screens for the other apps.

11_action_outcome_matrix
   action_matrix.csv: the per-app, per-action outcome table that Table 2 is
   built from (observed, partial, absent, not feasible, not applicable).

12_toolkit_snapshot
   A snapshot of the full eleven-step forensic toolkit referenced in Section 3,
   from the hardening scanner through acquisition, database diffing, decryption,
   carving, capture, the cloud client and the number checker. Includes the large
   public NANPA prefix file used by the offline lookup.

13_ethics_disclosure
   The coordinated-disclosure material: the draft disclosure emails to the
   vendor, and a redacted screenshot of the disclosure correspondence.

14_case_study_databases
   The sanitised device databases behind the Section 6 case study, with
   screenshots. case1_final_analysis shows messages surviving a UI deletion.
   case2_before_burn and case2_after_burn show the device state around a number
   burn: the active-line database drops the burned line, while the message
   database keeps the burned line's messages. The README inside gives the exact
   SQLite queries that reproduce the result. The databases are valid after
   masking (they pass an integrity check).

15_2ndline_burn_control
   UI-layer evidence that 2ndLine exposes a user-facing burn control, supporting
   the finding that three apps (Burner, Hushed, 2ndLine) offer a burn feature.

99_RESTRICTED_DO_NOT_SHARE
   Not for release. Holds the unredacted originals and anything that contains
   live secrets or real numbers: recovered credentials and refresh tokens, the
   Burner cloud exports and token-refresh data, the original device acquisitions
   and network captures, the autopsy cases, and the unmasked number lists
   (including number_collection_raw_toplevel). Share only with reviewers and
   verified law-enforcement agencies on request.


SANITISATION, IN BRIEF
Phone numbers keep the area code and exchange and have the last four digits
replaced. Account, user and line identifiers are replaced with fixed
placeholders. Tokens, keys and credentials are removed. Message text that the
research team authored is kept. Full details of every rule and count are in
06_number_corpus_burnercheck/public_masked/REDACTION_LOG.csv and in the README
files inside folders 07 and 14.


TOOLING DISCLOSURE
Generative-AI assistance was used while preparing and documenting these
artifacts. Every result is produced by running the released code on the
released data and can be reproduced as described above.
