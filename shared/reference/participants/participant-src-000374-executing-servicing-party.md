---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_sets: ["t2s-securities-and-penalty-reporting"]
participant_id: "participant-src-000374-executing-servicing-party"
title: "Executing / Servicing Party"
source_labels: ["Executing / Servicing Party", "Executing/Servicing Party."]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000374", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response", "Securities Settlement Transaction Query and Securities Settlement Transaction Query Response"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[3]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response", "Securities Settlement Transaction Query and Securities Settlement Transaction Query Response"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[4]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response", "Securities Settlement Transaction Query and Securities Settlement Transaction Query Response"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[5]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response", "Securities Settlement Transaction Query and Securities Settlement Transaction Query Response"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[6]", "paragraph_id": null, "table_id": "T11"}]
flows: ["flow-src-000374-p224-query-report-process", "flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp", "flow-src-000374-p239-securities-settlement-transaction-query-and-securities-settlement-tran", "flow-src-000374-p243-securities-transaction-penalties-report"]
process_sections: []
message_ids: ["semt.025.001.01", "semt.026.001.01", "semt.027.001.01", "semt.040.001.01", "semt.044.001.01"]
message_families: ["semt.025", "semt.026", "semt.027", "semt.040"]
search_terms: ["Executing / Servicing Party", "semt.025", "semt.026", "semt.027", "semt.040"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---

















# Executing / Servicing Party

Business context: T2S SecuritiesAndPenaltyReporting. Source classification: functional participant role.

## Definition

Party that processes, monitors and reports on transactions received from the Instructing party.

Evidence: [T5](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0005.md), source row 3.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Process Query. | Technical and business validation of the request query before further processing or not. <br>• If Yes, i.e., the request query is valid, go to Send Securities Settlement Instructions Query Response. <br>• If No, Error Processing is triggered. | Initiator | [T11](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0011.md) row 3 |
| Error Processing. | Adds operational errors to response before routing to Send Error Response. | Initiator | [T11](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0011.md) row 4 |
| Send Error Response. | Routes error response to communication layer. | Initiator | [T11](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0011.md) row 5 |
| Send Securities Settlement Instructions Query Response. | Routes response to communication layer. | Initiator | [T11](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0011.md) row 6 |

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [Settlement Infrastructure](participant-src-000374-settlement-infrastructure.md) | [T7](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0007.md) row 2, column 3 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Securities Account Position Query and Securities Account Position Response](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Settlement Transaction Query and Securities Settlement Transaction Query Response](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p239-securities-settlement-transaction-query-and-securities-settlement-tran.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `semt.025`, `semt.026`, `semt.027`, `semt.040`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Executing / Servicing Party`, `Executing/Servicing Party.`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000374](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`.

Securities and penalty reporting source context: [Securities account position query and response exchange](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0001.md). [flow Securities Account Position Query and Securities Account Position Response](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp.md).

Securities and penalty reporting source context: [Securities settlement transaction query and response exchange](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0002.md). [flow Securities Settlement Transaction Query and Securities Settlement Transaction Query Response](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p239-securities-settlement-transaction-query-and-securities-settlement-tran.md).

Securities and penalty reporting source context: [Penalty reporting in settlement instruction context](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0003.md). [flow Securities Transaction Penalties Report](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p243-securities-transaction-penalties-report.md).

Securities and penalty reporting source context: [Securities reporting business-process overview](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0005.md). [flow Query Report Process](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p224-query-report-process.md).

Securities and penalty reporting source context: [Securities position query activity with access and error decisions](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0010.md). [flow Securities Account Position Query and Securities Account Position Response](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp.md).

Securities and penalty reporting source context: [Securities settlement query activity and operational-error branch](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0011.md). [flow Securities Settlement Transaction Query and Securities Settlement Transaction Query Response](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p239-securities-settlement-transaction-query-and-securities-settlement-tran.md).

Securities and penalty reporting source context: [Scheduled cash-penalty reporting activity](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0012.md). [flow Securities Transaction Penalties Report](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p243-securities-transaction-penalties-report.md).

Securities and penalty reporting source context: [Reconciliation across status, penalty and settlement information](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0013.md). [flow Query Report Process](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p224-query-report-process.md).
