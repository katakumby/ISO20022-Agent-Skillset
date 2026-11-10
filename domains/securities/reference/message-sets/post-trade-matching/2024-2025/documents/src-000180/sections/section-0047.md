---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "BusinessTransactions - Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service Scenarios", "Tripartite Central Matching Without Confirmation Distribution Service Cancellation by Investment Manager"]
content_origin: "source-transcription"
---

# Tripartite Central Matching Without Confirmation Distribution Service Cancellation by Investment Manager

Source: [src-000180](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart1_PostTradeMatching_2024_2025_v2.docx). Locator: heading path BusinessTransactions / BusinessTransactions - Central Matching / Tripartite Central Matching Without Confirmation Distribution Service Scenarios / Tripartite Central Matching Without Confirmation Distribution Service Cancellation by Investment Manager.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P245** Tripartite Central Matching Without Confirmation Distribution Service Cancellation by Investment Manager

**P246** The executing broker sends a trade confirmation to the CMU. The CMU advise both parties that the trade confirmation is not paired yet. The investment manager sends the corresponding trade confirmation to the CMU. The CMU performs a matching process between the two confirmations and sends matching status messages to both parties, reflecting the outcome of the matching process. The investment manager may, for whatever reason, send a new confirmation or may, upon mutual agreement, send a confirmation cancellation. The CMU advise the investment manager that they send the cancellation to the executing broker. The CMU will forward the cancellation received from the investment manager and send the cancellation on behalf of the executing broker to the trustee.

[fig-0025 - original figure evidence](../diagrams/fig-0025.md)

**P248**   


