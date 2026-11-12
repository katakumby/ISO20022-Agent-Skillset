---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Cancellation and Status ", "Redemption ", "Request and Status - Direct"]
content_origin: "source-transcription"
---

# Request and Status - Direct

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Order Cancellation and Status  / Redemption  / Request and Status - Direct.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P534** Request and Status - Direct

**P535** The instructing party sends a RedemptionOrder message to the executing party. 

**P536** Subsequently, the instructing party sends a RedemptionOrderCancellationRequest message to the executing party. 

**P537** As it is possible to cancel the order, the executing party responds by sending an OrderCancellationStatusReport message, with the status CancellationCompleted (CAND), to the instructing party.

[fig-0075 - original figure evidence](../diagrams/fig-0075.md)

