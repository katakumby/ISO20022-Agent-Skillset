---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p282-producing-an-intra-balance-modification-cancellation-report-at-a-busin"
title: "Producing an Intra Balance Modification/Cancellation Report at a business event."
source_locations: [{"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Intra-Balance Movement Modification/Cancellation Query and Report Process", "Producing an Intra Balance Modification/Cancellation Report at a business event."], "locator": "/w:document/w:body/w:p[282]", "paragraph_id": "P282", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Intra-Balance Movement Modification/Cancellation Query and Report Process", "Producing an Intra Balance Modification/Cancellation Report at a business event."], "locator": "/w:document/w:body/w:p[283]", "paragraph_id": "P283", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Intra-Balance Movement Modification/Cancellation Query and Report Process", "Producing an Intra Balance Modification/Cancellation Report at a business event."], "locator": "/w:document/w:body/w:p[284]", "paragraph_id": "P284", "table_id": null}]
participants: ["participant-src-000359-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[6]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[7]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[8]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[12]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[14]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["camt.072.001.02", "camt.073.001.02", "camt.074.001.02", "camt.075.001.02", "camt.081.001.02", "camt.083.001.02"]
message_families: ["camt.072", "camt.073", "camt.074", "camt.075", "camt.081", "camt.083"]
search_terms: ["Producing an Intra Balance Modification/Cancellation Report at a business event.", "Instructing Party", "camt.072", "camt.073", "camt.074", "camt.075", "camt.081", "camt.083"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000359-account-owner", "participant-src-000359-instructing-party", "participant-src-000359-servicing-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0022.md"]
---



# Producing an Intra Balance Modification/Cancellation Report at a business event.

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P284** Servicing PartyInstructing Party IntraBalanceMovementModificationReport (camt.081)IntraBalanceMovementModificationRequest (camt.072)IntraBalanceMovementModificationRequestStatusAdvice (camt.073)IntraBalanceMovementCancellationRequest (camt.074)IntraBalanceMovementCancellationRequestStatusAdvice (camt.075)IntraBalanceMovementCancellationReport (camt.083)Servicing PartyInstructing Party IntraBalanceMovementModificationReport (camt.081)IntraBalanceMovementModificationRequest (camt.072)IntraBalanceMovementModificationRequestStatusAdvice (camt.073)IntraBalanceMovementCancellationRequest (camt.074)IntraBalanceMovementCancellationRequestStatusAdvice (camt.075)IntraBalanceMovementCancellationReport (camt.083)

Source diagram evidence: [fig-0022](../documents/src-000359/diagrams/fig-0022.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `camt.072`, `camt.073`, `camt.074`, `camt.075`, `camt.081`, `camt.083`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: BusinessTransactions / Intra-Balance Movement Modification/Cancellation Query and Report Process / Producing an Intra Balance Modification/Cancellation Report at a business event..

<!-- INTRABALANCE-FIG-22-START -->
## Curated scenario and source responsibilities

[Event-triggered cancellation and modification reporting — source diagram and directions](../diagrams/intrabalance/fig-0022.md)

| Step | Sender / transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party | Servicing Party | IntraBalanceMovementCancellationRequest (camt.074)<br/>IntraBalanceMovementModificationRequest (camt.072) |
| 2 | Servicing Party | Instructing Party | IntraBalanceMovementCancellationRequestStatusAdvice (camt.075)<br/>IntraBalanceMovementModificationRequestStatusAdvice (camt.073) |
| 3 | Servicing Party | Instructing Party | IntraBalanceMovementCancellationReport (camt.083) |
| 4 | Servicing Party | Instructing Party | IntraBalanceMovementModificationReport (camt.081) |


### Narrative conditions, actions and outcomes

**src-000359 P282** — Producing an Intra Balance Modification/Cancellation Report at a business event.

**src-000359 P285** — IntraBalance Movement Cancellation Request

**src-000359 P286** — The instructing Party requests the cancellation of the intra-balance movement instruction previously sent.

**src-000359 P287** — IntraBalance Movement Modification Request

**src-000359 P288** — The instructing Party requests the modification of a processing indicator or other information of an intra-balance movement instruction previously sent.

**src-000359 P289** — IntraBalance Movement Cancellation Request Status Advice

**src-000359 P290** — The Servicing Party informs the Instructing Party about the status of the intra-balance movement cancellation request previously sent.

**src-000359 P291** — IntraBalance Movement Modification Request Status Advice

**src-000359 P292** — The Servicing/Executing Party informs the Instructing Party about the status of the intra-balance movement modification request previously sent.

**src-000359 P293** — IntraBalance Movement Cancellation Report 

**src-000359 P294** — The Servicing party sends to the Instructing party a report with the details of its Intra-Balance Movement Cancellation Instruction/s at a moment in time. 

**src-000359 P295** — IntraBalance Movement Modification Report 

**src-000359 P296** — The Servicing party sends to the Instructing party a report with the details of its Intra-Balance Movement Modification Instruction/s at a moment in time. 

### Source-defined triggers, preconditions, postconditions and activity responsibilities

[Complete T16 with exact source rows](../documents/src-000359/tables/tbl-0016.md)

| Source item | Source definition |
| --- | --- |
| Definition | The Instructing Party asks the Servicing Party a response to a query concerning a previously sent intra-balance movement cancellation instruction/modification. |
| Trigger | The process is triggered either by the system at the end-of-date event or by the receipt of a query request.  |
| Pre-conditions | Existence of an intra-balance cancellation instruction/modification. |
| Post-conditions | The acknowledgement of the processing of the query and the generation of a valid intra-balance movement cancellation/modification report. |
| Role | Account owner (Instructing Party) for the Query.<br>Executing/Servicing Party for the Report. |


[Complete T23 with exact source rows](../documents/src-000359/tables/tbl-0023.md)

| Source step | Description / conditions | Initiator / responsible role |
| --- | --- | --- |
| System Event Triggered | External process resulting in need for liquidity movements reporting. | Servicing/Executing Party Instructing Party |
| Report Required  | Verification that reporting required for parties under current conditions. <br>If YES, then go to the Generate Report Process. <br>If NO, then end of activity.   | Servicing/Executing Party |
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
| [camt.072.001.02](../../../../messages/camt.072.001.02/index.md) | src-000360 file page 66: 5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 |
| [camt.073.001.02](../../../../messages/camt.073.001.02/index.md) | src-000360 file page 90: 6 camt.073.001.02 IntraBalanceMovementModificationRequestStatusAdviceV02 |
| [camt.074.001.02](../../../../messages/camt.074.001.02/index.md) | src-000360 file page 115: 7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 |
| [camt.075.001.02](../../../../messages/camt.075.001.02/index.md) | src-000360 file page 132: 8 camt.075.001.02 IntraBalanceMovementCancellationRequestStatusAdviceV02 |
| [camt.081.001.02](../../../../messages/camt.081.001.02/index.md) | src-000360 file page 245: 12 camt.081.001.02 IntraBalanceMovementModificationReportV02 |
| [camt.083.001.02](../../../../messages/camt.083.001.02/index.md) | src-000360 file page 300: 14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 |


Part 1 uses family identifiers or unversioned names. These exact references come separately from supplied Part 2 headings. Where no exact message is printed or otherwise established, none is invented.

### Alternatives and source limitations

- The complete rendered picture shows one request arrow and one dashed status arrow; the labels cover cancellation/modification variants. Both native source labels are preserved on those shared arrows, without adding unseen connectors. The modification-status label and code suffixes are clipped/overlapped in the local Word view but present at P284 and P291–P292.
- The two report arrows are separate in the source. No query arrow is supplied in this event-triggered scenario.
- Source-native text boxes and connector objects form a complete figure. The retained Word page is the complete composite; the small WMF bank pictograms are not treated as standalone diagrams.
- Solid/dashed connectors and their directions are preserved. Source colours are recorded per message step below; colours distinguish pictured context without asserting extra protocol semantics.
- Native Mermaid boxes replace institutional pictograms; labels define the functional participants and do not bind a role to one institution.

[issue-000047 — unresolved source wording and rendered-label differences](../../../../../../../tracking/issues.md)

<!-- INTRABALANCE-FIG-22-END -->
