---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p193-internal-scenario"
title: "Internal Scenario"
source_locations: [{"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Process", "Internal Scenario"], "locator": "/w:document/w:body/w:p[193]", "paragraph_id": "P193", "table_id": null}, {"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Process", "Internal Scenario"], "locator": "/w:document/w:body/w:p[194]", "paragraph_id": "P194", "table_id": null}, {"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Process", "Internal Scenario"], "locator": "/w:document/w:body/w:p[195]", "paragraph_id": "P195", "table_id": null}, {"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Process", "Internal Scenario"], "locator": "/w:document/w:body/w:tbl[21]", "paragraph_id": null, "table_id": "T21"}, {"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Process", "Internal Scenario"], "locator": "/w:document/w:body/w:p[196]", "paragraph_id": "P196", "table_id": null}]
participants: ["participant-src-000359-servicing-executing-party", "participant-src-000359-third-party"]
message_mapping_evidence: []
message_ids: ["camt.066.001.02", "camt.067.001.02", "camt.068.001.02"]
message_families: []
search_terms: ["Internal Scenario", "Servicing/Executing Party", "Third Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000359-account-owner", "participant-src-000359-servicing-executing-party", "participant-src-000359-third-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0011.md"]
---



# Internal Scenario

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Servicing/Executing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Third Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-third-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P194** It covers the internal scenario where the servicing/executing party initiates a movement in response to settlement activity and must subsequently inform a third party of activity on sub balances within their holdings.

Source diagram evidence: [fig-0011](../documents/src-000359/diagrams/fig-0011.md). Mermaid reconstruction and visual review are pending.

Source table [T21](../documents/src-000359/tables/tbl-0021.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Process Instruction | Process Instruction:  Validation of the movement request. | Servicing/Executing Party |
| Settle Instruction | Attempt to credit and debit cash account sub balances as instructed.  | Servicing/Executing Party |
| Settled | Settled If YES, i.e., the request is settled then go to the Confirm Movement choice.<br>If NO, then Advice Status. | Servicing/Executing Party |
| Process Instruction | Validation of the movement request. | Servicing/Executing Party |
| Confirm Movement | Routes confirmation report to communication layer | Servicing/Executing Party |
| Advice Status | Routes status report to communication layer. | Servicing/Executing Party |
| Monitor | Check for incoming communications associated with original instruction.<br> | Third Party |
| Reconcile | External process reconciling impact of current status of original instruction. | Third Party |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: Description of BusinessActivities / Intra-Balance Movement Process / Internal Scenario.

<!-- INTRABALANCE-FIG-11-START -->
## Curated scenario and source responsibilities

[Internal intra-balance movement activity — source diagram and directions](../diagrams/intrabalance/fig-0011.md)

### Narrative conditions, actions and outcomes

**src-000359 P193** — Internal Scenario

**src-000359 P194** — It covers the internal scenario where the servicing/executing party initiates a movement in response to settlement activity and must subsequently inform a third party of activity on sub balances within their holdings.

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


[Complete T21 with exact source rows](../documents/src-000359/tables/tbl-0021.md)

| Source step | Description / conditions | Initiator / responsible role |
| --- | --- | --- |
| Process Instruction | Process Instruction:  Validation of the movement request. | Servicing/Executing Party |
| Settle Instruction | Attempt to credit and debit cash account sub balances as instructed.  | Servicing/Executing Party |
| Settled | Settled If YES, i.e., the request is settled then go to the Confirm Movement choice.<br>If NO, then Advice Status. | Servicing/Executing Party |
| Process Instruction | Validation of the movement request. | Servicing/Executing Party |
| Confirm Movement | Routes confirmation report to communication layer | Servicing/Executing Party |
| Advice Status | Routes status report to communication layer. | Servicing/Executing Party |
| Monitor | Check for incoming communications associated with original instruction.<br> | Third Party |
| Reconcile | External process reconciling impact of current status of original instruction. | Third Party |


### Scoped participants

- [Account owner](../../../../../../../shared/reference/participants/participant-src-000359-account-owner.md)
- [Servicing/Executing Party](../../../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party.md)
- [Third Party](../../../../../../../shared/reference/participants/participant-src-000359-third-party.md)

### Exact supplied message definitions

| Exact definition | Binding evidence |
| --- | --- |
| [camt.066.001.02](../../../../messages/camt.066.001.02/index.md) | src-000360 file page 10: 2 camt.066.001.02 IntraBalanceMovementInstructionV02 |
| [camt.067.001.02](../../../../messages/camt.067.001.02/index.md) | src-000360 file page 31: 3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 |
| [camt.068.001.02](../../../../messages/camt.068.001.02/index.md) | src-000360 file page 50: 4 camt.068.001.02 IntraBalanceMovementConfirmationV02 |


Part 1 uses family identifiers or unversioned names. These exact references come separately from supplied Part 2 headings. Where no exact message is printed or otherwise established, none is invented.

### Alternatives and source limitations

- T21 repeats Process Instruction as two table rows; the picture has one occurrence. The table is preserved intact, without fabricating a second picture activity.
- The picture and T21 assign Monitor/Reconcile to Third Party. Transaction narrative P235/P237 instead says Instructing Party; no global equivalence is inferred.
- Native Mermaid flowchart subgraphs retain source swimlane responsibility. Source start/end glyphs, labelled decisions and bars remain explicit. T19 defines bars as parallel actions; the original uses some bars at converging alternative paths, so no extra execution semantics are inferred.

[issue-000047 — unresolved source wording and rendered-label differences](../../../../../../../tracking/issues.md)

<!-- INTRABALANCE-FIG-11-END -->
