---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status ", "Transfer Cancellation Status – Intermediary"]
content_origin: "source-transcription"
---

# Transfer Cancellation Status – Intermediary

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Individual Asset Transfer / Request for Transfer Status and Transfer Status  / Transfer Cancellation Status – Intermediary.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P893** Transfer Cancellation Status – Intermediary

**P894** An instructing party sends a TransferInInstruction message to the executing party via one or several intermediaries.

**P895** There is an SLA in place between the instructing party and the executing party that allows the instructing party to cancel the transfer instructions, if necessary and if in accordance with the SLA. Subsequently, the instructing party sends a TransferInCancellationRequest message to cancel the TransferInInstruction message.

**P896** Subsequently, the instructing party sends a RequestForTransferStatusReport message to the executing party. The message requests the status of the TransferInCancellationRequest message.

**P897** In response, the executing party sends a TransferCancellationStatusReport message to the instructing party, via one or several intermediaries. The report gives the status of the TransferInCancellationRequest message, for example, Cancelled.

**P898** The message flow works in a similar way when a TransferOutInstruction message is sent and subsequently, a TransferOutCancellationRequest message is sent, with the status Cancelled.

[fig-0128 - original figure evidence](../diagrams/fig-0128.md)

