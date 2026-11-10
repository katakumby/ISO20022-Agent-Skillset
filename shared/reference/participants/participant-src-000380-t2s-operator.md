---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_sets: ["t2s-settlement-restrictions"]
participant_id: "participant-src-000380-t2s-operator"
title: "T2S Operator"
source_labels: ["T2S Operator"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000380", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[6]", "paragraph_id": null, "table_id": "T6"}]
flows: []
process_sections: []
message_ids: []
message_families: []
search_terms: ["T2S Operator"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# T2S Operator

Business context: T2S SettlementRestrictions. Source classification: business role.

## Definition

The T2S operator is the top level of the hierarchical role and access rights model. The T2S operator role classification includes all T2S system users of the entity, which will be responsible for the day-to-day operation and management of T2S. The T2S actors managed by this entity shall be CSDs and NCBs participating in T2S. At the highest level, the T2S operator shall have access to all data and functionality in the subordinate level.

Evidence: [T6](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000380/tables/tbl-0006.md), source row 6.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Instructing Party](participant-src-000380-instructing-party.md) | [T7](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000380/tables/tbl-0007.md) row 6, column 2 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `T2S Operator`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000380](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`.
