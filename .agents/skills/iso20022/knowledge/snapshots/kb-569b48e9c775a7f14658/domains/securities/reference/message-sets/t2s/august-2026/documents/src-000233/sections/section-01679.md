---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["60 reda.043.001.02 PartyAuditTrailReportV02", "60.4 Message Building Blocks", "60.4.2 ReportOrError <RptOrErr>", "60.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>", "60.4.2.1.1 PartyAuditTrailOrError <PtyAudtTrlOrErr>", "60.4.2.1.1.1 AuditTrail <AudtTrl>", "60.4.2.1.1.1.1 Record <Rcrd>", "60.4.2.1.1.1.1.10 LockStatus <LckSts>", "60.4.2.1.1.1.1.10.2 New <New>", "60.4.2.1.1.1.1.10.2.3 LockReason <LckRsn>"]
file_pages: [2327]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 60.4.2.1.1.1.1.10.2.3 LockReason <LckRsn>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2327 to 2327.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2327

```text
60.4.2.1.1.1.1.10.2.3  LockReason <LckRsn>
Presence: [0..*]
Definition: Specifies the underlying reason for the locking of the party.
Datatype: "Max35Text" on page 3328
60.4.2.1.1.1.1.11  Restriction <Rstrctn>
Presence: [1..1]
Definition: Defines the specific processing characteristics for a party to ensure configurability of specific
requirements, as prescribed by national legal and regulatory requirements and practices.
Restriction <Rstrctn> contains the following UpdateLogRestriction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1]  2327
     RestrictionType <RstrctnTp> [1..1]  2328
{Or       Code <Cd> [1..1] Text 2328
Or}       Proprietary <Prtry> [1..1] ± 2328
     ValidFrom <VldFr> [1..1] DateTime 2328
     ValidUntil <VldUntil> [0..1] DateTime 2328
   New <New> [1..1]  2328
     RestrictionType <RstrctnTp> [1..1]  2329
{Or       Code <Cd> [1..1] Text 2329
Or}       Proprietary <Prtry> [1..1] ± 2329
     ValidFrom <VldFr> [1..1] DateTime 2329
     ValidUntil <VldUntil> [0..1] DateTime 2330
60.4.2.1.1.1.1.11.1  Old <Od>
Presence: [1..1]
Definition: Old value before the update.
Old <Od> contains the following Restriction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RestrictionType <RstrctnTp> [1..1]  2328
{Or     Code <Cd> [1..1] Text 2328
Or}     Proprietary <Prtry> [1..1] ± 2328
   ValidFrom <VldFr> [1..1] DateTime 2328
   ValidUntil <VldUntil> [0..1] DateTime 2328
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities 2327 August 2026
```

