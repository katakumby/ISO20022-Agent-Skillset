---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "participant"
curated: true
participant_id: "investment-funds-model-legal-guardian-role"
title: "LegalGuardianRole — Investment Funds business model"
source_labels: ["LegalGuardianRole"]
aliases: []
role_type: "contextual business role"
applicable_domains: ["securities"]
source_ids: ["src-000097"]
source_editions: ["2025-2026"]
source_locations: ["FullBusinessModel!A2545:F2545", "Parties; xl/drawings/drawing6.xml; anchor 1"]
message_sets: ["investment-funds"]
message_ids: []
flows: []
limitations: ["This business-model role definition does not by itself establish an initiating, sending, receiving or executing role for any exact message or ordered flow."]
---

# LegalGuardianRole — Investment Funds business model

## Definition and applicable context

Entity that has been appointed by a legal authority to act on behalf of a person judged to be incapacitated.

Evidence: [FullBusinessModel!A2545:F2545](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/sheets/02-fullbusinessmodel/tbl-0014.md). This record is scoped to the supplied Investment Funds Part 3 model and its Parties diagram. It describes a business role; the institution or person playing it may perform different functional roles in different relationships. The model does not equate a role with a permanent institutional identity.

## Responsibilities and actions

Entity that has been appointed by a legal authority to act on behalf of a person judged to be incapacitated.

[FullBusinessModel!A2545:F2545](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/sheets/02-fullbusinessmodel/tbl-0014.md) supplies these duties and qualifications. Parent-role definitions and source-defined local attributes below provide additional context. No message direction is inferred from class inheritance or an association.

## Relationships with other participants

Specializes [InvestmentAccountPartyRole](investment-funds-model-investment-account-party-role.md); parent is explicitly recorded in column C of [FullBusinessModel!A2545:F2545](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/sheets/02-fullbusinessmodel/tbl-0014.md).

## Local attributes, relationships and identifier evidence

No local attribute row is supplied for this component; inherited context remains available through the parent-role links. This does not establish absence of identifiers in every business usage.

No external participant identifier scheme is specified by these local rows. References to an Account, InvestmentAccount or RolePlayer identify a related conceptual component; they are not themselves a supplied BIC, LEI or account-number scheme. Source code-type names such as PartyRoleCode or FATCAFormTypeCode remain separately defined types, not an invented identifier list.

## Flows, messages and model evidence

Applicable domain: Securities. Applicable message set: Investment Funds. [Process references](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/index.md) and [message-set participants](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/participants.md) provide additional independently sourced context. No exact message or ordered flow is assigned solely from this conceptual view. The [Parties diagram](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/diagrams/fig-0006.md) is a reusable role hierarchy, and the [Account model](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/diagrams/fig-0005.md) supplies related account context without changing this role’s scope.

## Provenance, review and limitations

[src-000097](../../../evidence/omitted/3ea6002607634c1b65cb5c88.md); [FullBusinessModel!A2545:F2545](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/sheets/02-fullbusinessmodel/tbl-0014.md). Source definitions and the complete role hierarchy were visually checked on 2026-11-09. Source diagram reconstructions parsed/rendered with Mermaid 12.3.0 and were visually compared. This record remains needs-review for process-specific actor/message applicability, which the model does not supply.

- This business-model role definition does not by itself establish an initiating, sending, receiving or executing role for any exact message or ordered flow.
