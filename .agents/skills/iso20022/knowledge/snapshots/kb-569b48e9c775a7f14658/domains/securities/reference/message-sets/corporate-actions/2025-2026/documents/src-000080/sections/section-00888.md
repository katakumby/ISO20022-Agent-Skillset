---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.22 Rate", "16.1.22.7 SolicitationFeeRateFormat12Choice", "16.1.22.7.2 AmountToQuantity <AmtToQty>", "16.1.22.7.2.1 Amount <Amt>"]
file_pages: [1106]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.22.7.2.1 Amount <Amt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1106 to 1106.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1106

```text
16.1.22.7.2.1  Amount <Amt>
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
16.1.22.7.2.2  Quantity <Qty>
Presence: [1..1]
Definition: Quantity expressed as number.
Datatype: "DecimalNumber" on page 1246
16.1.22.7.3  Amount <Amt>
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
16.1.22.8  RateFormat27Choice
Definition: Choice between a rate or an unspecified rate.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1106
Or}   Amount <Amt> [1..1] Amount C1 1107
16.1.22.8.1  Rate <Rate>
Presence: [1..1]
Definition: Value is expressed as a rate.
Datatype: "Percentage14Rate" on page 1247
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1106 February 2026
```

