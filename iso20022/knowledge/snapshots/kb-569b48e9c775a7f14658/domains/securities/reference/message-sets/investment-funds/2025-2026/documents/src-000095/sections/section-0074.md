---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order and Confirmation", "Subscription ", "Direct"]
content_origin: "source-transcription"
---

# Direct

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Order and Confirmation / Subscription  / Direct.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P368** Direct

**P369** An instructing party sends a SubscriptionOrder message to the executing party.

**P370** To confirm execution of the order, the executing party sends a SubscriptionOrderConfirmation message to the instructing party. 

[fig-0046 - original figure evidence](../diagrams/fig-0046.md)

**P372** When more than one order is sent within the same order message, the response to the SubscriptionOrder message may be more than one SubscriptionOrderConfirmation message, as the valuation cycle of the financial instruments of each individual order may be different. 

[fig-0047 - original figure evidence](../diagrams/fig-0047.md)

