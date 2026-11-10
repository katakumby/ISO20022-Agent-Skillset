---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "System Status ", "Get/Return Member Scenario"]
content_origin: "source-transcription"
---

# Get/Return Member Scenario

Source: [src-000014](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx). Locator: heading path BusinessTransactions / System Status  / Get/Return Member Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P319** Get/Return Member Scenario

**P320** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with business information related to the management of the system, not related to the transactions created in the system.

**P321** At any time during the operating hours of the system, a member can query the transaction administrator to get information about the membership of the system. For this, the member can initiate the exchange by sending a GetMember message to the transaction administrator. The transaction administrator replies with a ReturnMember message that will contain either the response to the criteria expressed in the GetMember message, or an error indication.

[fig-0028 - original figure evidence](../diagrams/fig-0028.md)

