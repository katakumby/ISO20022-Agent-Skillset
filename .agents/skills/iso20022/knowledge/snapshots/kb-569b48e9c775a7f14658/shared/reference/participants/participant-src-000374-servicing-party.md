---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_sets: ["t2s-securities-and-penalty-reporting"]
participant_id: "participant-src-000374-servicing-party"
title: "Servicing Party"
source_labels: ["Servicing Party"]
role_type: "activity participant; classification not established"
aliases: []
source_locations: [{"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[3]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[4]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[5]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response", "Securities Transaction Penalties Report"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[2]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response", "Securities Transaction Penalties Report"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[3]", "paragraph_id": null, "table_id": "T12"}]
flows: ["flow-src-000374-p224-query-report-process", "flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp", "flow-src-000374-p243-securities-transaction-penalties-report"]
process_sections: []
message_ids: ["semt.025.001.01", "semt.040.001.01", "semt.044.001.01"]
message_families: ["semt.025", "semt.040", "semt.044"]
search_terms: ["Servicing Party", "semt.025", "semt.040", "semt.044"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---









# Servicing Party

Business context: T2S SecuritiesAndPenaltyReporting. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Validate Request | Technical and business validation of the query before further processing or not. <br>• If Yes, i.e., the request is valid, go to Querying process based in the selected criteria. <br>• If No, Update Status is triggered. | Initiator | [T10](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0010.md) row 3 |
| Update Status | Routes error response to communication layer | Initiator | [T10](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0010.md) row 4 |
| Querying process based in the selected criteria | Retrieves the requested data and routes the response message to communication layer. | Initiator | [T10](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0010.md) row 5 |
| Generate Report | System process that creates report from previously calculated cash penalties satisfying reporting criteria (i.e., business day, debtor, creditor…), assuming the Instructing Party has specified an interested in Receiving the Report. | Initiator | [T12](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0012.md) row 2 |
| Report cash Penalties Calculated | Route the previously generated report to the communication layer | Initiator | [T12](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0012.md) row 3 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Query Report Process](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p224-query-report-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Account Position Query and Securities Account Position Response](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Transaction Penalties Report](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p243-securities-transaction-penalties-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `semt.025`, `semt.040`, `semt.044`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Servicing Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000374](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`.

Securities and penalty reporting source context: [Securities account position query and response exchange](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0001.md). [flow Securities Account Position Query and Securities Account Position Response](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp.md).

Securities and penalty reporting source context: [Penalty reporting in settlement instruction context](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0003.md). [flow Securities Transaction Penalties Report](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p243-securities-transaction-penalties-report.md).

Securities and penalty reporting source context: [Securities position query activity with access and error decisions](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0010.md). [flow Securities Account Position Query and Securities Account Position Response](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp.md).

Securities and penalty reporting source context: [Scheduled cash-penalty reporting activity](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0012.md). [flow Securities Transaction Penalties Report](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p243-securities-transaction-penalties-report.md).
