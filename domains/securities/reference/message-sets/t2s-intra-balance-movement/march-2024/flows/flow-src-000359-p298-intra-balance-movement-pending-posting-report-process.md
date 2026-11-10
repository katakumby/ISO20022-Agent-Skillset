---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p298-intra-balance-movement-pending-posting-report-process"
title: "Intra-Balance Movement Pending/Posting Report Process"
source_locations: [{"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Intra-Balance Movement Pending/Posting Report Process "], "locator": "/w:document/w:body/w:p[298]", "paragraph_id": "P298", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Intra-Balance Movement Pending/Posting Report Process "], "locator": "/w:document/w:body/w:p[299]", "paragraph_id": "P299", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Intra-Balance Movement Pending/Posting Report Process "], "locator": "/w:document/w:body/w:p[300]", "paragraph_id": "P300", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Intra-Balance Movement Pending/Posting Report Process "], "locator": "/w:document/w:body/w:p[301]", "paragraph_id": "P301", "table_id": null}]
participants: ["participant-src-000359-servicing-executing-party-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[17]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[15]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[16]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["camt.066.001.02", "camt.084.001.02", "camt.085.001.02"]
message_families: ["camt.066", "camt.084", "camt.085"]
search_terms: ["Intra-Balance Movement Pending/Posting Report Process", "Servicing/Executing Party Instructing Party", "camt.066", "camt.084", "camt.085"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000359-account-owner", "participant-src-000359-instructing-party", "participant-src-000359-servicing-executing-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0023.md"]
---



# Intra-Balance Movement Pending/Posting Report Process

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Servicing/Executing Party Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P300** Servicing/Executing PartyInstructing Party IntraBalanceMovementInstruction (camt.066)IntraBalanceMovementPendingReport (camt.085)IntraBalanceMovementPostingReport (camt.084)Servicing/Executing PartyInstructing Party IntraBalanceMovementInstruction (camt.066)IntraBalanceMovementPendingReport (camt.085)IntraBalanceMovementPostingReport (camt.084)

Source diagram evidence: [fig-0023](../documents/src-000359/diagrams/fig-0023.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `camt.066`, `camt.084`, `camt.085`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: BusinessTransactions / Intra-Balance Movement Pending/Posting Report Process .

<!-- INTRABALANCE-FIG-23-START -->
## Curated scenario and source responsibilities

[Pending and posting report exchange — source diagram and directions](../diagrams/intrabalance/fig-0023.md)

| Step | Sender / transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party | Servicing/Executing Party | IntraBalanceMovementInstruction (camt.066) |
| 2 | Servicing/Executing Party | Instructing Party | IntraBalanceMovementPendingReport (camt.085) |
| 3 | Servicing/Executing Party | Instructing Party | IntraBalanceMovementPostingReport (camt.084) |


### Narrative conditions, actions and outcomes

**src-000359 P298** — Intra-Balance Movement Pending/Posting Report Process 

**src-000359 P302** — IntraBalance Movement Instruction

**src-000359 P303** — The Instructing Party sends the instruction to the Servicing/Executing Party to allocate money from a specific cash account. This instruction contains all the information needed for the movement of cash between balances. 

**src-000359 P304** — IntraBalance Movement Pending Report

**src-000359 P305** — The Servicing/Executing Party sends a report to the Instructing Party with the information of the intra-balance movement instructions previously sent by the Instructing Party, which have a status of pending.

**src-000359 P306** — IntraBalance Movement Posting Report

**src-000359 P307** —  The Servicing/Executing Party sends a report to the Instructing Party with the information of the intra-balance movement instructions previously sent by the Instructing Party, which have been settled.

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
| [camt.066.001.02](../../../../messages/camt.066.001.02/index.md) | src-000360 file page 10: 2 camt.066.001.02 IntraBalanceMovementInstructionV02 |
| [camt.084.001.02](../../../../messages/camt.084.001.02/index.md) | src-000360 file page 331: 15 camt.084.001.02 IntraBalanceMovementPostingReportV02 |
| [camt.085.001.02](../../../../messages/camt.085.001.02/index.md) | src-000360 file page 358: 16 camt.085.001.02 IntraBalanceMovementPendingReportV02 |


Part 1 uses family identifiers or unversioned names. These exact references come separately from supplied Part 2 headings. Where no exact message is printed or otherwise established, none is invented.

### Alternatives and source limitations

- Source-native text boxes and connector objects form a complete figure. The retained Word page is the complete composite; the small WMF bank pictograms are not treated as standalone diagrams.
- Solid/dashed connectors and their directions are preserved. Source colours are recorded per message step below; colours distinguish pictured context without asserting extra protocol semantics.
- Native Mermaid boxes replace institutional pictograms; labels define the functional participants and do not bind a role to one institution.

[issue-000047 — unresolved source wording and rendered-label differences](../../../../../../../tracking/issues.md)

<!-- INTRABALANCE-FIG-23-END -->
