---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Announcement ", "Announcement and Cancellation of Event"]
content_origin: "source-transcription"
---

# Announcement and Cancellation of Event

Source: [src-000079](../../../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Locator: heading path BusinessTransactions / Announcement  / Announcement and Cancellation of Event.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P217** Announcement and Cancellation of Event

**P218** This scenario illustrates a classical sequence of corporate action messages when a corporate action event is withdrawn by the issuer after having been previously announced through the chain of intermediaries and possibly to the end investor.

**P219** The account servicer sends a CorporateActionNotification to the account owner as an announcement of a corporate action event concerning a security in which the account owner has holdings on its account.

**P220** Once the account servicer has been informed that the corporate action event is withdrawn by the Issuer, the account servicer sends a CorporateActionCancellationAdvice to the account owner with the cancellation reason indicating a withdrawal of the event.

**P221** A corporate action event may be withdrawn by the Issuer at any moment during its life cycle. It is possible that CorporateActionCancellationAdvice is sent after several replacement CorporateActionNotification or CorporateActionMovementPreliminaryAdvice messages have been sent or even after the election phase of an event.

[fig-0021 - original figure evidence](../diagrams/fig-0021.md)

