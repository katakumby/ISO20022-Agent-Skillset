---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Confirmation Amendment ", "Subscription ", "Intermediary "]
content_origin: "source-transcription"
---

# Intermediary 

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order Confirmation Amendment  / Subscription  / Intermediary .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P624** Intermediary 

**P625** An instructing party sends a SubscriptionOrder message to the intermediary party. In turn, the intermediary party sends a SubscriptionOrder message to the executing party.

**P626** To confirm execution of the order, the executing party sends a SubscriptionOrderConfirmation message to the intermediary party. In turn, the intermediary party sends a SubscriptionOrderConfirmation message to the instructing party.

**P627** As an amendment has to be made to the SubscriptionOrderConfirmation message details, another SubscriptionOrderConfirmation is sent by the executing party to inform the intermediary about the amended details, with the AmendmentIndicator set to 'true' or '1'. 

**P628** In turn, the intermediary party sends a SubscriptionOrderConfirmation message to the instructing party, with the AmendmentIndicator set to 'true' or '1'.

[fig-0088 - original figure evidence](../diagrams/fig-0088.md)

