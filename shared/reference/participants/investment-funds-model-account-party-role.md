---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "participant"
curated: true
participant_id: "investment-funds-model-account-party-role"
title: "AccountPartyRole — Investment Funds business model"
source_labels: ["AccountPartyRole"]
aliases: []
role_type: "contextual business role"
applicable_domains: ["securities"]
source_ids: ["src-000097"]
source_editions: ["2025-2026"]
source_locations: ["FullBusinessModel!A90:F91", "Parties; xl/drawings/drawing6.xml; anchor 1"]
message_sets: ["investment-funds"]
message_ids: []
flows: []
limitations: ["This business-model role definition does not by itself establish an initiating, sending, receiving or executing role for any exact message or ordered flow."]
---

# AccountPartyRole — Investment Funds business model

## Definition and applicable context

Role played by a party in the context of account operations.

Evidence: [FullBusinessModel!A90:F90](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/sheets/02-fullbusinessmodel/tbl-0002.md). This record is scoped to the supplied Investment Funds Part 3 model and its Parties diagram. It describes a business role; the institution or person playing it may perform different functional roles in different relationships. The model does not equate a role with a permanent institutional identity.

## Responsibilities and actions

Role played by a party in the context of account operations.

[FullBusinessModel!A90:F90](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/sheets/02-fullbusinessmodel/tbl-0002.md) supplies these duties and qualifications. Parent-role definitions and source-defined local attributes below provide additional context. No message direction is inferred from class inheritance or an association.

## Relationships with other participants

Specializes [Role](investment-funds-model-role.md); parent is explicitly recorded in column C of [FullBusinessModel!A90:F90](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/sheets/02-fullbusinessmodel/tbl-0002.md).

Source-defined specializations: [InvestmentAccountPartyRole](investment-funds-model-investment-account-party-role.md). These are inheritance relationships in the [reviewed Parties model](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/diagrams/fig-0006.md), not aliases.

## Local attributes, relationships and identifier evidence

| Source attribute | Definition | Type or related component | Opposite role | Precise evidence |
| --- | --- | --- | --- | --- |
| Account | Identifies the account for which a party plays a role. | Account | PartyRole | [FullBusinessModel!A91:F91](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/sheets/02-fullbusinessmodel/tbl-0002.md) |

No external participant identifier scheme is specified by these local rows. References to an Account, InvestmentAccount or RolePlayer identify a related conceptual component; they are not themselves a supplied BIC, LEI or account-number scheme. Source code-type names such as PartyRoleCode or FATCAFormTypeCode remain separately defined types, not an invented identifier list.

## Flows, messages and model evidence

Applicable domain: Securities. Applicable message set: Investment Funds. [Process references](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/index.md) and [message-set participants](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/participants.md) provide additional independently sourced context. No exact message or ordered flow is assigned solely from this conceptual view. The [Parties diagram](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/diagrams/fig-0006.md) is a reusable role hierarchy, and the [Account model](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/diagrams/fig-0005.md) supplies related account context without changing this role’s scope.

## Provenance, review and limitations

[src-000097](../../../raw-input/investment_funds/ISO20022_MDRPart3_Investment-Funds_2025_2026_v2.xlsx); [FullBusinessModel!A90:F90](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/sheets/02-fullbusinessmodel/tbl-0002.md). Source definitions and the complete role hierarchy were visually checked on 2026-11-09. Source diagram reconstructions parsed/rendered with Mermaid 12.3.0 and were visually compared. This record remains needs-review for process-specific actor/message applicability, which the model does not supply.

- This business-model role definition does not by itself establish an initiating, sending, receiving or executing role for any exact message or ordered flow.
