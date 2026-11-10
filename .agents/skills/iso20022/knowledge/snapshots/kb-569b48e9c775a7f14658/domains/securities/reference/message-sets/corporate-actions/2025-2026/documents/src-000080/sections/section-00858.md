---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.20 Price", "16.1.20.8 PriceFormat72Choice"]
file_pages: [1076]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.20.8 PriceFormat72Choice

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1076 to 1076.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1076

```text
CodeName Name Definition
UKWN Unknown Price is unknown by the sender or has
not been established.
16.1.20.8  PriceFormat72Choice
Definition: Choice between a percentage price or an amount price or an unspecified price or an amount
price per amount or an amount price per financial instrument quantity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1076
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1076
     PriceValue <PricVal> [1..1] Rate 1077
Or   AmountPrice <AmtPric> [1..1] ± 1077
Or   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1077
Or   AmountPricePerFinancialInstrumentQuantity
<AmtPricPerFinInstrmQty>
[1..1]  1077
     AmountPriceType <AmtPricTp> [1..1] CodeSet 1078
     PriceValue <PricVal> [1..1] Amount C1 1078
     FinancialInstrumentQuantity <FinInstrmQty> [1..1] ± C13 1078
Or   AmountPricePerAmount <AmtPricPerAmt> [1..1]  1079
     AmountPriceType <AmtPricTp> [1..1] CodeSet 1079
     PriceValue <PricVal> [1..1] Amount C1 1079
     Amount <Amt> [1..1] Amount C1 1080
Or}   IndexPoints <IndxPts> [1..1] Quantity 1080
16.1.20.8.1  PercentagePrice <PctgPric>
Presence: [1..1]
Definition: Price expressed as a percentage.
PercentagePrice <PctgPric> contains the following PercentagePrice2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PercentagePriceType <PctgPricTp> [1..1] CodeSet 1076
   PriceValue <PricVal> [1..1] Rate 1077
16.1.20.8.1.1  PercentagePriceType <PctgPricTp>
Presence: [1..1]
Definition: Specifies the type of percentage price.
Datatype: "PriceRateType3Code" on page 1231
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1076 February 2026
```

