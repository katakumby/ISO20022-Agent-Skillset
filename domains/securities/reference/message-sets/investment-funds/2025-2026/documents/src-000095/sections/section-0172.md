---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status ", "Request for Status"]
content_origin: "source-transcription"
---

# Request for Status

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Individual Asset Transfer / Request for Transfer Status and Transfer Status  / Request for Status.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P867** Request for Status

**P868** An instructing party sends a transfer instruction, for example, a TransferOutInstruction message, to the executing party.

**P869** Subsequently, the instructing party sends a RequestForTransferStatusReport message to request the status of the TransferOutInstruction message. In response, the executing party sends a TransferInstructionStatusReport message to the instructing party giving the status of the TransferOutInstruction message, for example, Accepted (PACK).

[fig-0123 - original figure evidence](../diagrams/fig-0123.md)

