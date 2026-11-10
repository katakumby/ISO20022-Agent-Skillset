---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_sets: ["t2s-settlement-restrictions"]
participant_id: "participant-src-000380-instructing-party"
title: "Instructing Party"
source_labels: ["Instructing Party", "Instructing Party."]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000380", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000380", "heading_path": ["Description of BusinessActivities", "Intra Position Movement Query, Query Response and Pending Report", "Pull mode"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[2]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000380", "heading_path": ["Description of BusinessActivities", "Intra Position Movement Query, Query Response and Pending Report", "Pull mode"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[7]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000380", "heading_path": ["Description of BusinessActivities", "Intra Position Movement Query, Query Response and Pending Report", "Pull mode"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[8]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000380", "heading_path": ["Description of BusinessActivities", "Intra Position Movement Query, Query Response and Pending Report", "Push mode"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[6]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000380", "heading_path": ["Description of BusinessActivities", "Intra Position Movement Query, Query Response and Pending Report", "Push mode"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[7]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000380", "heading_path": ["Description of BusinessActivities", "Securities Transaction Cancellation/Modification Request Query/Report", "Pull mode"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[2]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000380", "heading_path": ["Description of BusinessActivities", "Securities Transaction Cancellation/Modification Request Query/Report", "Pull mode"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[7]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000380", "heading_path": ["Description of BusinessActivities", "Securities Transaction Cancellation/Modification Request Query/Report", "Pull mode"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[8]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000380", "heading_path": ["Description of BusinessActivities", "Securities Transaction Cancellation/Modification Request Query/Report", "Push mode"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[6]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000380", "heading_path": ["Description of BusinessActivities", "Securities Transaction Cancellation/Modification Request Query/Report", "Push mode"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[7]", "paragraph_id": null, "table_id": "T13"}]
flows: ["flow-src-000380-p253-query-report-process", "flow-src-000380-p259-pull-mode", "flow-src-000380-p263-push-mode", "flow-src-000380-p268-pull-mode", "flow-src-000380-p272-push-mode"]
process_sections: []
message_ids: ["semt.028.001.01", "semt.029.001.01", "semt.030.001.01", "semt.031.001.01", "semt.032.001.01", "semt.033.001.01", "semt.034.001.01"]
message_families: []
search_terms: ["Instructing Party"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000380-p101-settlement-condition-modification-request-query-and-report", "flow-src-000380-p111-transaction-cancellation-request-query-and-report", "flow-src-000380-p248-business-process-description", "flow-src-000380-p259-pull-mode", "flow-src-000380-p263-push-mode", "flow-src-000380-p268-pull-mode", "flow-src-000380-p272-push-mode", "flow-src-000380-p276-business-transactions", "flow-src-000380-p282-intra-position-movement-query-semt-028", "flow-src-000380-p285-intra-position-movement-query-response-semt-029", "flow-src-000380-p289-securities-settlement-conditions-modification-request-query-semt-030", "flow-src-000380-p293-securities-settlement-conditions-modification-request-report-semt-031", "flow-src-000380-p299-securities-transaction-cancellation-request-query-semt-032", "flow-src-000380-p304-securities-transaction-cancellation-request-report-semt-033", "flow-src-000380-p308-intra-position-movement-pending-report-semt-034", "flow-src-000380-p91-intra-position-movement-query-response-and-pending-report"]
---

































































# Instructing Party

Business context: T2S SettlementRestrictions. Source classification: functional participant role.

## Definition

Party that instructs the executing/servicing party to process and monitor a transaction.

Evidence: [T5](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000380/tables/tbl-0005.md), source row 2.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Request Intra Position Movement Instructions. | Instructing Party sends a query to the Executing/Servicing Party to request details of any previously sent Intra Position Movement Instructions and the related securities positions. | Initiator | [T10](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000380/tables/tbl-0010.md) row 2 |
| Monitor | Check for incoming communications associated with original instruction. | Initiator | [T10](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000380/tables/tbl-0010.md) row 7 |
| Reconcile | External process reconciling impact of current status of original instruction. | Initiator | [T10](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000380/tables/tbl-0010.md) row 8 |
| Monitor. | Check for incoming communications associated with original instruction. | Initiator | [T11](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000380/tables/tbl-0011.md) row 6 |
| Reconcile. | External process reconciling impact of current status of original instruction. | Initiator | [T11](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000380/tables/tbl-0011.md) row 7 |
| Request Cancellation/Modification Instructions details  | Instructing Party sends a query to the Executing/Servicing Party to request details of any previously sent Cancellation or Modification Instructions | Initiator | [T12](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000380/tables/tbl-0012.md) row 2 |
| Monitor | Check for incoming communications associated with original instruction. | Initiator | [T12](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000380/tables/tbl-0012.md) row 7 |
| Reconcile | External process reconciling impact of current status of original instruction. | Initiator | [T12](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000380/tables/tbl-0012.md) row 8 |
| Monitor. | Check for incoming communications (Settlement or Intra Position Movement Cancellation/Modification Report). | Initiator | [T13](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000380/tables/tbl-0013.md) row 6 |
| Reconcile. | External process reconciling impact of current status of original instruction. | Initiator | [T13](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000380/tables/tbl-0013.md) row 7 |

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [Central Securities Depositories (CSD)](participant-src-000380-central-securities-depositories-csd.md) | [T7](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000380/tables/tbl-0007.md) row 3, column 2 |
| Business role listed for this functional participant | [Direct Connected Participant (DCP)](participant-src-000380-direct-connected-participant-dcp.md) | [T7](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000380/tables/tbl-0007.md) row 4, column 2 |
| Business role listed for this functional participant | [Central Counterparty](participant-src-000380-central-counterparty.md) | [T7](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000380/tables/tbl-0007.md) row 5, column 2 |
| Business role listed for this functional participant | [T2S Operator](participant-src-000380-t2s-operator.md) | [T7](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000380/tables/tbl-0007.md) row 6, column 2 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Query Report Process](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p253-query-report-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Pull mode](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p259-pull-mode.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Push mode](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p263-push-mode.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Pull mode](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p268-pull-mode.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Push mode](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p272-push-mode.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Instructing Party`, `Instructing Party.`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000380](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`.

















<!-- SETTLEMENT-RESTRICTIONS-FIG-1-START -->
[Intra-position movement query, response and pending report](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p91-intra-position-movement-query-response-and-pending-report.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/diagrams/settlement-restrictions/fig-0001.md)
<!-- SETTLEMENT-RESTRICTIONS-FIG-1-END -->

<!-- SETTLEMENT-RESTRICTIONS-FIG-2-START -->
[Settlement-condition modification request query and report](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p101-settlement-condition-modification-request-query-and-report.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/diagrams/settlement-restrictions/fig-0002.md)
<!-- SETTLEMENT-RESTRICTIONS-FIG-2-END -->

<!-- SETTLEMENT-RESTRICTIONS-FIG-3-START -->
[Transaction cancellation request query and report](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p111-transaction-cancellation-request-query-and-report.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/diagrams/settlement-restrictions/fig-0003.md)
<!-- SETTLEMENT-RESTRICTIONS-FIG-3-END -->

<!-- SETTLEMENT-RESTRICTIONS-FIG-5-START -->
[Settlement and reconciliation high-level process relationships](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p248-business-process-description.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/diagrams/settlement-restrictions/fig-0005.md)
<!-- SETTLEMENT-RESTRICTIONS-FIG-5-END -->

<!-- SETTLEMENT-RESTRICTIONS-FIG-10-START -->
[Pull-mode intra-position movement query processing](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p259-pull-mode.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/diagrams/settlement-restrictions/fig-0010.md)
<!-- SETTLEMENT-RESTRICTIONS-FIG-10-END -->

<!-- SETTLEMENT-RESTRICTIONS-FIG-11-START -->
[Push-mode pending intra-position movement reporting](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p263-push-mode.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/diagrams/settlement-restrictions/fig-0011.md)
<!-- SETTLEMENT-RESTRICTIONS-FIG-11-END -->

<!-- SETTLEMENT-RESTRICTIONS-FIG-12-START -->
[Pull-mode cancellation or modification query processing](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p268-pull-mode.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/diagrams/settlement-restrictions/fig-0012.md)
<!-- SETTLEMENT-RESTRICTIONS-FIG-12-END -->

<!-- SETTLEMENT-RESTRICTIONS-FIG-13-START -->
[Push-mode cancellation or modification report processing](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p272-push-mode.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/diagrams/settlement-restrictions/fig-0013.md)
<!-- SETTLEMENT-RESTRICTIONS-FIG-13-END -->

<!-- SETTLEMENT-RESTRICTIONS-FIG-14-START -->
[Transaction reconciliation in instruction, cancellation and modification context](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p276-business-transactions.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/diagrams/settlement-restrictions/fig-0014.md)
<!-- SETTLEMENT-RESTRICTIONS-FIG-14-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.028-START -->
[semt.028.001.01 — role involvement and message direction](../../../domains/securities/reference/messages/semt.028.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.028-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.029-START -->
[semt.029.001.01 — role involvement and message direction](../../../domains/securities/reference/messages/semt.029.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.029-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.030-START -->
[semt.030.001.01 — role involvement and message direction](../../../domains/securities/reference/messages/semt.030.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.030-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.031-START -->
[semt.031.001.01 — role involvement and message direction](../../../domains/securities/reference/messages/semt.031.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.031-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.032-START -->
[semt.032.001.01 — role involvement and message direction](../../../domains/securities/reference/messages/semt.032.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.032-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.033-START -->
[semt.033.001.01 — role involvement and message direction](../../../domains/securities/reference/messages/semt.033.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.033-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.034-START -->
[semt.034.001.01 — role involvement and message direction](../../../domains/securities/reference/messages/semt.034.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.034-END -->
