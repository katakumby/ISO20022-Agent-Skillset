---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.2 ReportGeneralDetails <RptGnlDtls>", "81.4.2.1 ReportIdentification <RptId>"]
file_pages: [2769]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.2.1 ReportIdentification <RptId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2769 to 2769.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2769

```text
Constraints
• ReportDatePeriodPresenceRule
At least on occurence of ReportDate or ReportPeriod must be present.
Following Must be True
    /ReportDate Must be present
 Or    /ReportPeriod Must be present
81.4.2.1  ReportIdentification <RptId>
Presence: [1..1]
Definition: Reference common to all pages of a report.
Datatype: "Max35Text" on page 3328
81.4.2.2  ReportDate <RptDt>
Presence: [0..1]
Definition: Date of the report.
ReportDate <RptDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
81.4.2.3  ReportPeriod <RptPrd>
Presence: [0..1]
Definition: Period for the report.
ReportPeriod <RptPrd> contains one of the following elements (see "DatePeriod1Choice" on
page 2907 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2908
Or   DateMonth <DtMnth> [1..1] YearMonth 2908
Or}   FromDateToDate <FrDtToDt> [1..1] ± 2908
81.4.2.4  Frequency <Frqcy>
Presence: [0..1]
Definition: Frequency of the statement.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2769 August 2026
```

