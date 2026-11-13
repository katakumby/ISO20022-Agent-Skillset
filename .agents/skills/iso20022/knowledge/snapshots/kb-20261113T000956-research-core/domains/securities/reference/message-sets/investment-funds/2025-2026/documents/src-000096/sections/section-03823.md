---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.34 Price", "66.1.34.1 UnitPrice22", "66.1.34.1.7 PriceDifferenceReason <PricDiffRsn>"]
file_pages: [5112]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.34.1.7 PriceDifferenceReason <PricDiffRsn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5112 to 5112.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5112

```text
66.1.34.1.7  PriceDifferenceReason <PricDiffRsn>
Presence: [0..1]
Definition: Reason why the price is different from the current market price.
Datatype: "Max350Text" on page 5403
66.1.34.2  UnitPrice19
Definition: Amount of money for which goods or services are offered, sold, or bought.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PriceType <PricTp> [1..1]  5112
{Or     Code <Cd> [1..1] CodeSet 5112
Or}     Proprietary <Prtry> [1..1] ± 5113
   Value <Val> [1..1] ± 5113
66.1.34.2.1  PriceType <PricTp>
Presence: [1..1]
Definition: Type of price.
PriceType <PricTp> contains one of the following UnitPriceType2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5112
Or}   Proprietary <Prtry> [1..1] ± 5113
66.1.34.2.1.1  Code <Cd>
Presence: [1..1]
Definition:  Type of price expressed as a code.
Datatype: "TypeOfPrice10Code" on page 5383
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5112 May 2026
```

