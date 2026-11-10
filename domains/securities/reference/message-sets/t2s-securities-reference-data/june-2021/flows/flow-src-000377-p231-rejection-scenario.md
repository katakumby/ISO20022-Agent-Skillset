---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_sets: ["t2s-securities-reference-data"]
flow_id: "flow-src-000377-p231-rejection-scenario"
title: "Rejection Scenario"
source_locations: [{"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[231]", "paragraph_id": "P231", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[232]", "paragraph_id": "P232", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[233]", "paragraph_id": "P233", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[234]", "paragraph_id": "P234", "table_id": null}]
participants: ["participant-src-000377-executing-servicing-party", "participant-src-000377-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000377", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Securities Reference Data message "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000377", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Securities Reference Data message "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.007.001.01", "reda.029.001.01"]
message_families: ["reda.007", "reda.029"]
search_terms: ["Rejection Scenario", "Executing/Servicing Party", "Instructing Party", "reda.007", "reda.029"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000377-executing-servicing-party", "participant-src-000377-instructing-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0015.md"]
---







# Rejection Scenario

Source context: T2S SecuritiesReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing/Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000377-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000377-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P232** Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party

**P234** Security Maintenance Request (reda.007)Modification processSecurity Maintenance Status Advice (reda.029): QUEUEDSecurity Maintenance Status Advice (reda.029): REJECTEDSecurity Maintenance Request (reda.007)Modification processSecurity Maintenance Status Advice (reda.029): QUEUEDSecurity Maintenance Status Advice (reda.029): REJECTED

Source diagram evidence: [fig-0015](../documents/src-000377/diagrams/fig-0015.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `reda.007`, `reda.029`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000377](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Heading path: BusinessTransactions / Modification Process / Rejection Scenario.

<!-- SECREF-FIG-15-START -->
## Curated source-grounded flow

[Security maintenance — rejection](../diagrams/securities-reference/fig-0015.md)

| Picture step | Sender / responsible transmitter | Receiver | Source message |
| --- | --- | --- | --- |
| 1 | Instructing Party | Executing/Servicing Party | Security Maintenance Request (reda.007) |
| 2 | Executing/Servicing Party | Instructing Party | Security Maintenance Status Advice (reda.029): QUEUED |
| 3 | Executing/Servicing Party | Instructing Party | Security Maintenance Status Advice (reda.029): REJECTED |


### Source narrative, conditions and alternatives

**src-000377 P231** — Rejection Scenario

**src-000377 P232** — Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party

**src-000377 P235** — Security Maintenance Request

**src-000377 P236** — The Instructing Party sends an instruction to the Executing/Servicing Party to modify reference data for a Security. 

**src-000377 P237** — Security Maintenance Status Advice

**src-000377 P238** — The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**src-000377 P239** — Rejected

**src-000377 P240** — The instruction did not pass validation, some reasons could be:

**src-000377 P241** — the mandatory information is not present or incorrect,

**src-000377 P242** — the data cannot be updated,

**src-000377 P243** — the instruction has already been received and is being processed. 

**src-000377 P244** — This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

**src-000377 P245** — Queued

**src-000377 P246** — The Executing/Servicing Party might inform the Instructing party that the processing of the Modify Security instruction has been delayed. In case of e.g. a night-time cycle is running.  

**src-000377 P247** — Rejected

**src-000377 P248** — After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**src-000377 P249** — the mandatory information is not present or incorrect,

**src-000377 P250** — the data cannot be updated,

**src-000377 P251** — the instruction has already been received and is being processed. 

**src-000377 P252** — This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

### Triggers, preconditions, postconditions and activity definitions

[Complete T9](../documents/src-000377/tables/tbl-0009.md)

| Item | Description |
| --- | --- |
| Definition | When an Instructing Party is in charge of the modification of a specific security already supported by the Executing/Servicing Party system, the Instructing Party asks the Executing/Servicing Party to modify a security in the Executing/Servicing Party system. |
| Trigger | The process is triggered when the Instructing Party sends a Security Maintenance Request message. |
| Pre-conditions | The Instructing Party is known by the Executing/Servicing Party system and has been granted the appropriate privileges. An attribute of the security has changed which requires a modification of the security in the Executing/Servicing Party system. |
| Post-conditions | The acknowledgement of the processing of the maintenance request. |
| Role | Instructing Party |


[Complete T15](../documents/src-000377/tables/tbl-0015.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Instruction | Instructing Party instructs the Executing/Servicing Party to modify a security. | Instructing Party |
| Validate | Executing/Servicing Party checks if the instruction already exists in the system.<br>It checks also if the data can or cannot be updated.<br>If validation of the message fails, a status message “REJECTED” will be sent including the related errors and reason information.<br>If the message is valid and the time permits the update of the security (e.g. not during a night – time sequence), the data will be processed and a status message “COMPLETED” will be sent.<br>Otherwise a status message “QUEUED” will be sent and the instruction will be resubmit to validation after e.g. a night –time cycle. | Executing/Servicing Party |
| Process | If the instruction is accepted, the Executing/Servicing Party processes the instruction and informs the Instructing Party of the completeness of this instruction. | Executing/Servicing Party |
| Report | Executing/Servicing Party informs the Instructing Party that this instruction is rejected and why. | Executing/Servicing Party |
| Monitor Process | Instructing Party monitors the status of the instruction. | Instructing Party |


### Scoped participants and exact message references

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000377-instructing-party.md)
- [Executing/Servicing Party](../../../../../../../shared/reference/participants/participant-src-000377-executing-servicing-party.md)

| Canonical exact definition | Same-publication identifier evidence | Companion definition |
| --- | --- | --- |
| [reda.007.001.01](../../../../messages/reda.007.001.01/index.md) | src-000377 heading(s) P489 | src-000378 March2024 file page 21 |
| [reda.029.001.01](../../../../messages/reda.029.001.01/index.md) | src-000377 heading(s) P516, P523, P553, P588 | src-000378 March2024 file page 119 |



### Limits and source distinctions

- The source shows QUEUED with a dashed connector; narrative says this status might be sent when processing is delayed, for example during a night-time cycle. The picture does not make queuing compulsory.
- The narrative covers immediate validation rejection and re-validation after queuing, including multiple reasons, beyond the three pictured arrows. No second mandatory rejection is inferred.
- Source377 is June2021; companion source378 is March2024. Matching full identifiers do not erase the publication difference (issue-000010).
- The original figure is assembled from native Word connector/text objects and institutional pictograms. The retained full Word page is the complete composite; its pictograms alone are not counted as diagrams.
- Native Mermaid participant boxes replace the institutional drawings; sender and receiver roles, solid/dashed lines and visible arrow direction remain explicit. No institution is equated with a functional role.

<!-- SECREF-FIG-15-END -->
