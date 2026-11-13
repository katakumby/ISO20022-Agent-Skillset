---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Limit management ", "Create Limit Scenario"]
content_origin: "source-transcription"
---

# Create Limit Scenario

Source: [src-000014](../../../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md). Locator: heading path BusinessTransactions / Limit management  / Create Limit Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P217** Create Limit Scenario

**P218** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with information related to the limit it manages for them.

**P219** At any time during the operating hours of the system, a member can request the creation of a new limit  which will be managed by the transaction administrator. For this, the member can send a CreateLimit message to the transaction administrator. In this message, the member will provide all of the limit details that are required to setup the limit in the system. The transaction administrator will reply with a Receipt message that may contain the status of the request.

[fig-0012 - original figure evidence](../diagrams/fig-0012.md)

