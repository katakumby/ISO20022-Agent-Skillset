---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.22 Status19Choice", "35.1.29.22.7 InstructionProcessingStatus <InstrPrcgSts>", "35.1.29.22.7.2 Proprietary <Prtry>"]
file_pages: [1912]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.22.7.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1912 to 1912.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1912

```text
CodeName Name Definition
PACK AcknowledgedAccepted Instruction has been acknowledged/
accepted for further processing by the
account servicer.
PAFI PartialFill Order has been partially filled and the
remaining quantity is warehoused.
PART PartialCancel Order has been partially cancelled as
requested.
PPRC PendingProcessing Processing of the instruction is pending.
REJT Rejected Instruction has been rejected for further
processing.
REPR InRepair Instruction is accepted but in repair.
SESE SettlementInstructionSent Settlement instruction has been sent to
your custodian.
STIN StandingInstruction Standing instruction has been applied.
SUSP TradingSuspendedByStockExchange Trading is suspended by the stock
exchange.
TREA Treated Transaction has been treated (triparty
collateral status).
UNDE UnderAllocated Quantity of financial instrument of the
block trade has been under allocated.
MPRC ModificationRequested Modification request from the
counterparty is awaiting for your
modification request or your consent.
35.1.29.22.7.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Provides the status of an instruction.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.22.8  MatchingStatus <MtchgSts>
Presence: [1..1]
Definition: Provides the matching status of the instruction.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1912 March 2026
```

