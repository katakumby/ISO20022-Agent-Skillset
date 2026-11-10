---
template: false
review_status: "needs-review"
document_kind: "participant"
participant_id: "t2s-administration-system-party-role"
domain: "shared"
aliases: ["SystemPartyRole"]
source_ids: ["src-000345"]
source_locations: ["FullBusinessModel!A1700:F1701", "AdminFunction; xl/drawings/drawing2.xml anchor 1"]
message_sets: ["t2s-administration"]
message_ids: []
flows: []
limitations: ["The conceptual model does not establish the sender/receiver of an individual administrative message."]
curated: true
source_editions: ["march-2024"]
---

# SystemPartyRole — T2S administration model

## Definition and context

Role played by a party in a system.

This canonical record is scoped to the supplied T2S administration business model. It is not merged with identically labelled roles in other contexts merely by name.

## Responsibilities and relationships

Relates a party role to the system for which the role is played. It is a context-dependent business role.

Parent of ClearingMemberRole; related to System. See [clearing-member-role](t2s-administration-clearing-member-role.md).

## Identifiers and applicability

The role is a BusinessComponent in the conceptual model, not itself an identifier datatype or named institution. Identification schemes and related identifiers must be read from their linked model components; no universal role identifier scheme is inferred. This model belongs to T2S Administration. It does not by itself allocate an initiating, receiving or acting role to each exact administrative message, or define an ordered business flow.

## Provenance and review

[ISO20022_MDR_Target2Securities_August_2026_v1.zip](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) → archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx`; src-000345, FullBusinessModel!A1700:F1701; AdminFunction xl/drawings/drawing2.xml anchor 1. The [source reconstruction](../message-sets/t2s-administration/march-2024/workbooks/src-000345/diagrams/fig-0002.md) preserves the conceptual relationships. Definitions were read from the cited worksheet cells; the model was visually compared with the original. Cross-process role equivalence and per-message actor mappings remain needs-review.
