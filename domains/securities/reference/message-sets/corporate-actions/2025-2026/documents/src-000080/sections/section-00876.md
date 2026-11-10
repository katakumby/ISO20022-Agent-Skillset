---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.21 Quantity", "16.1.21.6 SignedQuantityFormat11"]
file_pages: [1094]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.21.6 SignedQuantityFormat11

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1094 to 1094.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1094

```text
Datatype: "Max30DecimalNumber" on page 1247
16.1.21.6  SignedQuantityFormat11
Definition: Signed quantity of security formats.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1094
   QuantityChoice <QtyChc> [1..1]  1094
{Or     Quantity <Qty> [1..1] ± C13 1095
Or}     ProprietaryQuantity <PrtryQty> [1..1]  1095
       Quantity <Qty> [1..1] Quantity 1095
       QuantityType <QtyTp> [1..1] Text 1095
       Issuer <Issr> [1..1] Text 1095
       SchemeName <SchmeNm> [0..1] Text 1096
16.1.21.6.1  ShortLongPosition <ShrtLngPos>
Presence: [1..1]
Definition: Sign of the quantity of security.
Datatype: "ShortLong1Code" on page 1242
CodeName Name Definition
SHOR Short Position is short, that is, the balance is
negative.
LONG Long Position is long, that is, the balance is
positive.
16.1.21.6.2  QuantityChoice <QtyChc>
Presence: [1..1]
Definition: Choice between different quantity of security formats.
QuantityChoice <QtyChc> contains one of the following Quantity48Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C13 1095
Or}   ProprietaryQuantity <PrtryQty> [1..1]  1095
     Quantity <Qty> [1..1] Quantity 1095
     QuantityType <QtyTp> [1..1] Text 1095
     Issuer <Issr> [1..1] Text 1095
     SchemeName <SchmeNm> [0..1] Text 1096
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1094 February 2026
```

