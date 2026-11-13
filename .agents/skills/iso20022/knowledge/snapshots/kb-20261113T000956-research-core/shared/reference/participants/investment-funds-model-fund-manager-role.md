---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "participant"
curated: true
participant_id: "investment-funds-model-fund-manager-role"
title: "FundManagerRole — Investment Funds business model"
source_labels: ["FundManagerRole"]
aliases: ["fund promoter", "fund sponsor"]
role_type: "contextual business role"
applicable_domains: ["securities"]
source_ids: ["src-000097"]
source_editions: ["2025-2026"]
source_locations: ["FullBusinessModel!A1947:F1947", "Parties; xl/drawings/drawing6.xml; anchor 1"]
message_sets: ["investment-funds"]
message_ids: []
flows: []
limitations: ["This business-model role definition does not by itself establish an initiating, sending, receiving or executing role for any exact message or ordered flow."]
---

# FundManagerRole — Investment Funds business model

## Definition and applicable context

Legal entity that sets up a fund, appoints agents, decides and implements an investment strategy. That is, selects portfolio investments in accordance with the objectives and strategy in the fund's prospectus, and places orders to effect or liquidate selected investments in accordance with net flow of capital into or out of the fund. Also called fund promoter or fund sponsor.

Evidence: [FullBusinessModel!A1947:F1947](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/sheets/02-fullbusinessmodel/tbl-0011.md). This record is scoped to the supplied Investment Funds Part 3 model and its Parties diagram. It describes a business role; the institution or person playing it may perform different functional roles in different relationships. The model does not equate a role with a permanent institutional identity.

## Responsibilities and actions

Legal entity that sets up a fund, appoints agents, decides and implements an investment strategy. That is, selects portfolio investments in accordance with the objectives and strategy in the fund's prospectus, and places orders to effect or liquidate selected investments in accordance with net flow of capital into or out of the fund. Also called fund promoter or fund sponsor.

[FullBusinessModel!A1947:F1947](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/sheets/02-fullbusinessmodel/tbl-0011.md) supplies these duties and qualifications. Parent-role definitions and source-defined local attributes below provide additional context. No message direction is inferred from class inheritance or an association.

## Relationships with other participants

Specializes [InvestmentFundPartyRole](investment-funds-model-investment-fund-party-role.md); parent is explicitly recorded in column C of [FullBusinessModel!A1947:F1947](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/sheets/02-fullbusinessmodel/tbl-0011.md).

Source-defined specializations: [FundPromoter](investment-funds-model-fund-promoter.md). These are inheritance relationships in the [reviewed Parties model](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/diagrams/fig-0006.md), not aliases.

The source definition uses “fund promoter” and “fund sponsor” as aliases. The same model also contains a distinct [FundPromoter subtype](investment-funds-model-fund-promoter.md); the subtype record is retained and is not collapsed merely because its label also appears as an alias.

The separately scoped [Part 1 narrative business-role record](participant-src-000095-fund-manager.md) supplies process-specific participation and functional-role mappings. Its overlapping definition is a navigational connection; those process claims are not automatically transferred to this model definition.

## Local attributes, relationships and identifier evidence

No local attribute row is supplied for this component; inherited context remains available through the parent-role links. This does not establish absence of identifiers in every business usage.

No external participant identifier scheme is specified by these local rows. References to an Account, InvestmentAccount or RolePlayer identify a related conceptual component; they are not themselves a supplied BIC, LEI or account-number scheme. Source code-type names such as PartyRoleCode or FATCAFormTypeCode remain separately defined types, not an invented identifier list.

## Flows, messages and model evidence

Applicable domain: Securities. Applicable message set: Investment Funds. [Process references](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/index.md) and [message-set participants](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/participants.md) provide additional independently sourced context. No exact message or ordered flow is assigned solely from this conceptual view. The [Parties diagram](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/diagrams/fig-0006.md) is a reusable role hierarchy, and the [Account model](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/diagrams/fig-0005.md) supplies related account context without changing this role’s scope.

## Provenance, review and limitations

[src-000097](../../../evidence/omitted/3ea6002607634c1b65cb5c88.md); [FullBusinessModel!A1947:F1947](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/sheets/02-fullbusinessmodel/tbl-0011.md). Source definitions and the complete role hierarchy were visually checked on 2026-11-09. Source diagram reconstructions parsed/rendered with Mermaid 12.3.0 and were visually compared. This record remains needs-review for process-specific actor/message applicability, which the model does not supply.

- This business-model role definition does not by itself establish an initiating, sending, receiving or executing role for any exact message or ordered flow.
