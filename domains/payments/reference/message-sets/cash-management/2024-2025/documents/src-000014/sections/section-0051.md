---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Reservation management BusinessTransactions", "Modify Reservation Scenario"]
content_origin: "source-transcription"
---

# Modify Reservation Scenario

Source: [src-000014](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx). Locator: heading path BusinessTransactions / Reservation management BusinessTransactions / Modify Reservation Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P251** Modify Reservation Scenario

**P252** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with information related to the reservation facility it manages for them.

**P253** At any time during the operating hours of the system, a member can request the modification of the reservation facility it has set and which is managed by the transaction administrator. For this, the member can send a ModifyReservation message to the transaction administrator. In this message, the member will identify the reservation facility it wants to have modified. The transaction administrator will reply with a Receipt message that may contain the status of the request.

[fig-0018 - original figure evidence](../diagrams/fig-0018.md)

