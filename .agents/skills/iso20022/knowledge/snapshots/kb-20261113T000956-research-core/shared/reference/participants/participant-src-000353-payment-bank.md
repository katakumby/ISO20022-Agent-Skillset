---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000353"]
source_editions: ["may-2025"]
message_sets: ["t2s-collateral-management-reference-data"]
participant_id: "participant-src-000353-payment-bank"
title: "Payment Bank"
source_labels: ["Payment Bank"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000353", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[4]", "paragraph_id": null, "table_id": "T6"}]
flows: []
process_sections: []
message_ids: []
message_families: []
search_terms: ["Payment Bank"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---



# Payment Bank

Business context: T2S CollateralManagementReferenceData. Source classification: business role.

## Definition

A Payment Bank is either a central bank or a private bank used to settle the cash leg of securities settlements: it provides the cash account to support the settlement of the securities transactions of another financial institution in central bank money (CeBM).

Evidence: [T6](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000353/tables/tbl-0006.md), source row 4.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Account Servicer](participant-src-000353-account-servicer.md) | [T7](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000353/tables/tbl-0007.md) row 4, column 2 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Payment Bank`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000353](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralManagementReferenceData_v2.docx`.

Collateral-reference source context: [Collateral-reference business-role context](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/diagrams/curated/fig-0001.md). .
