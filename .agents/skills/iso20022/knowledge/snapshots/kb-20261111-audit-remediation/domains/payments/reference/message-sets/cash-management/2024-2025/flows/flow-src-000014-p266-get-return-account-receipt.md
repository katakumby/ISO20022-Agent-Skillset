---
template: false
document_kind: "business-flow"
review_status: "needs-review"
manual_curated: true
flow_id: "flow-src-000014-p266-get-return-account-receipt"
title: "Get/Return Account Receipt"
domain: "payments"
source_ids: ["src-000014", "src-000015"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
participant_ids: ["participant-src-000014-system-direct-member", "participant-src-000014-system-transaction-administrator", "participant-src-000014-account-owner", "participant-src-000014-account-servicing-institution"]
message_ids: ["camt.003.001.08", "camt.004.001.10", "camt.025.001.09"]
message_families: ["camt.003", "camt.004", "camt.025"]
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "Account management", "Get/Return Account", "Get/Return Account Receipt"], "paragraphs": ["P266", "P271"], "rendered_file_page": 27}]
issue_ids: []
limitations: ["The picture shows only the System Direct Member and Transaction Administrator. Account owner/servicing institution are narrative relationship roles (P75–78), not extra lifelines.", "Solid source exchange lines and ordering are retained. No timeout, condition, response code or mandatory Receipt is inferred solely from the picture.", "The source prose permits a final Receipt from member to administrator to close the cycle. It is absent from the picture and retained as a narrative-only optional step in the flow. Only Figures7/11 draw an Execution Delay activation bar; it is not added to other figures."]
---

# Get/Return Account Receipt

[src-000014](../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md); P266–271; Word figure page27. Exact versions are independently named by Part2 src-000015; the Part1 diagrams use names/families.

## Purpose, trigger, preconditions, alternatives and outcomes

**P267** At any time during operating hours of a system, a (direct) member can query the transaction administrator (which can be a financial institution, a matching engine or a settlement engine) to get information about the balances of the account(s) that the transaction administrator maintains for the member. The member initiates the exchange by sending a GetAccount message to the transaction administrator.

**P268** If the transaction administrator cannot process the query received immediately, it will reply to the member with a Receipt message where it can indicate the status of the request.

**P269** Later on, the transaction administrator will reply with a ReturnAccount message that will contain either the response to the criteria expressed in the GetAccount message, or an error indication.

**P270** To close the cycle, the member can submit a Receipt message to the transaction administrator.


## Ordered picture exchanges

| Step | Sender | Receiver | Message | Exact supplied definition |
| --- | --- | --- | --- | --- |
| 1 | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | GetAccount | [camt.003.001.08](../../../../messages/camt.003.001.08/index.md) |
| 2 | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | Receipt | [camt.025.001.09](../../../../messages/camt.025.001.09/index.md) |
| 3 | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | ReturnAccount | [camt.004.001.10](../../../../messages/camt.004.001.10/index.md) |


The picture shows only the System Direct Member and Transaction Administrator. Account owner/servicing institution are narrative relationship roles (P75–78), not extra lifelines.

The optional final Receipt is a narrative-only step: System Direct Member sends it to Transaction Administrator after the Return response. The earlier administrator Receipt applies when immediate processing is unavailable. Return can contain results or an error indication.

## Related roles and references

[Account owner](../../../../../../../shared/reference/participants/participant-src-000014-account-owner.md) · [Account servicing institution](../../../../../../../shared/reference/participants/participant-src-000014-account-servicing-institution.md) · [Query, push, error and implementation rules](../usage/get-return-query-rules.md) · [Source reconstruction](../diagrams/operational-cash/fig-0021.md)

Cancellation, deletion and modification are the source-named operations. A settlement reversal is not inferred from these labels. Source-defined conditions are retained above; no unstated postcondition is added.
