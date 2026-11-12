---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000362"]
source_editions: ["february-2025"]
message_sets: ["t2s-limit-utilisation-journal"]
participant_id: "participant-src-000362-executing-servicing-party"
title: "Executing / Servicing Party"
source_labels: ["Executing / Servicing Party"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000362", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}]
flows: ["flow-src-000362-p132-query-report-process", "flow-src-000362-p137-pull-mode", "flow-src-000362-p143-push-mode"]
process_sections: []
message_ids: ["camt.064.001.01", "camt.065.001.01"]
message_families: []
search_terms: ["Executing / Servicing Party"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---











# Executing / Servicing Party

Business context: T2S LimitUtilisationJournal. Source classification: functional participant role.

## Definition

Party that processes, monitors and reports on transactions received from the Instructing party.

Evidence: [T5](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000362/tables/tbl-0005.md), source row 3.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [Settlement Infrastructure](participant-src-000362-settlement-infrastructure.md) | [T7](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000362/tables/tbl-0007.md) row 2, column 3 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Query Report Process](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p132-query-report-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Pull mode](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p137-pull-mode.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Executing / Servicing Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000362](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart1_Target2Securities_LimitUtilisationJournal_v2.docx`.

Limit-journal source context: [Limit-utilisation journal scope exchange](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/diagrams/curated/fig-0001.md). [flow Pull mode](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p137-pull-mode.md).

Limit-journal source context: [Limit reporting communication roles](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/diagrams/curated/fig-0003.md). [flow Pull mode](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p137-pull-mode.md).

Limit-journal source context: [Participant-triggered limit-journal pull activity](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/diagrams/curated/fig-0010.md). [flow Pull mode](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p137-pull-mode.md).

Limit-journal source context: [Scheduled limit-journal push activity](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/diagrams/curated/fig-0011.md). [flow Push mode](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p143-push-mode.md).

Limit-journal source context: [Limit-journal business transaction exchange](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/diagrams/curated/fig-0012.md). [flow Pull mode](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p137-pull-mode.md).
