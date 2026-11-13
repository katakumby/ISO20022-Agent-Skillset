---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.14 ProcessingStatus70Choice"]
file_pages: [483]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.14 ProcessingStatus70Choice

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 483 to 483.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 483

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.28.14  ProcessingStatus70Choice
Definition: Choice of format for the processing status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 483
Or}   Proprietary <Prtry> [1..1] ± 483
7.1.28.14.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the processing status of the instruction in a coded format.
Datatype: "TransactionProcessingStatus4Code" on page 546
CodeName Name Definition
PACK AcknowledgedAccepted Instruction has been acknowledged/
accepted for further processing by the
account servicer.
PPRC PendingProcessing Processing of the instruction is pending.
REJT Rejected Instruction has been rejected for further
processing.
REPR InRepair Instruction is accepted but in repair.
CAND Cancelled Instruction has been cancelled.
CANP PendingCancellation Cancellation request from yourself for
this instruction is pending waiting for
further processing.
CPRC CancellationRequested Cancellation request from the
counterparty is awaiting for your
cancellation request or your consent.
MPRC ModificationRequested Modification request from the
counterparty is awaiting for your
modification request or your consent.
7.1.28.14.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the processing status of the instruction in a proprietary format.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 483 March 2026
```

