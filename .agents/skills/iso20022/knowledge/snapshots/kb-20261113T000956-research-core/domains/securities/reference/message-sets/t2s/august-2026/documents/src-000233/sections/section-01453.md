---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["35 reda.015.001.01 PartyQueryV01", "35.4 Message Building Blocks", "35.4.2 SearchCriteria <SchCrit>", "35.4.2.9 LockStatus <LckSts>", "35.4.2.9.1 ValidFrom <VldFr>"]
file_pages: [2067]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.015.001.01"]
---

# 35.4.2.9.1 ValidFrom <VldFr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2067 to 2067.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2067

```text
35.4.2.9.1  ValidFrom <VldFr>
Presence: [0..1]
Definition: Specifies the date from which the lock status is valid.
Datatype: "ISODate" on page 3319
35.4.2.9.2  Status <Sts>
Presence: [1..1]
Definition: Lock status of the party.
Datatype: "LockStatus1Code" on page 3262
CodeName Name Definition
LOCK Locked Party has been locked for operations.
ULCK Unlocked Party is ready for operations.
35.4.2.9.3  LockReason <LckRsn>
Presence: [0..*]
Definition: Specifies the underlying reason for the locking of the party.
Datatype: "Max35Text" on page 3328
35.4.3 ReturnCriteria <RtrCrit>
Presence: [0..1]
Definition: Defines the expected party reference data to be returned.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.015.001.01 PartyQueryV01
Target2-Securities 2067 August 2026
```

