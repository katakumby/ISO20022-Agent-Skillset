---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
participant_id: "participant-src-000359-national-central-bank"
title: "National Central Bank"
source_labels: ["National Central Bank"]
role_type: "business role (matrix label; definition not extracted)"
aliases: []
source_locations: []
flows: []
process_sections: []
message_ids: []
message_families: []
search_terms: ["National Central Bank"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000359-p151-intra-balance-management"]
---



# National Central Bank

Business context: T2S IntraBalanceMovement. Source classification: business role (matrix label; definition not extracted).

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [System Member](participant-src-000359-system-member.md) | [T7](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/documents/src-000359/tables/tbl-0007.md) row 3, column 2 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `National Central Bank`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000359](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`.

<!-- INTRABALANCE-FIG-2-START -->
[Intra-balance management in its business context](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p151-intra-balance-management.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0002.md)
<!-- INTRABALANCE-FIG-2-END -->
