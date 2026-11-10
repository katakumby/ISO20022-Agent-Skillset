---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.15 ValuationStatistics <ValtnSttstcs>", "14.4.10.1.15.2 PriceTypeChangeBasis <PricTpChngBsis>", "14.4.10.1.15.2.2 AdditionalInformation <AddtlInf>"]
file_pages: [279]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.15.2.2 AdditionalInformation <AddtlInf>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 279 to 279.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 279

```text
CodeName Name Definition
redemptions, as an alternative to dilution
levy.
OTHR Other Price is another type of price, which is
not explicitly defined.
MIDD Mid Price is the average price between the
bid and offer prices.
RINV Reinvestment Price is the price used when reinvesting
units after distribution.
SWIC Switch Price is the price used when transferring
units between products.
DDVR DailyDividendRate Price is the net income of a financial
instrument, calculated on each dealing
day, and divided by all the units
outstanding on that day.
ACTU Actual True offer price.
NAUP NonAdjustedUnpublished The original NAV before the price of the
investment fund was swung.
14.4.10.1.15.2.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the type of charge.
Datatype: "Max350Text" on page 5403
14.4.10.1.15.3  PriceChange <PricChng>
Presence: [1..1]
Definition: Change in price since the previous valuation date.
Impacted by: C5 "AmountAndOrRateRule", C6 "AmountSignRule"
PriceChange <PricChng> contains the following PriceValueChange1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [0..1] Amount C3 280
   AmountSign <AmtSgn> [0..1] Indicator 280
   Rate <Rate> [0..1] Rate 280
Constraints
• AmountAndOrRateRule
If Amount is not present, then Rate is mandatory. If Amount is present, then Rate is optional.
• AmountSignRule
If Amount is present, then AmountSign is optional. If Amount is not present, then AmountSign is not
allowed.
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 279 May 2026
```

