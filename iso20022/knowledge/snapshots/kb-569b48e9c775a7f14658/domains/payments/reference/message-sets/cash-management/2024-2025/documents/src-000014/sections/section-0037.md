---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Transaction", "Get/Return Transaction"]
content_origin: "source-transcription"
---

# Get/Return Transaction

Source: [src-000014](../../../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md). Locator: heading path BusinessTransactions / Transaction / Get/Return Transaction.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P186** Get/Return Transaction

**P187** At any time during operating hours of a system, a (direct) member can query the transaction administrator (which can be a financial institution, a matching engine or a settlement engine) to get information about payment instructions held at the transaction administrator.

**P188** The member initiates the exchange by sending a GetTransaction message to the transaction administrator. The transaction administrator replies with a ReturnTransaction message that will contain either the response to the criteria expressed in the GetTransaction message, or an error indication.

[fig-0006 - original figure evidence](../diagrams/fig-0006.md)

