---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p310-intra-balance-movement-query-response-process"
title: "Intra-Balance Movement Query/Response Process"
source_locations: [{"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Intra-Balance Movement Query/Response Process "], "locator": "/w:document/w:body/w:p[310]", "paragraph_id": "P310", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Intra-Balance Movement Query/Response Process "], "locator": "/w:document/w:body/w:p[311]", "paragraph_id": "P311", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Intra-Balance Movement Query/Response Process "], "locator": "/w:document/w:body/w:p[312]", "paragraph_id": "P312", "table_id": null}]
participants: ["participant-src-000359-servicing-executing-party-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[9]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[10]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["camt.078.001.02", "camt.079.001.02"]
message_families: ["camt.078", "camt.079"]
search_terms: ["Intra-Balance Movement Query/Response Process", "Servicing/Executing Party Instructing Party", "camt.078", "camt.079"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000359-instructing-party", "participant-src-000359-servicing-executing-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0024.md"]
---



# Intra-Balance Movement Query/Response Process

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Servicing/Executing Party Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P312** Servicing/Executing PartyInstructing Party IntraBalanceMovementQuery (camt.078)IntraBalanceMovementQueryResponse (camt.079)Servicing/Executing PartyInstructing Party IntraBalanceMovementQuery (camt.078)IntraBalanceMovementQueryResponse (camt.079)

Source diagram evidence: [fig-0024](../documents/src-000359/diagrams/fig-0024.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `camt.078`, `camt.079`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: BusinessTransactions / Intra-Balance Movement Query/Response Process .

<!-- INTRABALANCE-FIG-24-START -->
## Curated scenario and source responsibilities

[Movement query and response exchange — source diagram and directions](../diagrams/intrabalance/fig-0024.md)

| Step | Sender / transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party | Servicing/Executing Party | IntraBalanceMovementQuery (camt.078) |
| 2 | Servicing/Executing Party | Instructing Party | IntraBalanceMovementQueryResponse (camt.079) |


### Narrative conditions, actions and outcomes

**src-000359 P310** — Intra-Balance Movement Query/Response Process 

**src-000359 P313** — IntraBalance Movement Query

**src-000359 P314** — The instructing Party requests a query to retrieve all the Intra-balance Movement Instructions previously sent, along with their current status, that satisfy the defined selection criteria. 

**src-000359 P315** — IntraBalance Movement Query Response

**src-000359 P316** — The Servicing/Executing Party sends to the Instructing party the response of the query with the full details of the Intra-Balance Movement Instruction/s that fulfilled the selection criteria.

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

- Source-native text boxes and connector objects form a complete figure. The retained Word page is the complete composite; the small WMF bank pictograms are not treated as standalone diagrams.
- Solid/dashed connectors and their directions are preserved. Source colours are recorded per message step below; colours distinguish pictured context without asserting extra protocol semantics.
- Native Mermaid boxes replace institutional pictograms; labels define the functional participants and do not bind a role to one institution.

[issue-000047 — unresolved source wording and rendered-label differences](../../../../../../../tracking/issues.md)

<!-- INTRABALANCE-FIG-24-END -->
