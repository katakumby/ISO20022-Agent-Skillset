---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Confirmation Status Reporting ", "Switch "]
content_origin: "source-transcription"
---

# Switch 

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order Confirmation Status Reporting  / Switch .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P607** Switch 

**P608** The instructing party sends a SwitchOrder message to the executing party. 

**P609** After execution of the order, the executing party sends a SwitchOrderConfirmation message to the instructing party.

**P610** As the executing party has quoted an order reference that is not recognised, the instructing party sends an OrderConfirmationStatusReport message to inform that the confirmation message is rejected.

[fig-0086 - original figure evidence](../diagrams/fig-0086.md)

