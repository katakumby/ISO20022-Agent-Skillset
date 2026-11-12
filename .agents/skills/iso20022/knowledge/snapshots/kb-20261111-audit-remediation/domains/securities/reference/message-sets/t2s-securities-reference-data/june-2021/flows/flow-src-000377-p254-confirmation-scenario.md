---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_sets: ["t2s-securities-reference-data"]
flow_id: "flow-src-000377-p254-confirmation-scenario"
title: "Confirmation Scenario"
source_locations: [{"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Deletion Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[254]", "paragraph_id": "P254", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Deletion Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[255]", "paragraph_id": "P255", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Deletion Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[256]", "paragraph_id": "P256", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Deletion Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[257]", "paragraph_id": "P257", "table_id": null}]
participants: ["participant-src-000377-executing-servicing-party", "participant-src-000377-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000377", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Securities Reference Data message "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[6]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000377", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Securities Reference Data message "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[7]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.013.001.01", "reda.030.001.01"]
message_families: ["reda.013", "reda.030"]
search_terms: ["Confirmation Scenario", "Executing/Servicing Party", "Instructing Party", "reda.013", "reda.030"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000377-executing-servicing-party", "participant-src-000377-instructing-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0016.md"]
---







# Confirmation Scenario

Source context: T2S SecuritiesReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing/Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000377-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000377-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P255** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing party

**P257** Security Deletion Request (reda.013)Deletion processSecurity Deletion Status Advice (reda.030): QUEUEDSecurity Deletion Status Advice (reda.030):  COMPLETEDSecurity Deletion Request (reda.013)Deletion processSecurity Deletion Status Advice (reda.030): QUEUEDSecurity Deletion Status Advice (reda.030):  COMPLETED

Source diagram evidence: [fig-0016](../documents/src-000377/diagrams/fig-0016.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `reda.013`, `reda.030`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000377](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Heading path: BusinessTransactions / Deletion Process / Confirmation Scenario.

<!-- SECREF-FIG-16-START -->
## Curated source-grounded flow

[Security deletion — confirmation](../diagrams/securities-reference/fig-0016.md)

| Picture step | Sender / responsible transmitter | Receiver | Source message |
| --- | --- | --- | --- |
| 1 | Instructing Party | Executing/Servicing Party | Security Deletion Request (reda.013) |
| 2 | Executing/Servicing Party | Instructing Party | Security Deletion Status Advice (reda.030): QUEUED |
| 3 | Executing/Servicing Party | Instructing Party | Security Deletion Status Advice (reda.030): COMPLETED |


### Source narrative, conditions and alternatives

**src-000377 P254** — Confirmation Scenario

**src-000377 P255** — Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing party

**src-000377 P258** — Security Deletion Request

**src-000377 P259** — The Instructing Party sends an instruction to the Executing/Servicing Party to delete a security. This instruction contains information that uniquely identifies the security and it is used when a security is no longer active.

**src-000377 P260** — Security Deletion Status Advice

**src-000377 P261** — The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**src-000377 P262** — Queued

**src-000377 P263** — The Executing/Servicing Party might inform the Instructing party that the processing of the Delete Security instruction has been delayed. In case of e.g. a night-time cycle is running.  

**src-000377 P264** — Completed

**src-000377 P265** — The Executing/Servicing Party informs the Instructing party that the Delete Securiy instruction has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the security that has been processed.

### Triggers, preconditions, postconditions and activity definitions

[Complete T10](../documents/src-000377/tables/tbl-0010.md)

| Item | Description |
| --- | --- |
| Definition | When an Instructing Party would like to delete a specific security already supported by the Executing/Servicing Party system, an Instructing Party asks the Executing/Servicing Party to delete the security in its system. |
| Trigger | The process is triggered when the Instructing Party sends a Security Deletion Request message. |
| Pre-conditions | The Instructing Party is known by the Executing/Servicing Party system and has been granted the appropriate privileges. The Instructing Party identified a gap in the Security’ coverage of the Executing/Servicing Party. The Instructing Party needs to remove this security at the Executing /Servicing Party. |
| Post-conditions | The acknowledgement of the processing of the deletion request. |
| Role | Instructing Party |


[Complete T16](../documents/src-000377/tables/tbl-0016.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Instruction | Instructing Party instructs the Executing/Servicing Party to delete a security. | Instructing Party |
| Validate | Executing/Servicing Party checks if the instruction already exists in the system.<br>It checks also if the security can or cannot be deleted.<br>If validation of the message fails, a status message “REJECTED” will be sent including the related errors and reason information.<br>If the message is valid and the time permits the deletion of the security (e.g. not during a night – time sequence), the data will be processed and a status message “COMPLETED” will be sent.<br>Otherwise a status message “QUEUED” will be sent and the instruction will be resubmit to validation after e.g. a night –time cycle. | Executing/Servicing Party |
| Process | If the instruction is accepted, the Executing/Servicing Party processes the instruction and informs the Instructing Party of the completeness of this instruction. | Executing/Servicing Party |
| Report | Executing/Servicing Party informs the Instructing Party that this instruction is rejected and why. | Executing/Servicing Party |
| Monitor Process | Instructing Party monitors the status of the instruction. | Instructing Party |


### Scoped participants and exact message references

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000377-instructing-party.md)
- [Executing/Servicing Party](../../../../../../../shared/reference/participants/participant-src-000377-executing-servicing-party.md)

| Canonical exact definition | Same-publication identifier evidence | Companion definition |
| --- | --- | --- |
| [reda.013.001.01](../../../../messages/reda.013.001.01/index.md) | src-000377 heading(s) P622 | src-000378 March2024 file page 115 |
| [reda.030.001.01](../../../../messages/reda.030.001.01/index.md) | src-000377 heading(s) P637, P644, P674, P709 | src-000378 March2024 file page 124 |



### Limits and source distinctions

- The dashed QUEUED advice is conditional in the narrative, for example a running night-time cycle; the picture does not make it compulsory.
- Source377 is June2021; companion source378 is March2024. Matching full identifiers do not erase the publication difference (issue-000010).
- The original figure is assembled from native Word connector/text objects and institutional pictograms. The retained full Word page is the complete composite; its pictograms alone are not counted as diagrams.
- Native Mermaid participant boxes replace the institutional drawings; sender and receiver roles, solid/dashed lines and visible arrow direction remain explicit. No institution is equated with a functional role.

<!-- SECREF-FIG-16-END -->
