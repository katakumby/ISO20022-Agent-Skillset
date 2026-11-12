---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p151-intra-balance-management"
title: "Intra-Balance Management"
source_locations: [{"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:p[151]", "paragraph_id": "P151", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:p[152]", "paragraph_id": "P152", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:p[153]", "paragraph_id": "P153", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:p[154]", "paragraph_id": "P154", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:p[155]", "paragraph_id": "P155", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:p[156]", "paragraph_id": "P156", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:p[157]", "paragraph_id": "P157", "table_id": null}]
participants: []
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Intra-Balance Management"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000359-account-owner", "participant-src-000359-central-counterparty", "participant-src-000359-central-securities-depository", "participant-src-000359-csd-participant", "participant-src-000359-national-central-bank", "participant-src-000359-payment-agent", "participant-src-000359-system-application"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0002.md"]
---



# Intra-Balance Management

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P152** The following diagram shows the high level business processes covered by the T2S project. 

**P153** However the Intra-Balance Movement messages only cover the Intra-Balance Management process in green. The other processes are included for completeness.

Source diagram evidence: [fig-0002](../documents/src-000359/diagrams/fig-0002.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: BusinessProcess Description / Intra-Balance Management.

<!-- INTRABALANCE-FIG-2-START -->
## Curated scenario and source responsibilities

[Intra-balance management in its business context — source diagram and directions](../diagrams/intrabalance/fig-0002.md)

### Narrative conditions, actions and outcomes

**src-000359 P151** — Intra-Balance Management

**src-000359 P152** — The following diagram shows the high level business processes covered by the T2S project. 

**src-000359 P153** — However the Intra-Balance Movement messages only cover the Intra-Balance Management process in green. The other processes are included for completeness.

**src-000359 P158** — Movement Process

**src-000359 P159** — Status Advice Process

**src-000359 P160** — Confirmation Process

**src-000359 P161** — Modification Process

**src-000359 P162** — Cancellation Process

**src-000359 P164** — Modification/Cancellation Status Advice Process

**src-000359 P165** — Movement Querying Process

**src-000359 P166** — Movement Reporting Process

**src-000359 P169** — Modification/Cancellation Query and Report Process

**src-000359 P170** — Pending Reporting Process

**src-000359 P171** — Posting Reporting Process

### Source-defined triggers, preconditions, postconditions and activity responsibilities

[Complete T8 with exact source rows](../documents/src-000359/tables/tbl-0008.md)

| Source item | Source definition |
| --- | --- |
| Definition | The process of enabling the movement of liquidity between sub-balances within the holdings of an account owner in order to proceed with a liquidity restriction. |
| Trigger | The process is triggered by an instructing party decision or a market infrastructure generated instruction resulting in an intra-balance movement. |
| Pre-conditions | Existence of sub-balances on a cash account held within a market infrastructure. |
| Post-conditions | A valid liquidity restriction is generated. |
| Role | Instructing party for the movement instruction.<br>Executing/Servicing Party for the receipt of the movement instruction. |


[Complete T9 with exact source rows](../documents/src-000359/tables/tbl-0009.md)

| Source item | Source definition |
| --- | --- |
| Definition | The process of informing the current status of a liquidity restriction instruction.  |
| Trigger | The process is triggered by market infrastructure when the status changes. |
| Pre-conditions | Existence of a liquidity restriction in a market infrastructure. |
| Post-conditions | A status change is generated. |
| Role | Account owner (Instructing Party) for the receipt of the Status Advice.<br>Executing/Servicing Party for the sending of the Status Advice. |


[Complete T10 with exact source rows](../documents/src-000359/tables/tbl-0010.md)

| Source item | Source definition |
| --- | --- |
| Definition | The process of informing that a liquidity restriction instruction has been successfully settled.  |
| Trigger | The process is triggered by a market infrastructure when the liquidity restriction is settled. |
| Pre-conditions | Restriction on a cash account held within a market infrastructure. |
| Post-conditions | A confirmation settled is generated. |
| Role | Account owner (Instructing Party) for the receipt of the Confirmation.<br>Executing/Servicing Party for the sending of the Confirmation. |


[Complete T11 with exact source rows](../documents/src-000359/tables/tbl-0011.md)

| Source item | Source definition |
| --- | --- |
| Definition | The process to request the modification of process indicators or other information as concerns a previously sent intra-balance movement instruction. |
| Trigger | The process is triggered by an instructing party decision to alter an intra-balance movement instruction. |
| Pre-conditions | Existence of a liquidity restriction instruction. |
| Post-conditions | A valid liquidity restriction modification request is generated. |
| Role | Instructing Party - for the modification request.<br>Executing/Servicing Party - for the receipt of the modification request. |


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


[Complete T16 with exact source rows](../documents/src-000359/tables/tbl-0016.md)

| Source item | Source definition |
| --- | --- |
| Definition | The Instructing Party asks the Servicing Party a response to a query concerning a previously sent intra-balance movement cancellation instruction/modification. |
| Trigger | The process is triggered either by the system at the end-of-date event or by the receipt of a query request.  |
| Pre-conditions | Existence of an intra-balance cancellation instruction/modification. |
| Post-conditions | The acknowledgement of the processing of the query and the generation of a valid intra-balance movement cancellation/modification report. |
| Role | Account owner (Instructing Party) for the Query.<br>Executing/Servicing Party for the Report. |


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


### Scoped participants

- [Account owner](../../../../../../../shared/reference/participants/participant-src-000359-account-owner.md)
- [Central Counterparty](../../../../../../../shared/reference/participants/participant-src-000359-central-counterparty.md)
- [Central Securities Depository](../../../../../../../shared/reference/participants/participant-src-000359-central-securities-depository.md)
- [CSDParticipant](../../../../../../../shared/reference/participants/participant-src-000359-csd-participant.md)
- [National Central Bank](../../../../../../../shared/reference/participants/participant-src-000359-national-central-bank.md)
- [PaymentAgent](../../../../../../../shared/reference/participants/participant-src-000359-payment-agent.md)
- [SystemApplication](../../../../../../../shared/reference/participants/participant-src-000359-system-application.md)

### Exact supplied message definitions

| Exact definition | Binding evidence |
| --- | --- |


Part 1 uses family identifiers or unversioned names. These exact references come separately from supplied Part 2 headings. Where no exact message is printed or otherwise established, none is invented.

### Alternatives and source limitations

- The source has no enclosing system boundary and no include/extend labels. Plain process associations and directed actor associations are preserved; no generalization is inferred.
- Source IntraBalanceManagement is green; all other process ovals are grey context. The original retains this colour distinction; the native use-case layout retains exact labels, stereotypes and connector semantics.

[issue-000047 — unresolved source wording and rendered-label differences](../../../../../../../tracking/issues.md)

<!-- INTRABALANCE-FIG-2-END -->
