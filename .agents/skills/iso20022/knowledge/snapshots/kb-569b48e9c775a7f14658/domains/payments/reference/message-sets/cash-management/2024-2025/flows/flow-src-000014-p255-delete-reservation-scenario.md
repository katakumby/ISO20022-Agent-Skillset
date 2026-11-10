---
template: false
document_kind: "business-flow"
review_status: "needs-review"
manual_curated: true
flow_id: "flow-src-000014-p255-delete-reservation-scenario"
title: "Delete Reservation Scenario"
domain: "payments"
source_ids: ["src-000014", "src-000015"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
participant_ids: ["participant-src-000014-system-direct-member", "participant-src-000014-system-transaction-administrator", "participant-src-000014-account-owner", "participant-src-000014-account-servicing-institution"]
message_ids: ["camt.025.001.09", "camt.049.001.07"]
message_families: ["camt.025", "camt.049"]
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "Reservation management BusinessTransactions", "Delete Reservation Scenario"], "paragraphs": ["P255", "P259"], "rendered_file_page": 26}]
issue_ids: []
limitations: ["The picture shows only the System Direct Member and Transaction Administrator. Account owner/servicing institution are narrative relationship roles (P75–78), not extra lifelines.", "Solid source exchange lines and ordering are retained. No timeout, condition, response code or mandatory Receipt is inferred solely from the picture."]
---

# Delete Reservation Scenario

[src-000014](../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md); P255–259; Word figure page26. Exact versions are independently named by Part2 src-000015; the Part1 diagrams use names/families.

## Purpose, trigger, preconditions, alternatives and outcomes

**P229** Reservation management BusinessTransactions

**P230** The purpose of establishing reservations facilities is to ensure part of the liquidity on the account will be used exclusively for specific cash flow operations.

**P231** The system may define multiple reservation types as defined through a separate external code set.

**P232** The reservation can be effected directly by the member, who has the possibility to :

**P233** reset the reserved liquidity to zero

**P234** change the reservation amount during the day with immediate effect

**P235** input a default reservation amount for the following day(s); valid until a new reservation amount is requested

**P256** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with information related to the reservation facility it manages for them.

**P257** At any time during the operating hours of the system, a member can request the deletion of a reservation facility it has set and which is managed by the transaction administrator. For this, the member can send a DeleteReservation message to the transaction administrator. In this message, the member will identify the reservation facility it wants to have deleted.

**P258** The transaction administrator will reply with a Receipt message that may contain the status of the request.


## Ordered picture exchanges

| Step | Sender | Receiver | Message | Exact supplied definition |
| --- | --- | --- | --- | --- |
| 1 | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | DeleteReservation | [camt.049.001.07](../../../../messages/camt.049.001.07/index.md) |
| 2 | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | Receipt | [camt.025.001.09](../../../../messages/camt.025.001.09/index.md) |


The picture shows only the System Direct Member and Transaction Administrator. Account owner/servicing institution are narrative relationship roles (P75–78), not extra lifelines.

## Related roles and references

[Account owner](../../../../../../../shared/reference/participants/participant-src-000014-account-owner.md) · [Account servicing institution](../../../../../../../shared/reference/participants/participant-src-000014-account-servicing-institution.md) · [Query, push, error and implementation rules](../usage/get-return-query-rules.md) · [Source reconstruction](../diagrams/operational-cash/fig-0019.md)

Cancellation, deletion and modification are the source-named operations. A settlement reversal is not inferred from these labels. Source-defined conditions are retained above; no unstated postcondition is added.
