---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
participant_id: "participant-src-000371-instructing-party"
title: "Instructing Party"
source_labels: ["Instructing Party"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000371", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000371", "heading_path": ["Description of BusinessActivities", "Securities Account Reference Data", "Creation Process"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[2]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000371", "heading_path": ["Description of BusinessActivities", "Securities Account Reference Data", "Creation Process"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[6]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000371", "heading_path": ["Description of BusinessActivities", "Securities Account Reference Data", "Modification Process "], "locator": "/w:document/w:body/w:tbl[15]/w:tr[2]", "paragraph_id": null, "table_id": "T15"}, {"source_id": "src-000371", "heading_path": ["Description of BusinessActivities", "Securities Account Reference Data", "Modification Process "], "locator": "/w:document/w:body/w:tbl[15]/w:tr[6]", "paragraph_id": null, "table_id": "T15"}, {"source_id": "src-000371", "heading_path": ["Description of BusinessActivities", "Securities Account Reference Data", "Deletion Process "], "locator": "/w:document/w:body/w:tbl[16]/w:tr[2]", "paragraph_id": null, "table_id": "T16"}, {"source_id": "src-000371", "heading_path": ["Description of BusinessActivities", "Securities Account Reference Data", "Deletion Process "], "locator": "/w:document/w:body/w:tbl[16]/w:tr[6]", "paragraph_id": null, "table_id": "T16"}, {"source_id": "src-000371", "heading_path": ["Description of BusinessActivities", "Securities Account Reference Data", "Query/Query Response process"], "locator": "/w:document/w:body/w:tbl[17]/w:tr[2]", "paragraph_id": null, "table_id": "T17"}, {"source_id": "src-000371", "heading_path": ["Description of BusinessActivities", "Securities Account Reference Data", "Query/Query Response process"], "locator": "/w:document/w:body/w:tbl[17]/w:tr[5]", "paragraph_id": null, "table_id": "T17"}, {"source_id": "src-000371", "heading_path": ["Description of BusinessActivities", "Securities Account Reference Data", "Statement process"], "locator": "/w:document/w:body/w:tbl[18]/w:tr[2]", "paragraph_id": null, "table_id": "T18"}, {"source_id": "src-000371", "heading_path": ["Description of BusinessActivities", "Securities Account Reference Data", "Statement process"], "locator": "/w:document/w:body/w:tbl[18]/w:tr[5]", "paragraph_id": null, "table_id": "T18"}]
flows: ["flow-src-000371-p152-create-securities-account", "flow-src-000371-p155-delete-securities-account", "flow-src-000371-p156-query", "flow-src-000371-p162-creation-process", "flow-src-000371-p164-modification-process", "flow-src-000371-p166-deletion-process", "flow-src-000371-p169-query-query-response-process", "flow-src-000371-p172-statement-process"]
process_sections: ["flow-src-000371-p178-confirmation-scenario", "flow-src-000371-p182-securities-account-creation-request", "flow-src-000371-p184-securities-account-status-advice", "flow-src-000371-p190-rejection-scenario", "flow-src-000371-p193-securities-account-creation-request", "flow-src-000371-p195-securities-account-status-advice", "flow-src-000371-p217-confirmation-scenario", "flow-src-000371-p224-securities-account-status-advice", "flow-src-000371-p232-rejection-scenario", "flow-src-000371-p238-securities-account-status-advice", "flow-src-000371-p259-confirmation-scenario", "flow-src-000371-p265-securities-account-status-advice", "flow-src-000371-p274-rejection-scenario", "flow-src-000371-p279-securities-account-status-advice", "flow-src-000371-p305-securities-account-query", "flow-src-000371-p307-securities-account-report", "flow-src-000371-p309-securities-account-report", "flow-src-000371-p314-securities-account-audit-trail-query", "flow-src-000371-p316-securities-account-audit-trail-report", "flow-src-000371-p318-securities-account-audit-trail-report", "flow-src-000371-p324-securities-account-activity-advice"]
message_ids: ["reda.018.001.01", "reda.019.001.01", "reda.020.001.01", "reda.021.001.01", "reda.023.001.01", "reda.032.001.01", "reda.035.001.01", "reda.036.001.01", "reda.037.001.01"]
message_families: ["reda.018", "reda.019", "reda.020", "reda.021", "reda.023", "reda.032", "reda.035", "reda.036"]
search_terms: ["Instructing Party", "reda.018", "reda.019", "reda.020", "reda.021", "reda.023", "reda.032", "reda.035", "reda.036"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000371-p152-create-securities-account", "flow-src-000371-p154-modify-a-securities-account", "flow-src-000371-p155-delete-securities-account", "flow-src-000371-p156-query", "flow-src-000371-p157-generate-statement"]
---

# Instructing Party

Business context: T2S SecuritiesAccountReferenceData. Source classification: functional participant role.

## Definition

Party that instructs the executing/servicing party to process and monitor a transaction.

Evidence: [T5](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000371/tables/tbl-0005.md), source row 2.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Instruction | Instructing Party instructs the Executing/Servicing Party to create a securities account. | Initiator | [T14](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000371/tables/tbl-0014.md) row 2 |
| Monitor process | Instructing Party monitors the status of the instruction. | Initiator | [T14](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000371/tables/tbl-0014.md) row 6 |
| Instruction | Instructing Party instructs the Executing/Servicing Party to modify a securities account. | Initiator | [T15](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000371/tables/tbl-0015.md) row 2 |
| Monitor process | Instructing Party monitors the status of the instruction. | Initiator | [T15](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000371/tables/tbl-0015.md) row 6 |
| Instruction | Instructing Party instructs the Executing/Servicing Party to delete a securities account. | Initiator | [T16](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000371/tables/tbl-0016.md) row 2 |
| Monitor process | Monitor process: Instructing Party monitors the status of the instruction. | Initiator | [T16](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000371/tables/tbl-0016.md) row 6 |
| Instruction | Instructing Party instructs Executing/Servicing Party to run a query or Audit Trail Query. | Initiator | [T17](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000371/tables/tbl-0017.md) row 2 |
| Monitor Process | Instructing Party monitors the status of the instruction. | Initiator | [T17](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000371/tables/tbl-0017.md) row 5 |
| Instruction | Instructing Party might instruct Executing/Servicing Party to run a statement.<br>This is not covered by the current process as NO message will be created to cover this. | Initiator | [T18](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000371/tables/tbl-0018.md) row 2 |
| Monitor Process | Instructing Party monitors the status of the instruction. | Initiator | [T18](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000371/tables/tbl-0018.md) row 5 |

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [Bank](participant-src-000371-bank.md) | [T7](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000371/tables/tbl-0007.md) row 2, column 2 |
| Business role listed for this functional participant | [Corporate](participant-src-000371-corporate.md) | [T7](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000371/tables/tbl-0007.md) row 3, column 2 |
| Business role listed for this functional participant | [CSD](participant-src-000371-csd.md) | [T7](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000371/tables/tbl-0007.md) row 4, column 2 |
| Business role listed for this functional participant | [Market Data Provider](participant-src-000371-market-data-provider.md) | [T7](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000371/tables/tbl-0007.md) row 5, column 2 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Create Securities Account](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p152-create-securities-account.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Delete Securities Account](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p155-delete-securities-account.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Query](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p156-query.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Creation Process](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p162-creation-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Modification Process](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p164-modification-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Deletion Process](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p166-deletion-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Query/Query Response process](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p169-query-query-response-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Statement process](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p172-statement-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Confirmation Scenario](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p178-confirmation-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Account Creation Request](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p182-securities-account-creation-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Account Status Advice](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p184-securities-account-status-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Rejection Scenario](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p190-rejection-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Account Creation Request](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p193-securities-account-creation-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Account Status Advice](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p195-securities-account-status-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Confirmation Scenario](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p217-confirmation-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Account Status Advice](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p224-securities-account-status-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Rejection Scenario](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p232-rejection-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Account Status Advice](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p238-securities-account-status-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Confirmation Scenario](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p259-confirmation-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Account Status Advice](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p265-securities-account-status-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Rejection Scenario](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p274-rejection-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Account Status Advice](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p279-securities-account-status-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Account Query](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p305-securities-account-query.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Account Report](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p307-securities-account-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Account Report](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p309-securities-account-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Account Audit Trail Query](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p314-securities-account-audit-trail-query.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Account Audit Trail Report](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p316-securities-account-audit-trail-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Account Audit Trail Report](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p318-securities-account-audit-trail-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Account Activity Advice](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p324-securities-account-activity-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `reda.018`, `reda.019`, `reda.020`, `reda.021`, `reda.023`, `reda.032`, `reda.035`, `reda.036`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Instructing Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000371](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`.

<!-- SECACCOUNT-FLOWS -->
## Flows and responsibilities

- [Create a securities account](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p152-create-securities-account.md)
- [Modify a securities account](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p154-modify-a-securities-account.md)
- [Delete a securities account](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p155-delete-securities-account.md)
- [Query securities account data or audit trail](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p156-query.md)
- [Receive unsolicited securities account activity](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p157-generate-statement.md)
