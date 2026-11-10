---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.22 Rate", "16.1.22.4 RatioFormat19Choice"]
file_pages: [1101]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.22.4 RatioFormat19Choice

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1101 to 1101.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1101

```text
CodeName Name Definition
UKWN Unknown Rate is unknown by the sender or has
not been established.
16.1.22.4  RatioFormat19Choice
Definition: Choice of format to expressed a ratio.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   QuantityToQuantity <QtyToQty> [1..1] ± 1101
Or   AmountToAmount <AmtToAmt> [1..1]  1101
     Amount1 <Amt1> [1..1] Amount C1 1102
     Amount2 <Amt2> [1..1] Amount C1 1102
Or   AmountToQuantity <AmtToQty> [1..1]  1102
     Amount <Amt> [1..1] Amount C1 1102
     Quantity <Qty> [1..1] Quantity 1103
Or}   QuantityToAmount <QtyToAmt> [1..1]  1103
     Amount <Amt> [1..1] Amount C1 1103
     Quantity <Qty> [1..1] Quantity 1103
16.1.22.4.1  QuantityToQuantity <QtyToQty>
Presence: [1..1]
Definition: Ratio expressed as a quotient of quantities.
QuantityToQuantity <QtyToQty> contains the following elements (see "QuantityToQuantityRatio1" on
page 871 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity1 <Qty1> [1..1] Quantity 871
   Quantity2 <Qty2> [1..1] Quantity 871
16.1.22.4.2  AmountToAmount <AmtToAmt>
Presence: [1..1]
Definition: Ratio expressed as a quotient of amounts.
AmountToAmount <AmtToAmt> contains the following AmountToAmountRatio2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount1 <Amt1> [1..1] Amount C1 1102
   Amount2 <Amt2> [1..1] Amount C1 1102
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1101 February 2026
```

