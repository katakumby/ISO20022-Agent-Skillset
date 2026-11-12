---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["54 reda.034.001.01 SecuritiesAuditTrailReportV01", "54.4 Message Building Blocks", "54.4.2 ReportOrError <RptOrErr>", "54.4.2.1 SecuritiesAuditTrailReport <SctiesAudtTrlRpt>", "54.4.2.1.1 SecuritiesAuditTrailOrError <SctiesAudtTrlOrErr>", "54.4.2.1.1.1 AuditTrail <AudtTrl>", "54.4.2.1.1.1.3 NewFieldValue <NewFldVal>"]
file_pages: [2231]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.034.001.01"]
---

# 54.4.2.1.1.1.3 NewFieldValue <NewFldVal>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2231 to 2231.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2231

```text
Datatype: "Max350Text" on page 3328
54.4.2.1.1.1.3  NewFieldValue <NewFldVal>
Presence: [1..1]
Definition: Value of the field after the change.
Datatype: "Max350Text" on page 3328
54.4.2.1.1.1.4  OperationTimeStamp <OprTmStmp>
Presence: [1..1]
Definition: Timestamp of the change.
Datatype: "ISODateTime" on page 3320
54.4.2.1.1.1.5  InstructingUser <InstgUsr>
Presence: [1..1]
Definition: User who instructed the change.
Datatype: "Max256Text" on page 3327
54.4.2.1.1.1.6  ApprovingUser <ApprvgUsr>
Presence: [0..1]
Definition: User who approved the change instructed by the instructing user.
Datatype: "Max256Text" on page 3327
54.4.2.1.1.2  BusinessError <BizErr>
Presence: [1..*]
Definition: Business error resulting from a rejection.
BusinessError <BizErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  2231
{Or     Code <Cd> [1..1] CodeSet 2232
Or}     Proprietary <Prtry> [1..1] Text 2232
   Description <Desc> [0..1] Text 2232
54.4.2.1.1.2.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Error <Err> contains one of the following ErrorHandling3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2232
Or}   Proprietary <Prtry> [1..1] Text 2232
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.034.001.01 SecuritiesAuditTrailReportV01
Target2-Securities 2231 August 2026
```

