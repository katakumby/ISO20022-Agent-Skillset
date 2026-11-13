---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.20 Price", "16.1.20.9 PriceFormat76Choice", "16.1.20.9.1 PercentagePrice <PctgPric>", "16.1.20.9.1.2 PriceValue <PricVal>"]
file_pages: [1082]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.20.9.1.2 PriceValue <PricVal>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1082 to 1082.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1082

```text
CodeName Name Definition
YIEL Yield Price expressed as a yield.
16.1.20.9.1.2  PriceValue <PricVal>
Presence: [1..1]
Definition: Specifies the value of price.
Datatype: "Percentage14Rate" on page 1247
16.1.20.9.2  AmountPrice <AmtPric>
Presence: [1..1]
Definition: Price expressed as a currency and amount.
AmountPrice <AmtPric> contains the following elements (see "AmountPrice3" on page 1067 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AmountPriceType <AmtPricTp> [1..1] CodeSet 1068
   PriceValue <PricVal> [1..1] Amount C1 1068
16.1.20.9.3  AmountPricePerFinancialInstrumentQuantity <AmtPricPerFinInstrmQty>
Presence: [1..1]
Definition: Price expressed as a ratio: amount price per financial instrument quantity.
AmountPricePerFinancialInstrumentQuantity <AmtPricPerFinInstrmQty> contains the following
AmountPricePerFinancialInstrumentQuantity10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AmountPriceType <AmtPricTp> [1..1] CodeSet 1082
   PriceValue <PricVal> [1..1] Amount C1 1083
   FinancialInstrumentQuantity <FinInstrmQty> [1..1] ± C13 1083
16.1.20.9.3.1  AmountPriceType <AmtPricTp>
Presence: [1..1]
Definition: Type of amount price.
Datatype: "AmountPriceType1Code" on page 1163
CodeName Name Definition
ACTU ActualAmount Price expressed as a currency and
amount per unit or per share.
DISC Discount Price expressed as a discount amount.
PLOT Lot Price expressed as an amount of money
per lot.
PREM Premium Price expressed as a premium.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1082 February 2026
```

