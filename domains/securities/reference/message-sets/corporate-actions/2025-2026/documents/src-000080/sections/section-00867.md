---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.20 Price", "16.1.20.10 PriceFormat73Choice"]
file_pages: [1085]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.20.10 PriceFormat73Choice

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1085 to 1085.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1085

```text
16.1.20.10  PriceFormat73Choice
Definition: Choice between a percentage price or an amount price or an unspecified price or index
points.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1085
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1085
     PriceValue <PricVal> [1..1] Rate 1085
Or   AmountPrice <AmtPric> [1..1] ± 1086
Or   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1086
Or}   IndexPoints <IndxPts> [1..1] Quantity 1086
16.1.20.10.1  PercentagePrice <PctgPric>
Presence: [1..1]
Definition: Price expressed as a percentage.
PercentagePrice <PctgPric> contains the following PercentagePrice2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PercentagePriceType <PctgPricTp> [1..1] CodeSet 1085
   PriceValue <PricVal> [1..1] Rate 1085
16.1.20.10.1.1  PercentagePriceType <PctgPricTp>
Presence: [1..1]
Definition: Specifies the type of percentage price.
Datatype: "PriceRateType3Code" on page 1231
CodeName Name Definition
DISC Discount Price expressed as a number of
percentage points below par, for
example, a discount price of 2.0%
equals a price of 98 when par is 100.
PREM Premium Price expressed as a number of
percentage points above par, for
example, a premium price of 2.0%
equals a price of 102 when par is 100.
PRCT Percentage Price expressed as a percentage of par.
YIEL Yield Price expressed as a yield.
16.1.20.10.1.2  PriceValue <PricVal>
Presence: [1..1]
Definition: Specifies the value of price.
Datatype: "Percentage14Rate" on page 1247
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1085 February 2026
```

