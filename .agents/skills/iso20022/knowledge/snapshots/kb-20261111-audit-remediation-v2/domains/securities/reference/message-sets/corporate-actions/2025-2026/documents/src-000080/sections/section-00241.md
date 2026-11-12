---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.10 ProtectInstruction <PrtctInstr>", "5.4.10.1 TransactionType <TxTp>"]
file_pages: [318]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.10.1 TransactionType <TxTp>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 318 to 318.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 318

```text
ProtectInstruction <PrtctInstr> contains the following ProtectInstruction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionType <TxTp> [1..1] CodeSet 318
   TransactionIdentification <TxId> [0..1] Text 318
   ProtectSafekeepingAccount <PrtctSfkpgAcct> [0..1] Text 318
   ProtectDate <PrtctDt> [0..1] Date 318
5.4.10.1  TransactionType <TxTp>
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
5.4.10.2  TransactionIdentification <TxId>
Presence: [0..1]
Definition: Unique reference of the protect transaction assigned by the depository and used for cover
protect validation.
Datatype: "Max15Text" on page 1249
5.4.10.3  ProtectSafekeepingAccount <PrtctSfkpgAcct>
Presence: [0..1]
Definition: Account which submitted the original protect instruction used for cover protect instructions
whereby one safekeeping account is covering on behalf of another safekeeping account.
Datatype: "Max35Text" on page 1251
5.4.10.4  ProtectDate <PrtctDt>
Presence: [0..1]
Definition: Date at which the protect instruction was created and used for cover protect validation.
Datatype: "ISODate" on page 1243
5.4.11 AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information.
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 318 February 2026
```

