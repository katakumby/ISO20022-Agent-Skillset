---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_sets: ["t2s-securities-reference-data"]
flow_id: "flow-src-000377-p165-statement-process"
title: "Statement Process"
source_locations: [{"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Statement Process"], "locator": "/w:document/w:body/w:p[165]", "paragraph_id": "P165", "table_id": null}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Statement Process"], "locator": "/w:document/w:body/w:p[166]", "paragraph_id": "P166", "table_id": null}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Statement Process"], "locator": "/w:document/w:body/w:tbl[18]", "paragraph_id": null, "table_id": "T18"}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Statement Process"], "locator": "/w:document/w:body/w:p[167]", "paragraph_id": "P167", "table_id": null}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Statement Process"], "locator": "/w:document/w:body/w:p[168]", "paragraph_id": "P168", "table_id": null}]
participants: ["participant-src-000377-executing-servicing-party", "participant-src-000377-instructing-party"]
message_mapping_evidence: []
message_ids: ["reda.009.001.01"]
message_families: []
search_terms: ["Statement Process", "Executing/Servicing Party", "Instructing Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000377-executing-party", "participant-src-000377-executing-servicing-party", "participant-src-000377-instructing-party", "participant-src-000377-recipient-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0011.md"]
---







# Statement Process

Source context: T2S SecuritiesReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing/Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000377-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000377-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0011](../documents/src-000377/diagrams/fig-0011.md). Mermaid reconstruction and visual review are pending.

Source table [T18](../documents/src-000377/tables/tbl-0018.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Instruction | Instructing Party might instruct Executing/Servicing Party to run a statement.<br>This is not covered by the current process as NO message will be created to cover this. | Instructing Party |
| Process statement | Executing/Servicing Party processes the statement. | Executing/Servicing Party |
| Response | Executing/Servicing Party sends the statement to the Instructing Party. | Executing/Servicing Party |
| Monitor Process | Instructing Party monitors the status of the instruction. | Instructing Party |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000377](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Heading path: Description of BusinessActivities / Statement Process.

<!-- SECREF-FIG-11-START -->
## Curated source-grounded flow

[Security activity statement production](../diagrams/securities-reference/fig-0011.md)

### Source narrative, conditions and alternatives

**src-000377 P165** — Statement Process

### Triggers, preconditions, postconditions and activity definitions

[Complete T12](../documents/src-000377/tables/tbl-0012.md)

| Item | Description |
| --- | --- |
| Definition | The Recipient Party receives a Security Activity Advice statement which has been automatically produced by the Executing/Servicing Party. |
| Trigger | The process is triggered automatically. |
| Pre-conditions | A standing instruction is in place at the Executing/Servicing Party for sending of the statement. |
| Post-conditions | The acknowledgement of the sending of the statement. |
| Role | Executing/Servicing Party |


[Complete T18](../documents/src-000377/tables/tbl-0018.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Instruction | Instructing Party might instruct Executing/Servicing Party to run a statement.<br>This is not covered by the current process as NO message will be created to cover this. | Instructing Party |
| Process statement | Executing/Servicing Party processes the statement. | Executing/Servicing Party |
| Response | Executing/Servicing Party sends the statement to the Instructing Party. | Executing/Servicing Party |
| Monitor Process | Instructing Party monitors the status of the instruction. | Instructing Party |


### Scoped participants and exact message references

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000377-instructing-party.md)
- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000377-executing-party.md)
- [Executing/Servicing Party](../../../../../../../shared/reference/participants/participant-src-000377-executing-servicing-party.md)
- [Recipient Party](../../../../../../../shared/reference/participants/participant-src-000377-recipient-party.md)

| Canonical exact definition | Same-publication identifier evidence | Companion definition |
| --- | --- | --- |
| [reda.009.001.01](../../../../messages/reda.009.001.01/index.md) | src-000377 heading(s) P859 | src-000378 March2024 file page 71 |



### Limits and source distinctions

- No start/end glyph or error decision is supplied in this activity picture. The linked table/narrative preserves additional error conditions without adding unseen diagram nodes.
- T18 explicitly says the initial instruction is outside this process and no message is created for it. P315–P316 describe the statement as unilateral and unsolicited; no request message is inferred from the conceptual Instruction arrow.
- T12 calls the recipient Recipient Party; the picture and transaction narrative call it Instructing Party. These source-scoped roles are linked without asserting global equivalence.
- Source377 is June2021; companion source378 is March2024. Matching full identifiers do not erase the publication difference (issue-000010).

<!-- SECREF-FIG-11-END -->
