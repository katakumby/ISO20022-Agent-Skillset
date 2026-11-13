---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "BusinessTransactions - Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service Scenarios", "Tripartite Central Matching Without Confirmation Distribution Service Rejection"]
content_origin: "source-transcription"
---

# Tripartite Central Matching Without Confirmation Distribution Service Rejection

Source: [src-000180](../../../../../../../../../evidence/omitted/620693d01e301c06503cea9a.md). Locator: heading path BusinessTransactions / BusinessTransactions - Central Matching / Tripartite Central Matching Without Confirmation Distribution Service Scenarios / Tripartite Central Matching Without Confirmation Distribution Service Rejection.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P249** Tripartite Central Matching Without Confirmation Distribution Service Rejection

**P250** The executing broker sends a trade confirmation to the CMU. The CMU advise both parties that the trade confirmation is not paired yet. The investment manager sends the corresponding trade confirmation to the CMU. The CMU performs a matching process between the two confirmations and sends matching status messages to both parties, reflecting the outcome of the matching process. The CMU forward the confirmation received from both the executing broker and investment manager to the trustee. Should the trustee not agree with the details of the confirmations, it may send a disaffirmation message to the CMU. The CMU sends a disaffirmation status message to the executing broker, which may lead to a new confirmation being sent to the CMU of a confirmation cancellation being sent to the CMU. The CMU forward the cancellation to the investment manager. The CMU advise the executing broker that they send the cancellation to the investment manager. The CMU will forward the cancellation received from the investment manager and send the cancellation on behalf of the executing broker to the trustee.

[fig-0026 - original figure evidence](../diagrams/fig-0026.md)

**P253**   


