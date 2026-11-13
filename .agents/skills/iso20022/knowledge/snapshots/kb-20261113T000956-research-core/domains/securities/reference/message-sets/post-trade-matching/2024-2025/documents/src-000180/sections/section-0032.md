---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Through Type Scenarios", "Through Type Cancellation"]
content_origin: "source-transcription"
---

# Through Type Cancellation

Source: [src-000180](../../../../../../../../../evidence/omitted/620693d01e301c06503cea9a.md). Locator: heading path BusinessTransactions / BusinessTransactions - Local Matching Scenarios / Through Type Scenarios / Through Type Cancellation.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P198** Through Type Cancellation

**P199** The executing broker and the investment manager send a confirmation to the CMU. The CMU will forward the two confirmations received to the trustee. The trustee will send an affirmation message to the CMU if it agrees with the detail of the trade. The message will bind the parties to the trade details of the confirmation being affirmed. The CMU will send an affirmation status message to the executing broker upon receipt of the affirmation message from the trustee. The executing broker and investment manager may, for whatever reason, decide to cancel the confirmation and a new confirmation may be sent. Cancellation of the confirmation may also imply the cancellation of the trade, in which case a new confirmation will not be sent.

[fig-0015 - original figure evidence](../diagrams/fig-0015.md)

**P201**   


