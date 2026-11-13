---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.14 PriceDetails <PricDtls>", "14.4.10.1.14.8 EstimatedPriceIndicator <EstmtdPricInd>"]
file_pages: [261]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.14.8 EstimatedPriceIndicator <EstmtdPricInd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 261 to 261.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 261

```text
Datatype: "PercentageRate" on page 5401
14.4.10.1.14.8  EstimatedPriceIndicator <EstmtdPricInd>
Presence: [1..1]
Definition: Indicates whether the price is an estimated price.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
14.4.10.1.14.9  NumberOfDaysAccrued <NbOfDaysAcrd>
Presence: [0..1]
Definition: Specifies the number of days from trade date that the counterparty on the other side of the
trade should "given up" or divulged.
Datatype: "Number" on page 5400
14.4.10.1.14.10  TaxableIncomePerShare <TaxblIncmPerShr>
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
14.4.10.1.14.11  TaxableIncomePerShareCalculated <TaxblIncmPerShrClctd>
Presence: [0..1]
Definition: Specifies whether the fund calculates a taxable interest per share (TIS).
TaxableIncomePerShareCalculated <TaxblIncmPerShrClctd> contains one of the following
TaxableIncomePerShareCalculated3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 261
Or}   Proprietary <Prtry> [1..1] Text 262
14.4.10.1.14.11.1  Code <Cd>
Presence: [1..1]
Definition: Specifies whether the fund calculates a taxable interest per share (TIS) expressed as a code.
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 261 May 2026
```

