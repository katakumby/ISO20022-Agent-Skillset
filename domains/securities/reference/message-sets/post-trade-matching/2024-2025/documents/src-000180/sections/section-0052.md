---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "BusinessTransactions - Central Matching", "Tripartite Central Matching With Confirmation Distribution Service Scenarios", "Tripartite Central Matching With Confirmation Distribution Service Cancellation by Investment Manager"]
content_origin: "source-transcription"
---

# Tripartite Central Matching With Confirmation Distribution Service Cancellation by Investment Manager

Source: [src-000180](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart1_PostTradeMatching_2024_2025_v2.docx). Locator: heading path BusinessTransactions / BusinessTransactions - Central Matching / Tripartite Central Matching With Confirmation Distribution Service Scenarios / Tripartite Central Matching With Confirmation Distribution Service Cancellation by Investment Manager.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P265** Tripartite Central Matching With Confirmation Distribution Service Cancellation by Investment Manager

**P266** The executing broker sends a trade confirmation to the CMU. The CMU forwards the confirmation received from the broker to the investment manager. The investment manager compares the details of the trade to its own details and sends a trade confirmation to the CMU. The CMU performs a matching process and sends matching status messages to both parties reflecting the outcome of the matching process. The investment manager may, for whatever reason, send a confirmation cancellation message to the CMU or it may send a new confirmation to the CMU. The CMU forwards a cancellation message to the executing broker. The CMU advise the investment manager that they send a cancellation to the executing broker. The CMU will forward the cancellation received from the investment manager and send the cancellation on behalf of the executing broker to the trustee.

[fig-0029 - original figure evidence](../diagrams/fig-0029.md)

**P268**   


