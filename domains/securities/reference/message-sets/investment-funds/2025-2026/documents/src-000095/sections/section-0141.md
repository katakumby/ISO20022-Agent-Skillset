---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Confirmation Cancellation ", "Redemption ", "Intermediary"]
content_origin: "source-transcription"
---

# Intermediary

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order Confirmation Cancellation  / Redemption  / Intermediary.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P701** Intermediary

**P702** An instructing party sends a RedemptionOrder message to the intermediary party. 

**P703** The intermediary party sends a RedemptionOrder to the executing party. 

**P704** To confirm execution of the order, the executing party sends a RedemptionOrderConfirmation message to the intermediary party. In turn, the intermediary party sends a RedemptionOrderConfirmation message to the instructing party. 

**P705** As the confirmation needs to be cancelled, a RedemptionOrderConfirmationCancellationInstruction message is sent by the executing party to inform the intermediary. In turn, the intermediary party sends a RedemptionOrderConfirmationCancellationInstruction message to the instructing party. 

[fig-0099 - original figure evidence](../diagrams/fig-0099.md)

