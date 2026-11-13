---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "BusinessTransactions - Central Matching", "Tripartite Central Matching With Confirmation Distribution Service Scenarios", "Tripartite Central Matching With Confirmation Distribution Service Rejection"]
content_origin: "source-transcription"
---

# Tripartite Central Matching With Confirmation Distribution Service Rejection

Source: [src-000180](../../../../../../../../../evidence/omitted/620693d01e301c06503cea9a.md). Locator: heading path BusinessTransactions / BusinessTransactions - Central Matching / Tripartite Central Matching With Confirmation Distribution Service Scenarios / Tripartite Central Matching With Confirmation Distribution Service Rejection.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P269** Tripartite Central Matching With Confirmation Distribution Service Rejection

**P270** The executing broker sends a trade confirmation to the CMU. The CMU forwards the confirmation received from the broker to the investment manager. The investment manager compares the details of the trade to its own details and sends a trade confirmation to the CMU. The CMU performs a matching process and sends matching status messages to both parties reflecting the outcome of the matching process. If matched, the CMU sends both the confirmations received from the investment manager and from the executing broker to the trustee. If the trustee does not agree with the details of the trade, it sends a disaffirmation message to the CMU. Upon receipt of the disaffirmation message from the trustee, the CMU sends a disaffirmation status message to the broker, which may lead to the broker sending a new confirmation to the CMU or a confirmation cancellation. The CMU forwards a cancellation message to the investment manager. The CMU advise the executing broker that they send a cancellation to the investment manager. The CMU will forward the cancellation received from the investment manager and send the cancellation on behalf of the executing broker to the trustee.

[fig-0030 - original figure evidence](../diagrams/fig-0030.md)

**P272**   


