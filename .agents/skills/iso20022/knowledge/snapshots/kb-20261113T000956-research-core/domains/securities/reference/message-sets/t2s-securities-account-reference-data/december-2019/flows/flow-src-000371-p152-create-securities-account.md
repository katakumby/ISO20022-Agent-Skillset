---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
flow_id: "flow-src-000371-p152-create-securities-account"
title: "Create a securities account"
source_locations: [{"source_id": "src-000371", "table_id": "T8", "xml_path": "/w:document/w:body/w:tbl[8]"}, {"source_id": "src-000371", "table_id": "T14", "xml_path": "/w:document/w:body/w:tbl[14]"}]
participants: ["participant-src-000371-executing-servicing-party", "participant-src-000371-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000371", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000371", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.018.001.01", "reda.020.001.01"]
message_families: ["reda.018", "reda.020"]
search_terms: ["Create Securities Account", "Executing/Servicing Party", "Instructing Party", "reda.018", "reda.023"]
limitations: ["Exact definitions independently confirmed in supplied Part2 src-000372; family labels in Part1 retained."]
manual_curated: true
participant_ids: ["participant-src-000371-account-owner", "participant-src-000371-account-owner-parent", "participant-src-000371-executing-servicing-party", "participant-src-000371-instructing-party"]
issue_ids: ["issue-000050"]
---

# Create a securities account

[src-000371](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`; [T8](../documents/src-000371/tables/tbl-0008.md) and [T14](../documents/src-000371/tables/tbl-0014.md).

## Purpose, trigger, preconditions and outcome

| Item | Description |
| --- | --- |
| Definition | When an Instructing Party would like to create a specific securities account that is not yet supported by the Executing/Servicing Party, an Instructing Party asks the Executing/Servicing Party to create the securities account in its system.  |
| Trigger | The process is triggered when the Instructing Party sends a Securities Account Creation Request message. |
| Pre-conditions | The Instructing Party is known by the Executing/Servicing Party system and has been granted the appropriate privileges. The Instructing Party identified a gap in the securities accounts’ coverage of the Executing/Servicing Party. The Instructing Party needs this securities account to be set-up at the Executing /Servicing Party to perform its activities. |
| Post-conditions | The acknowledgement of the processing of the creation request. |
| Role | Instructing Party |


## Participants and ordered activities

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000371-instructing-party.md)
- [Executing/Servicing Party](../../../../../../../shared/reference/participants/participant-src-000371-executing-servicing-party.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Instruction | Instructing Party instructs the Executing/Servicing Party to create a securities account. | Instructing Party |
| Validate | Executing/Servicing Party system checks if this instruction is a new occurrence or not. <br>It also checks if this instruction is already handled or not.<br>If validation of the message fails, a status message “REJECTED” will be sent including the related errors and reason information.<br>If the message is valid and the time permits the creation of the securities account (e.g. not during a night –time sequence), the data will be processed and a status message “COMPLETED” will be sent.<br>Otherwise, a status message “QUEUED” will be sent and the instruction will be resubmit to validation after e.g. a night –time cycle. | Executing/Servicing Party |
| Process | If the instruction is accepted, the Executing/Servicing Party processes the instruction and informs the Instructing Party of the completeness of this instruction. | Executing/Servicing Party |
| Report | Executing/Servicing Party informs the Instructing Party that this instruction is rejected and why. | Executing/Servicing Party |
| Monitor process | Instructing Party monitors the status of the instruction. | Instructing Party |


## Scenarios, alternatives and failures

**P177** Creation Process

**P178** Confirmation Scenario

**P179** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing Party.

**P182** Securities Account Creation Request

**P183** The Instructing Party sends the instruction to the Executing/Servicing Party to create a new securities account. This instruction contains information that clearly identify the securities account. 

**P184** Securities Account Status Advice

**P185** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P187** Queued
The Executing/Servicing Party might inform the Instructing party that the processing of Securities Account Creation Request has been delayed. In case of e.g. a night-time cycle is running.

**P189** Completed
The Executing/Servicing Party informs the Instructing party that the Securities Account Creation Request has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the Securities Account that has been processed.

**P190** Rejection Scenario

**P191** Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party.

**P193** Securities Account Creation Request

**P194** The Instructing Party sends the instruction to the Executing/Servicing Party to create a new securities account. This instruction contains information that clearly identify the securities account. 

**P195** Securities Account Status Advice

**P196** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P197** Rejected

**P198** The instruction did not pass validation, some reasons could be:

**P199** the mandatory information is not present or incorrect,

**P200** the instruction is not a new occurrence,

**P201** the instruction has already been received and is being processed. 

**P202** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

**P204** Queued
The Executing/Servicing Party might inform the Instructing party that the processing of the Create Securities Account instruction has been delayed. In case of e.g. a night-time cycle is running.

**P206** Rejected

**P207** After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P208** the mandatory information is not present or incorrect,

**P209** the instruction is not a new occurrence,

**P210** the instruction has already been received and is being processed 

**P211** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

## Diagrams and messages

- [Creation activity](../diagrams/securities-account-reference-data/fig-0007.md)
- [Creation confirmation sequence](../diagrams/securities-account-reference-data/fig-0012.md)
- [Creation rejection sequence](../diagrams/securities-account-reference-data/fig-0013.md)

- [reda.018.001.01](../../../../messages/reda.018.001.01/index.md)
- [reda.020.001.01](../../../../messages/reda.020.001.01/index.md)

## Scope

P85/P89 establishes BAH usage. The source does not define a cancellation or reversal request for these flows. Conditional queuing is not made mandatory. T18 explicitly excludes the optional statement instruction from message scope; T12 requires a standing instruction and P326 makes delivery unsolicited.

<!-- DATA-ROLE-account-owner -->
[Account owner](../../../../../../../shared/reference/participants/participant-src-000371-account-owner.md) appears in the narrative/reference data; no extra actor lane or message direction is inferred.

<!-- DATA-ROLE-account-owner-parent -->
[Account owner Parent](../../../../../../../shared/reference/participants/participant-src-000371-account-owner-parent.md) appears in the narrative/reference data; no extra actor lane or message direction is inferred.
