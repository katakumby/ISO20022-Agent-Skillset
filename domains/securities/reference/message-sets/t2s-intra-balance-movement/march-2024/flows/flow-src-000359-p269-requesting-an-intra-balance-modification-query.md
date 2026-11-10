---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p269-requesting-an-intra-balance-modification-query"
title: "Requesting an Intra Balance Modification Query"
source_locations: [{"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Intra-Balance Movement Modification/Cancellation Query and Report Process", "Requesting an Intra Balance Modification Query"], "locator": "/w:document/w:body/w:p[269]", "paragraph_id": "P269", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Intra-Balance Movement Modification/Cancellation Query and Report Process", "Requesting an Intra Balance Modification Query"], "locator": "/w:document/w:body/w:p[270]", "paragraph_id": "P270", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Intra-Balance Movement Modification/Cancellation Query and Report Process", "Requesting an Intra Balance Modification Query"], "locator": "/w:document/w:body/w:p[271]", "paragraph_id": "P271", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Intra-Balance Movement Modification/Cancellation Query and Report Process", "Requesting an Intra Balance Modification Query"], "locator": "/w:document/w:body/w:p[272]", "paragraph_id": "P272", "table_id": null}]
participants: ["participant-src-000359-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[6]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[11]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[12]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["camt.072.001.02", "camt.073.001.02", "camt.080.001.02", "camt.081.001.02"]
message_families: ["camt.072", "camt.073", "camt.080", "camt.081"]
search_terms: ["Requesting an Intra Balance Modification Query", "Instructing Party", "camt.072", "camt.073", "camt.080", "camt.081"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000359-account-owner", "participant-src-000359-instructing-party", "participant-src-000359-servicing-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0021.md"]
---



# Requesting an Intra Balance Modification Query

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P271** Servicing PartyInstructing Party IntraBalanceMovementModificationQuery (camt.080)IntraBalanceMovementModificationReport (camt.081)IntraBalanceMovementModificationRequest (camt.072)IntraBalanceMovementModificationRequestStatusAdvice (camt.073)Servicing PartyInstructing Party IntraBalanceMovementModificationQuery (camt.080)IntraBalanceMovementModificationReport (camt.081)IntraBalanceMovementModificationRequest (camt.072)IntraBalanceMovementModificationRequestStatusAdvice (camt.073)

Source diagram evidence: [fig-0021](../documents/src-000359/diagrams/fig-0021.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `camt.072`, `camt.073`, `camt.080`, `camt.081`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: BusinessTransactions / Intra-Balance Movement Modification/Cancellation Query and Report Process / Requesting an Intra Balance Modification Query.

<!-- INTRABALANCE-FIG-21-START -->
## Curated scenario and source responsibilities

[Modification query and report exchange — source diagram and directions](../diagrams/intrabalance/fig-0021.md)

| Step | Sender / transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party | Servicing Party | IntraBalanceMovementModificationRequest (camt.072) |
| 2 | Servicing Party | Instructing Party | IntraBalanceMovementModificationRequestStatusAdvice (camt.073) |
| 3 | Instructing Party | Servicing Party | IntraBalanceMovementModificationQuery (camt.080) |
| 4 | Servicing Party | Instructing Party | IntraBalanceMovementModificationReport (camt.081) |


### Narrative conditions, actions and outcomes

**src-000359 P269** — Requesting an Intra Balance Modification Query

**src-000359 P273** — IntraBalance Movement Modification Request

**src-000359 P274** — The instructing Party requests the modification of a processing indicator or other information of an intra-balance movement instruction previously sent.

**src-000359 P275** — IntraBalance Movement Modification Request Status Advice

**src-000359 P276** — The Servicing/Executing Party informs the Instructing Party about the status of the intra-balance movement modification request previously sent.

**src-000359 P277** — IntraBalance Movement Modification Query

**src-000359 P278** — The instructing Party requests a query to retrieve all the Intra-balance Movement Modification Requests, along with their current status, that satisfy the defined selection criteria. 

**src-000359 P279** — IntraBalance Movement Modification Report 

**src-000359 P280** — The Servicing party sends to the Instructing party the response of the query with the full details of the Intra-Balance Movement Modification Instruction/s that fulfilled the selection criteria.

### Source-defined triggers, preconditions, postconditions and activity responsibilities

[Complete T11 with exact source rows](../documents/src-000359/tables/tbl-0011.md)

| Source item | Source definition |
| --- | --- |
| Definition | The process to request the modification of process indicators or other information as concerns a previously sent intra-balance movement instruction. |
| Trigger | The process is triggered by an instructing party decision to alter an intra-balance movement instruction. |
| Pre-conditions | Existence of a liquidity restriction instruction. |
| Post-conditions | A valid liquidity restriction modification request is generated. |
| Role | Instructing Party - for the modification request.<br>Executing/Servicing Party - for the receipt of the modification request. |


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
| [camt.072.001.02](../../../../messages/camt.072.001.02/index.md) | src-000360 file page 66: 5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 |
| [camt.073.001.02](../../../../messages/camt.073.001.02/index.md) | src-000360 file page 90: 6 camt.073.001.02 IntraBalanceMovementModificationRequestStatusAdviceV02 |
| [camt.080.001.02](../../../../messages/camt.080.001.02/index.md) | src-000360 file page 232: 11 camt.080.001.02 IntraBalanceMovementModificationQueryV02 |
| [camt.081.001.02](../../../../messages/camt.081.001.02/index.md) | src-000360 file page 245: 12 camt.081.001.02 IntraBalanceMovementModificationReportV02 |


Part 1 uses family identifiers or unversioned names. These exact references come separately from supplied Part 2 headings. Where no exact message is printed or otherwise established, none is invented.

### Alternatives and source limitations

- The outgoing green query arrow has no visible text in the local Word render. Its exact name/code is retained in native source drawing text P271, and P277–P278 independently describe it. The reconstruction restores that supplied label and does not claim the local render displays it.
- Source-native text boxes and connector objects form a complete figure. The retained Word page is the complete composite; the small WMF bank pictograms are not treated as standalone diagrams.
- Solid/dashed connectors and their directions are preserved. Source colours are recorded per message step below; colours distinguish pictured context without asserting extra protocol semantics.
- Native Mermaid boxes replace institutional pictograms; labels define the functional participants and do not bind a role to one institution.

[issue-000047 — unresolved source wording and rendered-label differences](../../../../../../../tracking/issues.md)

<!-- INTRABALANCE-FIG-21-END -->
