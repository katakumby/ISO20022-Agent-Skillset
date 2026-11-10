---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p211-intra-balance-movement-query-response-process"
title: "Intra-Balance Movement Query/Response Process"
source_locations: [{"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Query/Response Process"], "locator": "/w:document/w:body/w:p[211]", "paragraph_id": "P211", "table_id": null}, {"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Query/Response Process"], "locator": "/w:document/w:body/w:p[212]", "paragraph_id": "P212", "table_id": null}, {"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Query/Response Process"], "locator": "/w:document/w:body/w:p[213]", "paragraph_id": "P213", "table_id": null}, {"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Query/Response Process"], "locator": "/w:document/w:body/w:p[214]", "paragraph_id": "P214", "table_id": null}, {"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Query/Response Process"], "locator": "/w:document/w:body/w:tbl[26]", "paragraph_id": null, "table_id": "T26"}, {"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Query/Response Process"], "locator": "/w:document/w:body/w:p[215]", "paragraph_id": "P215", "table_id": null}]
participants: ["participant-src-000359-servicing-executing-party-instructing-party", "participant-src-000359-servicing-executing-party", "participant-src-000359-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[9]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[10]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["camt.078.001.02", "camt.079.001.02"]
message_families: ["camt.078", "camt.079"]
search_terms: ["Intra-Balance Movement Query/Response Process", "Servicing/Executing Party Instructing Party", "Servicing/Executing Party", "Instructing Party", "camt.078", "camt.079"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000359-instructing-party", "participant-src-000359-servicing-executing-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0016.md"]
---



# Intra-Balance Movement Query/Response Process

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Servicing/Executing Party Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Servicing/Executing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0016](../documents/src-000359/diagrams/fig-0016.md). Mermaid reconstruction and visual review are pending.

Source table [T26](../documents/src-000359/tables/tbl-0026.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Query | Intra-Balance Movement Query to Servicing/Executing Party | Instructing Party |
| Process Query | Technical and business validation of the query before further processing or not. | Servicing/Executing Party |
| Successful Process  | If YES, the report is properly generated then go to the Send Intra Balance Movement Report process. <br>If NO; then Error Processing to advise the Instructing Party.  | Servicing/Executing Party |
| Send Intra Balance Movement Report | Route Report to Instructing Party under a selected criterion. | Servicing/Executing Party |
| Error Processing | Adds operational errors to response before routing to Instructing Party | Servicing/Executing Party |
| Monitor | Monitor: Check for incoming communications associated with original instruction | Instructing Party |
| Reconcile | Reconcile: External process reconciling impact of current status of original instruction. | Instructing Party |

## Messages and alternative paths

Source-supported message family mentions: `camt.078`, `camt.079`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: Description of BusinessActivities / Intra-Balance Movement Query/Response Process.

<!-- INTRABALANCE-FIG-16-START -->
## Curated scenario and source responsibilities

[Movement query and response activity — source diagram and directions](../diagrams/intrabalance/fig-0016.md)

### Narrative conditions, actions and outcomes

**src-000359 P211** — Intra-Balance Movement Query/Response Process

### Source-defined triggers, preconditions, postconditions and activity responsibilities

[Complete T14 with exact source rows](../documents/src-000359/tables/tbl-0014.md)

| Source item | Source definition |
| --- | --- |
| Definition | The process of enabling the reconciliation of cash movements through the querying of available and necessary data using defined selection criteria. |
| Trigger | The process is triggered by reconciliation processing (e.g. missing instructions or system errors) resulting in the sending of a query request by the Instructing Party. |
| Pre-conditions | Instructing Party must hold necessary privileges within the Static Data configuration. |
| Post-conditions | None. |
| Role | Instructing Party for the Query.  |


[Complete T15 with exact source rows](../documents/src-000359/tables/tbl-0015.md)

| Source item | Source definition |
| --- | --- |
| Definition | The process of responding, to a received cash movement query. |
| Trigger | The process is triggered by a system event (e.g. end-of-day or end of night-time cycle…). |
| Pre-conditions | Receipt of an incoming query. |
| Post-conditions | A valid Intra-Balance Movement Query Response is generated containing either a business report or operational error. |
| Role | Executing/Servicing Party for the response. |


[Complete T26 with exact source rows](../documents/src-000359/tables/tbl-0026.md)

| Source step | Description / conditions | Initiator / responsible role |
| --- | --- | --- |
| Query | Intra-Balance Movement Query to Servicing/Executing Party | Instructing Party |
| Process Query | Technical and business validation of the query before further processing or not. | Servicing/Executing Party |
| Successful Process  | If YES, the report is properly generated then go to the Send Intra Balance Movement Report process. <br>If NO; then Error Processing to advise the Instructing Party.  | Servicing/Executing Party |
| Send Intra Balance Movement Report | Route Report to Instructing Party under a selected criterion. | Servicing/Executing Party |
| Error Processing | Adds operational errors to response before routing to Instructing Party | Servicing/Executing Party |
| Monitor | Monitor: Check for incoming communications associated with original instruction | Instructing Party |
| Reconcile | Reconcile: External process reconciling impact of current status of original instruction. | Instructing Party |


### Scoped participants

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000359-instructing-party.md)
- [Servicing/Executing Party](../../../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party.md)

### Exact supplied message definitions

| Exact definition | Binding evidence |
| --- | --- |
| [camt.078.001.02](../../../../messages/camt.078.001.02/index.md) | src-000360 file page 150: 9 camt.078.001.02 IntraBalanceMovementQueryV02 |
| [camt.079.001.02](../../../../messages/camt.079.001.02/index.md) | src-000360 file page 190: 10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 |


Part 1 uses family identifiers or unversioned names. These exact references come separately from supplied Part 2 headings. Where no exact message is printed or otherwise established, none is invented.

### Alternatives and source limitations

- The picture prints Movemenrt in the response activity; it is preserved literally. T26 uses Send Intra Balance Movement Report and the transaction sequence uses IntraBalanceMovementQueryResponse. These source labels remain distinct.
- T15 names a system-event trigger while requiring receipt of an incoming query; this wording is retained, without imposing a timing rule beyond the source.
- Native Mermaid flowchart subgraphs retain source swimlane responsibility. Source start/end glyphs, labelled decisions and bars remain explicit. T19 defines bars as parallel actions; the original uses some bars at converging alternative paths, so no extra execution semantics are inferred.

[issue-000047 — unresolved source wording and rendered-label differences](../../../../../../../tracking/issues.md)

<!-- INTRABALANCE-FIG-16-END -->
