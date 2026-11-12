---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["37 reda.017.001.02 PartyReportV02", "37.4 Message Building Blocks", "37.4.2 ReportOrError <RptOrErr>", "37.4.2.1 PartyReport <PtyRpt>", "37.4.2.1.2 PartyOrError <PtyOrErr>", "37.4.2.1.2.1 SystemParty <SysPty>", "37.4.2.1.2.1.10 ResidenceType <ResTp>"]
file_pages: [2094]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.017.001.02"]
---

# 37.4.2.1.2.1.10 ResidenceType <ResTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2094 to 2094.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2094

```text
Definition: Specifies the short name of the organisation.
Datatype: "Max35Text" on page 3328
37.4.2.1.2.1.10  ResidenceType <ResTp>
Presence: [0..1]
Definition: Specifies the type of residence where the party has its permanent home or principal
establishment.
Datatype: "ResidenceType1Code" on page 3288
CodeName Name Definition
DMST Domestic Residence is domestic.
FRGN Foreign Residence is foreign.
MXED Mixed Residence is mixed
37.4.2.1.2.1.11  LockStatus <LckSts>
Presence: [0..1]
Definition: Specifies whether the party is locked or not, and the reason for this status, when required.
LockStatus <LckSts> contains the following PartyLockStatus1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [0..1] Date 2094
   Status <Sts> [1..1] CodeSet 2094
   LockReason <LckRsn> [0..*] Text 2094
37.4.2.1.2.1.11.1  ValidFrom <VldFr>
Presence: [0..1]
Definition: Specifies the date from which the lock status is valid.
Datatype: "ISODate" on page 3319
37.4.2.1.2.1.11.2  Status <Sts>
Presence: [1..1]
Definition: Lock status of the party.
Datatype: "LockStatus1Code" on page 3262
CodeName Name Definition
LOCK Locked Party has been locked for operations.
ULCK Unlocked Party is ready for operations.
37.4.2.1.2.1.11.3  LockReason <LckRsn>
Presence: [0..*]
Definition: Specifies the underlying reason for the locking of the party.
Datatype: "Max35Text" on page 3328
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.017.001.02 PartyReportV02
Target2-Securities 2094 August 2026
```

