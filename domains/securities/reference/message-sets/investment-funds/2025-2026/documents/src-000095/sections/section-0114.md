---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request", "Request Status of Subscription"]
content_origin: "source-transcription"
---

# Request Status of Subscription

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order Cancellation and Status  / Order Cancellation Status Request / Request Status of Subscription.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P569** Request Status of Subscription

**P570** An instructing party sends a SubscriptionOrder message to the executing party.

**P571** Subsequently, the instructing party sends a SubscriptionOrderCancellationRequest message to the executing party.

**P572** Later, the instructing party sends a RequestForOrderStatusReport message to find out the status of its cancellation request.

**P573** As the executing party has now effected the cancellation, it sends an OrderCancellationStatusReport message, with the status CancellationCompleted (CAND), to the instructing party.

[fig-0080 - original figure evidence](../diagrams/fig-0080.md)

