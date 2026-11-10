---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status ", "Cancellation Status – Direct"]
content_origin: "source-transcription"
---

# Cancellation Status – Direct

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Individual Asset Transfer / Request for Transfer Status and Transfer Status  / Cancellation Status – Direct.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P886** Cancellation Status – Direct

**P887** The instructing party sends a TransferInInstruction message to the executing party. 

**P888** There is an SLA in place between the instructing party and the executing party that allows the instructing party to cancel the transfer instructions, if necessary and if in accordance with the SLA. Subsequently, the instructing party sends a TransferInCancellationRequest message to cancel the TransferInInstruction message. 

**P889** Subsequently, the instructing party sends a RequestForTransferStatusReport message to the executing party, to request the status of the TransferInCancellationRequest message. 

**P890** In response, the executing party sends a TransferCancellationStatusReport message to the instructing party, giving the status of the TransferInCancellationRequest message, for example, Cancelled.

**P891** The message flow works in a similar way when a TransferOutInstruction message is sent and subsequently, a TransferOutCancellationRequest message is sent.

[fig-0127 - original figure evidence](../diagrams/fig-0127.md)

