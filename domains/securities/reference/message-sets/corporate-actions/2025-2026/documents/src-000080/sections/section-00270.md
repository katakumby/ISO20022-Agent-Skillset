---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.4 Message Building Blocks", "6.4.6 ProtectInstruction <PrtctInstr>", "6.4.6.1 TransactionType <TxTp>"]
file_pages: [357]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.4.6.1 TransactionType <TxTp>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 357 to 357.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 357

```text
ProtectInstruction <PrtctInstr> contains the following ProtectInstruction2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionType <TxTp> [1..1] CodeSet 357
   ProtectTransactionStatus <PrtctTxSts> [0..1] CodeSet 357
   TransactionIdentification <TxId> [0..1] Text 357
   ProtectSafekeepingAccount <PrtctSfkpgAcct> [0..1] Text 358
   ProtectDate <PrtctDt> [0..1] Date 358
   UncoveredProtectQuantity <UcvrdPrtctQty> [0..1] ± 358
6.4.6.1  TransactionType <TxTp>
Presence: [1..1]
Definition: Indicates whether the instruction is a protect or a cover protect instruction.
Datatype: "ProtectTransactionType2Code" on page 1233
CodeName Name Definition
PROT ProtectTransaction Reorganisation is a protect transaction
type.
COVP CoverOnBehalfOfAnotherParticipantTransaction Reorganisation is a cover on behalf of
another participant transaction type.
COVR CoverProtectTransaction Reorganisation is a cover protect
transaction type.
6.4.6.2  ProtectTransactionStatus <PrtctTxSts>
Presence: [0..1]
Definition: Status of the protect transaction.
Datatype: "ProtectInstructionStatus3Code" on page 1233
CodeName Name Definition
OPEN Open Protect instruction which has not been
fully covered. Will include partial covers.
COVR FullyCovered Protect instruction has been fully
covered.
EXPI Expired Protect instruction has expired.
6.4.6.3  TransactionIdentification <TxId>
Presence: [0..1]
Definition: Unique reference of the protect transaction assigned by the depository and used for cover
protect validation.
Datatype: "Max15Text" on page 1249
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 357 February 2026
```

