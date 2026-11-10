---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request", "Request Status of Switch"]
content_origin: "source-transcription"
---

# Request Status of Switch

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Order Cancellation and Status  / Order Cancellation Status Request / Request Status of Switch.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P586** Request Status of Switch

**P587** An instructing party sends a SwitchOrder message to the executing party. 

**P588** Subsequently, the instructing party sends a SwitchOrderCancellationRequest message to the executing party.

**P589** Later, the instructing party sends a RequestForOrderStatusReport message to find out the status of its cancellation request.

**P590** As the executing party has now effected the cancellation, it sends an OrderCancellationStatusReport message, with the status CancellationCompleted (CAND), to the instructing party.

[fig-0083 - original figure evidence](../diagrams/fig-0083.md)

