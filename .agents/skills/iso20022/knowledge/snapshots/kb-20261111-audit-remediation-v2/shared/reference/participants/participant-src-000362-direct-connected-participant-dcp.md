---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000362"]
source_editions: ["february-2025"]
message_sets: ["t2s-limit-utilisation-journal"]
participant_id: "participant-src-000362-direct-connected-participant-dcp"
title: "Direct Connected Participant (DCP)"
source_labels: ["Direct Connected Participant (DCP)"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000362", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[4]", "paragraph_id": null, "table_id": "T6"}]
flows: ["flow-src-000362-p132-query-report-process", "flow-src-000362-p137-pull-mode"]
process_sections: []
message_ids: ["camt.064.001.01", "camt.065.001.01"]
message_families: []
search_terms: ["Direct Connected Participant (DCP)"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---











# Direct Connected Participant (DCP)

Business context: T2S LimitUtilisationJournal. Source classification: business role.

## Definition

The party, which is not a CSD and that, is directly connected to the Settlement Infrastructure Platform. It could be a local custodian, a global custodian, a stock exchange , a central counterparty, etc.

Evidence: [T6](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000362/tables/tbl-0006.md), source row 4.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Instructing Party](participant-src-000362-instructing-party.md) | [T7](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000362/tables/tbl-0007.md) row 4, column 2 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Direct Connected Participant (DCP)`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000362](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart1_Target2Securities_LimitUtilisationJournal_v2.docx`.

Limit-journal source context: [Limit-utilisation journal scope exchange](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/diagrams/curated/fig-0001.md). [flow Pull mode](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p137-pull-mode.md).

Limit-journal source context: [Limit reporting communication roles](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/diagrams/curated/fig-0003.md). [flow Pull mode](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p137-pull-mode.md).

Limit-journal source context: [Query taxonomy and limit-journal scope](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/diagrams/curated/fig-0005.md). [flow Query Report Process](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p132-query-report-process.md).

Limit-journal source context: [Participant-triggered limit-journal pull activity](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/diagrams/curated/fig-0010.md). [flow Pull mode](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p137-pull-mode.md).

Limit-journal source context: [Limit-journal business transaction exchange](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/diagrams/curated/fig-0012.md). [flow Pull mode](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p137-pull-mode.md).
