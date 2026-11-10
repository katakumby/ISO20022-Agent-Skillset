---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.20 Price", "16.1.20.9 PriceFormat76Choice", "16.1.20.9.1 PercentagePrice <PctgPric>"]
file_pages: [1081]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.20.9.1 PercentagePrice <PctgPric>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1081 to 1081.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1081

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1081
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1081
     PriceValue <PricVal> [1..1] Rate 1082
Or   AmountPrice <AmtPric> [1..1] ± 1082
Or   AmountPricePerFinancialInstrumentQuantity
<AmtPricPerFinInstrmQty>
[1..1]  1082
     AmountPriceType <AmtPricTp> [1..1] CodeSet 1082
     PriceValue <PricVal> [1..1] Amount C1 1083
     FinancialInstrumentQuantity <FinInstrmQty> [1..1] ± C13 1083
Or   AmountPricePerAmount <AmtPricPerAmt> [1..1]  1083
     AmountPriceType <AmtPricTp> [1..1] CodeSet 1084
     PriceValue <PricVal> [1..1] Amount C1 1084
     Amount <Amt> [1..1] Amount C1 1084
Or}   IndexPoints <IndxPts> [1..1] Quantity 1084
16.1.20.9.1  PercentagePrice <PctgPric>
Presence: [1..1]
Definition: Price expressed as a percentage.
PercentagePrice <PctgPric> contains the following PercentagePrice2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PercentagePriceType <PctgPricTp> [1..1] CodeSet 1081
   PriceValue <PricVal> [1..1] Rate 1082
16.1.20.9.1.1  PercentagePriceType <PctgPricTp>
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1081 February 2026
```

