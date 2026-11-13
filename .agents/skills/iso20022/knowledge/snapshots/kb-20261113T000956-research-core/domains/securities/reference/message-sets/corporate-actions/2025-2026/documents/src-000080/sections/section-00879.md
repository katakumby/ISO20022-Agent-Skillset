---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.21 Quantity", "16.1.21.7 FinancialInstrumentQuantity34Choice", "16.1.21.7.5 DigitalTokenUnit <DgtlTknUnit>"]
file_pages: [1097]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.21.7.5 DigitalTokenUnit <DgtlTknUnit>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1097 to 1097.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1097

```text
Definition: Quantity expressed as a code.
Datatype: "Quantity4Code" on page 1234
CodeName Name Definition
UKWN UnknownQuantity Quantity is unknown by the sender or
has not been established.
ANYA AnyAndAll Instruction applies to the entire eligible
balance of underlying securities.
16.1.21.7.5  DigitalTokenUnit <DgtlTknUnit>
Presence: [1..1]
Definition: Quantity of digital tokens expressed as a number, for example, a number of blockchain
tokens.
Datatype: "Max30DecimalNumber" on page 1247
16.1.21.8  Quantity52Choice
Definition: Choice between different formats of securities quantity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1097
Or   OriginalAndCurrentFaceAmount <OrgnlAndCurFaceAmt> [1..1] ± 1097
Or}   Quantity <Qty> [1..1] ± C13 1098
16.1.21.8.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify quantity of a financial instrument.
Datatype: "Quantity1Code" on page 1233
CodeName Name Definition
QALL AllSecurities Instruction applies to the entire eligible
balance of underlying securities.
16.1.21.8.2  OriginalAndCurrentFaceAmount <OrgnlAndCurFaceAmt>
Presence: [1..1]
Definition: Face amount and amortised value of security.
OriginalAndCurrentFaceAmount <OrgnlAndCurFaceAmt> contains the following elements (see
"OriginalAndCurrentQuantities1" on page 1133 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FaceAmount <FaceAmt> [1..1] Amount 1133
   AmortisedValue <AmtsdVal> [1..1] Amount 1133
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1097 February 2026
```

