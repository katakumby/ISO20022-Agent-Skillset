---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Confirmation Amendment ", "Redemption ", "Bulk "]
content_origin: "source-transcription"
---

# Bulk 

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order Confirmation Amendment  / Redemption  / Bulk .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P650** Bulk 

**P651** Instructing party 1 sends a RedemptionOrder message to the intermediary party. Instructing party 2 sends a RedemptionOrder message to the intermediary party. 

**P652** The intermediary party collects the individual orders. As the orders sent by instructing parties 1 and 2 are for the same financial instrument, the orders are grouped together and the intermediary sends a RedemptionBulkOrder message to the transfer agent. 

**P653** The executing party sends a RedemptionBulkOrderConfirmation message to the intermediary party. 

**P654** The intermediary party splits up the confirmation according to the originating chain of instructions and sends a RedemptionOrderConfirmation message to instructing party 1 and a RedemptionOrderConfirmation message to instructing party 2. 

**P655** As an amendment has to be made to the RedemptionBulkOrderConfirmation message details, another RedemptionBulkOrderConfirmation message is sent by the executing party to inform the intermediary about the amended details, with the AmendmentIndicator set to 'true' or '1'.. 

**P656** In turn, the intermediary party splits up the confirmation message according to the originating chain of instructions and sends a RedemptionOrderConfirmation message to instructing party 1 with the AmendmentIndicator set to 'true' or '1' and a RedemptionOrderConfirmation message to instructing party 2 with the AmendmentIndicator set to 'true' or '1'.

[fig-0092 - original figure evidence](../diagrams/fig-0092.md)

