---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.22 Rate", "16.1.22.4 RatioFormat19Choice", "16.1.22.4.2 AmountToAmount <AmtToAmt>", "16.1.22.4.2.1 Amount1 <Amt1>"]
file_pages: [1102]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.22.4.2.1 Amount1 <Amt1>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1102 to 1102.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1102

```text
16.1.22.4.2.1  Amount1 <Amt1>
Presence: [1..1]
Definition: Numerator of the quotient of amounts.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
16.1.22.4.2.2  Amount2 <Amt2>
Presence: [1..1]
Definition: Denominator of the quotient of amounts.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
16.1.22.4.3  AmountToQuantity <AmtToQty>
Presence: [1..1]
Definition: Ratio expressed as an amount to quantity ratio.
AmountToQuantity <AmtToQty> contains the following AmountAndQuantityRatio4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1 1102
   Quantity <Qty> [1..1] Quantity 1103
16.1.22.4.3.1  Amount <Amt>
Presence: [1..1]
Definition: Cash amount.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1102 February 2026
```

