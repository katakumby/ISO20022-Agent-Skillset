---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["8 reda.041.001.02 PartyActivityAdviceV02", "8.4 Message Building Blocks", "8.4.2 PartyActivity <PtyActvty>", "8.4.2.2 Change <Chng>", "8.4.2.2.2 Record <Rcrd>", "8.4.2.2.2.10 LockStatus <LckSts>", "8.4.2.2.2.10.1 Old <Od>", "8.4.2.2.2.10.1.1 ValidFrom <VldFr>"]
file_pages: [105]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.041.001.02"]
---

# 8.4.2.2.2.10.1.1 ValidFrom <VldFr>

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 105 to 105.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 105

```text
8.4.2.2.2.10.1.1  ValidFrom <VldFr>
Presence: [0..1]
Definition: Specifies the date from which the lock status is valid.
Datatype: "ISODate" on page 184
8.4.2.2.2.10.1.2  Status <Sts>
Presence: [1..1]
Definition: Lock status of the party.
Datatype: "LockStatus1Code" on page 182
CodeName Name Definition
LOCK Locked Party has been locked for operations.
ULCK Unlocked Party is ready for operations.
8.4.2.2.2.10.1.3  LockReason <LckRsn>
Presence: [0..*]
Definition: Specifies the underlying reason for the locking of the party.
Datatype: "Max35Text" on page 188
8.4.2.2.2.10.2  New <New>
Presence: [1..1]
Definition: New value after the update.
New <New> contains the following PartyLockStatus1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [0..1] Date 105
   Status <Sts> [1..1] CodeSet 105
   LockReason <LckRsn> [0..*] Text 106
8.4.2.2.2.10.2.1  ValidFrom <VldFr>
Presence: [0..1]
Definition: Specifies the date from which the lock status is valid.
Datatype: "ISODate" on page 184
8.4.2.2.2.10.2.2  Status <Sts>
Presence: [1..1]
Definition: Lock status of the party.
Datatype: "LockStatus1Code" on page 182
CodeName Name Definition
LOCK Locked Party has been locked for operations.
ULCK Unlocked Party is ready for operations.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
105 March 2024
```

