---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
flow_id: "flow-src-000368-p122-modify-party"
title: "Modify or block/unblock a party"
source_locations: [{"source_id": "src-000368", "table_id": "T9", "xml_path": "/w:document/w:body/w:tbl[9]", "heading_path": ["BusinessProcess Description"]}, {"source_id": "src-000368", "table_id": "T15", "xml_path": "/w:document/w:body/w:tbl[15]", "heading_path": ["Description of BusinessActivities", "Party Reference Data", "Modification Process"]}]
participants: ["participant-src-000368-instructing-party", "participant-src-000368-executing-servicing-party"]
message_mapping_evidence: [{"source_id": "src-000368", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Party Reference Data"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.022.001.02", "reda.016.001.01"]
message_families: ["reda.022", "reda.016"]
search_terms: ["Modify Party", "Executing / Servicing Party", "Instructing Party", "reda.022"]
limitations: ["Part1 figures use message families; exact supplied definitions are independently confirmed in Part2 src-000369.", "Source conditions, queuing and rejection reasons remain scenario-specific."]
manual_curated: true
participant_ids: ["participant-src-000368-instructing-party", "participant-src-000368-executing-servicing-party"]
issue_ids: []
---

# Modify or block/unblock a party

[src-000368](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`; [T9](../documents/src-000368/tables/tbl-0009.md) and [T15](../documents/src-000368/tables/tbl-0015.md).

## Purpose, trigger, preconditions and outcomes

| Item | Description |
| --- | --- |
| Definition | When an Instructing Party is in charge of the modification of a specific Party already supported by the Executing/Servicing Party system, the Instructing Party asks the Executing/Servicing Party to modify a party in the Executing/Servicing Party system. <br>The Instructing Party can block/unblock a Party; they ask the Executing/Servicing Party to block/unblock the Party. |
| Trigger | The process is triggered when the Instructing Party sends a Party Modification Request message. |
| Pre-conditions | The Instructing Party is known by the Executing/Servicing Party system and has been granted the appropriate privileges. An attribute of the party has changed which requires a modification of the party in the Executing/Servicing Party system. <br>The party needs to be blocked/unblocked. |
| Post-conditions | The acknowledgement of the processing of the modification request. |
| Role | Instructing Party |


## Participants, activities and responsibilities

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000368-instructing-party.md)
- [Executing / Servicing Party](../../../../../../../shared/reference/participants/participant-src-000368-executing-servicing-party.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Instruction | Instructing Party instructs the Executing/Servicing Party to modify a party. | Instructing Party |
| Validate: | Executing/Servicing Party checks if the instruction already exists in the system.<br>It checks also if the data can or cannot be updated.<br>In case of a Block/Unblock instruction, the Executing/Servicing Party checks also if the party can or cannot be blocked/unblocked <br>If validation of the message fails, a status message “REJECTED” will be sent including the related errors and reason information.<br>If the message is valid and the time permits the update of the party (e.g. not during a night –time sequence), the data will be processed and a status message “COMPLETED” will be sent.<br>Otherwise a status message “QUEUED” will be sent and the instruction will be resubmit to validation after e.g. a night –time cycle. | Executing/Servicing Party |
| Process | If the instruction is accepted, the Executing/Servicing Party processes the instruction and informs the Instructing Party of the completeness of this instruction. | Executing/Servicing Party |
| Report | Executing/Servicing Party informs the Instructing Party that this instruction is rejected and why. | Executing/Servicing Party |
| Monitor process | Instructing Party monitors the status of the instruction. | Instructing Party |


## Ordered scenarios, alternative and failure paths

**P196** Modification Process

**P197** Confirmation Scenario

**P198** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing party

**P201** Party Maintenance Request

**P202** The Instruction Party sends an instruction to the Executing/Servicing Party to modify data for a Party. This instruction contains information that uniquely identify the Party. 

**P203** In this instruction, the Instruction Party can also send to the Executing/Servicing Party the request to block/unblock a Party for settlement. 

**P204** In this case, this instruction contains details of the restriction like the restriction type and timeframe.

**P205** Party Status Advice

**P206** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:


**P207** Queued:
The Executing/Servicing Party might informs the Instructing party that the processing of the Modify Party instruction has been delayed. In case of e.g. a night-time cycle is running.  


**P208** Completed:
The Executing/Servicing Party informs the Instructing party that the Modify Party instruction has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the Party that has been processed.

**P210** Rejection Scenario

**P211** Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party

**P214** Party Maintenance Request

**P215** The Instruction Party sends an instruction to the Executing/Servicing Party to modify reference data for a party. 

**P216** Party Status Advice

**P217** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:


**P218** Rejected:
The instruction did not pass validation, some reasons could be:

**P219** the mandatory information is not present or incorrect,

**P220** the data cannot be updated,

**P221** the party cannot be blocked/unblocked,

**P222** the Instructing Party does not have the right to (un)block party

**P223** the instruction has already been received and is being processed 

**P224** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.


**P225** Queued:
The Executing/Servicing Party might inform the Instructing party that the processing of the Modify Party instruction has been delayed. In case of e.g. a night-time cycle is running.  

**P227** Rejected after dequeuing:
After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P228** the mandatory information is not present or incorrect,

**P229** the data cannot be updated,

**P230** the party cannot be blocked,

**P231** the Instructing Party does not have the right to block/unblock Party

**P232** the instruction has already been received and is being processed 

**P234** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

## Diagrams and exact supplied message definitions

- [Party modification activity](../diagrams/party-reference-data/fig-0008.md)
- [Modification confirmation sequence](../diagrams/party-reference-data/fig-0014.md)
- [Modification rejection sequence](../diagrams/party-reference-data/fig-0015.md)

- [reda.022.001.02](../../../../messages/reda.022.001.02/index.md)
- [reda.016.001.01](../../../../messages/reda.016.001.01/index.md)

## Scope qualifications

A successful submission can be queued and revalidated. Rejection can happen before or after queuing; multiple reasons may be supplied. The conditional narrative is not flattened into a mandatory QUEUED status before every final result.

P87 supplies the publication-specific BAH context. No cancellation or reversal of these reference-data requests is established by these source flows.
