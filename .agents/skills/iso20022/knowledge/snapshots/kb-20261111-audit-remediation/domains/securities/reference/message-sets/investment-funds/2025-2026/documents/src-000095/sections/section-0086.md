---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Instruction Status Reporting", "Subscription", "Direct"]
content_origin: "source-transcription"
---

# Direct

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Order Instruction Status Reporting / Subscription / Direct.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P425** Direct

**P426** The instructing party sends a SubscriptionOrder message to the executing party. 

**P427** As the execution of the order in the SubscriptionOrder message is pending until there is enough cash in the account to pay for the subscription, the executing party responds with an OrderInstructionStatusReport message, with the status ConditionallyAccepted, and awaiting money.

[fig-0058 - original figure evidence](../diagrams/fig-0058.md)

