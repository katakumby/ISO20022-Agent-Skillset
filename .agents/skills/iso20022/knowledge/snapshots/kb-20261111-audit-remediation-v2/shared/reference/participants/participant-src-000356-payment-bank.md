---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000356"]
source_editions: ["march-2024"]
message_sets: ["t2s-collateral-reporting"]
participant_id: "participant-src-000356-payment-bank"
title: "Payment Bank"
source_labels: ["Payment Bank"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000356", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[11]", "paragraph_id": null, "table_id": "T6"}]
flows: ["flow-src-000356-p138-query-management-process"]
process_sections: []
message_ids: ["colr.001.001.02", "colr.002.001.02"]
message_families: ["colr.001"]
search_terms: ["Payment Bank", "colr.001"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---







# Payment Bank

Business context: T2S CollateralReporting. Source classification: business role.

## Definition

The payment bank role includes all T2S system users of payment banks that require access to the T2S dedicated cash account balances and postings of the T2S dedicated cash accounts they provide for the purpose of securities settlement.

Evidence: [T6](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/documents/src-000356/tables/tbl-0006.md), source row 11.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [System Member](participant-src-000356-system-member.md) | [T7](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/documents/src-000356/tables/tbl-0007.md) row 4, column 2 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Query Management Process](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/flows/flow-src-000356-p138-query-management-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `colr.001`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Payment Bank`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000356](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralReporting_2023_2024_v2.docx`.

Collateral-reporting source context: [T2S hierarchy of roles and access rights](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/diagrams/curated/fig-0001.md). .

Collateral-reporting source context: [Central-system query taxonomy and communication modes](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/diagrams/curated/fig-0002.md). .

Collateral-reporting source context: [Collateral-query member and administrator activity](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/diagrams/curated/fig-0008.md). [flow Query Management Process](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/flows/flow-src-000356-p138-query-management-process.md).
