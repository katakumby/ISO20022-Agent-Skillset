---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.21 Quantity", "16.1.21.1 Quantity49Choice", "16.1.21.1.1 QuantityChoice <QtyChc>"]
file_pages: [1087]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.21.1.1 QuantityChoice <QtyChc>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1087 to 1087.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1087

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   QuantityChoice <QtyChc> [1..1]  1087
{Or     OriginalAndCurrentFaceAmount
<OrgnlAndCurFaceAmt>
[1..1]  1087
       ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1088
       FaceAmount <FaceAmt> [1..1] Amount 1088
       AmortisedValue <AmtsdVal> [1..1] Amount 1088
Or}     SignedQuantity <SgndQty> [1..1] ± 1088
Or}   ProprietaryQuantity <PrtryQty> [1..1]  1088
     ShortLongPosition <ShrtLngPos> [0..1] CodeSet 1089
     Quantity <Qty> [1..1] Quantity 1089
     QuantityType <QtyTp> [1..1] Text 1089
     Issuer <Issr> [1..1] Text 1089
     SchemeName <SchmeNm> [0..1] Text 1089
16.1.21.1.1  QuantityChoice <QtyChc>
Presence: [1..1]
Definition: Choice between different quantity of security formats.
QuantityChoice <QtyChc> contains one of the following Quantity50Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OriginalAndCurrentFaceAmount <OrgnlAndCurFaceAmt> [1..1]  1087
     ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1088
     FaceAmount <FaceAmt> [1..1] Amount 1088
     AmortisedValue <AmtsdVal> [1..1] Amount 1088
Or}   SignedQuantity <SgndQty> [1..1] ± 1088
16.1.21.1.1.1  OriginalAndCurrentFaceAmount <OrgnlAndCurFaceAmt>
Presence: [1..1]
Definition: Signed face amount and amortised value of security.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1087 February 2026
```

