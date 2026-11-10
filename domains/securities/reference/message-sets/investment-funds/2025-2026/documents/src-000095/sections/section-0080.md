---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order and Confirmation", "Redemption", "Bulk"]
content_origin: "source-transcription"
---

# Bulk

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order and Confirmation / Redemption / Bulk.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P400** Bulk

**P401** Instructing party 1 sends a RedemptionOrder message to the intermediary party. Instructing party 2 sends a RedemptionOrder message to the intermediary party.

**P402** The intermediary party collects the individual orders. As the orders sent by instructing parties 1 and 2 are for the same financial instrument, the orders are grouped together and the intermediary party sends a RedemptionBulkOrder message to the executing party. 

**P403** The executing party sends a RedemptionBulkOrderConfirmation message to the intermediary party. 

**P404** The intermediary party splits up the confirmation according to the originating chain of instructions and sends a RedemptionOrderConfirmation message to instructing party 1 and a RedemptionOrderConfirmation message to instructing party 2. 

[fig-0055 - original figure evidence](../diagrams/fig-0055.md)

