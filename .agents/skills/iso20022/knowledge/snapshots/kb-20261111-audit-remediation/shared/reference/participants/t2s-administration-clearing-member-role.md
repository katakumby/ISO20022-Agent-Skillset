---
template: false
review_status: "needs-review"
document_kind: "participant"
participant_id: "t2s-administration-clearing-member-role"
domain: "shared"
aliases: ["ClearingMemberRole"]
source_ids: ["src-000345"]
source_locations: ["FullBusinessModel!A1708:F1714", "AdminFunction; xl/drawings/drawing2.xml anchor 1"]
message_sets: ["t2s-administration"]
message_ids: []
flows: []
limitations: ["The conceptual model does not establish the sender/receiver of an individual administrative message."]
curated: true
source_editions: ["march-2024"]
---

# ClearingMemberRole — T2S administration model

## Definition and context

Member of an exchange's clearing corporation, responsible for executing client trades and involved in the clearing of trades.

This canonical record is scoped to the supplied T2S administration business model. It is not merged with identically labelled roles in other contexts merely by name.

## Responsibilities and relationships

Executes client trades and participates in clearing. The default-fund-account relationship points to an account at an ICSD or central bank. Clearing-system-member identification is assigned by the system or administrator.

Specializes SystemPartyRole; links Account through DefaultFundAccount/DefaultFundAccountOwner and CashClearingSystemMember through clearing-member identification. See [system-party-role](t2s-administration-system-party-role.md).

## Identifiers and applicability

The role is a BusinessComponent in the conceptual model, not itself an identifier datatype or named institution. Identification schemes and related identifiers must be read from their linked model components; no universal role identifier scheme is inferred. This model belongs to T2S Administration. It does not by itself allocate an initiating, receiving or acting role to each exact administrative message, or define an ordered business flow.

## Provenance and review

[ISO20022_MDR_Target2Securities_August_2026_v1.zip](../../../evidence/omitted/e6546c5f64c53f963440988a.md) → archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx`; src-000345, FullBusinessModel!A1708:F1714; AdminFunction xl/drawings/drawing2.xml anchor 1. The [source reconstruction](../message-sets/t2s-administration/march-2024/workbooks/src-000345/diagrams/fig-0002.md) preserves the conceptual relationships. Definitions were read from the cited worksheet cells; the model was visually compared with the original. Cross-process role equivalence and per-message actor mappings remain needs-review.
