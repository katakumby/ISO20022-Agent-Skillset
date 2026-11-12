---
template: false
document_kind: "business-flow"
review_status: "needs-review"
manual_curated: true
flow_id: "flow-src-000014-p281-get-return-business-day-information-receipt"
title: "Get/Return Business Day Information Receipt"
domain: "payments"
source_ids: ["src-000014", "src-000015"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
participant_ids: ["participant-src-000014-system-direct-member", "participant-src-000014-system-transaction-administrator", "participant-src-000014-account-owner", "participant-src-000014-account-servicing-institution"]
message_ids: ["camt.018.001.05", "camt.019.001.07", "camt.025.001.09"]
message_families: ["camt.018", "camt.019", "camt.025"]
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "System Status ", "Business Day Information", "Get/Return Business Day Information Receipt"], "paragraphs": ["P281", "P287"], "rendered_file_page": 29}]
issue_ids: []
limitations: ["The picture shows only the System Direct Member and Transaction Administrator. Account owner/servicing institution are narrative relationship roles (P75–78), not extra lifelines.", "Solid source exchange lines and ordering are retained. No timeout, condition, response code or mandatory Receipt is inferred solely from the picture.", "The source prose permits a final Receipt from member to administrator to close the cycle. It is absent from the picture and retained as a narrative-only optional step in the flow. Only Figures7/11 draw an Execution Delay activation bar; it is not added to other figures."]
---

# Get/Return Business Day Information Receipt

[src-000014](../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md); P281–287; Word figure page29. Exact versions are independently named by Part2 src-000015; the Part1 diagrams use names/families.

## Purpose, trigger, preconditions, alternatives and outcomes

**P273** Business Day Information

**P274** The transaction administrator is in charge of providing the members with business information. The term business day information covers all information related to the management of the system that is, not related to the transactions or requests created in the system. The type of business information available can vary depending on the system.

**P275** The member can request information about the static data of the system through a series of criteria, corresponding to the known information stored within the transaction administrator. Based on the criteria received within the request, the transaction administrator will select items that match the request and report them to the requester.

**P276** The transaction administrator may also send a ReturnBusinessDayInformation message with pre-defined information at times previously agreed with the member or to warn the member about a particular problem that may have arisen and which needs attention.

**P282** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with general business information related to foreseen or unexpected events affecting the system.

**P283** At any time during the operating hours of the system, a member can query the transaction administrator to get information about a broadcast-type message previously sent by the transaction administrator. For this, the member can initiate the exchange by sending a GetBusinessDayInformation message to the transaction administrator.

**P284** If the transaction administrator cannot process the query received immediately, it will reply to the member with a Receipt message where it can indicate the status of the request.

**P285** Later on, the transaction administrator will reply with a ReturnBusinessDayInformation message that will contain either the response to the criteria expressed in the GetBusinessDayInformation message, or an error indication.

**P286** To close the cycle, the member can submit a Receipt message to the transaction administrator.


## Ordered picture exchanges

| Step | Sender | Receiver | Message | Exact supplied definition |
| --- | --- | --- | --- | --- |
| 1 | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | GetBusinessDayInformation | [camt.018.001.05](../../../../messages/camt.018.001.05/index.md) |
| 2 | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | Receipt | [camt.025.001.09](../../../../messages/camt.025.001.09/index.md) |
| 3 | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | ReturnBusinessDayInformation | [camt.019.001.07](../../../../messages/camt.019.001.07/index.md) |


The picture shows only the System Direct Member and Transaction Administrator. Account owner/servicing institution are narrative relationship roles (P75–78), not extra lifelines.

The optional final Receipt is a narrative-only step: System Direct Member sends it to Transaction Administrator after the Return response. The earlier administrator Receipt applies when immediate processing is unavailable. Return can contain results or an error indication.

## Related roles and references

[Account owner](../../../../../../../shared/reference/participants/participant-src-000014-account-owner.md) · [Account servicing institution](../../../../../../../shared/reference/participants/participant-src-000014-account-servicing-institution.md) · [Query, push, error and implementation rules](../usage/get-return-query-rules.md) · [Source reconstruction](../diagrams/operational-cash/fig-0023.md)

Cancellation, deletion and modification are the source-named operations. A settlement reversal is not inferred from these labels. Source-defined conditions are retained above; no unstated postcondition is added.
