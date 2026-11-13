---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Limit management ", "Modify Limit Scenario"]
content_origin: "source-transcription"
---

# Modify Limit Scenario

Source: [src-000014](../../../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md). Locator: heading path BusinessTransactions / Limit management  / Modify Limit Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P225** Modify Limit Scenario

**P226** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with information related to the limit it manages for them.

**P227** At any time during the operating hours of the system, a member can request the modification of one particular limit it has set and which is managed by the transaction administrator. For this, the member can send a ModifyLimit message to the transaction administrator. In this message, the member will identify the limit it wants to have modified. The transaction administrator will reply with a Receipt message that may contain the status of the request.

[fig-0014 - original figure evidence](../diagrams/fig-0014.md)

