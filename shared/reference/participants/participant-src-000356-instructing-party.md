---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000356"]
source_editions: ["march-2024"]
message_sets: ["t2s-collateral-reporting"]
participant_id: "participant-src-000356-instructing-party"
title: "Instructing Party"
source_labels: ["Instructing Party"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000356", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[2]", "paragraph_id": null, "table_id": "T6"}]
flows: ["flow-src-000356-p138-query-management-process"]
process_sections: []
message_ids: ["colr.001.001.02", "colr.002.001.02"]
message_families: ["colr.001"]
search_terms: ["Instructing Party", "colr.001"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---





# Instructing Party

Business context: T2S CollateralReporting. Source classification: business role.

## Definition

Party that instructs the executing/servicing party to process and monitor a transaction.

Evidence: [T6](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/documents/src-000356/tables/tbl-0006.md), source row 2.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [System Member](participant-src-000356-system-member.md) | [T7](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/documents/src-000356/tables/tbl-0007.md) row 7, column 2 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Query Management Process](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/flows/flow-src-000356-p138-query-management-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `colr.001`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Instructing Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000356](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralReporting_2023_2024_v2.docx`.

Collateral-reporting source context: [Collateral-query member and administrator activity](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/diagrams/curated/fig-0008.md). [flow Query Management Process](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/flows/flow-src-000356-p138-query-management-process.md).

Classification nuance: T5 defines System Member as a participant, while T6 repeats that definition in Business Roles and labels Instructing/Executing parties there. T7 supplies the explicit mappings. These source classifications are preserved as context, not collapsed into an institution identity.
