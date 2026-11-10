---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Transaction", "Cancel Transaction Scenario"]
content_origin: "source-transcription"
---

# Cancel Transaction Scenario

Source: [src-000014](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx). Locator: heading path BusinessTransactions / Transaction / Cancel Transaction Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P194** Cancel Transaction Scenario

**P195** At any time during operating hours of a system, a (direct) member can query the transaction administrator (which can be a financial institution, a matching engine or a settlement engine) to get information about payment instructions held at the transaction administrator.

**P196** The member initiates the exchange by sending a GetTransaction message to the transaction administrator. If the transaction administrator cannot process the query received immediately, it will reply to the member with a Receipt message where it can indicate the status of the request. Later on, the transaction administrator will reply with a ReturnTransaction message that will contain either the response to the criteria expressed in the GetTransaction message, or an error indication. To close the cycle, the member can submit a Receipt message to the transaction administrator.

[fig-0008 - original figure evidence](../diagrams/fig-0008.md)

