---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 semt.013.001.07 IntraPositionMovementInstructionV07", "4.4 Message Building Blocks"]
file_pages: [140]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.013.001.07"]
---

# 4.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 140 to 140.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 140

```text
4.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
4.4.1 TransactionIdentification <TxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the instructing party.
Datatype: "Max35Text" on page 2192
4.4.2 CorporateActionEventIdentification <CorpActnEvtId>
Presence: [0..1]
Definition: Identification assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 2192
4.4.3 NumberCounts <NbCounts>
Presence: [0..1]
Definition: Count of the number of transactions linked.
Impacted by: C8 "CurrentInstructionNumberRule"
NumberCounts <NbCounts> contains one of the following elements (see "NumberCount1Choice" on
page 1619 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CurrentInstructionNumber <CurInstrNb> [1..1] Text 1620
Or}   TotalNumber <TtlNb> [1..1]  C9, C6 1620
     CurrentInstructionNumber <CurInstrNb> [1..1] Text 1620
     TotalOfLinkedInstructions <TtlOfLkdInstrs> [1..1] Text 1620
Constraints
• CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement instruction,
then the CurrentInstructionNumber must be specified.
4.4.4 Linkages <Lnkgs>
Presence: [0..*]
Definition: Link to another transaction that must be processed after, before or at the same time.
Approved by the Securities SEG on 27 January 2026 semt.013.001.07
IntraPositionMovementInstructionV07
Settlement And Reconciliation - Maintenance 2025 - 2026 140 March 2026
```

