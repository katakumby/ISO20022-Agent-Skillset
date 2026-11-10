---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Own Account Trade Type Scenarios", "Own Account Trade Type Cancellation"]
content_origin: "source-transcription"
---

# Own Account Trade Type Cancellation

Source: [src-000180](../../../../../../../../../evidence/omitted/620693d01e301c06503cea9a.md). Locator: heading path BusinessTransactions / BusinessTransactions - Local Matching Scenarios / Own Account Trade Type Scenarios / Own Account Trade Type Cancellation.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P208** Own Account Trade Type Cancellation

**P209** The executing broker sends a trade confirmation to the CMU. Once received from the broker, The CMU forwards the trade confirmation to the Institutional Investor. The Institutional Investor will compare the details of the confirmation with their details of the trade. If the details are irreconcilable, a disaffirmation message will be sent to the CMU. The CMU sends a disaffirmation status message to the executing broker upon receipt of the disaffirmation message from the Institutional Investor which may result in the cancellation of the trade or the sending of a new confirmation.

[fig-0017 - original figure evidence](../diagrams/fig-0017.md)

**P212**   


