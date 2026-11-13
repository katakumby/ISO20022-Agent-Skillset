---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
participant_id: "participant-src-000368-instructing-party"
title: "Instructing Party"
source_labels: ["Instructing Party"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000368", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000368", "heading_path": ["Description of BusinessActivities", "Party Reference Data", "Creation Process"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[2]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000368", "heading_path": ["Description of BusinessActivities", "Party Reference Data", "Creation Process"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[6]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000368", "heading_path": ["Description of BusinessActivities", "Party Reference Data", "Modification Process"], "locator": "/w:document/w:body/w:tbl[15]/w:tr[2]", "paragraph_id": null, "table_id": "T15"}, {"source_id": "src-000368", "heading_path": ["Description of BusinessActivities", "Party Reference Data", "Modification Process"], "locator": "/w:document/w:body/w:tbl[15]/w:tr[6]", "paragraph_id": null, "table_id": "T15"}, {"source_id": "src-000368", "heading_path": ["Description of BusinessActivities", "Party Reference Data", "Deletion Process "], "locator": "/w:document/w:body/w:tbl[16]/w:tr[2]", "paragraph_id": null, "table_id": "T16"}, {"source_id": "src-000368", "heading_path": ["Description of BusinessActivities", "Party Reference Data", "Deletion Process "], "locator": "/w:document/w:body/w:tbl[16]/w:tr[6]", "paragraph_id": null, "table_id": "T16"}, {"source_id": "src-000368", "heading_path": ["Description of BusinessActivities", "Party Reference Data", "Query/Query Response process"], "locator": "/w:document/w:body/w:tbl[17]/w:tr[2]", "paragraph_id": null, "table_id": "T17"}, {"source_id": "src-000368", "heading_path": ["Description of BusinessActivities", "Party Reference Data", "Query/Query Response process"], "locator": "/w:document/w:body/w:tbl[17]/w:tr[5]", "paragraph_id": null, "table_id": "T17"}, {"source_id": "src-000368", "heading_path": ["Description of BusinessActivities", "Party Reference Data", "Statement process"], "locator": "/w:document/w:body/w:tbl[18]/w:tr[2]", "paragraph_id": null, "table_id": "T18"}, {"source_id": "src-000368", "heading_path": ["Description of BusinessActivities", "Party Reference Data", "Statement process"], "locator": "/w:document/w:body/w:tbl[18]/w:tr[5]", "paragraph_id": null, "table_id": "T18"}]
flows: ["flow-src-000368-p120-create-party", "flow-src-000368-p122-modify-party", "flow-src-000368-p124-delete-party", "flow-src-000368-p126-query", "flow-src-000368-p133-creation-process", "flow-src-000368-p137-modification-process", "flow-src-000368-p140-deletion-process", "flow-src-000368-p144-query-query-response-process", "flow-src-000368-p147-statement-process"]
process_sections: ["flow-src-000368-p155-confirmation-scenario", "flow-src-000368-p159-party-creation-request", "flow-src-000368-p161-party-status-advice", "flow-src-000368-p167-party-creation-request-reda-014-creation-process-party-status-advice-r", "flow-src-000368-p178-party-creation-request", "flow-src-000368-p180-party-status-advice", "flow-src-000368-p197-confirmation-scenario", "flow-src-000368-p205-party-status-advice", "flow-src-000368-p210-rejection-scenario", "flow-src-000368-p216-party-status-advice", "flow-src-000368-p237-confirmation-scenario", "flow-src-000368-p243-party-status-advice", "flow-src-000368-p248-rejection-scenario", "flow-src-000368-p254-party-status-advice", "flow-src-000368-p275-party-query", "flow-src-000368-p277-party-report", "flow-src-000368-p279-party-report", "flow-src-000368-p285-party-audit-trail-query", "flow-src-000368-p287-party-audit-trail-report", "flow-src-000368-p289-party-audit-trail-report", "flow-src-000368-p295-party-activity-advice"]
message_ids: ["reda.014.001.02", "reda.015.001.01", "reda.016.001.01", "reda.017.001.02", "reda.022.001.02", "reda.031.001.01", "reda.041.001.02", "reda.042.001.01", "reda.043.001.02"]
message_families: ["reda.014", "reda.015", "reda.016", "reda.017", "reda.022", "reda.031", "reda.041", "reda.042", "reda.043"]
search_terms: ["Instructing Party", "reda.014", "reda.015", "reda.016", "reda.017", "reda.022", "reda.031", "reda.041", "reda.042", "reda.043"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000368-p120-create-party", "flow-src-000368-p122-modify-party", "flow-src-000368-p124-delete-party", "flow-src-000368-p126-query", "flow-src-000368-p128-statement"]
---

# Instructing Party

Business context: T2S PartyReferenceData. Source classification: functional participant role.

## Definition

Party that instructs the executing/servicing party to process and monitor a transaction.

Evidence: [T5](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/documents/src-000368/tables/tbl-0005.md), source row 2.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Instruction | Instructing Party instructs the Executing/Servicing Party to create a party | Initiator | [T14](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/documents/src-000368/tables/tbl-0014.md) row 2 |
| Monitor process | Instructing Party monitors the status of the instruction. | Initiator | [T14](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/documents/src-000368/tables/tbl-0014.md) row 6 |
| Instruction | Instructing Party instructs the Executing/Servicing Party to modify a party. | Initiator | [T15](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/documents/src-000368/tables/tbl-0015.md) row 2 |
| Monitor process | Instructing Party monitors the status of the instruction. | Initiator | [T15](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/documents/src-000368/tables/tbl-0015.md) row 6 |
| Instruction | Instructing Party instructs the Executing/Servicing Party to delete a party. | Initiator | [T16](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/documents/src-000368/tables/tbl-0016.md) row 2 |
| Monitor process | Instructing Party monitors the status of the instruction. | Initiator | [T16](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/documents/src-000368/tables/tbl-0016.md) row 6 |
| Instruction | Instructing Party instructs Executing/Servicing Party to run a query or Audit Trail Query. | Initiator | [T17](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/documents/src-000368/tables/tbl-0017.md) row 2 |
| Monitor process | Instructing Party monitors the status of the instruction. | Initiator | [T17](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/documents/src-000368/tables/tbl-0017.md) row 5 |
| Instruction | Instructing Party might instruct Executing/Servicing Party to run a statement.<br>This is not covered by the current process as NO message will be created to cover this. | Initiator | [T18](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/documents/src-000368/tables/tbl-0018.md) row 2 |
| Monitor process | Instructing Party monitors the status of the instruction. | Initiator | [T18](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/documents/src-000368/tables/tbl-0018.md) row 5 |

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [Bank](participant-src-000368-bank.md) | [T7](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/documents/src-000368/tables/tbl-0007.md) row 2, column 2 |
| Business role listed for this functional participant | [Corporate](participant-src-000368-corporate.md) | [T7](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/documents/src-000368/tables/tbl-0007.md) row 3, column 2 |
| Business role listed for this functional participant | [CSD](participant-src-000368-csd.md) | [T7](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/documents/src-000368/tables/tbl-0007.md) row 4, column 2 |
| Business role listed for this functional participant | [Market Data Provider](participant-src-000368-market-data-provider.md) | [T7](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/documents/src-000368/tables/tbl-0007.md) row 5, column 2 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Create Party](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p120-create-party.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Modify Party](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p122-modify-party.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Delete Party](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p124-delete-party.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Query](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p126-query.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Creation Process](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p133-creation-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Modification Process](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p137-modification-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Deletion Process](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p140-deletion-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Query/Query Response process](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p144-query-query-response-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Statement process](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p147-statement-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Confirmation Scenario](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p155-confirmation-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Party Creation Request](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p159-party-creation-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Party Status Advice](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p161-party-status-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Party Creation Request (reda.014)Creation processParty Status Advice (reda.016): QUEUEDParty Status Advice (reda.016): REJECTEDRejection Scenario](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p167-party-creation-request-reda-014-creation-process-party-status-advice-r.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Party Creation Request:](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p178-party-creation-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Party Status Advice:](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p180-party-status-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Confirmation Scenario](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p197-confirmation-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Party Status Advice](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p205-party-status-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Rejection Scenario](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p210-rejection-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Party Status Advice](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p216-party-status-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Confirmation Scenario](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p237-confirmation-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Party Status Advice](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p243-party-status-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Rejection Scenario](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p248-rejection-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Party Status Advice](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p254-party-status-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Party query](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p275-party-query.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Party Report](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p277-party-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Party Report](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p279-party-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Party Audit Trail Query](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p285-party-audit-trail-query.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Party Audit Trail Report](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p287-party-audit-trail-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Party Audit Trail Report](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p289-party-audit-trail-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Party Activity Advice](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p295-party-activity-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `reda.014`, `reda.015`, `reda.016`, `reda.017`, `reda.022`, `reda.031`, `reda.041`, `reda.042`, `reda.043`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Instructing Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000368](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`.

<!-- PARTY-FLOWS -->
## Curated flows and responsibilities

- [Create a party](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p120-create-party.md)
- [Modify or block/unblock a party](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p122-modify-party.md)
- [Delete a party](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p124-delete-party.md)
- [Query party reference data or audit trail](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p126-query.md)
- [Receive an unsolicited party activity statement](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/flow-src-000368-p128-statement.md)
