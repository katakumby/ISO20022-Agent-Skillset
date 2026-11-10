---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Portfolio Transfer Management", "Status ", "Request Status"]
content_origin: "source-transcription"
---

# Request Status

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Portfolio Transfer Management / Status  / Request Status.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P783** Request Status

**P784** A transferee (new plan manager or instructing party) sends a PortfolioTransferInstruction message to the transferor (old plan manager or executing party) to transfer the products held by an investor on an account serviced by the transferor.

**P785** Subsequently, the transferee sends a RequestForTransferStatusReport message to the transferor to request the status of its instruction.

**P786** The transferor replies with a TransferInstructionStatusReport message with the appropriate status, for example, Accepted (PACK).

[fig-0110 - original figure evidence](../diagrams/fig-0110.md)

