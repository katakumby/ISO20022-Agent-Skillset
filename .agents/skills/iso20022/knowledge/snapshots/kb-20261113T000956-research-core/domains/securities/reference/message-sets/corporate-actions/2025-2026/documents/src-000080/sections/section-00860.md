---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.20 Price", "16.1.20.8 PriceFormat72Choice", "16.1.20.8.4 AmountPricePerFinancialInstrumentQuantity <AmtPricPerFinInstrmQty>", "16.1.20.8.4.1 AmountPriceType <AmtPricTp>"]
file_pages: [1078]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.20.8.4.1 AmountPriceType <AmtPricTp>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1078 to 1078.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1078

```text
AmountPricePerFinancialInstrumentQuantity <AmtPricPerFinInstrmQty> contains the following
AmountPricePerFinancialInstrumentQuantity10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AmountPriceType <AmtPricTp> [1..1] CodeSet 1078
   PriceValue <PricVal> [1..1] Amount C1 1078
   FinancialInstrumentQuantity <FinInstrmQty> [1..1] ± C13 1078
16.1.20.8.4.1  AmountPriceType <AmtPricTp>
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
16.1.20.8.4.2  PriceValue <PricVal>
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
16.1.20.8.4.3  FinancialInstrumentQuantity <FinInstrmQty>
Presence: [1..1]
Definition: Quantity of financial instrument.
Impacted by: C13 "DigitalTokenUnitUsageRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1078 February 2026
```

