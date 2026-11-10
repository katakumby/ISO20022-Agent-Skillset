---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_sets: ["t2s-securities-and-penalty-reporting"]
participant_id: "participant-src-000374-instructing-party"
title: "Instructing Party"
source_labels: ["Instructing Party", "Instructing Party."]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000374", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[2]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[6]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[7]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response", "Securities Settlement Transaction Query and Securities Settlement Transaction Query Response"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[2]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response", "Securities Settlement Transaction Query and Securities Settlement Transaction Query Response"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[7]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response", "Securities Settlement Transaction Query and Securities Settlement Transaction Query Response"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[8]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response", "Securities Transaction Penalties Report"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[4]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000374", "heading_path": ["Description of BusinessActivities", "Securities Account Position Query and Securities Account Position Response", "Securities Transaction Penalties Report"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[5]", "paragraph_id": null, "table_id": "T12"}]
flows: ["flow-src-000374-p224-query-report-process", "flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp", "flow-src-000374-p239-securities-settlement-transaction-query-and-securities-settlement-tran", "flow-src-000374-p243-securities-transaction-penalties-report"]
process_sections: []
message_ids: ["semt.025.001.01", "semt.026.001.01", "semt.027.001.01", "semt.040.001.01", "semt.044.001.01"]
message_families: ["semt.025", "semt.026", "semt.027", "semt.040", "semt.044"]
search_terms: ["Instructing Party", "semt.025", "semt.026", "semt.027", "semt.040", "semt.044"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---

















# Instructing Party

Business context: T2S SecuritiesAndPenaltyReporting. Source classification: functional participant role.

## Definition

Party that instructs the executing/servicing party to process and monitor a transaction.

Evidence: [T5](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0005.md), source row 2.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Reconcile Securities Positions | Instructing Party sends a query to the Executing/Servicing Party to request details of the related securities positions. | Initiator | [T10](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0010.md) row 2 |
| Process Status | Check for incoming communications associated with original instruction and process its content. | Initiator | [T10](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0010.md) row 6 |
| Update Securities Account Position | External process of reconciling based on the content of the message response to the original instruction. | Initiator | [T10](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0010.md) row 7 |
| Send Securities Settlement Instructions Query. | Instructing Party sends a query to the Executing/Servicing Party for querying all securities settlement instructions corresponding to the criteria as defined within the query message. | Initiator | [T11](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0011.md) row 2 |
| Monitor. | Check for incoming communications associated with original instruction. | Initiator | [T11](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0011.md) row 7 |
| Reconcile. | External process reconciling impact of current status of original instruction. | Initiator | [T11](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0011.md) row 8 |
| Monitor | Check for incoming communications associated with the Report configuration previously introduced in the system. | Initiator | [T12](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0012.md) row 4 |
| Reconcile | External process reconciling impact of the penalties computed on the Settlement instructions previously sent to the system. | Initiator | [T12](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0012.md) row 5 |

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [Central Securities Depositories (CSD)](participant-src-000374-central-securities-depositories-csd.md) | [T7](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0007.md) row 3, column 2 |
| Business role listed for this functional participant | [Direct Connected Participant (DCP)](participant-src-000374-direct-connected-participant-dcp.md) | [T7](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0007.md) row 4, column 2 |
| Business role listed for this functional participant | [Central Counterparty](participant-src-000374-central-counterparty.md) | [T7](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0007.md) row 5, column 2 |
| Business role listed for this functional participant | [T2S Operator](participant-src-000374-t2s-operator.md) | [T7](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000374/tables/tbl-0007.md) row 6, column 2 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Query Report Process](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p224-query-report-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Account Position Query and Securities Account Position Response](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Settlement Transaction Query and Securities Settlement Transaction Query Response](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p239-securities-settlement-transaction-query-and-securities-settlement-tran.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Transaction Penalties Report](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p243-securities-transaction-penalties-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `semt.025`, `semt.026`, `semt.027`, `semt.040`, `semt.044`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Instructing Party`, `Instructing Party.`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000374](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`.

Securities and penalty reporting source context: [Securities account position query and response exchange](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0001.md). [flow Securities Account Position Query and Securities Account Position Response](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp.md).

Securities and penalty reporting source context: [Securities settlement transaction query and response exchange](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0002.md). [flow Securities Settlement Transaction Query and Securities Settlement Transaction Query Response](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p239-securities-settlement-transaction-query-and-securities-settlement-tran.md).

Securities and penalty reporting source context: [Penalty reporting in settlement instruction context](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0003.md). [flow Securities Transaction Penalties Report](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p243-securities-transaction-penalties-report.md).

Securities and penalty reporting source context: [Securities reporting business-process overview](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0005.md). [flow Query Report Process](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p224-query-report-process.md).

Securities and penalty reporting source context: [Securities position query activity with access and error decisions](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0010.md). [flow Securities Account Position Query and Securities Account Position Response](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp.md).

Securities and penalty reporting source context: [Securities settlement query activity and operational-error branch](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0011.md). [flow Securities Settlement Transaction Query and Securities Settlement Transaction Query Response](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p239-securities-settlement-transaction-query-and-securities-settlement-tran.md).

Securities and penalty reporting source context: [Scheduled cash-penalty reporting activity](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0012.md). [flow Securities Transaction Penalties Report](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p243-securities-transaction-penalties-report.md).

Securities and penalty reporting source context: [Reconciliation across status, penalty and settlement information](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0013.md). [flow Query Report Process](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p224-query-report-process.md).
