---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
flow_id: "flow-src-000368-p124-delete-party"
title: "Delete a party"
source_locations: [{"source_id": "src-000368", "table_id": "T10", "xml_path": "/w:document/w:body/w:tbl[10]", "heading_path": ["BusinessProcess Description"]}, {"source_id": "src-000368", "table_id": "T16", "xml_path": "/w:document/w:body/w:tbl[16]", "heading_path": ["Description of BusinessActivities", "Party Reference Data", "Deletion Process "]}]
participants: ["participant-src-000368-instructing-party", "participant-src-000368-executing-servicing-party"]
message_mapping_evidence: [{"source_id": "src-000368", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Party Reference Data"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.031.001.01", "reda.016.001.01"]
message_families: ["reda.031", "reda.016"]
search_terms: ["Delete Party", "Executing / Servicing Party", "Instructing Party", "reda.031"]
limitations: ["Part1 figures use message families; exact supplied definitions are independently confirmed in Part2 src-000369.", "Source conditions, queuing and rejection reasons remain scenario-specific."]
manual_curated: true
participant_ids: ["participant-src-000368-instructing-party", "participant-src-000368-executing-servicing-party"]
issue_ids: ["issue-000046"]
---

# Delete a party

[src-000368](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`; [T10](../documents/src-000368/tables/tbl-0010.md) and [T16](../documents/src-000368/tables/tbl-0016.md).

## Purpose, trigger, preconditions and outcomes

| Item | Description |
| --- | --- |
| Definition | When an Instructing Party would like to delete a specific party already supported by the Executing/Servicing Party system, an Instructing Party asks the Executing/Servicing Party to delete the party in its system.  |
| Trigger | The process is triggered when the Instructing Party sends a Party Deletion Request message. |
| Pre-conditions | The Instructing Party is known by the Executing/Servicing Party system and has been granted the appropriate privileges. The Instructing Party identified a gap in the parties’ coverage of the Executing/Servicing Party. The Instructing Party needs to remove this party at the Executing /Servicing Party. |
| Post-conditions | The acknowledgement of the processing of the deletion request. |
| Role | Instructing Party |


## Participants, activities and responsibilities

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000368-instructing-party.md)
- [Executing / Servicing Party](../../../../../../../shared/reference/participants/participant-src-000368-executing-servicing-party.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Instruction | Instructing Party instructs the Executing/Servicing Party to delete a party. | Instructing Party |
| Validate: | Executing/Servicing Party checks if the instruction already exists in the system.<br>It checks also if the data can or cannot be updated.<br>In case of a Block/Unblock instruction, the Executing/Servicing Party checks also if the party can or cannot be blocked/unblocked <br>If validation of the message fails, a status message “REJECTED” will be sent including the related errors and reason information.<br>If the message is valid and the time permits the update of the party (e.g. not during a night –time sequence), the data will be processed and a status message “COMPLETED” will be sent.<br>Otherwise a status message “QUEUED” will be sent and the instruction will be resubmit to validation after e.g. a night –time cycle. | Executing/Servicing Party |
| Process | If the instruction is accepted, the Executing/Servicing Party processes the instruction and informs the Instructing Party of the completeness of this instruction. | Executing/Servicing Party |
| Report | Executing/Servicing Party informs the Instructing Party that this instruction is rejected and why. | Executing/Servicing Party |
| Monitor process | Instructing Party monitors the status of the instruction. | Instructing Party |


## Ordered scenarios, alternative and failure paths

**P236** Deletion Process

**P237** Confirmation Scenario

**P238** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing party:

**P241** Party Deletion Request

**P242** The Instruction Party sends an instruction to the Executing/Servicing Party to delete a Party. This instruction contains information that uniquely identifies the party and it is used when a party is no longer active.

**P243** Party Status Advice

**P244** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:


**P245** Queued
The Executing/Servicing Party might inform the Instructing party that the processing of the Delete Party instruction has been delayed. In case of e.g. a night-time cycle is running.  


**P246** Completed
The Executing/Servicing Party informs the Instructing party that the Delete Party instruction has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the party that has been processed.

**P248** Rejection Scenario

**P249** Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party

**P252** Party Deletion Request

**P253** The Instruction Party sends an instruction to the Executing/Servicing Party to delete a Party. 

**P254** Party Status Advice

**P255** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:


**P256** Rejected
The instruction did not pass validation, some reasons could be:

**P257** the mandatory information is not present or incorrect;

**P258** the Instructing Party does not have the right to delete Party;

**P259** the instruction has already been received and is being processed;

**P260** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status


**P261** Queued
The Executing/Servicing Party might inform the Instructing party that the processing of the Delete Party instruction has been delayed. In case of e.g. a night-time cycle is running.  

**P263** Rejected after dequeuing
After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P264**  the mandatory information is not present or incorrect;

**P265**  the Party cannot be deleted;

**P266**  the Instructing Party does not have the right to delete Party;

**P267**  the instruction has already been received and is being processed;

**P268** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

## Diagrams and exact supplied message definitions

- [Party deletion activity](../diagrams/party-reference-data/fig-0009.md)
- [Deletion confirmation sequence](../diagrams/party-reference-data/fig-0016.md)
- [Deletion rejection sequence](../diagrams/party-reference-data/fig-0017.md)

- [reda.031.001.01](../../../../messages/reda.031.001.01/index.md)
- [reda.016.001.01](../../../../messages/reda.016.001.01/index.md)

## Scope qualifications

The deletion table repeats update and block/unblock validation wording; deletion figures carry the caption Modification process. Literal wording remains visible under issue-000046. The source-defined deletion request does not become a modification request.

P87 supplies the publication-specific BAH context. No cancellation or reversal of these reference-data requests is established by these source flows.
