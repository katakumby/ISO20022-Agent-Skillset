---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.20 Price", "16.1.20.3 PriceFormat61Choice", "16.1.20.3.1 AmountPrice <AmtPric>", "16.1.20.3.1.1 AmountPriceType <AmtPricTp>"]
file_pages: [1067]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.20.3.1.1 AmountPriceType <AmtPricTp>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1067 to 1067.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1067

```text
AmountPrice <AmtPric> contains the following AmountPrice6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AmountPriceType <AmtPricTp> [1..1] CodeSet 1067
   PriceValue <PricVal> [1..1] Amount C1 1067
16.1.20.3.1.1  AmountPriceType <AmtPricTp>
Presence: [1..1]
Definition: Type of amount price.
Datatype: "AmountPriceType3Code" on page 1163
CodeName Name Definition
ACTU ActualAmount Price expressed as a currency and
amount per unit or per share.
PLOT Lot Price expressed as an amount of money
per lot.
16.1.20.3.1.2  PriceValue <PricVal>
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
16.1.20.3.2  NotSpecifiedPrice <NotSpcfdPric>
Presence: [1..1]
Definition: Value of the price not specified.
Datatype: "PriceValueType10Code" on page 1231
CodeName Name Definition
UKWN Unknown Price is unknown by the sender or has
not been established.
16.1.20.4  AmountPrice3
Definition: Price expressed as an amount.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1067 February 2026
```

