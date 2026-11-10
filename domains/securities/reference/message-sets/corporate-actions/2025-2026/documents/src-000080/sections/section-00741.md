---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.31 RatioFormat18Choice", "16.1.15.31.4 AmountToQuantity <AmtToQty>"]
file_pages: [934]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.31.4 AmountToQuantity <AmtToQty>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 934 to 934.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 934

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
16.1.15.31.4  AmountToQuantity <AmtToQty>
Presence: [1..1]
Definition: Ratio expressed as an amount to quantity ratio.
AmountToQuantity <AmtToQty> contains the following AmountAndQuantityRatio4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1 934
   Quantity <Qty> [1..1] Quantity 934
16.1.15.31.4.1  Amount <Amt>
Presence: [1..1]
Definition: Cash amount.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
16.1.15.31.4.2  Quantity <Qty>
Presence: [1..1]
Definition: Quantity expressed as number.
Datatype: "DecimalNumber" on page 1246
16.1.15.31.5  QuantityToAmount <QtyToAmt>
Presence: [1..1]
Definition: Ratio expressed as a quantity to amount ratio.
QuantityToAmount <QtyToAmt> contains the following AmountAndQuantityRatio4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1 934
   Quantity <Qty> [1..1] Quantity 935
16.1.15.31.5.1  Amount <Amt>
Presence: [1..1]
Definition: Cash amount.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 934 February 2026
```

