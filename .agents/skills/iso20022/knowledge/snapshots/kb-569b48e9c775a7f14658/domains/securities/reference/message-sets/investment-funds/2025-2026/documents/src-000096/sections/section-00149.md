---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.4 Message Building Blocks", "13.4.3 PreviousReference <PrvsRef>", "13.4.9.15 ValuationStatistics <ValtnSttstcs>", "13.4.9.15.5 ByPredefinedTimePeriods <ByPrdfndTmPrds>", "13.4.9.15.5.5 FiveYearPriceChange <FiveYrPricChng>", "13.4.9.15.5.5.1 Amount <Amt>"]
file_pages: [216]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.4.9.15.5.5.1 Amount <Amt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 216 to 216.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 216

```text
Definition: Change in price over a five year period.
Impacted by: C5 "AmountAndOrRateRule", C6 "AmountSignRule"
FiveYearPriceChange <FiveYrPricChng> contains the following PriceValueChange1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [0..1] Amount C3 216
   AmountSign <AmtSgn> [0..1] Indicator 216
   Rate <Rate> [0..1] Rate 216
Constraints
• AmountAndOrRateRule
If Amount is not present, then Rate is mandatory. If Amount is present, then Rate is optional.
• AmountSignRule
If Amount is present, then AmountSign is optional. If Amount is not present, then AmountSign is not
allowed.
13.4.9.15.5.5.1  Amount <Amt>
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
13.4.9.15.5.5.2  AmountSign <AmtSgn>
Presence: [0..1]
Definition: Indicates a positive or negative amount change.
Datatype: One of the following values must be used (see "PlusOrMinusIndicator" on page 5399):
• Meaning When True: Plus
• Meaning When False: Minus
13.4.9.15.5.5.3  Rate <Rate>
Presence: [0..1]
Definition: Rate by which the price has changed.
Datatype: "PercentageRate" on page 5401
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 216 May 2026
```

