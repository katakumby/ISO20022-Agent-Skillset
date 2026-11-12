---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
message_sets: ["t2s-billing"]
participant_id: "participant-src-000347-national-central-bank"
title: "National Central Bank"
source_labels: ["National Central Bank"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000347", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[3]", "paragraph_id": null, "table_id": "T6"}]
flows: ["flow-src-000347-p121-billing-report", "flow-src-000347-p156-billing-report"]
process_sections: []
message_ids: ["camt.077.001.01"]
message_families: []
search_terms: ["National Central Bank"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---







# National Central Bank

Business context: T2S Billing. Source classification: business role.

## Definition

The principal monetary authority of a nation, a central bank performs several key functions, including issuing currency and regulating the supply of credit in the economy. 

Evidence: [T6](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/documents/src-000347/tables/tbl-0006.md), source row 3.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Account Servicer](participant-src-000347-account-servicer.md) | [T7](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/documents/src-000347/tables/tbl-0007.md) row 3, column 2 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `National Central Bank`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000347](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`.

Billing source context: [Billing business roles and functional participants](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0001.md). Source role-matrix inconsistency remains open under issue-000038.

Billing source context: [Billing report activity](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0008.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p121-billing-report.md).

Billing source context: [Billing report push sequence](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0011.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p156-billing-report.md).
