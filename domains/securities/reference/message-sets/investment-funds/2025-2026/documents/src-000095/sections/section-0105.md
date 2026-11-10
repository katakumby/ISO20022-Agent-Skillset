---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Cancellation and Status ", "Subscription ", "Request and Status - Bulk "]
content_origin: "source-transcription"
---

# Request and Status - Bulk 

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order Cancellation and Status  / Subscription  / Request and Status - Bulk .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P524** Request and Status - Bulk 

**P525** Instructing party 1 sends a SubscriptionOrder message to the intermediary party. Instructing party 2 sends a SubscriptionOrder message to the intermediary party. There may be many instructing parties sending subscription orders to the intermediary party. 

**P526** The intermediary party collects the individual orders. As the orders sent by instructing parties 1 and 2 are for the same financial instrument, the orders are grouped together and the intermediary sends a SubscriptionBulkOrder message to the executing party.

**P527** Subsequently, instructing party 1 sends a SubscriptionOrderCancellationRequest message to the intermediary party. In turn, the intermediary party sends a SubscriptionBulkOrderCancellationRequest message to the executing party. 

**P528** As the bulk order has not yet been executed, the executing party effects the cancellation and sends an OrderCancellationStatusReport message, with the status CancellationCompleted (CAND), to the intermediary party.

**P529** The SubscriptionBulkOrderCancellationRequest message cancels the entire previously sent bulk order message, therefore, the intermediary party sends a SubscriptionBulkOrder message to re-instruct the order from instructing party 2 (and orders from other instructing parties for the same financial instrument). 

**P530** After the intermediary party cancels the order of instructing party 1, the intermediary party sends an OrderCancellationStatusReport message, with the status CancellationCompleted (CAND), to instructing party 1.

**P531** Later, when the new bulk order has been executed, the executing party sends a SubscriptionBulkOrderConfirmation message to the intermediary party. In turn, the intermediary party sends a SubscriptionOrderConfirmation message to instructing party 2. 

[fig-0074 - original figure evidence](../diagrams/fig-0074.md)

