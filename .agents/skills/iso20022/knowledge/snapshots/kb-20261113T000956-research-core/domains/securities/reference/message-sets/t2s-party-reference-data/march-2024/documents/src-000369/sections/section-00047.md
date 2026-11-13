---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 reda.017.001.02 PartyReportV02", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 PartyReport <PtyRpt>", "5.4.2.1.2 PartyOrError <PtyOrErr>", "5.4.2.1.2.1 SystemParty <SysPty>", "5.4.2.1.2.1.10 ResidenceType <ResTp>"]
file_pages: [57]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.017.001.02"]
---

# 5.4.2.1.2.1.10 ResidenceType <ResTp>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 57 to 57.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 57

```text
Definition: Specifies the short name of the organisation.
Datatype: "Max35Text" on page 188
5.4.2.1.2.1.10  ResidenceType <ResTp>
Presence: [0..1]
Definition: Specifies the type of residence where the party has its permanent home or principal
establishment.
Datatype: "ResidenceType1Code" on page 184
CodeName Name Definition
DMST Domestic Residence is domestic.
FRGN Foreign Residence is foreign.
MXED Mixed Residence is mixed
5.4.2.1.2.1.11  LockStatus <LckSts>
Presence: [0..1]
Definition: Specifies whether the party is locked or not, and the reason for this status, when required.
LockStatus <LckSts> contains the following PartyLockStatus1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [0..1] Date 57
   Status <Sts> [1..1] CodeSet 57
   LockReason <LckRsn> [0..*] Text 57
5.4.2.1.2.1.11.1  ValidFrom <VldFr>
Presence: [0..1]
Definition: Specifies the date from which the lock status is valid.
Datatype: "ISODate" on page 184
5.4.2.1.2.1.11.2  Status <Sts>
Presence: [1..1]
Definition: Lock status of the party.
Datatype: "LockStatus1Code" on page 182
CodeName Name Definition
LOCK Locked Party has been locked for operations.
ULCK Unlocked Party is ready for operations.
5.4.2.1.2.1.11.3  LockReason <LckRsn>
Presence: [0..*]
Definition: Specifies the underlying reason for the locking of the party.
Datatype: "Max35Text" on page 188
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.017.001.02 PartyReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
57 March 2024
```

