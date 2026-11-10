---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order and Confirmation", "Redemption", "Direct"]
content_origin: "source-transcription"
---

# Direct

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Order and Confirmation / Redemption / Direct.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P388** Direct

**P389** An instructing party sends a RedemptionOrder message to the executing party. 

**P390** To confirm execution of the order, the executing party sends a RedemptionOrderConfirmation message to the instructing party. 

[fig-0051 - original figure evidence](../diagrams/fig-0051.md)

**P392** When more than one order is sent within the same order message, the response to the RedemptionOrder message may be more than one RedemptionOrderConfirmation message, as the valuation cycle of the financial instruments of each individual order may be different.

[fig-0052 - original figure evidence](../diagrams/fig-0052.md)

