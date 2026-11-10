---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Reservation management BusinessTransactions", "Get/Return Reservation Scenario"]
content_origin: "source-transcription"
---

# Get/Return Reservation Scenario

Source: [src-000014](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx). Locator: heading path BusinessTransactions / Reservation management BusinessTransactions / Get/Return Reservation Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P236** Get/Return Reservation Scenario

**P237** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with information related to the reservation facilities it manages for them.

**P238** At any time during the operating hours of the system, a member can request information about a particular reservation facility it has set and which is managed by the transaction administrator.

**P239** For this, the member can initiate the exchange by sending a GetReservation message to the transaction administrator. The transaction administrator replies with a ReturnReservation message that will contain either the response to the criteria expressed in the GetReservation message, or an error indication.

[fig-0015 - original figure evidence](../diagrams/fig-0015.md)

