---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Confirmation Cancellation ", "Subscription ", "Bulk"]
content_origin: "source-transcription"
---

# Bulk

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order Confirmation Cancellation  / Subscription  / Bulk.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P687** Bulk

**P688** Instructing party 1 sends a SubscriptionOrder message to the intermediary party. Instructing party 2 sends a SubscriptionOrder message to the intermediary party. 

**P689** The intermediary party collects the individual orders. As the orders sent by instructing parties 1 and 2 are for the same financial instrument, the orders are grouped together and the intermediary sends a SubscriptionBulkOrder message to the transfer agent. 

**P690** The executing party sends a SubscriptionBulkOrderConfirmation message to the intermediary party. 

**P691** The intermediary party splits up the confirmation according to the originating chain of instructions and sends a SubscriptionOrderConfirmation message to instructing party 1 and a SubscriptionOrderConfirmation message to instructing party 2. 

**P692** As the confirmation needs to be cancelled, a SubscriptionBulkOrderConfirmationCancellationInstruction message is sent by the executing party to inform the intermediary. 

**P693** In turn, the intermediary party splits up the confirmation amendment message according to the originating chain of instructions and sends a SubscriptionOrderConfirmationCancellationInstruction message to instructing party 1 and a SubscriptionOrderConfirmationCancellationInstruction message to instructing party 2.

[fig-0097 - original figure evidence](../diagrams/fig-0097.md)

