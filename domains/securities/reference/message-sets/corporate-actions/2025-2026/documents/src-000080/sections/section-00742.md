---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.31 RatioFormat18Choice", "16.1.15.31.5 QuantityToAmount <QtyToAmt>", "16.1.15.31.5.2 Quantity <Qty>"]
file_pages: [935]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.31.5.2 Quantity <Qty>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 935 to 935.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 935

```text
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
16.1.15.31.5.2  Quantity <Qty>
Presence: [1..1]
Definition: Quantity expressed as number.
Datatype: "DecimalNumber" on page 1246
16.1.15.32  RatioFormat17Choice
Definition: Choice of format to express a ratio.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   QuantityToQuantity <QtyToQty> [1..1] ± 935
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 935
Or}   AmountToAmount <AmtToAmt> [1..1]  936
     Amount1 <Amt1> [1..1] Amount C1 936
     Amount2 <Amt2> [1..1] Amount C1 936
16.1.15.32.1  QuantityToQuantity <QtyToQty>
Presence: [1..1]
Definition: Ratio expressed as a quotient of quantities.
QuantityToQuantity <QtyToQty> contains the following elements (see "QuantityToQuantityRatio1" on
page 871 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity1 <Qty1> [1..1] Quantity 871
   Quantity2 <Qty2> [1..1] Quantity 871
16.1.15.32.2  NotSpecifiedRate <NotSpcfdRate>
Presence: [1..1]
Definition: Value of the ratio not specified.
Datatype: "RateValueType7Code" on page 1235
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 935 February 2026
```

