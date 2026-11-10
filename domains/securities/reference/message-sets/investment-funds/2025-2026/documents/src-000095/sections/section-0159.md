---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Portfolio Transfer Management", "Cancellation", "Rejected Cancellation - Invalid Reference"]
content_origin: "source-transcription"
---

# Rejected Cancellation - Invalid Reference

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Portfolio Transfer Management / Cancellation / Rejected Cancellation - Invalid Reference.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P794** Rejected Cancellation - Invalid Reference

**P795** A transferee (new plan manager or instructing party) sends a PortfolioTransferInstruction message to the transferor (old plan manager or executing party) to transfer the products held by an investor on an account serviced by the transferor.

**P796** Subsequently, the transferee sends a PortfolioTransferCancellationRequest message to the transferor to request the cancellation of the previously sent PortfolioTransferInstruction message, but, for example, misquotes the message reference of the PortfolioTransferInstruction.

**P797** The transferor replies with a SecuritiesMessageRejection message containing the reason InvalidOrUnrecognisedReference.

[fig-0112 - original figure evidence](../diagrams/fig-0112.md)

