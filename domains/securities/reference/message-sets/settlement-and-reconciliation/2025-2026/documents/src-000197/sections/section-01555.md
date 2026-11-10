---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.35 DeniedReason6Code"]
file_pages: [2060]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.35 DeniedReason6Code

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 2060 to 2060.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2060

```text
CodeName Name Definition
DSET DeniedSinceAlreadySettled Cancellation request was denied
because the instruction was already
settled.
LATE MarketDeadlineMissed Received after market deadline.
OTHR Other Other. See Narrative.
CDRG ConditionalRegistrar Execution is denied due to the execution
of a process at the registrar.
CDCY ConditionalCurrency Execution is denied due to a process
linked to the currency of the transaction.
CDRE ConditionalRealignement Execution is denied due to the execution
of a process of realignment at the issuer
CSD.
35.2.2.35  DeniedReason6Code
Definition: Specifies the denied reason.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline.
CDCY ConditionalCurrency Execution is denied due to a process
linked to the currency of the transaction.
CDRE ConditionalRealignement Execution is denied due to the execution
of a process of realignment at the issuer
CSD.
DCAN DeniedSinceCancelled Request was denied since the instruction
has been cancelled.
DSET DeniedSinceSettled Request was denied because the
instruction was settled.
DPRG DeniedSinceInProgress Request was denied because the
process of settlement is in progress.
DREP DeniedSinceRepoEnded Request was denied because the repo
was cancelled.
LATE MarketDeadlineMissed Received after market deadline.
OTHR Other Other. See Narrative.
CDRG ConditionalRegistrar Execution is denied due to the execution
of a process at the registrar.
35.2.2.36  DeniedReason7Code
Definition: Specifies the denied reason.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2060 March 2026
```

