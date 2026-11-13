---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03", "15.4 Message Building Blocks", "15.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "15.4.2.6 Liquidity <Lqdty>"]
file_pages: [241]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.045.001.03"]
---

# 15.4.2.6 Liquidity <Lqdty>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 241 to 241.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 241

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
15.4.2.6  Liquidity <Lqdty>
Presence: [0..1]
Definition: Flag to say if this ISIN is liquid or not post calculations.
Usage:
When not present, this field should be treated as not applicable.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 451):
• Meaning When True: True
• Meaning When False: False
15.4.2.7  PreTradeLargeInScaleThreshold <PreTradLrgInScaleThrshld>
Presence: [0..1]
Definition: The pre-trade Large in Scale threshold.
PreTradeLargeInScaleThreshold <PreTradLrgInScaleThrshld> contains one of the following
elements (see "TonsOrCurrency2Choice" on page 338 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Number <Nb> [1..1] Quantity 338
Or}   Amount <Amt> [1..1] Amount C2, C5 338
15.4.2.8  PostTradeLargeInScaleThreshold <PstTradLrgInScaleThrshld>
Presence: [0..1]
Definition: The post-trade Large in Scale threshold.
PostTradeLargeInScaleThreshold <PstTradLrgInScaleThrshld> contains one of the following
elements (see "TonsOrCurrency2Choice" on page 338 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Number <Nb> [1..1] Quantity 338
Or}   Amount <Amt> [1..1] Amount C2, C5 338
Approved by the Securities SEG on 17 July 2025 auth.045.001.03
FinancialInstrumentReportingNonEquityTradingActi
vityResultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
241 July 2025
```

