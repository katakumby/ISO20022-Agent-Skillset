---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.15 CancellationProcessingStatus1Code"]
file_pages: [2047]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.15 CancellationProcessingStatus1Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2047 to 2047.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2047

```text
CodeName Name Definition
BLCH Child Transaction is a block trade child.
35.2.2.15  CancellationProcessingStatus1Code
Definition: Specifies the status of a cancellation request.
Type: CodeSet
CodeName Name Definition
CAND CancellationCompleted Cancellation has been completed.
CANP PendingCancellation Cancellation is pending. It is not known
at this time whether cancellation can be
affected.
DEND Denied Cancellation will not be executed.
EXCH ReceivedAtStockExchange Cancellation has been received at the
stock exchange.
INTE ReceivedAtIntermediary Cancellation has been received at the
intermediary.
PACK Accepted Cancellation request has been
acknowledged for further processing by
the account servicer.
PARF PartiallyFilled Order is partially filled, cancellation
processing accepted for the remainder.
REJT Rejected Cancellation has been rejected for
further processing.
REPR InRepair Cancellation request is in repair.
35.2.2.16  CancelledStatusReason12Code
Definition: Specifies the underlying reason for the cancellation of the associated transaction.
Type: CodeSet
CodeName Name Definition
CANI CancelledByYourself Transaction is cancelled by yourself.
CANS CancelledBySystem Transaction is cancelled by the system.
CSUB CancelledByAgent Instruction has been cancelled by the
agent due to an event deadline
extension.
CXLR EndOfLife Transaction is rejected by the executing
party, the rejection is final therefore the
order is cancelled in the system.
CANT CancelledDueToTransformation Original transaction has been cancelled
and replaced due to a corporate action.
CANZ CancelledSplitPartialSettlement Original transaction has been cancelled
and replaced to allow a partial or split
settlement.
CORP CancelledDueToCorporateAction Transaction has been cancelled due to a
corporate action.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2047 March 2026
```

