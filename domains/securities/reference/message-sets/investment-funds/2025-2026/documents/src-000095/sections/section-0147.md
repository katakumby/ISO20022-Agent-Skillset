---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Confirmation Status Request ", "Subscription "]
content_origin: "source-transcription"
---

# Subscription 

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order Confirmation Status Request  / Subscription .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P731** Subscription 

**P732** An instructing party sends a SubscriptionOrder message to the executing party.

**P733** The executing party replies with a SubscriptionOrderConfirmation message.

**P734** As execution details need to be amended, the executing party sends another SubscriptionOrderConfirmation message, with the AmendmentIndicator set to 'true' or '1'.

**P735** Later, the executing party sends a RequestForOrderConfirmationStatusReport message to find out the status of its SubscriptionOrderConfirmation (amendment) message.

**P736** The instructing party sends an OrderConfirmationStatusReport message to the executing party, indicating the status of the SubscriptionOrderConfirmation (amendment) message is accepted.

[fig-0103 - original figure evidence](../diagrams/fig-0103.md)

