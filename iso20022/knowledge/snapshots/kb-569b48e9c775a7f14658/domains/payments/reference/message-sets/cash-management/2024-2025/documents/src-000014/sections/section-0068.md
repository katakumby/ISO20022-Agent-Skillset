---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "System Status ", "Create Member Scenario"]
content_origin: "source-transcription"
---

# Create Member Scenario

Source: [src-000014](../../../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md). Locator: heading path BusinessTransactions / System Status  / Create Member Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P329** Create Member Scenario

**P330** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with business information related to the management of the system, not related to the transactions created in the system.

**P331** At any time during the operating hours of the system, a member can request the creation of the information that the transaction administrator maintains related to the member. For this, the member can send a ModifyMember message to the transaction administrator. The transaction administrator will reply with a Receipt message that may contain the status of the request.

[fig-0030 - original figure evidence](../diagrams/fig-0030.md)

