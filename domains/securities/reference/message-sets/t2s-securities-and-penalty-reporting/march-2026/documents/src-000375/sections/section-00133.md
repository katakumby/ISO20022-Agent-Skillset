---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.2 ReportGeneralDetails <RptGnlDtls>", "6.4.2.1 ReportIdentification <RptId>"]
file_pages: [187]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.2.1 ReportIdentification <RptId>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 187 to 187.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 187

```text
Constraints
• ReportDatePeriodPresenceRule
At least on occurence of ReportDate or ReportPeriod must be present.
Following Must be True
    /ReportDate Must be present
 Or    /ReportPeriod Must be present
6.4.2.1  ReportIdentification <RptId>
Presence: [1..1]
Definition: Reference common to all pages of a report.
Datatype: "Max35Text" on page 557
6.4.2.2  ReportDate <RptDt>
Presence: [0..1]
Definition: Date of the report.
ReportDate <RptDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 321 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 321
Or}   DateTime <DtTm> [1..1] DateTime 321
6.4.2.3  ReportPeriod <RptPrd>
Presence: [0..1]
Definition: Period for the report.
ReportPeriod <RptPrd> contains one of the following elements (see "DatePeriod1Choice" on
page 315 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 316
Or   DateMonth <DtMnth> [1..1] YearMonth 316
Or}   FromDateToDate <FrDtToDt> [1..1] ± 316
6.4.2.4  Frequency <Frqcy>
Presence: [0..1]
Definition: Frequency of the statement.
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 187 March 2026
```

