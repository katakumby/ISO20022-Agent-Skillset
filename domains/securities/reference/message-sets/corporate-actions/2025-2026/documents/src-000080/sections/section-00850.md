---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.20 Price", "16.1.20.4 AmountPrice3", "16.1.20.4.1 AmountPriceType <AmtPricTp>"]
file_pages: [1068]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.20.4.1 AmountPriceType <AmtPricTp>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1068 to 1068.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1068

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AmountPriceType <AmtPricTp> [1..1] CodeSet 1068
   PriceValue <PricVal> [1..1] Amount C1 1068
16.1.20.4.1  AmountPriceType <AmtPricTp>
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
16.1.20.4.2  PriceValue <PricVal>
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
16.1.20.5  PriceFormat75Choice
Definition: Choice between a percentage price or an amount price or index points.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1069
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1069
     PriceValue <PricVal> [1..1] Rate 1069
Or   AmountPrice <AmtPric> [1..1] ± 1069
Or}   IndexPoints <IndxPts> [1..1] Quantity 1069
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1068 February 2026
```

