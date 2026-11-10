---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.51 RestrictionIdentification1", "35.1.16.51.2 Identification <Id>"]
file_pages: [1590]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.51.2 Identification <Id>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1590 to 1590.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1590

```text
35.1.16.51.2  Identification <Id>
Presence: [1..1]
Definition: Restriction identification applied on the transaction.
Datatype: "Max35Text" on page 2192
35.1.16.52  NumberCount2Choice
Definition: Choice of number count type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CurrentInstructionNumber <CurInstrNb> [1..1] Text 1590
Or}   TotalNumber <TtlNb> [1..1]  C19, C9 1590
     CurrentInstructionNumber <CurInstrNb> [1..1] Text 1591
     TotalOfLinkedInstructions <TtlOfLkdInstrs> [1..1] Text 1591
Constraints
• CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement instruction,
then the CurrentInstructionNumber must be specified.
35.1.16.52.1  CurrentInstructionNumber <CurInstrNb>
Presence: [1..1]
Definition: Sequential number of the instruction in a range of linked settlement instructions.
Datatype: "Max6NumericText" on page 2192
35.1.16.52.2  TotalNumber <TtlNb>
Presence: [1..1]
Definition: Total numbers of settlement transactions, receipts and deliveries, and the concerned
settlement transaction number.
Impacted by: C19 "CurrentInstructionNumberRule", C9 "BlockTradeGuideline"
TotalNumber <TtlNb> contains the following TotalNumber2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CurrentInstructionNumber <CurInstrNb> [1..1] Text 1591
   TotalOfLinkedInstructions <TtlOfLkdInstrs> [1..1] Text 1591
Constraints
• BlockTradeGuideline
In a block trade instruction, the total number of children must be provided using
TotalOfLinkedInstructions.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1590 March 2026
```

