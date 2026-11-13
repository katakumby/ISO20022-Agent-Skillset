---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000362"]
source_editions: ["february-2025"]
message_sets: ["t2s-limit-utilisation-journal"]
participant_id: "participant-src-000362-executing-servicing-party-t2s-in-this-case"
title: "Executing/Servicing Party (T2S in this case)"
source_labels: ["Executing/Servicing Party (T2S in this case)"]
role_type: "activity participant; classification not established"
aliases: []
source_locations: [{"source_id": "src-000362", "heading_path": ["Description of BusinessActivities", "Pull mode"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[3]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000362", "heading_path": ["Description of BusinessActivities", "Pull mode"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[4]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000362", "heading_path": ["Description of BusinessActivities", "Pull mode"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[5]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000362", "heading_path": ["Description of BusinessActivities", "Pull mode"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[6]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000362", "heading_path": ["Description of BusinessActivities", "Push mode"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[2]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000362", "heading_path": ["Description of BusinessActivities", "Push mode"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[3]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000362", "heading_path": ["Description of BusinessActivities", "Push mode"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[4]", "paragraph_id": null, "table_id": "T11"}]
flows: ["flow-src-000362-p137-pull-mode", "flow-src-000362-p143-push-mode"]
process_sections: []
message_ids: []
message_families: []
search_terms: ["Executing/Servicing Party (T2S in this case)"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# Executing/Servicing Party (T2S in this case)

Business context: T2S LimitUtilisationJournal. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Validate Request | Technical and business validation of the request before further processing or not.<br>• If Yes, i.e., the request is valid, go to the Process Request. <br>• If No, the Send Reject is triggered. | Initiator | [T10](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000362/tables/tbl-0010.md) row 3 |
| Send Reject | Generate a report and route it to the communication layer to inform the Instructing Party that the Request is rejected with a specification of the operational error resulting from the validation of a request. | Initiator | [T10](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000362/tables/tbl-0010.md) row 4 |
| Process Request | Generate a report providing information regarding the limits as managed by the credit provider and corresponding to the criteria received within the incoming query message and trigger the Send Report. | Initiator | [T10](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000362/tables/tbl-0010.md) row 5 |
| Send Report | Route a report to the communication layer. | Initiator | [T10](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000362/tables/tbl-0010.md) row 6 |
| Request Limit Utilisation Journal | Requests reports as part of end of day report management events. | Initiator | [T11](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000362/tables/tbl-0011.md) row 2 |
| Process Request | Generate a report providing information regarding the limits as managed by the credit provider and trigger the Send Report. | Initiator | [T11](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000362/tables/tbl-0011.md) row 3 |
| Send Report | Route a report to the communication layer. | Initiator | [T11](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000362/tables/tbl-0011.md) row 4 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Pull mode](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p137-pull-mode.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Push mode](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p143-push-mode.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Executing/Servicing Party (T2S in this case)`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000362](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart1_Target2Securities_LimitUtilisationJournal_v2.docx`.
