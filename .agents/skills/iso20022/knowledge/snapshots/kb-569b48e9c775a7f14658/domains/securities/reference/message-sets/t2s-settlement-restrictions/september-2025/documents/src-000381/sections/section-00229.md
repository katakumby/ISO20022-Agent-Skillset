---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.8 PendingReason30Choice", "9.1.21.8.2 Proprietary <Prtry>"]
file_pages: [275]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.8.2 Proprietary <Prtry>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 275 to 275.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 275

```text
CodeName Name Definition
CDRE ConditionalRealignement Execution is conditional to the execution
of a process of realignment at the issuer
CSD.
CDAC ConditionalDeliveryAwaitingCancellation Awaiting cancellation of one of the party.
INBC IncompleteNumberCount Not all the instructions part of a pool
have been received.
9.1.21.8.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the cancellation request is pending.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 224 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 224
   Issuer <Issr> [1..1] Text 224
   SchemeName <SchmeNm> [0..1] Text 224
9.1.21.9  ProcessingStatus68Choice
Definition: Choice of format for the processing status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 275
Or}   Proprietary <Prtry> [1..1] ± 275
9.1.21.9.1  Code <Cd>
Presence: [1..1]
Definition: Provides the status of an instruction.
Datatype: "TransactionProcessingStatus3Code" on page 340
CodeName Name Definition
CAND Cancelled Instruction has been cancelled.
PACK AcknowledgedAccepted Instruction has been acknowledged/
accepted for further processing by the
account servicer.
REJT Rejected Instruction has been rejected for further
processing.
REPR InRepair Instruction is accepted but in repair.
9.1.21.9.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 275 September 2025
```

