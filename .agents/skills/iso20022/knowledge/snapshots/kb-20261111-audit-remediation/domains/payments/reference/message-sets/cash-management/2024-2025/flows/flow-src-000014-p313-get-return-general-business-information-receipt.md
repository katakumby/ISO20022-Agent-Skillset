---
template: false
document_kind: "business-flow"
review_status: "needs-review"
manual_curated: true
flow_id: "flow-src-000014-p313-get-return-general-business-information-receipt"
title: "Get/Return General Business Information Receipt"
domain: "payments"
source_ids: ["src-000014", "src-000015"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
participant_ids: ["participant-src-000014-system-direct-member", "participant-src-000014-system-transaction-administrator", "participant-src-000014-account-owner", "participant-src-000014-account-servicing-institution"]
message_ids: ["camt.020.001.04", "camt.021.001.06", "camt.025.001.09"]
message_families: ["camt.020", "camt.021", "camt.025"]
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "System Status ", "General Business Information", "Get/Return General Business Information Receipt"], "paragraphs": ["P313", "P318"], "rendered_file_page": 32}]
issue_ids: []
limitations: ["The picture shows only the System Direct Member and Transaction Administrator. Account owner/servicing institution are narrative relationship roles (P75–78), not extra lifelines.", "Solid source exchange lines and ordering are retained. No timeout, condition, response code or mandatory Receipt is inferred solely from the picture.", "The source prose permits a final Receipt from member to administrator to close the cycle. It is absent from the picture and retained as a narrative-only optional step in the flow. Only Figures7/11 draw an Execution Delay activation bar; it is not added to other figures."]
---

# Get/Return General Business Information Receipt

[src-000014](../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md); P313–318; Word figure page32. Exact versions are independently named by Part2 src-000015; the Part1 diagrams use names/families.

## Purpose, trigger, preconditions, alternatives and outcomes

**P305** General Business Information

**P306** The transaction administrator can send general business information messages to the members, which may request further action from them. General business information can contain either, static data announcing foreseen events affecting the system, or dynamic data, warning or notifying about unexpected events.

**P307** This type of information can be transmitted in either of the two following ways:

**P314** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with business information related to the management of the system, not related to the transactions created in the system.

**P315** At any time during the operating hours of the system, a member can query the transaction administrator to get information about different types of administrative data linked to the system. For this, the member can initiate the exchange by sending a GetGeneralBusinessInformation message to the transaction administrator.

**P316** If the transaction administrator cannot process the query received immediately, it will reply to the member with a Receipt message where it can indicate the status of the request.

**P317** Later on, the transaction administrator will reply with a ReturnGeneralBusinessInformation message that will contain either the response to the criteria expressed in the GetGeneralBusinessInformation message, or an error indication. To close the cycle, the member can submit a Receipt message to the transaction administrator.


## Ordered picture exchanges

| Step | Sender | Receiver | Message | Exact supplied definition |
| --- | --- | --- | --- | --- |
| 1 | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | GetGeneralBusinessInformation | [camt.020.001.04](../../../../messages/camt.020.001.04/index.md) |
| 2 | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | Receipt | [camt.025.001.09](../../../../messages/camt.025.001.09/index.md) |
| 3 | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | ReturnGeneralBusinessInformation | [camt.021.001.06](../../../../messages/camt.021.001.06/index.md) |


The picture shows only the System Direct Member and Transaction Administrator. Account owner/servicing institution are narrative relationship roles (P75–78), not extra lifelines.

The optional final Receipt is a narrative-only step: System Direct Member sends it to Transaction Administrator after the Return response. The earlier administrator Receipt applies when immediate processing is unavailable. Return can contain results or an error indication.

## Related roles and references

[Account owner](../../../../../../../shared/reference/participants/participant-src-000014-account-owner.md) · [Account servicing institution](../../../../../../../shared/reference/participants/participant-src-000014-account-servicing-institution.md) · [Query, push, error and implementation rules](../usage/get-return-query-rules.md) · [Source reconstruction](../diagrams/operational-cash/fig-0027.md)

Cancellation, deletion and modification are the source-named operations. A settlement reversal is not inferred from these labels. Source-defined conditions are retained above; no unstated postcondition is added.
