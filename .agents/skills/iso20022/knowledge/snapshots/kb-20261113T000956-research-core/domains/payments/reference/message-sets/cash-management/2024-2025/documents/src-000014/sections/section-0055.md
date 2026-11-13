---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Account management", "Get/Return Account", "Get/Return Account Receipt"]
content_origin: "source-transcription"
---

# Get/Return Account Receipt

Source: [src-000014](../../../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md). Locator: heading path BusinessTransactions / Account management / Get/Return Account / Get/Return Account Receipt.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P266** Get/Return Account Receipt

**P267** At any time during operating hours of a system, a (direct) member can query the transaction administrator (which can be a financial institution, a matching engine or a settlement engine) to get information about the balances of the account(s) that the transaction administrator maintains for the member. The member initiates the exchange by sending a GetAccount message to the transaction administrator.

**P268** If the transaction administrator cannot process the query received immediately, it will reply to the member with a Receipt message where it can indicate the status of the request.

**P269** Later on, the transaction administrator will reply with a ReturnAccount message that will contain either the response to the criteria expressed in the GetAccount message, or an error indication.

**P270** To close the cycle, the member can submit a Receipt message to the transaction administrator.

[fig-0021 - original figure evidence](../diagrams/fig-0021.md)

