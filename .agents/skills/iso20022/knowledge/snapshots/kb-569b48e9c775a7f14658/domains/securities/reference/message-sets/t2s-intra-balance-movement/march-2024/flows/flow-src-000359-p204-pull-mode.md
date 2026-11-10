---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p204-pull-mode"
title: "Pull Mode"
source_locations: [{"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Modification/Cancellation Query/Report Process", "Pull Mode"], "locator": "/w:document/w:body/w:p[204]", "paragraph_id": "P204", "table_id": null}, {"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Modification/Cancellation Query/Report Process", "Pull Mode"], "locator": "/w:document/w:body/w:p[205]", "paragraph_id": "P205", "table_id": null}, {"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Modification/Cancellation Query/Report Process", "Pull Mode"], "locator": "/w:document/w:body/w:p[206]", "paragraph_id": "P206", "table_id": null}, {"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Modification/Cancellation Query/Report Process", "Pull Mode"], "locator": "/w:document/w:body/w:tbl[24]", "paragraph_id": null, "table_id": "T24"}, {"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Modification/Cancellation Query/Report Process", "Pull Mode"], "locator": "/w:document/w:body/w:p[207]", "paragraph_id": "P207", "table_id": null}]
participants: ["participant-src-000359-servicing-executing-party", "participant-src-000359-instructing-party"]
message_mapping_evidence: []
message_ids: ["camt.080.001.02", "camt.081.001.02", "camt.082.001.02", "camt.083.001.02"]
message_families: []
search_terms: ["Pull Mode", "Servicing/Executing Party", "Instructing Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000359-account-owner", "participant-src-000359-instructing-party", "participant-src-000359-servicing-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0014.md"]
---



# Pull Mode

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Servicing/Executing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0014](../documents/src-000359/diagrams/fig-0014.md). Mermaid reconstruction and visual review are pending.

Source table [T24](../documents/src-000359/tables/tbl-0024.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Send Intra-Balance Movement Cancellation/Modification Query | Request Query to Servicing Party under a selected criterion. | Instructing Party |
| Validate Request | Technical and business validation of the request before further processing or not. | Servicing/Executing Party |
| Generate Report | Build a report for Intra Balance Movement Cancellation/Modification Instructions satisfying a previously selected criterion. | Servicing/Executing Party |
| Successful Process  | If YES, the report is properly generated then go to the Send Intra Balance Movement Cancellation/Modification Report process. <br>If NO; then Error Processing to advise the Instructing Party.  | Servicing/Executing Party |
| Send Intra Balance Movement Cancellation/Modification Report | Route Report to Instructing Party under a selected criterion. | Servicing/Executing Party |
| Error Processing | Adds operational errors to response before routing to Instructing Party | Servicing/Executing Party |
| Monitor | Monitor: Check for incoming communications (Intra Balance Movement Cancellation/Modification Report). | Instructing Party |
| Reconcile | Reconcile: External process reconciling impact of current status of original instruction. | Instructing Party |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: Description of BusinessActivities / Intra-Balance Movement Modification/Cancellation Query/Report Process / Pull Mode.

<!-- INTRABALANCE-FIG-14-START -->
## Curated scenario and source responsibilities

[Pull modification and cancellation reporting activity — source diagram and directions](../diagrams/intrabalance/fig-0014.md)

### Narrative conditions, actions and outcomes

**src-000359 P204** — Pull Mode

### Source-defined triggers, preconditions, postconditions and activity responsibilities

[Complete T16 with exact source rows](../documents/src-000359/tables/tbl-0016.md)

| Source item | Source definition |
| --- | --- |
| Definition | The Instructing Party asks the Servicing Party a response to a query concerning a previously sent intra-balance movement cancellation instruction/modification. |
| Trigger | The process is triggered either by the system at the end-of-date event or by the receipt of a query request.  |
| Pre-conditions | Existence of an intra-balance cancellation instruction/modification. |
| Post-conditions | The acknowledgement of the processing of the query and the generation of a valid intra-balance movement cancellation/modification report. |
| Role | Account owner (Instructing Party) for the Query.<br>Executing/Servicing Party for the Report. |


[Complete T24 with exact source rows](../documents/src-000359/tables/tbl-0024.md)

| Source step | Description / conditions | Initiator / responsible role |
| --- | --- | --- |
| Send Intra-Balance Movement Cancellation/Modification Query | Request Query to Servicing Party under a selected criterion. | Instructing Party |
| Validate Request | Technical and business validation of the request before further processing or not. | Servicing/Executing Party |
| Generate Report | Build a report for Intra Balance Movement Cancellation/Modification Instructions satisfying a previously selected criterion. | Servicing/Executing Party |
| Successful Process  | If YES, the report is properly generated then go to the Send Intra Balance Movement Cancellation/Modification Report process. <br>If NO; then Error Processing to advise the Instructing Party.  | Servicing/Executing Party |
| Send Intra Balance Movement Cancellation/Modification Report | Route Report to Instructing Party under a selected criterion. | Servicing/Executing Party |
| Error Processing | Adds operational errors to response before routing to Instructing Party | Servicing/Executing Party |
| Monitor | Monitor: Check for incoming communications (Intra Balance Movement Cancellation/Modification Report). | Instructing Party |
| Reconcile | Reconcile: External process reconciling impact of current status of original instruction. | Instructing Party |


### Scoped participants

- [Account owner](../../../../../../../shared/reference/participants/participant-src-000359-account-owner.md)
- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000359-instructing-party.md)
- [Servicing Party](../../../../../../../shared/reference/participants/participant-src-000359-servicing-party.md)

### Exact supplied message definitions

| Exact definition | Binding evidence |
| --- | --- |
| [camt.080.001.02](../../../../messages/camt.080.001.02/index.md) | src-000360 file page 232: 11 camt.080.001.02 IntraBalanceMovementModificationQueryV02 |
| [camt.081.001.02](../../../../messages/camt.081.001.02/index.md) | src-000360 file page 245: 12 camt.081.001.02 IntraBalanceMovementModificationReportV02 |
| [camt.082.001.02](../../../../messages/camt.082.001.02/index.md) | src-000360 file page 286: 13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 |
| [camt.083.001.02](../../../../messages/camt.083.001.02/index.md) | src-000360 file page 300: 14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 |


Part 1 uses family identifiers or unversioned names. These exact references come separately from supplied Part 2 headings. Where no exact message is printed or otherwise established, none is invented.

### Alternatives and source limitations

- No start-point glyph is drawn in the source. T24 separately lists Generate Report; the picture proceeds directly from Validate Request to Successful Process? and therefore has no invented Generate Report box.
- Native Mermaid flowchart subgraphs retain source swimlane responsibility. Source start/end glyphs, labelled decisions and bars remain explicit. T19 defines bars as parallel actions; the original uses some bars at converging alternative paths, so no extra execution semantics are inferred.

[issue-000047 — unresolved source wording and rendered-label differences](../../../../../../../tracking/issues.md)

<!-- INTRABALANCE-FIG-14-END -->
