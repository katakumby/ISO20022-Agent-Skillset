---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p208-intra-balance-movement-pending-posting-report-process"
title: "Intra-Balance Movement Pending/Posting Report Process"
source_locations: [{"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Pending/Posting Report Process"], "locator": "/w:document/w:body/w:p[208]", "paragraph_id": "P208", "table_id": null}, {"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Pending/Posting Report Process"], "locator": "/w:document/w:body/w:p[209]", "paragraph_id": "P209", "table_id": null}, {"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Pending/Posting Report Process"], "locator": "/w:document/w:body/w:p[210]", "paragraph_id": "P210", "table_id": null}, {"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Pending/Posting Report Process"], "locator": "/w:document/w:body/w:tbl[25]", "paragraph_id": null, "table_id": "T25"}]
participants: ["participant-src-000359-servicing-executing-party-instructing-party", "participant-src-000359-servicing-executing-party", "participant-src-000359-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[17]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["camt.084.001.02", "camt.085.001.02"]
message_families: ["camt.066"]
search_terms: ["Intra-Balance Movement Pending/Posting Report Process", "Servicing/Executing Party Instructing Party", "Servicing/Executing Party", "Instructing Party", "camt.066"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000359-account-owner", "participant-src-000359-instructing-party", "participant-src-000359-servicing-executing-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0015.md"]
---



# Intra-Balance Movement Pending/Posting Report Process

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Servicing/Executing Party Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Servicing/Executing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0015](../documents/src-000359/diagrams/fig-0015.md). Mermaid reconstruction and visual review are pending.

Source table [T25](../documents/src-000359/tables/tbl-0025.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| System Event Triggered | External process resulting in need for liquidity movements reporting. | Servicing/Executing Party Instructing Party |
| Report Required  | Verification that reporting required for parties under current conditions. <br>If YES, then go to the Generate Report Process. <br>If NO, then end of activity.   | Servicing/Executing Party |
| Generate Report | System process that creates a report from previously received intra-balance instructions satisfying reporting criteria (i.e., pending or settled). | Servicing/Executing Party |
| Successful Process  | If YES, the report is properly generated then go to the Send Intra Balance Movement Cancellation/Modification Report process. <br>If NO; then Error Processing to advise the Instructing Party.  | Servicing/Executing Party |
| Report Pending/Settled Intra-Balance Movement Instruction | Route Report to Instructing Party under a selected criterion. | Servicing/Executing Party |
| Error Processing | Adds operational errors to response before routing to Instructing Party | Servicing/Executing Party |
| Monitor | Monitor: Check for incoming communications (Intra Balance Movement Cancellation/Modification Report). | Instructing Party |
| Reconcile | Reconcile: External process reconciling impact of current status of original instruction. | Instructing Party |

## Messages and alternative paths

Source-supported message family mentions: `camt.066`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: Description of BusinessActivities / Intra-Balance Movement Pending/Posting Report Process.

<!-- INTRABALANCE-FIG-15-START -->
## Curated scenario and source responsibilities

[Pending and posting reporting activity — source diagram and directions](../diagrams/intrabalance/fig-0015.md)

### Narrative conditions, actions and outcomes

**src-000359 P208** — Intra-Balance Movement Pending/Posting Report Process

### Source-defined triggers, preconditions, postconditions and activity responsibilities

[Complete T17 with exact source rows](../documents/src-000359/tables/tbl-0017.md)

| Source item | Source definition |
| --- | --- |
| Definition | The process of reporting, for a given period of time, previously sent intra-balance movement instructions with a status of pending. |
| Trigger | The process is triggered by a system event (e.g. end-of-day or end of night-time cycle…). |
| Pre-conditions | Static Data configuration satisfying the requirement for reporting of pending intra-balance movement instructions. |
| Post-conditions | A valid Intra-Balance Movement Pending report is generated. |
| Role | Executing/Servicing Party for the report / Account owner (Receiving Party) of instructions reported by the report. |


[Complete T18 with exact source rows](../documents/src-000359/tables/tbl-0018.md)

| Source item | Source definition |
| --- | --- |
| Definition | The process of reporting, for a given period of time, previously sent intra-balance movement instructions with a status of settled. |
| Trigger | The process is triggered by a system event (e.g. end-of-day or end of night-time cycle…). |
| Pre-conditions | Static Data configuration satisfying the requirement for reporting of settled intra-balance movement instructions. |
| Post-conditions | A valid Intra-Balance Movement Posting report is generated. |
| Role | Executing/Servicing Party for the report / Account owner (Receiving Party) of instructions reported by the report. |


[Complete T25 with exact source rows](../documents/src-000359/tables/tbl-0025.md)

| Source step | Description / conditions | Initiator / responsible role |
| --- | --- | --- |
| System Event Triggered | External process resulting in need for liquidity movements reporting. | Servicing/Executing Party Instructing Party |
| Report Required  | Verification that reporting required for parties under current conditions. <br>If YES, then go to the Generate Report Process. <br>If NO, then end of activity.   | Servicing/Executing Party |
| Generate Report | System process that creates a report from previously received intra-balance instructions satisfying reporting criteria (i.e., pending or settled). | Servicing/Executing Party |
| Successful Process  | If YES, the report is properly generated then go to the Send Intra Balance Movement Cancellation/Modification Report process. <br>If NO; then Error Processing to advise the Instructing Party.  | Servicing/Executing Party |
| Report Pending/Settled Intra-Balance Movement Instruction | Route Report to Instructing Party under a selected criterion. | Servicing/Executing Party |
| Error Processing | Adds operational errors to response before routing to Instructing Party | Servicing/Executing Party |
| Monitor | Monitor: Check for incoming communications (Intra Balance Movement Cancellation/Modification Report). | Instructing Party |
| Reconcile | Reconcile: External process reconciling impact of current status of original instruction. | Instructing Party |


### Scoped participants

- [Account owner](../../../../../../../shared/reference/participants/participant-src-000359-account-owner.md)
- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000359-instructing-party.md)
- [Servicing/Executing Party](../../../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party.md)

### Exact supplied message definitions

| Exact definition | Binding evidence |
| --- | --- |
| [camt.084.001.02](../../../../messages/camt.084.001.02/index.md) | src-000360 file page 331: 15 camt.084.001.02 IntraBalanceMovementPostingReportV02 |
| [camt.085.001.02](../../../../messages/camt.085.001.02/index.md) | src-000360 file page 358: 16 camt.085.001.02 IntraBalanceMovementPendingReportV02 |


Part 1 uses family identifiers or unversioned names. These exact references come separately from supplied Part 2 headings. Where no exact message is printed or otherwise established, none is invented.

### Alternatives and source limitations

- T25 Successful Process and Monitor rows refer to Cancellation/Modification Report, despite the pending/posting heading and picture. Those copied labels remain visible as issue-000047.
- T25 jointly names Servicing/Executing Party Instructing Party as event initiator and says Error Processing routes a response; the picture shows the event only in the servicing lane and an error end point.
- Native Mermaid flowchart subgraphs retain source swimlane responsibility. Source start/end glyphs, labelled decisions and bars remain explicit. T19 defines bars as parallel actions; the original uses some bars at converging alternative paths, so no extra execution semantics are inferred.

[issue-000047 — unresolved source wording and rendered-label differences](../../../../../../../tracking/issues.md)

<!-- INTRABALANCE-FIG-15-END -->
