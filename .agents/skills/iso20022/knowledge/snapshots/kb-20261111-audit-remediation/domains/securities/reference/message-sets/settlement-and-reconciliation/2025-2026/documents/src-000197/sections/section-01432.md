---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.22 Status19Choice", "35.1.29.22.12 CancellationProcessingStatus <CxlPrcgSts>"]
file_pages: [1916]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.22.12 CancellationProcessingStatus <CxlPrcgSts>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1916 to 1916.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1916

```text
35.1.29.22.12  CancellationProcessingStatus <CxlPrcgSts>
Presence: [1..1]
Definition: Provides the status of a cancellation request.
CancellationProcessingStatus <CxlPrcgSts> contains one of the following
CancellationProcessingStatus7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1916
Or}   Proprietary <Prtry> [1..1] ± 1916
35.1.29.22.12.1  Code <Cd>
Presence: [1..1]
Definition: Provides the status of a cancellation request.
Datatype: "CancellationProcessingStatus1Code" on page 2047
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
35.1.29.22.12.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Provides the status of a cancellation request.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1916 March 2026
```

