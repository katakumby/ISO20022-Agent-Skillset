---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.34 Price", "66.1.34.7 PriceInformation2", "66.1.34.7.3 Type <Tp>"]
file_pages: [5119]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.34.7.3 Type <Tp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5119 to 5119.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5119

```text
CodeName Name Definition
DISC Discount Price expressed as a number of
percentage points below par, for
example, a discount price of 2.0%
equals a price of 98 when par is 100.
PREM Premium Price expressed as a number of
percentage points above par, for
example, a premium price of 2.0%
equals a price of 102 when par is 100.
66.1.34.7.3  Type <Tp>
Presence: [1..1]
Warning   Either Type or ExtendedType must be present, but not both.
Definition: Type and information about a price.
Datatype: "TypeOfPrice11Code" on page 5384
CodeName Name Definition
BIDE Bid Price is the calculated bid price of a
dual-priced fund (offer-bid prices), that
is, the selling price of the units for the
investor.
OFFR Offer Price is the calculated offer price of a
dual-priced investment fund (offer-bid
prices), that is, the buying price of the
units for an investor.
NAVL NetAssetValue Price is the net asset value per unit that
is used either as a transacting price for a
single-priced investment fund class, or
as a notional price for the calculation of
other prices.
CREA Creation Price is the calculated creation price of a
dual-priced investment fund (creation-
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5119 May 2026
```

