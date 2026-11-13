---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13", "12.4 Message Building Blocks", "12.4.6 ProtectInstruction <PrtctInstr>"]
file_pages: [731]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.040.001.13"]
---

# 12.4.6 ProtectInstruction <PrtctInstr>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 731 to 731.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 731

```text
InstructedQuantity <InstdQty> contains one of the following elements (see "Quantity52Choice" on
page 1097 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1097
Or   OriginalAndCurrentFaceAmount <OrgnlAndCurFaceAmt> [1..1] ± 1097
Or}   Quantity <Qty> [1..1] ± C13 1098
12.4.6 ProtectInstruction <PrtctInstr>
Presence: [0..1]
Definition: Provides detailed information on protect and cover protect instructions.
ProtectInstruction <PrtctInstr> contains the following ProtectInstruction3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionType <TxTp> [1..1] CodeSet 731
   TransactionIdentification <TxId> [0..1] Text 731
   ProtectDate <PrtctDt> [0..1] Date 731
12.4.6.1  TransactionType <TxTp>
Presence: [1..1]
Definition: Indicates whether the instruction is a protect or a cover protect instruction.
Datatype: "ProtectTransactionType3Code" on page 1233
CodeName Name Definition
PROT ProtectTransaction Reorganisation is a protect transaction
type.
12.4.6.2  TransactionIdentification <TxId>
Presence: [0..1]
Definition: Unique reference of the protect transaction assigned by the depository and used for cover
protect validation.
Datatype: "Max15Text" on page 1249
12.4.6.3  ProtectDate <PrtctDt>
Presence: [0..1]
Definition: Date at which the protect instruction was created and used for cover protect validation.
Datatype: "ISODate" on page 1243
12.4.7 AdditionalInformation <AddtlInf>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 seev.040.001.13
CorporateActionInstructionCancellationRequestV13
Corporate Actions - Maintenance 2025 - 2026 731 February 2026
```

