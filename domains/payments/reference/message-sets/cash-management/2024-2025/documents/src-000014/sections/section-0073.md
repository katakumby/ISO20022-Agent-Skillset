---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Standing Orders BusinessTransactions", "Create Standing Order Scenario"]
content_origin: "source-transcription"
---

# Create Standing Order Scenario

Source: [src-000014](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx). Locator: heading path BusinessTransactions / Standing Orders BusinessTransactions / Create Standing Order Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P352** Create Standing Order Scenario

**P353** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with the ability to manage their liquidity.

**P354** At any time during the operating hours of the system, a member can request the transaction administrator to create a new standing order for the transfer of funds between two accounts that the transaction administrator maintains for the member.

**P355** For this, the member can send a CreateStandingOrder message to the transaction administrator. The transaction administrator will reply with a Receipt message that may contain the status of the request.

[fig-0034 - original figure evidence](../diagrams/fig-0034.md)

