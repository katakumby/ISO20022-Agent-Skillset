---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["60 reda.043.001.02 PartyAuditTrailReportV02", "60.4 Message Building Blocks", "60.4.2 ReportOrError <RptOrErr>", "60.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>", "60.4.2.1.1 PartyAuditTrailOrError <PtyAudtTrlOrErr>", "60.4.2.1.1.1 AuditTrail <AudtTrl>", "60.4.2.1.1.1.1 Record <Rcrd>", "60.4.2.1.1.1.1.9 ResidenceType <ResTp>", "60.4.2.1.1.1.1.9.2 New <New>"]
file_pages: [2325]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 60.4.2.1.1.1.1.9.2 New <New>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2325 to 2325.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2325

```text
CodeName Name Definition
MXED Mixed Residence is mixed
60.4.2.1.1.1.1.9.2  New <New>
Presence: [1..1]
Definition: New value after the update.
Datatype: "ResidenceType1Code" on page 3288
CodeName Name Definition
DMST Domestic Residence is domestic.
FRGN Foreign Residence is foreign.
MXED Mixed Residence is mixed
60.4.2.1.1.1.1.10  LockStatus <LckSts>
Presence: [1..1]
Definition: Specifies whether the party is locked or not, and the reason for this status, when required.
LockStatus <LckSts> contains the following UpdateLogPartyLockStatus1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1]  2325
     ValidFrom <VldFr> [0..1] Date 2326
     Status <Sts> [1..1] CodeSet 2326
     LockReason <LckRsn> [0..*] Text 2326
   New <New> [1..1]  2326
     ValidFrom <VldFr> [0..1] Date 2326
     Status <Sts> [1..1] CodeSet 2326
     LockReason <LckRsn> [0..*] Text 2327
60.4.2.1.1.1.1.10.1  Old <Od>
Presence: [1..1]
Definition: Old value before the update.
Old <Od> contains the following PartyLockStatus1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [0..1] Date 2326
   Status <Sts> [1..1] CodeSet 2326
   LockReason <LckRsn> [0..*] Text 2326
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities 2325 August 2026
```

