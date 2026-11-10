---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.14 PriceDetails <PricDtls>", "14.4.10.1.14.1 PriceType <PricTp>", "14.4.10.1.14.1.2 Proprietary <Prtry>"]
file_pages: [259]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.14.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 259 to 259.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 259

```text
CodeName Name Definition
lowest possible valuation of the units on
any one-day. The actual selling or bid
price is usually higher.
INTE Interim Price is the non-official interim price
given to an investor before the executed
price.
SWNG Swing Price is the calculated net asset value
price of a single-priced investment fund.
The price is adjusted to take into account
the dealing costs due to individual large
deals, or due to a significant imbalance
in volumes of subscriptions vs
redemptions, as an alternative to dilution
levy.
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
GUAR Guaranteed Price is a guaranteed price.
ENAV EstimatedNAV Price is an estimated net asset value per
unit.
14.4.10.1.14.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type and information about a price expressed as an extended type.
Datatype: "Max350Text" on page 5403
14.4.10.1.14.2  PriceMethod <PricMtd>
Presence: [0..1]
Definition: Type of pricing calculation method.
Datatype: "PriceMethod1Code" on page 5343
CodeName Name Definition
FORW ForwardPrice Price will be calculated after the close of
the dealing period. An investor,
therefore, does not know the exact buy
or sell price.
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 259 May 2026
```

