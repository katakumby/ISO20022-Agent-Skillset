---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03", "14.4 Message Building Blocks", "14.4.2 EquityTransparencyData <EqtyTrnsprncyData>", "14.4.2.10 Statistics <Sttstcs>"]
file_pages: [223]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.044.001.03"]
---

# 14.4.2.10 Statistics <Sttstcs>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 223 to 223.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 223

```text
CodeName Name Definition
SINT SystematicInternaliser Results of calculations supporting
Systematic Internaliser regime.
FFWK FirstFourWeeks Calculation based on first Four Weeks of
Trading for Equity Instruments.
ESTM Estimated Estimation for New Equity Instruments.
14.4.2.10  Statistics <Sttstcs>
Presence: [0..1]
Definition: Statistics for a financial instrument generated as part of transparency calculations.
Statistics <Sttstcs> contains the following StatisticsTransparency3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AverageDailyTurnover <AvrgDalyTrnvr> [0..1] Amount C1, C3 223
   AverageTransactionValue <AvrgTxVal> [0..1] Amount C1, C3 224
   LargeInScale <LrgInScale> [0..1] Quantity 224
   StandardMarketSize <StdMktSz> [0..1] Quantity 224
   AverageDailyNumberOfTransactions
<AvrgDalyNbOfTxs>
[0..1] Quantity 224
   TotalNumberOfTransactionsExecuted
<TtlNbOfTxsExctd>
[0..1] Quantity 224
   TotalVolumeOfTransactionsExecuted
<TtlVolOfTxsExctd>
[0..1] Quantity 225
   TotalNumberOfTradingDays <TtlNbOfTradgDays> [0..1] Quantity 225
14.4.2.10.1  AverageDailyTurnover <AvrgDalyTrnvr>
Presence: [0..1]
Definition: Average Daily Turnover for the instrument in Euros.
Impacted by: C1 "ActiveCurrency", C3 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 415
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Approved by the Securities SEG on 17 July 2025 auth.044.001.03
FinancialInstrumentReportingEquityTradingActivityR
esultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
223 July 2025
```

