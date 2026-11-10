---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Confirmation Cancellation ", "Subscription ", "Intermediary"]
content_origin: "source-transcription"
---

# Intermediary

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order Confirmation Cancellation  / Subscription  / Intermediary.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P682** Intermediary

**P683** An instructing party sends a SubscriptionOrder message to the intermediary party. The intermediary party sends a SubscriptionOrder message to the executing party.

**P684** To confirm execution of the order, the executing party sends a SubscriptionOrderConfirmation message to the intermediary party. In turn, the intermediary party sends a SubscriptionOrderConfirmation message to the instructing party.

**P685** As the confirmation needs to be cancelled, SubscriptionOrderConfirmationCancellationInstruction message is sent by the executing party to inform the intermediary. In turn, the intermediary party sends a SubscriptionOrderConfirmationCancellationInstruction message to the instructing party.

[fig-0096 - original figure evidence](../diagrams/fig-0096.md)

