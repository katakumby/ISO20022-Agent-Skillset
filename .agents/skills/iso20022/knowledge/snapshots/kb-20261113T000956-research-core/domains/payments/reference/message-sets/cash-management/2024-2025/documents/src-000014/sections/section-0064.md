---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "System Status ", "General Business Information", "Get/Return General Business Information Scenario"]
content_origin: "source-transcription"
---

# Get/Return General Business Information Scenario

Source: [src-000014](../../../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md). Locator: heading path BusinessTransactions / System Status  / General Business Information / Get/Return General Business Information Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P308** Get/Return General Business Information Scenario

**P309** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with business information related to the management of the system, not related to the transactions created in the system.

**P310** At any time during the operating hours of the system, a member can query the transaction administrator to get information about different types of administrative data linked to the system.

**P311** For this, the member can initiate the exchange by sending a GetGeneralBusinessInformation message to the transaction administrator. The transaction administrator replies with a ReturnGeneralBusinessInformation message that will contain either the response to the criteria expressed in the GetGeneralBusinessInformation message, or an error indication.

[fig-0026 - original figure evidence](../diagrams/fig-0026.md)

