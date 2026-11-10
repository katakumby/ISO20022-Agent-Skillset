---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Confirmation Status Reporting ", "Redemption "]
content_origin: "source-transcription"
---

# Redemption 

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order Confirmation Status Reporting  / Redemption .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P602** Redemption 

**P603** An instructing party sends a RedemptionOrder message to the executing party. 

**P604** After execution of the order, the executing party sends a RedemptionOrderConfirmation message to the instructing party.

**P605** As the executing party has quoted an order reference that is not recognised, the instructing party sends an OrderConfirmationStatusReport message to inform that the confirmation message is rejected.

[fig-0085 - original figure evidence](../diagrams/fig-0085.md)

