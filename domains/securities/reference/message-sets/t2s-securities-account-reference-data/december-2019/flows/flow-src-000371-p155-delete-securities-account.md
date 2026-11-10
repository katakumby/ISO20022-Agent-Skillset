---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
flow_id: "flow-src-000371-p155-delete-securities-account"
title: "Delete a securities account"
source_locations: [{"source_id": "src-000371", "table_id": "T10", "xml_path": "/w:document/w:body/w:tbl[10]"}, {"source_id": "src-000371", "table_id": "T16", "xml_path": "/w:document/w:body/w:tbl[16]"}]
participants: ["participant-src-000371-executing-servicing-party", "participant-src-000371-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000371", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.032.001.01", "reda.020.001.01"]
message_families: ["reda.032", "reda.020"]
search_terms: ["Delete Securities Account", "Executing/Servicing Party", "Instructing Party", "reda.032"]
limitations: ["Exact definitions independently confirmed in supplied Part2 src-000372; family labels in Part1 retained."]
manual_curated: true
participant_ids: ["participant-src-000371-instructing-party", "participant-src-000371-executing-servicing-party"]
issue_ids: ["issue-000050"]
---

# Delete a securities account

[src-000371](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`; [T10](../documents/src-000371/tables/tbl-0010.md) and [T16](../documents/src-000371/tables/tbl-0016.md).

## Purpose, trigger, preconditions and outcome

| Item | Description |
| --- | --- |
| Definition | When an Instructing Party would like to delete a specific securities account already supported by the Executing/Servicing Party system, an Instructing Party asks the Executing/Servicing Party to delete the securities account in its system. |
| Trigger | The process is triggered when the Instructing Party sends a Securities Account Deletion Request message. |
| Pre-conditions | The Instructing Party is known by the Executing/Servicing Party system and has been granted the appropriate privileges. The Instructing Party identified a gap in the Securities Accounts’ coverage of the Executing/Servicing Party. The Instructing Party needs to remove this securities account at the Executing /Servicing Party. |
| Post-conditions | The acknowledgement of the processing of the deletion request. |
| Role | Instructing Party |


## Participants and ordered activities

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000371-instructing-party.md)
- [Executing/Servicing Party](../../../../../../../shared/reference/participants/participant-src-000371-executing-servicing-party.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Instruction | Instructing Party instructs the Executing/Servicing Party to delete a securities account. | Instructing Party |
| Validate | Executing/Servicing Party checks if the instruction already exists in the system.<br>It checks also if the securities account can or cannot be deleted.<br>If validation of the message fails, a status message “REJECTED” will be sent including the related errors and reason information.<br>If the message is valid and the time permits the deletion of the securities account (e.g. not during a night –time sequence), the data will be processed and a status message “COMPLETED” will be sent.<br>Otherwise a status message “QUEUED” will be sent and the instruction will be resubmit to validation after e.g. a night –time cycle. | Executing/Servicing Party |
| Process | If the instruction is accepted, the Executing/Servicing Party processes the instruction and informs the Instructing Party of the completeness of this instruction. | Executing/Servicing Party |
| Report | Executing/Servicing Party informs the Instructing Party that this instruction is rejected and why. | Executing/Servicing Party |
| Monitor process | Monitor process: Instructing Party monitors the status of the instruction. | Instructing Party |


## Scenarios, alternatives and failures

**P258** Deletion Process

**P259** Confirmation Scenario

**P260** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing party

**P263** Securities Account Deletion Request

**P264** The Instruction Party sends an instruction to the Executing/Servicing Party to delete a securities account. This instruction contains information that uniquely identifies the party and it is used when a party is no longer active.

**P265** Securities Account Status Advice

**P266** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P268** Queued:

**P269** The Executing/Servicing Party might inform the Instructing party that the processing of the Delete Securities Account instruction has been delayed. In case of e.g. a night-time cycle is running.

**P271** Completed:

**P272** The Executing/Servicing Party informs the Instructing party that the Delete Securities Account instruction has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the securities account that has been processed.

**P274** Rejection Scenario

**P275** Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party

**P277** Securities Account Deletion Request

**P278** The Instruction Party sends an instruction to the Executing/Servicing Party to delete a securities account. 

**P279** Securities Account Status Advice

**P280** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P282** Rejected

**P283** The instruction did not pass validation, some reasons could be:

**P284** the mandatory information is not present or incorrect,

**P285** the Instructing Party does not have the right to delete securities account,

**P286** the instruction has already been received and is being processed. 

**P287** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

**P289** Queued

**P290** The Executing/Servicing Party might inform the Instructing party that the processing of the Delete Securities Account instruction has been delayed. In case of e.g. a night-time cycle is running.

**P292** Rejected

**P293** After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P294** the mandatory information is not present or incorrect,

**P295** the securities account cannot be deleted,

**P296** the Instructing Party does not have the right to delete securities account,

**P297** the instruction has already been received and is being processed 

**P298** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

## Diagrams and messages

- [Deletion activity](../diagrams/securities-account-reference-data/fig-0009.md)
- [Deletion confirmation sequence](../diagrams/securities-account-reference-data/fig-0016.md)
- [Deletion rejection sequence](../diagrams/securities-account-reference-data/fig-0017.md)

- [reda.032.001.01](../../../../messages/reda.032.001.01/index.md)
- [reda.020.001.01](../../../../messages/reda.020.001.01/index.md)

## Scope

P85/P89 establishes BAH usage. The source does not define a cancellation or reversal request for these flows. Conditional queuing is not made mandatory. T18 explicitly excludes the optional statement instruction from message scope; T12 requires a standing instruction and P326 makes delivery unsolicited.

P264 refers to identifying a party that is no longer active inside this account-deletion scenario. This copied-looking wording remains source evidence under issue-000050; it is not silently promoted to an account-deletion precondition.
