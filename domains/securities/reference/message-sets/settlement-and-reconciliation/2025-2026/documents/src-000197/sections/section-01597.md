---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.112 RepoCallAcknowledgementReason2Code"]
file_pages: [2133]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.112 RepoCallAcknowledgementReason2Code

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 2133 to 2133.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2133

```text
CodeName Name Definition
EXCH ReceivedAtStockExchange Replacement request previously
received from you has been received at
the stock exchange.
INTE ReceivedAtIntermediary Replacement request previously
received from you has been received at
intermediary (if not stock exchange).
PACK Accepted Replacement request has been
accepted for further processing by the
account servicer (technical receipt).
PART PartialReplacementAccepted Order is partially filled, replacement
processing accepted for the remaining.
PEND Pending Replacement request is pending.
REJT Rejected Replacement request has been rejected
for further processing.
REPL Completed Replacement request has been
completed.
REPR InRepair Replacement request previously
received from you is in repair.
35.2.2.112  RepoCallAcknowledgementReason2Code
Definition: Specifies additional information about the repurchase agreement call processed instruction.
Type: CodeSet
CodeName Name Definition
CALD InProcess Repurchase agreement call is in
process.
CALP Processed Repurchase agreement call is
processed.
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline. Processed on best effort basis.
35.2.2.113  RepoCallRequestStatus1Code
Definition: Specifies additional information about the status of the repurchase agreement call processed
instruction.
Type: CodeSet
CodeName Name Definition
CACK AcknowledgedAccepted Repurchase agreement call request is
acknowledged/accepted.
DEND Denied Repuchase agreement call request is
denied.
35.2.2.114  Reporting1Code
Definition: Identifies to which institution the reporting must be done.
Type: CodeSet
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2133 March 2026
```

