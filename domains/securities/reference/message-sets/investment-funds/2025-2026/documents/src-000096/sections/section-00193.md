---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.15 ValuationStatistics <ValtnSttstcs>", "14.4.10.1.15.3 PriceChange <PricChng>", "14.4.10.1.15.3.1 Amount <Amt>"]
file_pages: [280]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.15.3.1 Amount <Amt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 280 to 280.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 280

```text
14.4.10.1.15.3.1  Amount <Amt>
Presence: [0..1]
Definition: Amount by which the price has changed.
Impacted by: C3 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyAnd13DecimalAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
14.4.10.1.15.3.2  AmountSign <AmtSgn>
Presence: [0..1]
Definition: Indicates a positive or negative amount change.
Datatype: One of the following values must be used (see "PlusOrMinusIndicator" on page 5399):
• Meaning When True: Plus
• Meaning When False: Minus
14.4.10.1.15.3.3  Rate <Rate>
Presence: [0..1]
Definition: Rate by which the price has changed.
Datatype: "PercentageRate" on page 5401
14.4.10.1.15.4  Yield <Yld>
Presence: [0..1]
Definition: Rate of income from the financial instrument, usually calculated as total dividends or coupon
interest available to investors in the last year,divided by the current price.
Datatype: "PercentageRate" on page 5401
14.4.10.1.15.5  ByPredefinedTimePeriods <ByPrdfndTmPrds>
Presence: [0..1]
Definition: Information related to price variations, expressed using pre-defined periods.
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 280 May 2026
```

