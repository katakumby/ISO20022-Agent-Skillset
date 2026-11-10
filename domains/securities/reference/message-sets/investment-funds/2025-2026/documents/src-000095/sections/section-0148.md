---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Confirmation Status Request ", "Redemption "]
content_origin: "source-transcription"
---

# Redemption 

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order Confirmation Status Request  / Redemption .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P738** Redemption 

**P739** An instructing party sends a RedemptionOrder message to the executing party.

**P740** The executing party replies with a RedemptionOrderConfirmation message.

**P741** As execution details need to be amended, the executing party sends another RedemptionOrderConfirmation message, with the AmendmentIndicator set to 'true' or '1'.

**P742** Later, the executing party sends a RequestForOrderConfirmationStatusReport message to find out the status of its RedemptionOrderConfirmation message (amendment) message.

**P743** The instructing party sends an OrderConfirmationStatusReport message to the executing party, indicating the status of the RedemptionOrderConfirmation (amendment) message is accepted.

[fig-0104 - original figure evidence](../diagrams/fig-0104.md)

