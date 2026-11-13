---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Standing Orders BusinessTransactions", "Get/Return Standing Order Scenario", "Get/Return Standing Order Receipt"]
content_origin: "source-transcription"
---

# Get/Return Standing Order Receipt

Source: [src-000014](../../../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md). Locator: heading path BusinessTransactions / Standing Orders BusinessTransactions / Get/Return Standing Order Scenario / Get/Return Standing Order Receipt.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P346** Get/Return Standing Order Receipt

**P347** At any time during operating hours of a system, a (direct) member can query the transaction administrator (which can be a financial institution, a matching engine or a settlement engine) to get information about the standing orders that are defined for the account(s) that the transaction administrator maintains for the member. The member initiates the exchange by sending a GetStandingOrder message to the transaction administrator.

**P348** If the transaction administrator cannot process the query received immediately, it will reply to the member with a Receipt message where it can indicate the status of the request.

**P349** Later on, the transaction administrator will reply with a ReturnStandingOrder message that will contain either the response to the criteria expressed in the GetStandingOrder message, or an error indication.

**P350** To close the cycle, the member can submit a Receipt message to the transaction administrator.

[fig-0033 - original figure evidence](../diagrams/fig-0033.md)

