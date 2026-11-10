---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Portfolio Transfer Management", "Cancellation", "Rejected Cancellation – Already Executed"]
content_origin: "source-transcription"
---

# Rejected Cancellation – Already Executed

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Portfolio Transfer Management / Cancellation / Rejected Cancellation – Already Executed.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P799** Rejected Cancellation – Already Executed

**P800** A transferee (new plan manager or instructing party) sends a PortfolioTransferInstruction message to the transferor (old plan manager or executing party) to transfer the products held by an investor on an account serviced by the transferor.

**P801** The transferor sends a PortfolioTransferConfirmation message to confirm that the products have been transferred to the nominee account.

**P802** Later, the transferee sends a PortfolioTransferCancellationRequest message to the transferor.

**P803** The transferor replies with a TransferCancellationStatusReport message containing the status Rejected with reason Already Executed (COSE).

[fig-0113 - original figure evidence](../diagrams/fig-0113.md)

