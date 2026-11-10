---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Confirmation Amendment ", "Subscription ", "Bulk "]
content_origin: "source-transcription"
---

# Bulk 

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order Confirmation Amendment  / Subscription  / Bulk .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P630** Bulk 

**P631** Instructing party 1 sends a SubscriptionOrder message to the intermediary party. Instructing party 2 sends a SubscriptionOrder message to the intermediary party. 

**P632** The intermediary party collects the individual orders. As the orders sent by instructing parties 1 and 2 are for the same financial instrument, the orders are grouped together and the intermediary sends a SubscriptionBulkOrder message to the transfer agent. 

**P633** The executing party sends a SubscriptionBulkOrderConfirmation message to the intermediary party. 

**P634** The intermediary party splits up the confirmation according to the originating chain of instructions and sends a SubscriptionOrderConfirmation message to instructing party 1 and a SubscriptionOrderConfirmation message to instructing party 2. 

**P635** As an amendment has to be made to the SubscriptionBulkOrderConfirmation message details, another SubscriptionBulkOrderConfirmation message is sent by the executing party to inform the intermediary about the amended details, with the AmendmentIndicator set to 'true' or '1'.

**P636** In turn, the intermediary party splits up the confirmation message according to the originating chain of instructions and sends a SubscriptionOrderConfirmation message to instructing party 1 with the AmendmentIndicator set to 'true' or '1' and a SubscriptionOrderConfirmation message to instructing party 2 with the AmendmentIndicator set to 'true' or '1'.

[fig-0089 - original figure evidence](../diagrams/fig-0089.md)

