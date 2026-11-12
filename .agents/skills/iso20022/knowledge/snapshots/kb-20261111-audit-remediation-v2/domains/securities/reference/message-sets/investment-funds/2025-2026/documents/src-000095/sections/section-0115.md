---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request", "Request Status of Redemption"]
content_origin: "source-transcription"
---

# Request Status of Redemption

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Order Cancellation and Status  / Order Cancellation Status Request / Request Status of Redemption.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P575** Request Status of Redemption

**P576** An instructing party sends a RedemptionOrder message to the executing party.

**P577** Subsequently, the instructing party sends a RedemptionOrderCancellationRequest message to the executing party.

**P578** Later, the instructing party sends a RequestForOrderStatusReport message to find out the status of its cancellation request.

**P579** As the executing party has now effected the cancellation, it sends an OrderCancellationStatusReport message, with the status CancellationCompleted (CAND), to the instructing party.

[fig-0081 - original figure evidence](../diagrams/fig-0081.md)

