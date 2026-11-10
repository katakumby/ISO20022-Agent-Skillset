---
flow_id: "flow-src-000371-p154-modify-a-securities-account"
template: false
document_kind: "business-flow"
review_status: "needs-review"
manual_curated: true
title: "Modify a securities account"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
participant_ids: ["participant-src-000371-instructing-party", "participant-src-000371-executing-servicing-party"]
message_ids: ["reda.023.001.01", "reda.020.001.01"]
message_families: ["reda.023", "reda.020"]
source_locations: [{"source_id": "src-000371", "table_id": "T9", "xml_path": "/w:document/w:body/w:tbl[9]"}, {"source_id": "src-000371", "table_id": "T15", "xml_path": "/w:document/w:body/w:tbl[15]"}]
issue_ids: ["issue-000050"]
limitations: ["Exact definitions independently confirmed in supplied Part2 src-000372; family labels in Part1 retained."]
---

# Modify a securities account

[src-000371](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`; [T9](../documents/src-000371/tables/tbl-0009.md) and [T15](../documents/src-000371/tables/tbl-0015.md).

## Purpose, trigger, preconditions and outcome

| Item | Description |
| --- | --- |
| Definition | When an Instructing Party is in charge of the modification of a specific securities account already supported by the Executing/Servicing Party system, the Instructing Party asks the Executing/Servicing Party to modify a securities account in the Executing/Servicing Party system. |
| Trigger | The process is triggered when the Instructing Party sends a Securities Account Modification Request message. |
| Pre-conditions | The Instructing Party is known by the Executing/Servicing Party system and has been granted the appropriate privileges. An attribute of the securities account has changed which requires a modification of the securities account in the Executing/Servicing Party system. |
| Post-conditions | The acknowledgement of the processing of the modification request. |
| Role | Instructing Party |


## Participants and ordered activities

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000371-instructing-party.md)
- [Executing/Servicing Party](../../../../../../../shared/reference/participants/participant-src-000371-executing-servicing-party.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Instruction | Instructing Party instructs the Executing/Servicing Party to modify a securities account. | Instructing Party |
| Validate | Executing/Servicing Party checks if the instruction already exists in the system.<br>It checks also if the data can or cannot be updated.<br>If validation of the message fails, a status message “REJECTED” will be sent including the related errors and reason information.<br>If the message is valid and the time permits the update of the securities account (e.g. not during a night –time sequence), the data will be processed and a status message “COMPLETED” will be sent.<br>Otherwise a status message “QUEUED” will be sent and the instruction will be resubmit to validation after e.g. a night –time cycle. | Executing/Servicing Party |
| Process | If the instruction is accepted, Executing/Servicing Party processes the instruction and informs the Instructing Party of the completeness of this instruction. | Executing/Servicing Party |
| Report | Executing/Servicing Party informs the Instructing Party that this instruction is rejected and why. | Executing/Servicing Party |
| Monitor process | Instructing Party monitors the status of the instruction. | Instructing Party |


## Scenarios, alternatives and failures

**P216** Modification Process

**P217** Confirmation Scenario

**P218** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing party

**P221** Securities Account Maintenance Request

**P222** The Instruction Party sends an instruction to the Executing/Servicing Party to modify data for a securities account. This instruction contains information that uniquely identify the securities account. 

**P223** In this case, this instruction contains details of the restriction like the restriction type and timeframe.

**P224** Securities Account Status Advice

**P225** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P227** Queued

**P228** The Executing/Servicing Party might inform the Instructing party that the processing of the Modify Securities Account instruction has been delayed. In case of e.g. a night-time cycle is running

**P230** Completed

**P231** The Executing/Servicing Party informs the Instructing party that the Modify Securities Account instruction has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the securities account that has been processed.

**P232** Rejection Scenario

**P233** Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party.

**P236** Securities Account Maintenance Request

**P237** The Instruction Party sends an instruction to the Executing/Servicing Party to modify reference data for a securities account. 

**P238** Securities Account Status Advice

**P239** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P241** Rejected

**P242** The instruction did not pass validation, some reasons could be:

**P243** the mandatory information is not present or incorrect,

**P244** the data cannot be updated,

**P245** the instruction has already been received and is being processed 

**P246** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status

**P247** .

**P248** Queued

**P249** The Executing/Servicing Party might inform the Instructing party that the processing of the Modify Securities Account instruction has been delayed. In case of e.g. a night-time cycle is running.

**P251** Rejected

**P252** After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P253** the mandatory information is not present or incorrect,

**P254** the data cannot be updated,

**P255** the Instructing Party does not have the right to block/unblock security account,

**P256** the instruction has already been received and is being processed. 

**P257** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

## Diagrams and messages

- [Modification activity](../diagrams/securities-account-reference-data/fig-0008.md)
- [Modification confirmation sequence](../diagrams/securities-account-reference-data/fig-0014.md)
- [Modification rejection sequence](../diagrams/securities-account-reference-data/fig-0015.md)

- [reda.023.001.01](../../../../messages/reda.023.001.01/index.md)
- [reda.020.001.01](../../../../messages/reda.020.001.01/index.md)

## Scope

P85/P89 establishes BAH usage. The source does not define a cancellation or reversal request for these flows. Conditional queuing is not made mandatory. T18 explicitly excludes the optional statement instruction from message scope; T12 requires a standing instruction and P326 makes delivery unsolicited.

P221/P236 calls the request Maintenance Request while exact metadata/figure names Modification Request. P223 restriction-type/timeframe wording and P255 block/unblock rights remain local source claims under issue-000050.
