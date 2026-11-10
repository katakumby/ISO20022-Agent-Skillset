---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order and Confirmation", "Redemption", "Intermediary"]
content_origin: "source-transcription"
---

# Intermediary

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order and Confirmation / Redemption / Intermediary.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P394** Intermediary

**P395** An instructing party sends a RedemptionOrder message to the intermediary party. The intermediary party sends a RedemptionOrder message to the executing party. 

**P396** To confirm execution of the order, the executing party sends a RedemptionOrderConfirmation message to the intermediary party. In turn, the intermediary party sends a RedemptionOrderConfirmation message to the instructing party. 

[fig-0053 - original figure evidence](../diagrams/fig-0053.md)

**P398** When more than one order is sent within the same order message, the response to the RedemptionOrder message may be more than one RedemptionOrderConfirmation message, as the valuation cycle of the financial instruments of each individual order may be different.

[fig-0054 - original figure evidence](../diagrams/fig-0054.md)

