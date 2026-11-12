---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.22 Rate", "16.1.22.2 RatioFormat20Choice"]
file_pages: [1099]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.22.2 RatioFormat20Choice

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1099 to 1099.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1099

```text
16.1.22.2  RatioFormat20Choice
Definition: Choice of format to expressed a ratio.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   QuantityToQuantity <QtyToQty> [1..1] ± 1099
Or}   AmountToAmount <AmtToAmt> [1..1]  1099
     Amount1 <Amt1> [1..1] Amount C1 1099
     Amount2 <Amt2> [1..1] Amount C1 1100
16.1.22.2.1  QuantityToQuantity <QtyToQty>
Presence: [1..1]
Definition: Ratio expressed as a quotient of quantities.
QuantityToQuantity <QtyToQty> contains the following elements (see "QuantityToQuantityRatio1" on
page 871 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity1 <Qty1> [1..1] Quantity 871
   Quantity2 <Qty2> [1..1] Quantity 871
16.1.22.2.2  AmountToAmount <AmtToAmt>
Presence: [1..1]
Definition: Ratio expressed as a quotient of amounts.
AmountToAmount <AmtToAmt> contains the following AmountToAmountRatio2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount1 <Amt1> [1..1] Amount C1 1099
   Amount2 <Amt2> [1..1] Amount C1 1100
16.1.22.2.2.1  Amount1 <Amt1>
Presence: [1..1]
Definition: Numerator of the quotient of amounts.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1099 February 2026
```

