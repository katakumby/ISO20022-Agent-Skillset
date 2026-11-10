---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.20 Price", "16.1.20.8 PriceFormat72Choice", "16.1.20.8.5 AmountPricePerAmount <AmtPricPerAmt>"]
file_pages: [1079]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.20.8.5 AmountPricePerAmount <AmtPricPerAmt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1079 to 1079.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1079

```text
FinancialInstrumentQuantity <FinInstrmQty> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1091 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1092
Or   FaceAmount <FaceAmt> [1..1] Amount 1092
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1092
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1092
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
16.1.20.8.5  AmountPricePerAmount <AmtPricPerAmt>
Presence: [1..1]
Definition: Price expressed as a ratio: amount price per amount.
AmountPricePerAmount <AmtPricPerAmt> contains the following AmountPricePerAmount2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AmountPriceType <AmtPricTp> [1..1] CodeSet 1079
   PriceValue <PricVal> [1..1] Amount C1 1079
   Amount <Amt> [1..1] Amount C1 1080
16.1.20.8.5.1  AmountPriceType <AmtPricTp>
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
16.1.20.8.5.2  PriceValue <PricVal>
Presence: [1..1]
Definition: Value of the price.
Impacted by: C1 "ActiveCurrency"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1079 February 2026
```

