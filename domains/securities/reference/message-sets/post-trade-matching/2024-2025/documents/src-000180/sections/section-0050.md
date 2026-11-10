---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "BusinessTransactions - Central Matching", "Tripartite Central Matching With Confirmation Distribution Service Scenarios", "Tripartite Central Matching With Confirmation Distribution Service"]
content_origin: "source-transcription"
---

# Tripartite Central Matching With Confirmation Distribution Service

Source: [src-000180](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart1_PostTradeMatching_2024_2025_v2.docx). Locator: heading path BusinessTransactions / BusinessTransactions - Central Matching / Tripartite Central Matching With Confirmation Distribution Service Scenarios / Tripartite Central Matching With Confirmation Distribution Service.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P255** Tripartite Central Matching With Confirmation Distribution Service

**P256** The executing broker sends a trade confirmation to the CMU. The CMU forwards the confirmation received from the broker to the investment manager. The investment manager compares the details of the trade to its own details and sends a trade confirmation to the CMU. The CMU performs a matching process and sends matching status messages to both parties reflecting the outcome of the matching process. If matched, the CMU sends both the confirmations received from the investment manager and from the executing broker to the trustee. If the trustee agrees with the details of the trade, it sends an affirmation message to the CMU. The message will bind the parties to the trade details of the confirmation being affirmed. Upon receipt of the affirmation message from the trustee, the CMU sends an affirmation status message to the executing broker and the trade can move into the settlement process.

[fig-0027 - original figure evidence](../diagrams/fig-0027.md)

**P259**   


