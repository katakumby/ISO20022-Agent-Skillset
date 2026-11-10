---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "BusinessTransactions - Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service Scenarios", "Tripartite Central Matching Without Confirmation Distribution Service Cancellation"]
content_origin: "source-transcription"
---

# Tripartite Central Matching Without Confirmation Distribution Service Cancellation

Source: [src-000180](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart1_PostTradeMatching_2024_2025_v2.docx). Locator: heading path BusinessTransactions / BusinessTransactions - Central Matching / Tripartite Central Matching Without Confirmation Distribution Service Scenarios / Tripartite Central Matching Without Confirmation Distribution Service Cancellation.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P237** Tripartite Central Matching Without Confirmation Distribution Service Cancellation

**P238** The executing broker sends a trade confirmation to the CMU. The CMU advise both parties that the trade confirmation is not paired yet. The investment manager sends the corresponding trade confirmation to the CMU. The CMU performs a matching process between the two confirmations and sends matching status messages to both parties, reflecting the outcome of the matching process. If unmatched, the investment manager may send a new confirmation or may, upon mutual agreement, send a confirmation cancellation. Or, the executing broker may send a new confirmation or may, upon mutual agreement, send a confirmation cancellation. The CMU will send a cancellation status advice to the counterparty.

[fig-0023 - original figure evidence](../diagrams/fig-0023.md)

