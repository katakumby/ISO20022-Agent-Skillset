---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Standing Orders BusinessTransactions", "Get/Return Standing Order Scenario"]
content_origin: "source-transcription"
---

# Get/Return Standing Order Scenario

Source: [src-000014](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx). Locator: heading path BusinessTransactions / Standing Orders BusinessTransactions / Get/Return Standing Order Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P341** Get/Return Standing Order Scenario

**P342** At any time during operating hours of a system, a (direct) member can query the transaction administrator (which can be a financial institution, a matching engine or a settlement engine) to get information about the standing orders that are defined for the account(s) that the transaction administrator maintains for the member.

**P343** The member initiates the exchange by sending a GetStandingOrder message to the transaction administrator.

**P344** The transaction administrator replies with a ReturnStandingOrder message that will contain either the response to the criteria expressed in the GetStandingOrder message, or an error indication.

[fig-0032 - original figure evidence](../diagrams/fig-0032.md)

