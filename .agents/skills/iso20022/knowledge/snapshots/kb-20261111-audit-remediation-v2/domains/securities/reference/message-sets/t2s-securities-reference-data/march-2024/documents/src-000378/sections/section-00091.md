---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["12 reda.034.001.01 SecuritiesAuditTrailReportV01", "12.4 Message Building Blocks", "12.4.2 ReportOrError <RptOrErr>", "12.4.2.1 SecuritiesAuditTrailReport <SctiesAudtTrlRpt>", "12.4.2.1.1 SecuritiesAuditTrailOrError <SctiesAudtTrlOrErr>", "12.4.2.1.1.1 AuditTrail <AudtTrl>"]
file_pages: [140]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.034.001.01"]
---

# 12.4.2.1.1.1 AuditTrail <AudtTrl>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 140 to 140.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 140

```text
SecuritiesAuditTrailOrError <SctiesAudtTrlOrErr> contains one of the following
AuditTrailOrBusinessError6Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AuditTrail <AudtTrl> [1..*]  140
     FieldName <FldNm> [1..1] Text 140
     OldFieldValue <OdFldVal> [1..1] Text 140
     NewFieldValue <NewFldVal> [1..1] Text 141
     OperationTimeStamp <OprTmStmp> [1..1] DateTime 141
     InstructingUser <InstgUsr> [1..1] Text 141
     ApprovingUser <ApprvgUsr> [0..1] Text 141
Or}   BusinessError <BizErr> [1..*]  141
     Error <Err> [1..1]  141
{Or       Code <Cd> [1..1] CodeSet 142
Or}       Proprietary <Prtry> [1..1] Text 142
     Description <Desc> [0..1] Text 142
12.4.2.1.1.1  AuditTrail <AudtTrl>
Presence: [1..*]
Definition: Details of the static data audit trail retrieved from the system.
AuditTrail <AudtTrl> contains the following AuditTrail1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FieldName <FldNm> [1..1] Text 140
   OldFieldValue <OdFldVal> [1..1] Text 140
   NewFieldValue <NewFldVal> [1..1] Text 141
   OperationTimeStamp <OprTmStmp> [1..1] DateTime 141
   InstructingUser <InstgUsr> [1..1] Text 141
   ApprovingUser <ApprvgUsr> [0..1] Text 141
12.4.2.1.1.1.1  FieldName <FldNm>
Presence: [1..1]
Definition: Name of the field whose value has been changed.
Datatype: "Max35Text" on page 534
12.4.2.1.1.1.2  OldFieldValue <OdFldVal>
Presence: [1..1]
Definition: Value of the field before the change.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.034.001.01 SecuritiesAuditTrailReportV01
Target2-Securities - Securities Reference Data 140 March 2024
```

