---
template: false
document_kind: "business-flow"
review_status: "needs-review"
manual_curated: true
flow_id: "flow-src-000014-p241-get-return-reservation-receipt"
title: "Get/Return Reservation Receipt"
domain: "payments"
source_ids: ["src-000014", "src-000015"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
participant_ids: ["participant-src-000014-system-direct-member", "participant-src-000014-system-transaction-administrator", "participant-src-000014-account-owner", "participant-src-000014-account-servicing-institution"]
message_ids: ["camt.025.001.09", "camt.046.001.08", "camt.047.001.08"]
message_families: ["camt.025", "camt.046", "camt.047"]
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "Reservation management BusinessTransactions", "Get/Return Reservation Scenario", "Get/Return Reservation Receipt"], "paragraphs": ["P241", "P246"], "rendered_file_page": 25}]
issue_ids: []
limitations: ["The picture shows only the System Direct Member and Transaction Administrator. Account owner/servicing institution are narrative relationship roles (P75–78), not extra lifelines.", "Solid source exchange lines and ordering are retained. No timeout, condition, response code or mandatory Receipt is inferred solely from the picture.", "The source prose permits a final Receipt from member to administrator to close the cycle. It is absent from the picture and retained as a narrative-only optional step in the flow. Only Figures7/11 draw an Execution Delay activation bar; it is not added to other figures."]
---

# Get/Return Reservation Receipt

[src-000014](../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx); P241–246; Word figure page25. Exact versions are independently named by Part2 src-000015; the Part1 diagrams use names/families.

## Purpose, trigger, preconditions, alternatives and outcomes

**P229** Reservation management BusinessTransactions

**P230** The purpose of establishing reservations facilities is to ensure part of the liquidity on the account will be used exclusively for specific cash flow operations.

**P231** The system may define multiple reservation types as defined through a separate external code set.

**P232** The reservation can be effected directly by the member, who has the possibility to :

**P233** reset the reserved liquidity to zero

**P234** change the reservation amount during the day with immediate effect

**P235** input a default reservation amount for the following day(s); valid until a new reservation amount is requested

**P242** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with information related to the reservation facilities it manages for them.

**P243** At any time during the operating hours of the system, a member can request information of one or more reservation facility it has set and which is managed by the transaction administrator. For this, the member can initiate the exchange by sending a GetReservation message to the transaction administrator.

**P244** If the transaction administrator cannot process the query received immediately, it will reply to the member with a Receipt message where it can indicate the status of the request. Later on, the transaction administrator will reply with a ReturnReservation message that will contain either the response to the criteria expressed in the GetReservation message, or an error indication.

**P245** To close the cycle, the member can submit a Receipt message to the transaction administrator.


## Ordered picture exchanges

| Step | Sender | Receiver | Message | Exact supplied definition |
| --- | --- | --- | --- | --- |
| 1 | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | GetReservation | [camt.046.001.08](../../../../messages/camt.046.001.08/index.md) |
| 2 | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | Receipt | [camt.025.001.09](../../../../messages/camt.025.001.09/index.md) |
| 3 | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | ReturnReservation | [camt.047.001.08](../../../../messages/camt.047.001.08/index.md) |


The picture shows only the System Direct Member and Transaction Administrator. Account owner/servicing institution are narrative relationship roles (P75–78), not extra lifelines.

The optional final Receipt is a narrative-only step: System Direct Member sends it to Transaction Administrator after the Return response. The earlier administrator Receipt applies when immediate processing is unavailable. Return can contain results or an error indication.

## Related roles and references

[Account owner](../../../../../../../shared/reference/participants/participant-src-000014-account-owner.md) · [Account servicing institution](../../../../../../../shared/reference/participants/participant-src-000014-account-servicing-institution.md) · [Query, push, error and implementation rules](../usage/get-return-query-rules.md) · [Source reconstruction](../diagrams/operational-cash/fig-0016.md)

Cancellation, deletion and modification are the source-named operations. A settlement reversal is not inferred from these labels. Source-defined conditions are retained above; no unstated postcondition is added.
