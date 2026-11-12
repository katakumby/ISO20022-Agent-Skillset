---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_sets: ["t2s-securities-reference-data"]
flow_id: "flow-src-000377-p156-modification-process"
title: "Modification Process"
source_locations: [{"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Modification Process"], "locator": "/w:document/w:body/w:p[156]", "paragraph_id": "P156", "table_id": null}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Modification Process"], "locator": "/w:document/w:body/w:p[157]", "paragraph_id": "P157", "table_id": null}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Modification Process"], "locator": "/w:document/w:body/w:tbl[15]", "paragraph_id": null, "table_id": "T15"}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Modification Process"], "locator": "/w:document/w:body/w:p[158]", "paragraph_id": "P158", "table_id": null}]
participants: ["participant-src-000377-executing-servicing-party", "participant-src-000377-instructing-party"]
message_mapping_evidence: []
message_ids: ["reda.007.001.01", "reda.029.001.01"]
message_families: []
search_terms: ["Modification Process", "Executing/Servicing Party", "Instructing Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000377-executing-party", "participant-src-000377-executing-servicing-party", "participant-src-000377-instructing-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0008.md"]
---







# Modification Process

Source context: T2S SecuritiesReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing/Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000377-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000377-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0008](../documents/src-000377/diagrams/fig-0008.md). Mermaid reconstruction and visual review are pending.

Source table [T15](../documents/src-000377/tables/tbl-0015.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Instruction | Instructing Party instructs the Executing/Servicing Party to modify a security. | Instructing Party |
| Validate | Executing/Servicing Party checks if the instruction already exists in the system.<br>It checks also if the data can or cannot be updated.<br>If validation of the message fails, a status message “REJECTED” will be sent including the related errors and reason information.<br>If the message is valid and the time permits the update of the security (e.g. not during a night – time sequence), the data will be processed and a status message “COMPLETED” will be sent.<br>Otherwise a status message “QUEUED” will be sent and the instruction will be resubmit to validation after e.g. a night –time cycle. | Executing/Servicing Party |
| Process | If the instruction is accepted, the Executing/Servicing Party processes the instruction and informs the Instructing Party of the completeness of this instruction. | Executing/Servicing Party |
| Report | Executing/Servicing Party informs the Instructing Party that this instruction is rejected and why. | Executing/Servicing Party |
| Monitor Process | Instructing Party monitors the status of the instruction. | Instructing Party |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000377](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Heading path: Description of BusinessActivities / Modification Process.

<!-- SECREF-FIG-8-START -->
## Curated source-grounded flow

[Security modification activity](../diagrams/securities-reference/fig-0008.md)

### Source narrative, conditions and alternatives

**src-000377 P156** — Modification Process

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
- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000377-executing-party.md)
- [Executing/Servicing Party](../../../../../../../shared/reference/participants/participant-src-000377-executing-servicing-party.md)

| Canonical exact definition | Same-publication identifier evidence | Companion definition |
| --- | --- | --- |
| [reda.007.001.01](../../../../messages/reda.007.001.01/index.md) | src-000377 heading(s) P489 | src-000378 March2024 file page 21 |
| [reda.029.001.01](../../../../messages/reda.029.001.01/index.md) | src-000377 heading(s) P516, P523, P553, P588 | src-000378 March2024 file page 119 |



### Limits and source distinctions

- The source artwork uses Accepted/Rejected activity labels. The activity table and transaction messages distinguish COMPLETED, QUEUED and REJECTED. No equality of these separate status vocabularies is inferred.
- Source edge labels are literally Status <<Accepted>> and Status <<Rejected>>. Mermaid uses typographic double-angle guillemets around the unchanged values because ASCII angle groups are stripped as HTML by this renderer.
- The final No branch is dashed and returns to Instruction; the source does not supply a retry deadline or retry count. The blank diamond merges the accepted/rejected reporting paths without an added condition.
- Executing Party is the literal swimlane label; corresponding table rows use Executing/Servicing Party. Scoped records retain that explicit contextual relationship.
- Source377 is June2021; companion source378 is March2024. Matching full identifiers do not erase the publication difference (issue-000010).

<!-- SECREF-FIG-8-END -->
