---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Duplex Type Scenarios", "Duplex Type Rejection by Cash Correspondent"]
content_origin: "source-transcription"
---

# Duplex Type Rejection by Cash Correspondent

Source: [src-000180](../../../../../../../../../evidence/omitted/620693d01e301c06503cea9a.md). Locator: heading path BusinessTransactions / BusinessTransactions - Local Matching Scenarios / Duplex Type Scenarios / Duplex Type Rejection by Cash Correspondent.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P222** Duplex Type Rejection by Cash Correspondent

**P223** The Underwriter sends a trade confirmation to the CMU. The CMU forwards the confirmation received from the Underwriter to the Transfer Agent. Should the trade detail on the confirmation agree with that of the Transfer Agent, it sends an affirmation message to the CMU. Upon receipt of the affirmation message from the Transfer Agent, The CMU forwards the confirmation received from the Underwriter to the Cash Settlement Agent. The Cash Settlement Agent compares the trade details of the confirmation (Underwriter) with its own trade detail and if there are irreconcilable differences sends a disaffirmation message to the CMU. Upon receipt of the disaffirmation message from the Cash Settlement Agent, the CMU sends a disaffirmation status message to the Underwriter which may lead to a trade confirmation cancellation or a new trade confirmation message from the Underwriter to the CMU.

[fig-0020 - original figure evidence](../diagrams/fig-0020.md)

**P225**   


