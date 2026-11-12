---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.33 DeniedReason3Code"]
file_pages: [2059]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.33 DeniedReason3Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2059 to 2059.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2059

```text
CodeName Name Definition
DQUA WrongQuantity Wrong quantity delivered in the original
instruction.
DMON WrongSettlementAmount Wrong settlement amount settled in the
original delivery.
PART PartialDelivery Only a portion of the original transaction
quantity was delivered by the Central
Securities Depository (CSD).
SAFE AccountMissing Account information is missing in the
original delivery.
DUEB DueBiillMissing Due bill information missing in the
original delivery.
PARD PartialReturn Portion of the original transaction
quantity was returned by the receiver.
35.2.2.33  DeniedReason3Code
Definition: Specifies the denied reason.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline.
DCAL CallDeniedSinceAlreadyApplied Repo call request was denied since
another call already applies.
DFOR DeniedSinceNotAllowed Repo call request was denied. Call not
allowed on the concerned repo, for
example, out of delay.
LATE MarketDeadlineMissed Received after market deadline.
OTHR Other Other. See Narrative.
35.2.2.34  DeniedReason4Code
Definition: Specifies the denied reason.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline.
DCAN DeniedSinceAlreadyCancelled Cancellation request was denied since
the instruction has already been
cancelled.
DPRG DeniedSinceInProgress Cancellation request was denied
because the process of settlement is in
progress.
DREP DeniedSinceRepoEnded Cancellation request was denied
because the repo was cancelled.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2059 March 2026
```

