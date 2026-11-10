---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000356"]
source_editions: ["march-2024"]
message_sets: ["t2s-collateral-reporting"]
participant_id: "participant-src-000356-settlement-infrastructure-direct-participant"
title: "Settlement Infrastructure Direct Participant"
source_labels: ["Settlement Infrastructure Direct Participant"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000356", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[6]", "paragraph_id": null, "table_id": "T6"}]
flows: ["flow-src-000356-p138-query-management-process"]
process_sections: []
message_ids: ["colr.001.001.02", "colr.002.001.02"]
message_families: []
search_terms: ["Settlement Infrastructure Direct Participant"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---





# Settlement Infrastructure Direct Participant

Business context: T2S CollateralReporting. Source classification: business role.

## Definition

The party which is not a CSD and that is directly connected to the Settlement Infrastructure Platform. It could be a local custodian, a global custodian, a stock exchange, a central counterparty…

Evidence: [T6](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/documents/src-000356/tables/tbl-0006.md), source row 6.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [System Member](participant-src-000356-system-member.md) | [T7](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/documents/src-000356/tables/tbl-0007.md) row 6, column 2 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Settlement Infrastructure Direct Participant`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000356](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralReporting_2023_2024_v2.docx`.

Collateral-reporting source context: [Collateral-query member and administrator activity](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/diagrams/curated/fig-0008.md). [flow Query Management Process](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/flows/flow-src-000356-p138-query-management-process.md).

Collateral-reporting source context: [Collateral-value communication overview](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/diagrams/curated/fig-0009.md). [flow Query Management Process](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/flows/flow-src-000356-p138-query-management-process.md).
