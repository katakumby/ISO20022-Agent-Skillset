---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_sets: ["t2s-securities-reference-data"]
flow_id: "flow-src-000377-p172-confirmation-scenario"
title: "Confirmation Scenario"
source_locations: [{"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Creation Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[172]", "paragraph_id": "P172", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Creation Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[173]", "paragraph_id": "P173", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Creation Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[174]", "paragraph_id": "P174", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Creation Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[175]", "paragraph_id": "P175", "table_id": null}]
participants: ["participant-src-000377-executing-servicing-party", "participant-src-000377-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000377", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Securities Reference Data message "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000377", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Securities Reference Data message "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.006.001.01", "reda.008.001.01"]
message_families: ["reda.006", "reda.008"]
search_terms: ["Confirmation Scenario", "Executing/Servicing Party", "Instructing Party", "reda.006", "reda.008"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000377-executing-servicing-party", "participant-src-000377-instructing-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0012.md"]
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

**P173** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing Party.

**P175** Creation ProcessSecurity Creation Status Advice (reda.008): QUEUEDSecurity Creation Status Advice (reda.008): COMPLETEDCOMPLETEDSecurity Creation Request (reda.006)Creation ProcessSecurity Creation Status Advice (reda.008): QUEUEDSecurity Creation Status Advice (reda.008): COMPLETEDCOMPLETEDSecurity Creation Request (reda.006)

Source diagram evidence: [fig-0012](../documents/src-000377/diagrams/fig-0012.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `reda.006`, `reda.008`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000377](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Heading path: BusinessTransactions / Creation Process / Confirmation Scenario.

<!-- SECREF-FIG-12-START -->
## Curated source-grounded flow

[Security creation — confirmation](../diagrams/securities-reference/fig-0012.md)

| Picture step | Sender / responsible transmitter | Receiver | Source message |
| --- | --- | --- | --- |
| 1 | Instructing Party | Executing/Servicing Party | Security Creation Request (reda.006) |
| 2 | Executing/Servicing Party | Instructing Party | Security Creation Status Advice (reda.008): QUEUED |
| 3 | Executing/Servicing Party | Instructing Party | Security Creation Status Advice (reda.008): COMPLETED |


### Source narrative, conditions and alternatives

**src-000377 P172** — Confirmation Scenario

**src-000377 P173** — Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing Party.

**src-000377 P176** — Security Creation Request

**src-000377 P177** — The Instructing Party sends the instruction to the Executing/Servicing Party to create a new security. This instruction contains information that clearly identify the security. 

**src-000377 P178** — Security Creation Status Advice

**src-000377 P179** — The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**src-000377 P180** — Queued

**src-000377 P181** — The Executing/Servicing Party might inform the Instructing party that the processing of Security Creation Request has been delayed. In case of e.g. a night-time cycle is running.  

**src-000377 P182** — Completed

**src-000377 P183** — The Executing/Servicing Party informs the Instructing party that the Security Creation Request has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the Security that has been processed.

### Triggers, preconditions, postconditions and activity definitions

[Complete T8](../documents/src-000377/tables/tbl-0008.md)

| Item | Description |
| --- | --- |
| Definition | When an Instructing Party would like to create a specific security that is not yet supported by the Executing/Servicing Party, an Instructing Party asks the Executing/Servicing Party to create the security in its system. |
| Trigger | The process is triggered when the Instructing Party sends a Security Creation Request message. |
| Pre-conditions | The Instructing Party is known by the Executing/Servicing Party system and has been granted the appropriate privileges. The Instructing Party identified a gap in the securities’ coverage of the Executing/Servicing Party. The Instructing Party needs this security to be set-up at the Executing /Servicing Party to perform its activities. |
| Post-conditions | The acknowledgement of the processing of the creation request. |
| Role | Instructing Party |


[Complete T14](../documents/src-000377/tables/tbl-0014.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Instruction | Instructing Party instructs the Executing/Servicing Party to create a security. | Instructing Party |
| Validate | Executing/Servicing Party system checks if this instruction is a new occurrence or not. <br>It also checks if this instruction is already handled or not.<br>If validation of the message fails, a status message “REJECTED” will be sent including the related errors and reason information.<br>If the message is valid and the time permits the creation of the security (e.g. not during a night – time sequence), the data will be processed and a status message “COMPLETED” will be sent.<br>Otherwise a status message “QUEUED” will be sent and the instruction will be resubmit to validation after e.g. a night –time cycle. | Executing/Servicing Party |
| Process | If the instruction is accepted, the Executing/Servicing Party processes the instruction and informs the Instructing Party of the completeness of this instruction. | Executing/Servicing Party |
| Report | Executing/Servicing Party informs the Instructing Party that this instruction is rejected and why. | Executing/Servicing Party |
| Monitor Process | Instructing Party monitors the status of the instruction. | Instructing Party |


### Scoped participants and exact message references

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000377-instructing-party.md)
- [Executing/Servicing Party](../../../../../../../shared/reference/participants/participant-src-000377-executing-servicing-party.md)

| Canonical exact definition | Same-publication identifier evidence | Companion definition |
| --- | --- | --- |
| [reda.006.001.01](../../../../messages/reda.006.001.01/index.md) | src-000377 heading(s) P320 | src-000378 March2024 file page 8 |
| [reda.008.001.01](../../../../messages/reda.008.001.01/index.md) | src-000377 heading(s) P384, P391, P420, P455 | src-000378 March2024 file page 66 |



### Limits and source distinctions

- The dashed QUEUED advice is conditional in the narrative, for example a running night-time cycle; the picture does not make it compulsory.
- Source377 is June2021; companion source378 is March2024. Matching full identifiers do not erase the publication difference (issue-000010).
- The original figure is assembled from native Word connector/text objects and institutional pictograms. The retained full Word page is the complete composite; its pictograms alone are not counted as diagrams.
- Native Mermaid participant boxes replace the institutional drawings; sender and receiver roles, solid/dashed lines and visible arrow direction remain explicit. No institution is equated with a functional role.

<!-- SECREF-FIG-12-END -->
