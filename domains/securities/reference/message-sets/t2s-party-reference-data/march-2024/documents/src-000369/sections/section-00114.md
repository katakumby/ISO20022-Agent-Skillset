---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 reda.043.001.02 PartyAuditTrailReportV02", "10.4 Message Building Blocks", "10.4.2 ReportOrError <RptOrErr>", "10.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>", "10.4.2.1.1 PartyAuditTrailOrError <PtyAudtTrlOrErr>", "10.4.2.1.1.1 AuditTrail <AudtTrl>", "10.4.2.1.1.1.1 Record <Rcrd>", "10.4.2.1.1.1.1.9 ResidenceType <ResTp>", "10.4.2.1.1.1.1.9.2 New <New>"]
file_pages: [148]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 10.4.2.1.1.1.1.9.2 New <New>

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 148 to 148.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 148

```text
CodeName Name Definition
MXED Mixed Residence is mixed
10.4.2.1.1.1.1.9.2  New <New>
Presence: [1..1]
Definition: New value after the update.
Datatype: "ResidenceType1Code" on page 184
CodeName Name Definition
DMST Domestic Residence is domestic.
FRGN Foreign Residence is foreign.
MXED Mixed Residence is mixed
10.4.2.1.1.1.1.10  LockStatus <LckSts>
Presence: [1..1]
Definition: Specifies whether the party is locked or not, and the reason for this status, when required.
LockStatus <LckSts> contains the following UpdateLogPartyLockStatus1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1]  148
     ValidFrom <VldFr> [0..1] Date 149
     Status <Sts> [1..1] CodeSet 149
     LockReason <LckRsn> [0..*] Text 149
   New <New> [1..1]  149
     ValidFrom <VldFr> [0..1] Date 149
     Status <Sts> [1..1] CodeSet 149
     LockReason <LckRsn> [0..*] Text 150
10.4.2.1.1.1.1.10.1  Old <Od>
Presence: [1..1]
Definition: Old value before the update.
Old <Od> contains the following PartyLockStatus1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [0..1] Date 149
   Status <Sts> [1..1] CodeSet 149
   LockReason <LckRsn> [0..*] Text 149
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
148 March 2024
```

