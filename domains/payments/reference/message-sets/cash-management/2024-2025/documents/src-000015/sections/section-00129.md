---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.4 ReturnCriteria <RtrCrit>", "4.4.2.2.2.4.4 PaymentReturnCriteria <PmtRtrCrit>", "4.4.2.2.2.4.4.8 PriorityIndicator <PrtyInd>"]
file_pages: [202]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.4.4.8 PriorityIndicator <PrtyInd>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 202 to 202.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 202

```text
4.4.2.2.2.4.4.8  PriorityIndicator <PrtyInd>
Presence: [0..1]
Definition: Indicates whether the payment priority is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.9  ProcessingValidityTimeIndicator <PrcgVldtyTmInd>
Presence: [0..1]
Definition: Indicates whether the processing validity time is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.10  PurposeIndicator <PurpInd>
Presence: [0..1]
Definition: Indicates whether the transfer reason is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.11  InstructionCopyIndicator <InstrCpyInd>
Presence: [0..1]
Definition: Indicates whether the instruction copy is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.12  PaymentMessageTypeIndicator <PmtMTInd>
Presence: [0..1]
Definition: Indicates whether the payment message type is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.13  PaymentTypeIndicator <PmtTpInd>
Presence: [0..1]
Definition: Indicates whether the payment type is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 202 February 2025
```

