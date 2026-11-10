---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.22 Rate", "16.1.22.6 RateFormat31Choice", "16.1.22.6.3 Amount <Amt>"]
file_pages: [1105]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.22.6.3 Amount <Amt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1105 to 1105.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1105

```text
CodeName Name Definition
UKWN Unknown Rate is unknown by the sender or has
not been established.
16.1.22.6.3  Amount <Amt>
Presence: [1..1]
Definition: Value is expressed as an amount.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
16.1.22.7  SolicitationFeeRateFormat12Choice
Definition: Choice between a rate or an unspecified rate.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1105
Or   AmountToQuantity <AmtToQty> [1..1]  1105
     Amount <Amt> [1..1] Amount C1 1106
     Quantity <Qty> [1..1] Quantity 1106
Or}   Amount <Amt> [1..1] Amount C1 1106
16.1.22.7.1  Rate <Rate>
Presence: [1..1]
Definition: Value is expressed as a rate.
Datatype: "Percentage14Rate" on page 1247
16.1.22.7.2  AmountToQuantity <AmtToQty>
Presence: [1..1]
Definition: Ratio expressed as an amount to quantity ratio.
AmountToQuantity <AmtToQty> contains the following AmountAndQuantityRatio4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1 1106
   Quantity <Qty> [1..1] Quantity 1106
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1105 February 2026
```

