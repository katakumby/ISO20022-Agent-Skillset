---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Reservation management BusinessTransactions", "Create Reservation Scenario"]
content_origin: "source-transcription"
---

# Create Reservation Scenario

Source: [src-000014](../../../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md). Locator: heading path BusinessTransactions / Reservation management BusinessTransactions / Create Reservation Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P247** Create Reservation Scenario

**P248** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with information related to the reservation facility it manages for them.

**P249** At any time during the operating hours of the system, a member can request the creation of a reservation facility and which is managed by the transaction administrator. For this, the member can send a CreateReservation message to the transaction administrator. In this message, the member will identify the reservation facility it wants to create. The transaction administrator will reply with a Receipt message that may contain the status of the request.

[fig-0017 - original figure evidence](../diagrams/fig-0017.md)

