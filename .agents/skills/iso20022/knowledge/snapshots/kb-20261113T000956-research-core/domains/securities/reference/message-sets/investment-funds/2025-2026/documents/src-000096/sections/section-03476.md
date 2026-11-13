---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.3 InvestmentFundTransaction3", "66.1.26.3.22 PartiallyExecutedIndicator <PrtlyExctdInd>"]
file_pages: [4726]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.3.22 PartiallyExecutedIndicator <PrtlyExctdInd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4726 to 4726.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4726

```text
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.26.3.22  PartiallyExecutedIndicator <PrtlyExctdInd>
Presence: [1..1]
Definition: Indicates whether the order has been partially executed, ie, the confirmed quantity does not
match the ordered quantity for a given financial instrument.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.26.3.23  PriceDetails <PricDtls>
Presence: [0..1]
Definition: Price at which the order was executed.
PriceDetails <PricDtls> contains the following UnitPrice11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Type <Tp> [1..1] CodeSet 4726
Or}   ExtendedType <XtndedTp> [1..1] Text 4727
   Value <Val> [1..1] ± 4727
   PriceMethod <PricMtd> [0..1] CodeSet 4728
66.1.26.3.23.1  Type <Tp>
Presence: [1..1]
Warning   Either Type or ExtendedType must be present, but not both.
Definition: Type and information about a price.
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4726 May 2026
```

