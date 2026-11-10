---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Portfolio Transfer Management", "Cancellation", "Cancellation "]
content_origin: "source-transcription"
---

# Cancellation 

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Portfolio Transfer Management / Cancellation / Cancellation .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P789** Cancellation 

**P790** A transferee (new plan manager or instructing party) sends a PortfolioTransferInstruction message to the transferor (old plan manager or executing party) to transfer the products held by an investor on an account serviced by the transferor.

**P791** Subsequently, the transferee sends a PortfolioTransferCancellationRequest message to the transferor to request the cancellation of the previously sent PortfolioTransferInstruction message.

**P792** The transferor replies with a TransferCancellationStatusReport message with the appropriate status, for example, Accepted (PACK).

[fig-0111 - original figure evidence](../diagrams/fig-0111.md)

