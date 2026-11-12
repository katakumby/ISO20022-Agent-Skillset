---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
participant_id: "participant-src-000359-stock-exchange"
title: "Stock Exchange"
source_labels: ["Stock Exchange"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000359", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[7]", "paragraph_id": null, "table_id": "T6"}]
flows: []
process_sections: []
message_ids: []
message_families: []
search_terms: ["Stock Exchange"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# Stock Exchange

Business context: T2S IntraBalanceMovement. Source classification: business role.

## Definition

A market in which securities, commodities, options or futures are traded. 

Evidence: [T6](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/documents/src-000359/tables/tbl-0006.md), source row 7.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [System Member](participant-src-000359-system-member.md) | [T7](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/documents/src-000359/tables/tbl-0007.md) row 6, column 2 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Stock Exchange`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000359](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`.
