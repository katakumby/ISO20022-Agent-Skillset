---
template: false
document_kind: "business-flow"
review_status: "needs-review"
manual_curated: true
flow_id: "flow-src-000014-p221-delete-limit-scenario"
title: "Delete Limit Scenario"
domain: "payments"
source_ids: ["src-000014", "src-000015"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
participant_ids: ["participant-src-000014-system-direct-member", "participant-src-000014-system-transaction-administrator", "participant-src-000014-account-owner", "participant-src-000014-account-servicing-institution"]
message_ids: ["camt.012.001.08", "camt.025.001.09"]
message_families: ["camt.012", "camt.025"]
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "Limit management ", "Delete Limit Scenario"], "paragraphs": ["P221", "P224"], "rendered_file_page": 23}]
issue_ids: []
limitations: ["The picture shows only the System Direct Member and Transaction Administrator. Account owner/servicing institution are narrative relationship roles (P75–78), not extra lifelines.", "Solid source exchange lines and ordering are retained. No timeout, condition, response code or mandatory Receipt is inferred solely from the picture."]
---

# Delete Limit Scenario

[src-000014](../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md); P221–224; Word figure page23. Exact versions are independently named by Part2 src-000015; the Part1 diagrams use names/families.

## Purpose, trigger, preconditions, alternatives and outcomes

**P201** Limit management 

**P202** There are two purposes in establishing limits: to help members to make more efficient use of their liquidity and to facilitate risk management.

**P203** When limits are reached, the transaction administrator stops posting transactions to the account and puts them in a queue. The transaction administrator will resume processing the transactions held in the queue when the account balance of the member becomes sufficient to allow for the transactions to be executed while remaining within the limits.

**P204** Limits set by members are expressed as a maximum net position, and are managed by the transaction administrator. At any time during the day, the transaction administrator can ensure that the net position resulting from all incoming and outgoing transactions for a given member will not go over the fixed limit.

**P205** Limits are set by a member of the system either with regard to another specific member (bilateral limit) or with regard to all other participants (multilateral limit). As a result, there can be a maximum of one multilateral limit and as many bilateral limits as members of the system.

**P206** For a bilateral limit, a member always needs to identify the counterparty to which it applies.

**P222** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with information related to the limit it manages for them.

**P223** At any time during the operating hours of the system, a member can request the deletion of one particular limit it has set and which is managed by the transaction administrator. For this, the member can send a Delete Limit message to the transaction administrator. In this message, the member will identify the limit it wants to have deleted. The transaction administrator will reply with a Receipt message that may contain the status of the request.


## Ordered picture exchanges

| Step | Sender | Receiver | Message | Exact supplied definition |
| --- | --- | --- | --- | --- |
| 1 | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | DeleteLimit | [camt.012.001.08](../../../../messages/camt.012.001.08/index.md) |
| 2 | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | Receipt | [camt.025.001.09](../../../../messages/camt.025.001.09/index.md) |


The picture shows only the System Direct Member and Transaction Administrator. Account owner/servicing institution are narrative relationship roles (P75–78), not extra lifelines.

## Related roles and references

[Account owner](../../../../../../../shared/reference/participants/participant-src-000014-account-owner.md) · [Account servicing institution](../../../../../../../shared/reference/participants/participant-src-000014-account-servicing-institution.md) · [Query, push, error and implementation rules](../usage/get-return-query-rules.md) · [Source reconstruction](../diagrams/operational-cash/fig-0013.md)

Cancellation, deletion and modification are the source-named operations. A settlement reversal is not inferred from these labels. Source-defined conditions are retained above; no unstated postcondition is added.
