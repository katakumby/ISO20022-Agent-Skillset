---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Cancellation and Status ", "Redemption ", "Request and Status - Bulk"]
content_origin: "source-transcription"
---

# Request and Status - Bulk

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Order Cancellation and Status  / Redemption  / Request and Status - Bulk.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P544** Request and Status - Bulk

**P545** Instructing party 1 sends a RedemptionOrder message to the intermediary party. Instructing party 2 sends a RedemptionOrder message to the intermediary party. There may be many instructing parties sending redemption orders to the intermediary party. 

**P546** The intermediary party collects the individual orders. As the orders sent by instructing parties 1 and 2 are for the same financial instrument, the orders are grouped together and the intermediary sends a RedemptionBulkOrder message to the executing party.

**P547** Subsequently, instructing party 1 sends a RedemptionOrderCancellationRequest message to the intermediary party. In turn, the intermediary party sends a RedemptionBulkOrderCancellationRequest message to the executing party. 

**P548** As the bulk order has not yet been executed, the executing party effects the cancellation and sends an OrderCancellationStatusReport message, with the status CancellationCompleted (CAND), to the intermediary party. 

**P549** The RedemptionBulkOrderCancellationRequest message cancels the entire previously sent bulk order message, therefore, the intermediary party sends a RedemptionBulkOrder to re-instruct the order from instructing party 2 (and orders from other instructing parties for the same financial instrument). 

**P550** After the intermediary party cancels the order of instructing party 1, the intermediary party sends an OrderCancellationStatusReport message, with the status CancellationCompleted (CAND), to instructing party 1. 

**P551** Later, when the new bulk order has been executed, the executing party sends a RedemptionBulkOrderConfirmation message to the intermediary party. In turn, the intermediary party sends a RedemptionOrderConfirmation message to instructing party 2. 

[fig-0077 - original figure evidence](../diagrams/fig-0077.md)

