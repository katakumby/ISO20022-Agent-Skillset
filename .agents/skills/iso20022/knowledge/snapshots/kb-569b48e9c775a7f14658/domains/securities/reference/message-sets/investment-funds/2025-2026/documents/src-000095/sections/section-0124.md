---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Confirmation Amendment ", "Subscription ", "Direct"]
content_origin: "source-transcription"
---

# Direct

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Order Confirmation Amendment  / Subscription  / Direct.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P619** Direct

**P620** An instructing party sends a SubscriptionOrder message to the executing party.

**P621** To confirm execution of the order, the executing party sends a SubscriptionOrderConfirmation message to the instructing party. 

**P622** As an amendment has to be made to the SubscriptionOrderConfirmation message details, another SubscriptionOrderConfirmation is sent with the AmendmentIndicator set to 'true' or '1'.

[fig-0087 - original figure evidence](../diagrams/fig-0087.md)

