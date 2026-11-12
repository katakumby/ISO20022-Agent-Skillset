---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["12 reda.034.001.01 SecuritiesAuditTrailReportV01", "12.4 Message Building Blocks", "12.4.2 ReportOrError <RptOrErr>", "12.4.2.1 SecuritiesAuditTrailReport <SctiesAudtTrlRpt>", "12.4.2.1.1 SecuritiesAuditTrailOrError <SctiesAudtTrlOrErr>", "12.4.2.1.1.1 AuditTrail <AudtTrl>", "12.4.2.1.1.1.3 NewFieldValue <NewFldVal>"]
file_pages: [141]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.034.001.01"]
---

# 12.4.2.1.1.1.3 NewFieldValue <NewFldVal>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 141 to 141.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 141

```text
Datatype: "Max350Text" on page 534
12.4.2.1.1.1.3  NewFieldValue <NewFldVal>
Presence: [1..1]
Definition: Value of the field after the change.
Datatype: "Max350Text" on page 534
12.4.2.1.1.1.4  OperationTimeStamp <OprTmStmp>
Presence: [1..1]
Definition: Timestamp of the change.
Datatype: "ISODateTime" on page 529
12.4.2.1.1.1.5  InstructingUser <InstgUsr>
Presence: [1..1]
Definition: User who instructed the change.
Datatype: "Max256Text" on page 534
12.4.2.1.1.1.6  ApprovingUser <ApprvgUsr>
Presence: [0..1]
Definition: User who approved the change instructed by the instructing user.
Datatype: "Max256Text" on page 534
12.4.2.1.1.2  BusinessError <BizErr>
Presence: [1..*]
Definition: Business error resulting from a rejection.
BusinessError <BizErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  141
{Or     Code <Cd> [1..1] CodeSet 142
Or}     Proprietary <Prtry> [1..1] Text 142
   Description <Desc> [0..1] Text 142
12.4.2.1.1.2.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Error <Err> contains one of the following ErrorHandling3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 142
Or}   Proprietary <Prtry> [1..1] Text 142
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.034.001.01 SecuritiesAuditTrailReportV01
Target2-Securities - Securities Reference Data 141 March 2024
```

