---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Announcement ", "Announcement and Cancellation due to Processing Error"]
content_origin: "source-transcription"
---

# Announcement and Cancellation due to Processing Error

Source: [src-000079](../../../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Locator: heading path BusinessTransactions / Announcement  / Announcement and Cancellation due to Processing Error.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P223** Announcement and Cancellation due to Processing Error

**P224** This scenario illustrates a classical sequence of corporate action messages when a corporate action event is cancelled by the account servicer after having been previously but erroneously announced to the account owner. This might happen when the account servicer sends announcement messages to the account owner whilst for instance it has no holdings in the security concerned by the corporate action event announced. 

**P225** The account servicer sends a new CorporateActionNotification to the account owner as a preliminary announcement of a corporate action event concerning a security in which the account owner has for instance no holdings on its account.

**P226** Once the account servicer notices that the account owner should not have been informed about this corporate action event, the account servicer sends a CorporateActionCancellationAdvice to the account owner with the cancellation reason indicating a processing error.

**P227** Note also that it is likely that a CorporateActionCancellationAdvice is sent only after several replacement CorporateActionNotification or a CorporateActionMovementPreliminaryAdvice have been sent, should the account servicer not notice its mistake immediately.

[fig-0022 - original figure evidence](../diagrams/fig-0022.md)

