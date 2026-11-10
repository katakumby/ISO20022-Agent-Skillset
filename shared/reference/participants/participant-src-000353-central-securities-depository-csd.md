---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000353"]
source_editions: ["may-2025"]
message_sets: ["t2s-collateral-management-reference-data"]
participant_id: "participant-src-000353-central-securities-depository-csd"
title: "Central Securities Depository (CSD)"
source_labels: ["Central Securities Depository (CSD)"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000353", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[6]", "paragraph_id": null, "table_id": "T6"}]
flows: []
process_sections: []
message_ids: []
message_families: []
search_terms: ["Central Securities Depository (CSD)"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---



# Central Securities Depository (CSD)

Business context: T2S CollateralManagementReferenceData. Source classification: business role.

## Definition

An infrastructure that, holds or controls, the holding of physical or dematerialised financial instruments belonging to all, or a large portion of, the investors in a securities market. This affects the centralised transfer of ownership of such securities by entries on its books and records.

Evidence: [T6](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000353/tables/tbl-0006.md), source row 6.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Account Servicer](participant-src-000353-account-servicer.md) | [T7](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000353/tables/tbl-0007.md) row 6, column 2 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Central Securities Depository (CSD)`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000353](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralManagementReferenceData_v2.docx`.

Collateral-reference source context: [Collateral-reference business-role context](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/diagrams/curated/fig-0001.md). .
