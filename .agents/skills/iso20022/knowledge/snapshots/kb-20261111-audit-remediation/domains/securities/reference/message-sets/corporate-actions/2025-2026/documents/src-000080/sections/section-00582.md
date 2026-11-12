---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15", "13.4 Message Building Blocks", "13.4.6 ProtectInstruction <PrtctInstr>"]
file_pages: [754]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.041.001.15"]
---

# 13.4.6 ProtectInstruction <PrtctInstr>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 754 to 754.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 754

```text
13.4.6 ProtectInstruction <PrtctInstr>
Presence: [0..1]
Definition: Provides detailed information on protect and cover protect instructions.
ProtectInstruction <PrtctInstr> contains the following ProtectInstruction4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionType <TxTp> [1..1] CodeSet 754
   ProtectTransactionStatus <PrtctTxSts> [0..1] CodeSet 754
   TransactionIdentification <TxId> [0..1] Text 754
   ProtectDate <PrtctDt> [0..1] Date 754
   UncoveredProtectQuantity <UcvrdPrtctQty> [0..1] ± 755
13.4.6.1  TransactionType <TxTp>
Presence: [1..1]
Definition: Indicates whether the instruction is a protect or a cover protect instruction.
Datatype: "ProtectTransactionType3Code" on page 1233
CodeName Name Definition
PROT ProtectTransaction Reorganisation is a protect transaction
type.
13.4.6.2  ProtectTransactionStatus <PrtctTxSts>
Presence: [0..1]
Definition: Status of the protect transaction.
Datatype: "ProtectInstructionStatus4Code" on page 1233
CodeName Name Definition
OPEN Open Protect instruction which has not been
fully covered. Will include partial covers.
13.4.6.3  TransactionIdentification <TxId>
Presence: [0..1]
Definition: Unique reference of the protect transaction assigned by the depository and used for cover
protect validation.
Datatype: "Max15Text" on page 1249
13.4.6.4  ProtectDate <PrtctDt>
Presence: [0..1]
Definition: Date at which the protect instruction was created and used for cover protect validation.
Datatype: "ISODate" on page 1243
Approved by the Securities SEG on 27 January 2026 seev.041.001.15
CorporateActionInstructionCancellationRequestStat
usAdviceV15
Corporate Actions - Maintenance 2025 - 2026 754 February 2026
```

