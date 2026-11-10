---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.75 NumberCount1Choice", "35.1.16.75.1 CurrentInstructionNumber <CurInstrNb>"]
file_pages: [1620]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.75.1 CurrentInstructionNumber <CurInstrNb>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1620 to 1620.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1620

```text
Constraints
• CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement instruction,
then the CurrentInstructionNumber must be specified.
35.1.16.75.1  CurrentInstructionNumber <CurInstrNb>
Presence: [1..1]
Definition: Sequential number of the instruction in a range of linked settlement instructions.
Datatype: "Exact3NumericText" on page 2190
35.1.16.75.2  TotalNumber <TtlNb>
Presence: [1..1]
Definition: Total numbers of settlement transactions, receipts and deliveries, and the concerned
settlement transaction number.
Impacted by: C9 "CurrentInstructionNumberRule", C6 "BlockTradeGuideline"
TotalNumber <TtlNb> contains the following TotalNumber1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CurrentInstructionNumber <CurInstrNb> [1..1] Text 1620
   TotalOfLinkedInstructions <TtlOfLkdInstrs> [1..1] Text 1620
Constraints
• BlockTradeGuideline
In a block trade instruction, the total number of children must be provided using
TotalOfLinkedInstructions.
The CurrentInstructionNumber of the parent must be 000. The children must have an incremental
CurrentInstructionNumber from 001 to 999.
For more details, see the relevant market practice document on www.smpg.info.
• CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement instruction,
then the CurrentInstructionNumber must be specified.
35.1.16.75.2.1  CurrentInstructionNumber <CurInstrNb>
Presence: [1..1]
Definition: Sequential number of the instruction in a range of linked settlement instructions.
Datatype: "Exact3NumericText" on page 2190
35.1.16.75.2.2  TotalOfLinkedInstructions <TtlOfLkdInstrs>
Presence: [1..1]
Definition: Total number of settlement instructions that are linked together.
Datatype: "Exact3NumericText" on page 2190
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1620 March 2026
```

