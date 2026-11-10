---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.21 Quantity", "16.1.21.2 SignedQuantityFormat10"]
file_pages: [1090]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.21.2 SignedQuantityFormat10

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1090 to 1090.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1090

```text
16.1.21.2  SignedQuantityFormat10
Definition: Signed quantity of security formats.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
16.1.21.2.1  ShortLongPosition <ShrtLngPos>
Presence: [1..1]
Definition: Sign of the quantity of security.
Datatype: "ShortLong1Code" on page 1242
CodeName Name Definition
SHOR Short Position is short, that is, the balance is
negative.
LONG Long Position is long, that is, the balance is
positive.
16.1.21.2.2  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of security.
Impacted by: C13 "DigitalTokenUnitUsageRule"
Quantity <Qty> contains one of the following elements (see "FinancialInstrumentQuantity33Choice" on
page 1091 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1092
Or   FaceAmount <FaceAmt> [1..1] Amount 1092
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1092
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1092
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
16.1.21.3  Quantity51Choice
Definition: Choice of format for the quantity.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1090 February 2026
```

