---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Limit management ", "Get/Return Limit ", "Get/Return Limit Receipt"]
content_origin: "source-transcription"
---

# Get/Return Limit Receipt

Source: [src-000014](../../../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md). Locator: heading path BusinessTransactions / Limit management  / Get/Return Limit  / Get/Return Limit Receipt.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P212** Get/Return Limit Receipt

**P213** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with information related to the limit it manages for them.

**P214** At any time during the operating hours of the system, a member can request information of one or more limits it has set and which is managed by the transaction administrator. For this, the member can initiate the exchange by sending a GetLimit message to the transaction administrator.

**P215** If the transaction administrator cannot process the query received immediately, it will reply to the member with a Receipt message where it can indicate the status of the request. Later on, the transaction administrator will reply with a ReturnLimit message that will contain either the response to the criteria expressed in the GetLimit message, or an error indication. To close the cycle, the member can submit a Receipt message to the transaction administrator.

[fig-0011 - original figure evidence](../diagrams/fig-0011.md)

