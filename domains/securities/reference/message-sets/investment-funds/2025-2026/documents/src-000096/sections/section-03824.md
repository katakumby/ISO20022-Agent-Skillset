---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.34 Price", "66.1.34.2 UnitPrice19", "66.1.34.2.1 PriceType <PricTp>", "66.1.34.2.1.2 Proprietary <Prtry>"]
file_pages: [5113]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.34.2.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5113 to 5113.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5113

```text
CodeName Name Definition
cancellation prices) and the highest
possible buying price of the units before
the initial charge. The actual buying or
offer price, which includes charges, will
be higher.
CANC Cancellation Price is the calculated cancellation price
of a dual-priced investment fund
(creation-cancellation price), and the
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
66.1.34.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition:  Type of price expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.34.2.2  Value <Val>
Presence: [1..1]
Definition: Value of the price, that is, as a currency and value.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5113 May 2026
```

