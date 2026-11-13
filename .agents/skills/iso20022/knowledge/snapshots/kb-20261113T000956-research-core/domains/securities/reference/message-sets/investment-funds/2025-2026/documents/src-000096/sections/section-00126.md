---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.4 Message Building Blocks", "13.4.3 PreviousReference <PrvsRef>", "13.4.9.14 PriceDetails <PricDtls>", "13.4.9.14.8 EstimatedPriceIndicator <EstmtdPricInd>"]
file_pages: [192]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.4.9.14.8 EstimatedPriceIndicator <EstmtdPricInd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 192 to 192.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 192

```text
Definition: Ratio applied on the non-adjusted price.
Datatype: "PercentageRate" on page 5401
13.4.9.14.8  EstimatedPriceIndicator <EstmtdPricInd>
Presence: [1..1]
Definition: Indicates whether the price is an estimated price.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
13.4.9.14.9  NumberOfDaysAccrued <NbOfDaysAcrd>
Presence: [0..1]
Definition: Specifies the number of days from trade date that the counterparty on the other side of the
trade should "given up" or divulged.
Datatype: "Number" on page 5400
13.4.9.14.10  TaxableIncomePerShare <TaxblIncmPerShr>
Presence: [0..1]
Definition: Amount included in the NAV that corresponds to gains directly or indirectly derived from
interest payment in the scope of the European Directive on taxation of savings income in the form of
interest payments.
Impacted by: C3 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyAnd13DecimalAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
13.4.9.14.11  TaxableIncomePerShareCalculated <TaxblIncmPerShrClctd>
Presence: [0..1]
Definition: Specifies whether the fund calculates a taxable interest per share (TIS).
TaxableIncomePerShareCalculated <TaxblIncmPerShrClctd> contains one of the following
TaxableIncomePerShareCalculated3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 193
Or}   Proprietary <Prtry> [1..1] Text 193
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 192 May 2026
```

