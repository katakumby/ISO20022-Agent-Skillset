---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.21 Quantity", "16.1.21.1 Quantity49Choice", "16.1.21.1.1 QuantityChoice <QtyChc>", "16.1.21.1.1.1 OriginalAndCurrentFaceAmount <OrgnlAndCurFaceAmt>", "16.1.21.1.1.1.1 ShortLongPosition <ShrtLngPos>"]
file_pages: [1088]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.21.1.1.1.1 ShortLongPosition <ShrtLngPos>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1088 to 1088.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1088

```text
OriginalAndCurrentFaceAmount <OrgnlAndCurFaceAmt> contains the following
OriginalAndCurrentQuantities6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1088
   FaceAmount <FaceAmt> [1..1] Amount 1088
   AmortisedValue <AmtsdVal> [1..1] Amount 1088
16.1.21.1.1.1.1  ShortLongPosition <ShrtLngPos>
Presence: [1..1]
Definition: Sign of the quantity of security.
Datatype: "ShortLong1Code" on page 1242
CodeName Name Definition
SHOR Short Position is short, that is, the balance is
negative.
LONG Long Position is long, that is, the balance is
positive.
16.1.21.1.1.1.2  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, that is, the principal, of a
debt instrument.
Datatype: "ImpliedCurrencyAndAmount" on page 1157
16.1.21.1.1.1.3  AmortisedValue <AmtsdVal>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
Datatype: "ImpliedCurrencyAndAmount" on page 1157
16.1.21.1.1.2  SignedQuantity <SgndQty>
Presence: [1..1]
Definition: Signed quantity of security.
SignedQuantity <SgndQty> contains the following elements (see "SignedQuantityFormat10" on
page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
16.1.21.1.2  ProprietaryQuantity <PrtryQty>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1088 February 2026
```

