---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.30 CorporateActionEventStageFormat13Choice", "16.1.15.30.2 Proprietary <Prtry>"]
file_pages: [932]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.30.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 932 to 932.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 932

```text
16.1.15.30.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the stage of the corporate action event.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.31  RatioFormat18Choice
Definition: Choice of format to express a ratio.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   QuantityToQuantity <QtyToQty> [1..1] ± 932
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 933
Or   AmountToAmount <AmtToAmt> [1..1]  933
     Amount1 <Amt1> [1..1] Amount C1 933
     Amount2 <Amt2> [1..1] Amount C1 933
Or   AmountToQuantity <AmtToQty> [1..1]  934
     Amount <Amt> [1..1] Amount C1 934
     Quantity <Qty> [1..1] Quantity 934
Or}   QuantityToAmount <QtyToAmt> [1..1]  934
     Amount <Amt> [1..1] Amount C1 934
     Quantity <Qty> [1..1] Quantity 935
16.1.15.31.1  QuantityToQuantity <QtyToQty>
Presence: [1..1]
Definition: Ratio expressed as a quotient of quantities.
QuantityToQuantity <QtyToQty> contains the following elements (see "QuantityToQuantityRatio1" on
page 871 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity1 <Qty1> [1..1] Quantity 871
   Quantity2 <Qty2> [1..1] Quantity 871
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 932 February 2026
```

