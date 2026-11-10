---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "BusinessTransactions - Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service Scenarios", "Tripartite Central Matching Without Confirmation Distribution Service"]
content_origin: "source-transcription"
---

# Tripartite Central Matching Without Confirmation Distribution Service

Source: [src-000180](../../../../../../../../../evidence/omitted/620693d01e301c06503cea9a.md). Locator: heading path BusinessTransactions / BusinessTransactions - Central Matching / Tripartite Central Matching Without Confirmation Distribution Service Scenarios / Tripartite Central Matching Without Confirmation Distribution Service.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P232** Tripartite Central Matching Without Confirmation Distribution Service

**P233** The executing broker sends a trade confirmation to the CMU. The CMU advise both parties that the trade confirmation is not paired yet. The investment manager sends the corresponding trade confirmation to the CMU. The CMU performs a matching process between the two confirmations and sends matching status messages to both parties, reflecting the outcome of the matching process. The CMU will forward the confirmation received from both the executing broker and investment manager to the trustee. If the trustee agrees with the details of the confirmations, it may send an affirmation message to the CMU. The message will bind the parties to the trade details of the confirmation being affirmed. Upon receipt of the affirmation message, the CMU will send an affirmation status message to the executing broker and the trade may move into the settlement process.

[fig-0022 - original figure evidence](../diagrams/fig-0022.md)

**P236**   


