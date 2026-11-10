---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.20 Price", "16.1.20.6 PriceFormat78Choice"]
file_pages: [1070]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.20.6 PriceFormat78Choice

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1070 to 1070.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1070

```text
Definition: Price expressed as an index points.
Datatype: "DecimalNumber" on page 1246
16.1.20.6  PriceFormat78Choice
Definition: Choice between a percentage price or an amount price or an unspecified price or an amount
price per amount or an amount price per financial instrument quantity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1070
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1070
     PriceValue <PricVal> [1..1] Rate 1071
Or   AmountPrice <AmtPric> [1..1] ± 1071
Or   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1071
Or   AmountPricePerFinancialInstrumentQuantity
<AmtPricPerFinInstrmQty>
[1..1]  1071
     AmountPriceType <AmtPricTp> [1..1] CodeSet 1072
     PriceValue <PricVal> [1..1] Amount C1 1072
     FinancialInstrumentQuantity <FinInstrmQty> [1..1] ± C13 1072
Or   AmountPricePerAmount <AmtPricPerAmt> [1..1]  1073
     AmountPriceType <AmtPricTp> [1..1] CodeSet 1073
     PriceValue <PricVal> [1..1] Amount C1 1073
     Amount <Amt> [1..1] Amount C1 1074
Or}   IndexPoints <IndxPts> [1..1] Quantity 1074
16.1.20.6.1  PercentagePrice <PctgPric>
Presence: [1..1]
Definition: Price expressed as a percentage.
PercentagePrice <PctgPric> contains the following PercentagePrice2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PercentagePriceType <PctgPricTp> [1..1] CodeSet 1070
   PriceValue <PricVal> [1..1] Rate 1071
16.1.20.6.1.1  PercentagePriceType <PctgPricTp>
Presence: [1..1]
Definition: Specifies the type of percentage price.
Datatype: "PriceRateType3Code" on page 1231
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1070 February 2026
```

