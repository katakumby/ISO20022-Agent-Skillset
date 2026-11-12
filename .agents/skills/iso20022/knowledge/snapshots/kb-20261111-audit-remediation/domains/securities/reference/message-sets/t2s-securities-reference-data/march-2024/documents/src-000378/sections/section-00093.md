---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["12 reda.034.001.01 SecuritiesAuditTrailReportV01", "12.4 Message Building Blocks", "12.4.2 ReportOrError <RptOrErr>", "12.4.2.1 SecuritiesAuditTrailReport <SctiesAudtTrlRpt>", "12.4.2.1.1 SecuritiesAuditTrailOrError <SctiesAudtTrlOrErr>", "12.4.2.1.1.2 BusinessError <BizErr>", "12.4.2.1.1.2.1 Error <Err>", "12.4.2.1.1.2.1.1 Code <Cd>"]
file_pages: [142]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.034.001.01"]
---

# 12.4.2.1.1.2.1.1 Code <Cd>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 142 to 142.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 142

```text
12.4.2.1.1.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specification of the error, in coded form.
Datatype: "ExternalSystemErrorHandling1Code" on page 514
12.4.2.1.1.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specification of the error, in free format.
Datatype: "Max35Text" on page 534
12.4.2.1.1.2.2  Description <Desc>
Presence: [0..1]
Definition: Specification of the error, in free format.
Datatype: "Max140Text" on page 533
12.4.2.1.2  DatePeriod <DtPrd>
Presence: [0..1]
Definition: Period in dates for which the audit trail is provided.
DatePeriod <DtPrd> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 142
Or   ToDate <ToDt> [1..1] Date 142
Or   FromToDate <FrToDt> [1..1] ± 142
Or   EqualDate <EQDt> [1..1] Date 143
Or}   NotEqualDate <NEQDt> [1..1] Date 143
12.4.2.1.2.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 529
12.4.2.1.2.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 529
12.4.2.1.2.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.034.001.01 SecuritiesAuditTrailReportV01
Target2-Securities - Securities Reference Data 142 March 2024
```

