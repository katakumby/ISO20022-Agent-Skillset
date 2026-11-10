---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation Status Reporting"]
content_origin: "source-transcription"
---

# Order and Confirmation Status Reporting

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Scope and Functionality / Groups of MessageDefinitions and Functionality / Groups / Order and Confirmation Status Reporting.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P140** Order and Confirmation Status Reporting

**P141** The OrderInstructionStatusReport message informs the instructing party of the status of its order message, for example, SubscriptionOrder, SubscriptionBulkOrder, RedemptionOrder, RedemptionBulkOrder or SwitchOrder. 

**P142** The OrderCancellationStatusReport message informs the instructing party of the status of its order cancellation request message, for example, SubscriptionOrderCancellationRequest, SubscriptionBulkOrderCancellationRequest, RedemptionOrderCancellationRequest, RedemptionBulkOrderCancellationRequest or SwitchOrderCancellationRequest.

**P143** The RequestForOrderConfirmationStatusReport is used to request the status of a previously sent confirmation. The OrderConfirmationStatusReport is sent to the executing party to provide the status of an order confirmation. The RequestForOrderStatusReport message requests the status of an order message or an order cancellation request message.

[T9 - complete table](../tables/tbl-0009.md)

