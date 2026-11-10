---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000362"]
source_editions: ["february-2025"]
message_sets: ["t2s-limit-utilisation-journal"]
participant_id: "participant-src-000362-instructing-party-subscriber-to-receive-the-report"
title: "Instructing Party (Subscriber to receive the report)"
source_labels: ["Instructing Party (Subscriber to receive the report)"]
role_type: "activity participant; classification not established"
aliases: []
source_locations: [{"source_id": "src-000362", "heading_path": ["Description of BusinessActivities", "Push mode"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[5]", "paragraph_id": null, "table_id": "T11"}]
flows: ["flow-src-000362-p143-push-mode"]
process_sections: []
message_ids: ["camt.065.001.01"]
message_families: []
search_terms: ["Instructing Party (Subscriber to receive the report)"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---



# Instructing Party (Subscriber to receive the report)

Business context: T2S LimitUtilisationJournal. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Receive Report | Go to the requested reporting activity. | Initiator | [T11](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000362/tables/tbl-0011.md) row 5 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Push mode](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p143-push-mode.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Instructing Party (Subscriber to receive the report)`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000362](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart1_Target2Securities_LimitUtilisationJournal_v2.docx`.

Limit-journal source context: [Scheduled limit-journal push activity](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/diagrams/curated/fig-0011.md). [flow Push mode](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p143-push-mode.md).
