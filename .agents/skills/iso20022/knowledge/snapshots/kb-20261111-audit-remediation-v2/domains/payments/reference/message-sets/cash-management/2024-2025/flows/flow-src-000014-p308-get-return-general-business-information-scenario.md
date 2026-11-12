---
template: false
document_kind: "business-flow"
review_status: "needs-review"
manual_curated: true
flow_id: "flow-src-000014-p308-get-return-general-business-information-scenario"
title: "Get/Return General Business Information Scenario"
domain: "payments"
source_ids: ["src-000014", "src-000015"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
participant_ids: ["participant-src-000014-system-direct-member", "participant-src-000014-system-transaction-administrator", "participant-src-000014-account-owner", "participant-src-000014-account-servicing-institution"]
message_ids: ["camt.020.001.04", "camt.021.001.06"]
message_families: ["camt.020", "camt.021"]
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "System Status ", "General Business Information", "Get/Return General Business Information Scenario"], "paragraphs": ["P308", "P312"], "rendered_file_page": 31}]
issue_ids: []
limitations: ["The picture shows only the System Direct Member and Transaction Administrator. Account owner/servicing institution are narrative relationship roles (P75–78), not extra lifelines.", "Solid source exchange lines and ordering are retained. No timeout, condition, response code or mandatory Receipt is inferred solely from the picture."]
---

# Get/Return General Business Information Scenario

[src-000014](../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md); P308–312; Word figure page31. Exact versions are independently named by Part2 src-000015; the Part1 diagrams use names/families.

## Purpose, trigger, preconditions, alternatives and outcomes

**P305** General Business Information

**P306** The transaction administrator can send general business information messages to the members, which may request further action from them. General business information can contain either, static data announcing foreseen events affecting the system, or dynamic data, warning or notifying about unexpected events.

**P307** This type of information can be transmitted in either of the two following ways:

**P309** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with business information related to the management of the system, not related to the transactions created in the system.

**P310** At any time during the operating hours of the system, a member can query the transaction administrator to get information about different types of administrative data linked to the system.

**P311** For this, the member can initiate the exchange by sending a GetGeneralBusinessInformation message to the transaction administrator. The transaction administrator replies with a ReturnGeneralBusinessInformation message that will contain either the response to the criteria expressed in the GetGeneralBusinessInformation message, or an error indication.


## Ordered picture exchanges

| Step | Sender | Receiver | Message | Exact supplied definition |
| --- | --- | --- | --- | --- |
| 1 | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | GetGeneralBusinessInformation | [camt.020.001.04](../../../../messages/camt.020.001.04/index.md) |
| 2 | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | ReturnGeneralBusinessInformation | [camt.021.001.06](../../../../messages/camt.021.001.06/index.md) |


The picture shows only the System Direct Member and Transaction Administrator. Account owner/servicing institution are narrative relationship roles (P75–78), not extra lifelines.

## Related roles and references

[Account owner](../../../../../../../shared/reference/participants/participant-src-000014-account-owner.md) · [Account servicing institution](../../../../../../../shared/reference/participants/participant-src-000014-account-servicing-institution.md) · [Query, push, error and implementation rules](../usage/get-return-query-rules.md) · [Source reconstruction](../diagrams/operational-cash/fig-0026.md)

Cancellation, deletion and modification are the source-named operations. A settlement reversal is not inferred from these labels. Source-defined conditions are retained above; no unstated postcondition is added.
