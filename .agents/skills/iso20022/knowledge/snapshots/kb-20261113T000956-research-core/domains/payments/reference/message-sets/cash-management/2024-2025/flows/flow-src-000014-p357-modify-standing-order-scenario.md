---
template: false
document_kind: "business-flow"
review_status: "needs-review"
manual_curated: true
flow_id: "flow-src-000014-p357-modify-standing-order-scenario"
title: "Modify Standing Order Scenario"
domain: "payments"
source_ids: ["src-000014", "src-000015"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
participant_ids: ["participant-src-000014-system-direct-member", "participant-src-000014-system-transaction-administrator", "participant-src-000014-account-owner", "participant-src-000014-account-servicing-institution"]
message_ids: ["camt.024.001.08", "camt.025.001.09"]
message_families: ["camt.024", "camt.025"]
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "Standing Orders BusinessTransactions", "Modify Standing Order Scenario"], "paragraphs": ["P357", "P361"], "rendered_file_page": 36}]
issue_ids: []
limitations: ["The picture shows only the System Direct Member and Transaction Administrator. Account owner/servicing institution are narrative relationship roles (P75–78), not extra lifelines.", "Solid source exchange lines and ordering are retained. No timeout, condition, response code or mandatory Receipt is inferred solely from the picture."]
---

# Modify Standing Order Scenario

[src-000014](../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md); P357–361; Word figure page36. Exact versions are independently named by Part2 src-000015; the Part1 diagrams use names/families.

## Purpose, trigger, preconditions, alternatives and outcomes

**P337** Standing Orders BusinessTransactions

**P338** Standing orders trigger a transfer of funds between two accounts belonging to the member in the books of the transaction administrator.

**P339** Standing orders are permanent transfer orders input by the member into the system. They allow the member to move funds from outside the system into its accounts with the transaction administrator that are used for specific purposes (for example, the settlement account for RTGS operations), objective of these transfers being for example to provide sufficient liquidity for the start of operations at the beginning of the business day.

**P340** The standing order may be pre-set by the system and the necessary amount necessary left to the discretion of the members, or the transaction administrator may effect a calculation and a call for funds for efficient use of the liquidity.

**P358** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with the ability to manage their liquidity.

**P359** At any time during the operating hours of the system, a member can request the transaction administrator to modify a standing order for the transfer of funds between two accounts that the transaction administrator maintains for the member.

**P360** For this, the member can send a ModifyStandingOrder message to the transaction administrator. The transaction administrator will reply with a Receipt message that may contain the status of the request.


## Ordered picture exchanges

| Step | Sender | Receiver | Message | Exact supplied definition |
| --- | --- | --- | --- | --- |
| 1 | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | ModifyStandingOrder | [camt.024.001.08](../../../../messages/camt.024.001.08/index.md) |
| 2 | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | Receipt | [camt.025.001.09](../../../../messages/camt.025.001.09/index.md) |


The picture shows only the System Direct Member and Transaction Administrator. Account owner/servicing institution are narrative relationship roles (P75–78), not extra lifelines.

## Related roles and references

[Account owner](../../../../../../../shared/reference/participants/participant-src-000014-account-owner.md) · [Account servicing institution](../../../../../../../shared/reference/participants/participant-src-000014-account-servicing-institution.md) · [Query, push, error and implementation rules](../usage/get-return-query-rules.md) · [Source reconstruction](../diagrams/operational-cash/fig-0035.md)

Cancellation, deletion and modification are the source-named operations. A settlement reversal is not inferred from these labels. Source-defined conditions are retained above; no unstated postcondition is added.
