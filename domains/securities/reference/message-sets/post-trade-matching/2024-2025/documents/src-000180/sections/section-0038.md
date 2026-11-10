---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Duplex Type Scenarios", "Duplex Type Rejection by Transfer Agent"]
content_origin: "source-transcription"
---

# Duplex Type Rejection by Transfer Agent

Source: [src-000180](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart1_PostTradeMatching_2024_2025_v2.docx). Locator: heading path BusinessTransactions / BusinessTransactions - Local Matching Scenarios / Duplex Type Scenarios / Duplex Type Rejection by Transfer Agent.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P218** Duplex Type Rejection by Transfer Agent

**P219** The Underwriter sends a trade confirmation to the CMU. The CMU forwards the confirmation received from the Underwriter to the Transfer Agent. The Transfer Agent compares the trade detail with its own trade detail and if there are irreconcilable differences, sends a disaffirmation message to the CMU. Upon receipt of the disaffirmation message, the CMU sends a disaffirmation status message to the Underwriter which may lead to a new trade confirmation message from the Underwriter to the CMU or a confirmation cancellation message from the Underwriter to the CMU. The CMU will forward a cancellation to the Transfer Agent and send a cancellation status advice to the Underwriter.

[fig-0019 - original figure evidence](../diagrams/fig-0019.md)

**P221**   


