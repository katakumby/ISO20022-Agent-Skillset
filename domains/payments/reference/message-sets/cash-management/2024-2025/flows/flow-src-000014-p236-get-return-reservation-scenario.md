---
template: false
document_kind: "business-flow"
review_status: "needs-review"
manual_curated: true
flow_id: "flow-src-000014-p236-get-return-reservation-scenario"
title: "Get/Return Reservation Scenario"
domain: "payments"
source_ids: ["src-000014", "src-000015"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
participant_ids: ["participant-src-000014-system-direct-member", "participant-src-000014-system-transaction-administrator", "participant-src-000014-account-owner", "participant-src-000014-account-servicing-institution"]
message_ids: ["camt.046.001.08", "camt.047.001.08"]
message_families: ["camt.046", "camt.047"]
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "Reservation management BusinessTransactions", "Get/Return Reservation Scenario"], "paragraphs": ["P236", "P240"], "rendered_file_page": 24}]
issue_ids: []
limitations: ["The picture shows only the System Direct Member and Transaction Administrator. Account owner/servicing institution are narrative relationship roles (P75–78), not extra lifelines.", "Solid source exchange lines and ordering are retained. No timeout, condition, response code or mandatory Receipt is inferred solely from the picture."]
---

# Get/Return Reservation Scenario

[src-000014](../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx); P236–240; Word figure page24. Exact versions are independently named by Part2 src-000015; the Part1 diagrams use names/families.

## Purpose, trigger, preconditions, alternatives and outcomes

**P229** Reservation management BusinessTransactions

**P230** The purpose of establishing reservations facilities is to ensure part of the liquidity on the account will be used exclusively for specific cash flow operations.

**P231** The system may define multiple reservation types as defined through a separate external code set.

**P232** The reservation can be effected directly by the member, who has the possibility to :

**P233** reset the reserved liquidity to zero

**P234** change the reservation amount during the day with immediate effect

**P235** input a default reservation amount for the following day(s); valid until a new reservation amount is requested

**P237** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with information related to the reservation facilities it manages for them.

**P238** At any time during the operating hours of the system, a member can request information about a particular reservation facility it has set and which is managed by the transaction administrator.

**P239** For this, the member can initiate the exchange by sending a GetReservation message to the transaction administrator. The transaction administrator replies with a ReturnReservation message that will contain either the response to the criteria expressed in the GetReservation message, or an error indication.


## Ordered picture exchanges

| Step | Sender | Receiver | Message | Exact supplied definition |
| --- | --- | --- | --- | --- |
| 1 | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | GetReservation | [camt.046.001.08](../../../../messages/camt.046.001.08/index.md) |
| 2 | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | ReturnReservation | [camt.047.001.08](../../../../messages/camt.047.001.08/index.md) |


The picture shows only the System Direct Member and Transaction Administrator. Account owner/servicing institution are narrative relationship roles (P75–78), not extra lifelines.

## Related roles and references

[Account owner](../../../../../../../shared/reference/participants/participant-src-000014-account-owner.md) · [Account servicing institution](../../../../../../../shared/reference/participants/participant-src-000014-account-servicing-institution.md) · [Query, push, error and implementation rules](../usage/get-return-query-rules.md) · [Source reconstruction](../diagrams/operational-cash/fig-0015.md)

Cancellation, deletion and modification are the source-named operations. A settlement reversal is not inferred from these labels. Source-defined conditions are retained above; no unstated postcondition is added.
