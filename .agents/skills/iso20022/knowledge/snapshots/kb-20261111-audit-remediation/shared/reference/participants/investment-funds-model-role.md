---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "participant"
curated: true
participant_id: "investment-funds-model-role"
title: "Role — Investment Funds business model"
source_labels: ["Role"]
aliases: []
role_type: "contextual business role"
applicable_domains: ["securities"]
source_ids: ["src-000097"]
source_editions: ["2025-2026"]
source_locations: ["FullBusinessModel!A3839:F3844", "Parties; xl/drawings/drawing6.xml; anchor 1"]
message_sets: ["investment-funds"]
message_ids: []
flows: []
limitations: ["This business-model role definition does not by itself establish an initiating, sending, receiving or executing role for any exact message or ordered flow."]
---

# Role — Investment Funds business model

## Definition and applicable context

Role of a party in an activity.

Evidence: [FullBusinessModel!A3839:F3839](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/sheets/02-fullbusinessmodel/tbl-0021.md). This record is scoped to the supplied Investment Funds Part 3 model and its Parties diagram. It describes a business role; the institution or person playing it may perform different functional roles in different relationships. The model does not equate a role with a permanent institutional identity.

## Responsibilities and actions

Role of a party in an activity.

[FullBusinessModel!A3839:F3839](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/sheets/02-fullbusinessmodel/tbl-0021.md) supplies these duties and qualifications. Parent-role definitions and source-defined local attributes below provide additional context. No message direction is inferred from class inheritance or an association.

## Relationships with other participants

The component declaration supplies no parent role.

Source-defined specializations: [AssetPartyRole](investment-funds-model-asset-party-role.md), [GuaranteePartyRole](investment-funds-model-guarantee-party-role.md), [InvestmentFundPartyRole](investment-funds-model-investment-fund-party-role.md), [AccountPartyRole](investment-funds-model-account-party-role.md). These are inheritance relationships in the [reviewed Parties model](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/diagrams/fig-0006.md), not aliases.

## Local attributes, relationships and identifier evidence

| Source attribute | Definition | Type or related component | Opposite role | Precise evidence |
| --- | --- | --- | --- | --- |
| Player | Entity which plays a role in the context of the business domain in which the role is defined. | RolePlayer | Role | [FullBusinessModel!A3840:F3840](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/sheets/02-fullbusinessmodel/tbl-0021.md) |
| ContactPersonRole | Contact person in the context of a role played by an organisation. | ContactPersonRole | Role | [FullBusinessModel!A3841:F3841](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/sheets/02-fullbusinessmodel/tbl-0021.md) |
| PartyRole | Specifies the role of the party in the transaction. | PartyRoleCode | ∅ | [FullBusinessModel!A3842:F3842](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/sheets/02-fullbusinessmodel/tbl-0021.md) |
| CounterpartyRisk | Specifies the risk which is related to the role played by a party. | CounterpartyRisk | Party | [FullBusinessModel!A3843:F3843](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/sheets/02-fullbusinessmodel/tbl-0021.md) |
| Entry | Entry for which a role is specified. | Entry | Role | [FullBusinessModel!A3844:F3844](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/sheets/02-fullbusinessmodel/tbl-0021.md) |

No external participant identifier scheme is specified by these local rows. References to an Account, InvestmentAccount or RolePlayer identify a related conceptual component; they are not themselves a supplied BIC, LEI or account-number scheme. Source code-type names such as PartyRoleCode or FATCAFormTypeCode remain separately defined types, not an invented identifier list.

## Flows, messages and model evidence

Applicable domain: Securities. Applicable message set: Investment Funds. [Process references](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/index.md) and [message-set participants](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/participants.md) provide additional independently sourced context. No exact message or ordered flow is assigned solely from this conceptual view. The [Parties diagram](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/diagrams/fig-0006.md) is a reusable role hierarchy, and the [Account model](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/diagrams/fig-0005.md) supplies related account context without changing this role’s scope.

## Provenance, review and limitations

[src-000097](../../../evidence/omitted/3ea6002607634c1b65cb5c88.md); [FullBusinessModel!A3839:F3839](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/sheets/02-fullbusinessmodel/tbl-0021.md). Source definitions and the complete role hierarchy were visually checked on 2026-11-09. Source diagram reconstructions parsed/rendered with Mermaid 12.3.0 and were visually compared. This record remains needs-review for process-specific actor/message applicability, which the model does not supply.

- This business-model role definition does not by itself establish an initiating, sending, receiving or executing role for any exact message or ordered flow.
