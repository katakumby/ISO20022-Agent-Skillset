---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status ", "Request for Status Rejection"]
content_origin: "source-transcription"
---

# Request for Status Rejection

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Individual Asset Transfer / Request for Transfer Status and Transfer Status  / Request for Status Rejection.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P871** Request for Status Rejection

**P872** An instructing party sends a transfer instruction, for example, a TransferOutInstruction message, to the executing party.

**P873** Subsequently, the investor sends a RequestForTransferStatusReport message but, for example, it misquotes the message reference of the TransferOutInstruction message. The transfer agent cannot process the RequestForTransferStatusReport message because it does not know to which transfer instruction the investor is referring. Therefore, the transfer agent replies with a Rejection message with the reason 'UnknownOrInvalidReference'. 

**P874** The message flow works in a similar way when a TransferInInstruction message is sent.

[fig-0124 - original figure evidence](../diagrams/fig-0124.md)

