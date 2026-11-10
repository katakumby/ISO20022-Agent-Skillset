---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Confirmation Amendment ", "Redemption ", "Intermediary "]
content_origin: "source-transcription"
---

# Intermediary 

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order Confirmation Amendment  / Redemption  / Intermediary .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P644** Intermediary 

**P645** An instructing party sends a RedemptionOrder message to the intermediary party. In turn, the intermediary party sends a RedemptionOrder message to the executing party.

**P646** To confirm execution of the order, the executing party sends a RedemptionOrderConfirmation message to the intermediary party. In turn, the intermediary party sends a RedemptionOrderConfirmation message to the instructing party.

**P647** As an amendment has to be made to the RedemptionOrderConfirmation message details, another RedemptionOrderConfirmation message is sent by the executing party to inform the intermediary about the amended details, with the AmendmentIndicator set to 'true' or '1'. 

**P648** In turn, the intermediary party sends a RedemptionOrderConfirmation message to the instructing party, with the AmendmentIndicator set to 'true' or '1'. 

[fig-0091 - original figure evidence](../diagrams/fig-0091.md)

