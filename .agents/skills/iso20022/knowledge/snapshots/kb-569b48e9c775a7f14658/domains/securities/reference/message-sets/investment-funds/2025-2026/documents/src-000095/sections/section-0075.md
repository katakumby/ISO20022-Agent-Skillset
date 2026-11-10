---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order and Confirmation", "Subscription ", "Intermediary"]
content_origin: "source-transcription"
---

# Intermediary

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Order and Confirmation / Subscription  / Intermediary.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P374** Intermediary

**P375** An instructing party sends a SubscriptionOrder message to the intermediary party. The intermediary party sends a SubscriptionOrder message to the executing party.

**P376** To confirm execution of the order, the executing party sends a SubscriptionOrderConfirmation message to the intermediary party. In turn, the intermediary party sends a SubscriptionOrderConfirmation message to the instructing party.

**P377** When more than one order is sent within the same order message, the response to the SubscriptionOrder message may be more than one SubscriptionOrderConfirmation message, as the valuation cycle of the financial instruments of each individual order may be different.

[fig-0048 - original figure evidence](../diagrams/fig-0048.md)

**P379** When more than one order is sent within the same order message, the response to the SubscriptionOrder message may be more than one SubscriptionOrderConfirmation message, as the valuation cycle of the financial instruments of each individual order may be different.

[fig-0049 - original figure evidence](../diagrams/fig-0049.md)

