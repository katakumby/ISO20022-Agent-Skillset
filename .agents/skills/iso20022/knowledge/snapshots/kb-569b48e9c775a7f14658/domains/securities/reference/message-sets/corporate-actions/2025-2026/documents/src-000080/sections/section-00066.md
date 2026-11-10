---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.4 PriceDetails <PricDtls>", "3.4.10.4.2 MinimumPrice <MinPric>"]
file_pages: [112]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.4.2 MinimumPrice <MinPric>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 112 to 112.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 112

```text
MaximumPrice <MaxPric> contains one of the following elements (see "PriceFormat73Choice" on
page 1085 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1085
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1085
     PriceValue <PricVal> [1..1] Rate 1085
Or   AmountPrice <AmtPric> [1..1] ± 1086
Or   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1086
Or}   IndexPoints <IndxPts> [1..1] Quantity 1086
3.4.10.4.2  MinimumPrice <MinPric>
Presence: [0..1]
Definition: Minimum or floor price at which a holder can bid, for example, on a Dutch auction offer.
MinimumPrice <MinPric> contains one of the following elements (see "PriceFormat73Choice" on
page 1085 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1085
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1085
     PriceValue <PricVal> [1..1] Rate 1085
Or   AmountPrice <AmtPric> [1..1] ± 1086
Or   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1086
Or}   IndexPoints <IndxPts> [1..1] Quantity 1086
3.4.10.4.3  FirstBidIncrementPrice <FrstBidIncrmtPric>
Presence: [0..1]
Definition: First acceptable price after the Minimum Price at which a holder can bid, for example on a
Dutch auction offer.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 112 February 2026
```

