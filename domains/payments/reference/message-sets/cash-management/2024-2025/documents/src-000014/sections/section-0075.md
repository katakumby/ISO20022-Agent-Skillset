---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Standing Orders BusinessTransactions", "Delete Standing Order Scenario"]
content_origin: "source-transcription"
---

# Delete Standing Order Scenario

Source: [src-000014](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx). Locator: heading path BusinessTransactions / Standing Orders BusinessTransactions / Delete Standing Order Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P363** Delete Standing Order Scenario

**P364** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with information related to the reservation facility it manages for them.

**P365** At any time during the operating hours of the system, a member can request the deletion of a standing order for the transfer of the funds between two accounts that the transaction administrator maintains for the member. For this, the member can send a DeleteStandingOrder message to the transaction administrator. In this message, the member will identify the standing order it wants to have deleted.

**P366** The transaction administrator will reply with a Receipt message that may contain the status of the request.

[fig-0036 - original figure evidence](../diagrams/fig-0036.md)

