---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p256-requesting-an-intra-balance-cancellation-query"
title: "Requesting an Intra Balance Cancellation Query"
source_locations: [{"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Intra-Balance Movement Modification/Cancellation Query and Report Process", "Requesting an Intra Balance Cancellation Query"], "locator": "/w:document/w:body/w:p[256]", "paragraph_id": "P256", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Intra-Balance Movement Modification/Cancellation Query and Report Process", "Requesting an Intra Balance Cancellation Query"], "locator": "/w:document/w:body/w:p[257]", "paragraph_id": "P257", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Intra-Balance Movement Modification/Cancellation Query and Report Process", "Requesting an Intra Balance Cancellation Query"], "locator": "/w:document/w:body/w:p[258]", "paragraph_id": "P258", "table_id": null}]
participants: ["participant-src-000359-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[7]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[8]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[13]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[14]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["camt.074.001.02", "camt.075.001.02", "camt.082.001.02", "camt.083.001.02"]
message_families: ["camt.074", "camt.075", "camt.082", "camt.083"]
search_terms: ["Requesting an Intra Balance Cancellation Query", "Instructing Party", "camt.074", "camt.075", "camt.082", "camt.083"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000359-account-owner", "participant-src-000359-instructing-party", "participant-src-000359-servicing-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0020.md"]
---



# Requesting an Intra Balance Cancellation Query

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P258** Servicing PartyInstructing Party IntraBalanceMovementCancellationQuery (camt.082)IntraBalanceMovementCancellationReport (camt.083)IntraBalanceMovementCancellationRequest (camt.074)IntraBalanceMovementCancellationRequestStatusAdvice (camt.075)Servicing PartyInstructing Party IntraBalanceMovementCancellationQuery (camt.082)IntraBalanceMovementCancellationReport (camt.083)IntraBalanceMovementCancellationRequest (camt.074)IntraBalanceMovementCancellationRequestStatusAdvice (camt.075)

Source diagram evidence: [fig-0020](../documents/src-000359/diagrams/fig-0020.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `camt.074`, `camt.075`, `camt.082`, `camt.083`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: BusinessTransactions / Intra-Balance Movement Modification/Cancellation Query and Report Process / Requesting an Intra Balance Cancellation Query.

<!-- INTRABALANCE-FIG-20-START -->
## Curated scenario and source responsibilities

[Cancellation query and report exchange — source diagram and directions](../diagrams/intrabalance/fig-0020.md)

| Step | Sender / transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party | Servicing Party | IntraBalanceMovementCancellationRequest (camt.074) |
| 2 | Servicing Party | Instructing Party | IntraBalanceMovementCancellationRequestStatusAdvice (camt.075) |
| 3 | Instructing Party | Servicing Party | IntraBalanceMovementCancellationQuery (camt.082) |
| 4 | Servicing Party | Instructing Party | IntraBalanceMovementCancellationReport (camt.083) |


### Narrative conditions, actions and outcomes

**src-000359 P256** — Requesting an Intra Balance Cancellation Query

**src-000359 P259** — IntraBalance Movement Cancellation Request

**src-000359 P260** — The instructing Party requests the cancellation of the intra-balance movement instruction previously sent.

**src-000359 P261** — IntraBalance Movement Cancellation Request Status Advice

**src-000359 P262** — The Servicing Party informs the Instructing Party about the status of the intra-balance movement cancellation request previously sent.

**src-000359 P263** — IntraBalance Movement Cancellation Query

**src-000359 P264** — The instructing Party requests a query to retrieve all the Intra-balance Movement Cancellation Requests, along with their current status, that satisfy the defined selection criteria. 

**src-000359 P265** — IntraBalance Movement Cancellation Report 

**src-000359 P266** — The Servicing party sends to the Instructing party the response of the query with the full details of the Intra-Balance Movement Cancellation Instruction/s that fulfilled the selection criteria. 

### Source-defined triggers, preconditions, postconditions and activity responsibilities

[Complete T12 with exact source rows](../documents/src-000359/tables/tbl-0012.md)

| Source item | Source definition |
| --- | --- |
| Definition | The process to request the cancellation of an intra-balance movement instruction. |
| Trigger | The process is triggered by an instructing party decision to cancel an intra-balance movement instruction. |
| Pre-conditions | Existence of a liquidity restriction instruction. |
| Post-conditions | A valid liquidity restriction cancellation request is generated. |
| Role | Instructing Party -  for the cancellation request.<br>Executing/Servicing Party - for the receipt of the cancellation request. |


[Complete T13 with exact source rows](../documents/src-000359/tables/tbl-0013.md)

| Source item | Source definition |
| --- | --- |
| Definition | The process of informing the current status of a liquidity restriction modification or cancellation request. |
| Trigger | The process is triggered by market infrastructure when the status changes. |
| Pre-conditions | Existence of a liquidity restriction modification or cancellation request as received within a market infrastructure. |
| Post-conditions | A status change is generated. |
| Role | Account owner (Instructing party) - for the receipt of the Status Advice.<br>Executing/Servicing Party - for the sending of the Status Advice. |


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
| [camt.074.001.02](../../../../messages/camt.074.001.02/index.md) | src-000360 file page 115: 7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 |
| [camt.075.001.02](../../../../messages/camt.075.001.02/index.md) | src-000360 file page 132: 8 camt.075.001.02 IntraBalanceMovementCancellationRequestStatusAdviceV02 |
| [camt.082.001.02](../../../../messages/camt.082.001.02/index.md) | src-000360 file page 286: 13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 |
| [camt.083.001.02](../../../../messages/camt.083.001.02/index.md) | src-000360 file page 300: 14 camt.083.001.02 IntraBalanceMovementCancellationReportV02 |


Part 1 uses family identifiers or unversioned names. These exact references come separately from supplied Part 2 headings. Where no exact message is printed or otherwise established, none is invented.

### Alternatives and source limitations

- Clipped source labels and code suffixes are recovered from the original drawing text P258.
- Source-native text boxes and connector objects form a complete figure. The retained Word page is the complete composite; the small WMF bank pictograms are not treated as standalone diagrams.
- Solid/dashed connectors and their directions are preserved. Source colours are recorded per message step below; colours distinguish pictured context without asserting extra protocol semantics.
- Native Mermaid boxes replace institutional pictograms; labels define the functional participants and do not bind a role to one institution.

[issue-000047 — unresolved source wording and rendered-label differences](../../../../../../../tracking/issues.md)

<!-- INTRABALANCE-FIG-20-END -->
