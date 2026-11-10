---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "System Status ", "Business Day Information", "Get/Return Business Day Information "]
content_origin: "source-transcription"
---

# Get/Return Business Day Information 

Source: [src-000014](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx). Locator: heading path BusinessTransactions / System Status  / Business Day Information / Get/Return Business Day Information .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P277** Get/Return Business Day Information 

**P278** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with general business information related to foreseen or unexpected events affecting the system.

**P279** At any time during the operating hours of the system, a member can query the transaction administrator to get information about a broadcast-type message previously sent by the transaction administrator. For this, the member can initiate the exchange by sending a GetBusinessDayInformation message to the transaction administrator. The transaction administrator replies with a ReturnBusinessDayInformation message that will contain either the response to the criteria expressed in the GetBusinessDayInformation message, or an error indication.

[fig-0022 - original figure evidence](../diagrams/fig-0022.md)

