---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Confirmation and Reversal", "Reversal Pre-Advice Cancellation"]
content_origin: "source-transcription"
---

# Reversal Pre-Advice Cancellation

Source: [src-000079](../../../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Locator: heading path BusinessTransactions / Confirmation and Reversal / Reversal Pre-Advice Cancellation.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P276** Reversal Pre-Advice Cancellation

**P277** This scenario illustrates a classical sequence of corporate action messages for the confirmation and phase of a corporate action event when a cancellation of a reversal pre-advice occurs.

**P278** Once the announcement phase and the election phase (in the cases of elective corporate action events) are completed and the account servicer has confirmed to the account owner that the movements have been applied on its account, and for some reasons, the movements must be reversed, the account servicer may optionally send a reversal CorporateActionMovementPreliminaryAdvice to the account owner to pre-advise him that the securities and/or cash movements are going to be reversed. The account servicer may also indicate the reason for the reversal.

**P279** If it finally comes out after this that the movements will not be reversed, the account servicer must cancel the reversal pre-advice by sending a CorporateActionMovementPreliminaryAdviceCancellationAdvice to the account owner to confirm the cancellation of the announced reversal of the movements.

[fig-0030 - original figure evidence](../diagrams/fig-0030.md)

