---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["57 reda.037.001.01 SecuritiesAccountAuditTrailReportV01", "57.4 Message Building Blocks", "57.4.2 ReportOrError <RptOrErr>", "57.4.2.1 SecuritiesAccountAuditTrailReport <SctiesAcctAudtTrlRpt>", "57.4.2.1.1 SecuritiesAccountAuditTrailOrError <SctiesAcctAudtTrlOrErr>", "57.4.2.1.1.1 AuditTrail <AudtTrl>"]
file_pages: [2251]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.037.001.01"]
---

# 57.4.2.1.1.1 AuditTrail <AudtTrl>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2251 to 2251.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2251

```text
SecuritiesAccountAuditTrailOrError <SctiesAcctAudtTrlOrErr> contains one of the following
AuditTrailOrBusinessError6Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AuditTrail <AudtTrl> [1..*]  2251
     FieldName <FldNm> [1..1] Text 2251
     OldFieldValue <OdFldVal> [1..1] Text 2251
     NewFieldValue <NewFldVal> [1..1] Text 2252
     OperationTimeStamp <OprTmStmp> [1..1] DateTime 2252
     InstructingUser <InstgUsr> [1..1] Text 2252
     ApprovingUser <ApprvgUsr> [0..1] Text 2252
Or}   BusinessError <BizErr> [1..*]  2252
     Error <Err> [1..1]  2252
{Or       Code <Cd> [1..1] CodeSet 2253
Or}       Proprietary <Prtry> [1..1] Text 2253
     Description <Desc> [0..1] Text 2253
57.4.2.1.1.1  AuditTrail <AudtTrl>
Presence: [1..*]
Definition: Details of the static data audit trail retrieved from the system.
AuditTrail <AudtTrl> contains the following AuditTrail1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FieldName <FldNm> [1..1] Text 2251
   OldFieldValue <OdFldVal> [1..1] Text 2251
   NewFieldValue <NewFldVal> [1..1] Text 2252
   OperationTimeStamp <OprTmStmp> [1..1] DateTime 2252
   InstructingUser <InstgUsr> [1..1] Text 2252
   ApprovingUser <ApprvgUsr> [0..1] Text 2252
57.4.2.1.1.1.1  FieldName <FldNm>
Presence: [1..1]
Definition: Name of the field whose value has been changed.
Datatype: "Max35Text" on page 3328
57.4.2.1.1.1.2  OldFieldValue <OdFldVal>
Presence: [1..1]
Definition: Value of the field before the change.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.037.001.01
SecuritiesAccountAuditTrailReportV01
Target2-Securities 2251 August 2026
```

