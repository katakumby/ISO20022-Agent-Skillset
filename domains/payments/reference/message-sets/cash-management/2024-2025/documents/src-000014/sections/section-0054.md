---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Account management", "Get/Return Account"]
content_origin: "source-transcription"
---

# Get/Return Account

Source: [src-000014](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx). Locator: heading path BusinessTransactions / Account management / Get/Return Account.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P261** Get/Return Account

**P262** At any time during operating hours of a system, a (direct) member can query the transaction administrator (which can be a financial institution, a matching engine or a settlement engine) to get information about the balances of the account(s) that the transaction administrator maintains for the member.

**P263** The member initiates the exchange by sending a GetAccount message to the transaction administrator.

**P264** The transaction administrator replies with a ReturnAccount message that will contain either the response to the criteria expressed in the GetAccount message, or an error indication.

[fig-0020 - original figure evidence](../diagrams/fig-0020.md)

