---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.173 TransactionProcessingStatus3Code"]
file_pages: [3312]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.173 TransactionProcessingStatus3Code

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3312 to 3312.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3312

```text
CodeName Name Definition
BOLE BorrowingLendingActivity Transaction relates to lending/borrowing.
CLAI MarketClaim Transaction relates to a market claim
following a corporate action.
COLL CollateralActivity Transaction relates to collateral.
CORP CorporateActionActivity Transaction relates to corporate action.
SETT SettlementandClearingActivity Transaction relates to settlement and
clearing.
82.2.2.173  TransactionProcessingStatus3Code
Definition: Provides the processing status of a transaction (at account servicer level).
Type: CodeSet
CodeName Name Definition
CAND Cancelled Instruction has been cancelled.
PACK AcknowledgedAccepted Instruction has been acknowledged/
accepted for further processing by the
account servicer.
REJT Rejected Instruction has been rejected for further
processing.
REPR InRepair Instruction is accepted but in repair.
82.2.2.174  TransactionProcessingStatus4Code
Definition: Specifies the status of an instruction.
Type: CodeSet
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3312 August 2026
```

