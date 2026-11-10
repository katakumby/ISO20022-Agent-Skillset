---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Confirmation Status Reporting ", "Subscription "]
content_origin: "source-transcription"
---

# Subscription 

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order Confirmation Status Reporting  / Subscription .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P597** Subscription 

**P598** The instructing party sends a SubscriptionOrder message to the executing party. 

**P599** After execution of the order, the executing party sends a SubscriptionOrderConfirmation message to the instructing party.

**P600** As the executing party has quoted an order reference that is not recognised, the instructing party sends an OrderConfirmationStatusReport message to inform that the confirmation message is rejected.

[fig-0084 - original figure evidence](../diagrams/fig-0084.md)

