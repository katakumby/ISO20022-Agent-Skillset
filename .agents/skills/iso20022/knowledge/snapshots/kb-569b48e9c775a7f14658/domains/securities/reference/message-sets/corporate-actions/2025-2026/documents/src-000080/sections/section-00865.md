---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.20 Price", "16.1.20.9 PriceFormat76Choice", "16.1.20.9.3 AmountPricePerFinancialInstrumentQuantity <AmtPricPerFinInstrmQty>", "16.1.20.9.3.2 PriceValue <PricVal>"]
file_pages: [1083]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.20.9.3.2 PriceValue <PricVal>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1083 to 1083.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1083

```text
16.1.20.9.3.2  PriceValue <PricVal>
Presence: [1..1]
Definition: Value of the price.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
16.1.20.9.3.3  FinancialInstrumentQuantity <FinInstrmQty>
Presence: [1..1]
Definition: Quantity of financial instrument.
Impacted by: C13 "DigitalTokenUnitUsageRule"
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
16.1.20.9.4  AmountPricePerAmount <AmtPricPerAmt>
Presence: [1..1]
Definition: Price expressed as a ratio: amount price per amount.
AmountPricePerAmount <AmtPricPerAmt> contains the following AmountPricePerAmount2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AmountPriceType <AmtPricTp> [1..1] CodeSet 1084
   PriceValue <PricVal> [1..1] Amount C1 1084
   Amount <Amt> [1..1] Amount C1 1084
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1083 February 2026
```

