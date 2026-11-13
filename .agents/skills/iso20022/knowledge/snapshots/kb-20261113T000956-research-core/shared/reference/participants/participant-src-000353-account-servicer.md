---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000353"]
source_editions: ["may-2025"]
message_sets: ["t2s-collateral-management-reference-data"]
participant_id: "participant-src-000353-account-servicer"
title: "Account Servicer"
source_labels: ["Account Servicer"]
role_type: "functional participant role (matrix label; definition not extracted)"
aliases: []
source_locations: []
flows: []
process_sections: []
message_ids: []
message_families: []
search_terms: ["Account Servicer"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---



# Account Servicer

Business context: T2S CollateralManagementReferenceData. Source classification: functional participant role (matrix label; definition not extracted).

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [Collateral Management System](participant-src-000353-collateral-management-system.md) | [T7](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000353/tables/tbl-0007.md) row 2, column 2 |
| Business role listed for this functional participant | [National Central Bank](participant-src-000353-national-central-bank.md) | [T7](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000353/tables/tbl-0007.md) row 3, column 2 |
| Business role listed for this functional participant | [Payment Bank](participant-src-000353-payment-bank.md) | [T7](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000353/tables/tbl-0007.md) row 4, column 2 |
| Business role listed for this functional participant | [Central Database System](participant-src-000353-central-database-system.md) | [T7](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000353/tables/tbl-0007.md) row 5, column 2 |
| Business role listed for this functional participant | [Central Securities Depository (CSD)](participant-src-000353-central-securities-depository-csd.md) | [T7](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000353/tables/tbl-0007.md) row 6, column 2 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Account Servicer`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000353](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralManagementReferenceData_v2.docx`.

Collateral-reference source context: [Collateral-reference business-role context](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/diagrams/curated/fig-0001.md). .
