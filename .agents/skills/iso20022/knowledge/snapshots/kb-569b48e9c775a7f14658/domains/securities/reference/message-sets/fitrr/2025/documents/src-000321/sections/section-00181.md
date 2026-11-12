---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03", "14.4 Message Building Blocks", "14.4.2 EquityTransparencyData <EqtyTrnsprncyData>", "14.4.2.7 ApplicationPeriod <ApplPrd>"]
file_pages: [222]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.044.001.03"]
---

# 14.4.2.7 ApplicationPeriod <ApplPrd>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 222 to 222.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 222

```text
ReportingPeriod <RptgPrd> contains one of the following elements (see "Period4Choice" on
page 322 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 322
Or   FromDate <FrDt> [1..1] Date 323
Or   ToDate <ToDt> [1..1] Date 323
Or}   FromDateToDate <FrDtToDt> [1..1] ± 323
14.4.2.7  ApplicationPeriod <ApplPrd>
Presence: [0..1]
Definition: Period of application of the results.
ApplicationPeriod <ApplPrd> contains one of the following elements (see "Period4Choice" on
page 322 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 322
Or   FromDate <FrDt> [1..1] Date 323
Or   ToDate <ToDt> [1..1] Date 323
Or}   FromDateToDate <FrDtToDt> [1..1] ± 323
14.4.2.8  Liquidity <Lqdty>
Presence: [0..1]
Definition: Flag to say if this ISIN is liquid or not post calculations.
Usage:
When not present, this field should be treated as not applicable.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 451):
• Meaning When True: True
• Meaning When False: False
14.4.2.9  Methodology <Mthdlgy>
Presence: [0..1]
Definition: Methodology that has been used to calculate the result.
Datatype: "TransparencyMethodology2Code" on page 447
CodeName Name Definition
YEAR Year Calculation based on yearly cycle.
Approved by the Securities SEG on 17 July 2025 auth.044.001.03
FinancialInstrumentReportingEquityTradingActivityR
esultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
222 July 2025
```

