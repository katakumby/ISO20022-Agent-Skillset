---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.2 Message Datatypes", "9.2.2 CodeSet", "9.2.2.34 ProcessingPosition3Code"]
file_pages: [334]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.2.2.34 ProcessingPosition3Code

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 334 to 334.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 334

```text
CodeName Name Definition
example, a premium price of 2.0%
equals a price of 102 when par is 100.
PARV Par Price is the face amount.
9.2.2.34  ProcessingPosition3Code
Definition: Specifies the processing position.
Type: CodeSet
CodeName Name Definition
AFTE After Specifies that the transaction/instruction
is to be executed after the linked
transaction/instruction.
WITH With Specifies that the transaction/instruction
is to be executed with the linked
transaction/instruction.
BEFO Before Specifies that the transaction/instruction
is to be executed before the linked
transaction/instruction.
INFO Information Specifies that the transactions/
instructions are linked for information
purposes only.
9.2.2.35  Registration2Code
Definition: Specifies whether registration should occur upon receipt.
Type: CodeSet
CodeName Name Definition
PTYH PartyHold You or your party set the instruction in a
hold/frozen/preadvice mode.
CSDH CSDHold Central securities depository sets the
instruction in a hold/frozen/preadvice
mode.
CDEL ConditionalDelivery Instruction is in a hold/frozen/preadvice
mode as it fulfils predefined conditional
delivery rules in the market infrastructure
platform for conditional delivery.
CVAL CSDValidation Instruction is in a hold/frozen/preadvice
mode as it fulfils predefined conditions of
a restriction processing type in the
market infrastructure platform.
9.2.2.36  RejectionReason33Code
Definition: Specifies the reason why the instruction/cancellation request has a rejected status.
Type: CodeSet
CodeName Name Definition
CASH CashAccount Unrecognised or invalid cash account.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 334 September 2025
```

