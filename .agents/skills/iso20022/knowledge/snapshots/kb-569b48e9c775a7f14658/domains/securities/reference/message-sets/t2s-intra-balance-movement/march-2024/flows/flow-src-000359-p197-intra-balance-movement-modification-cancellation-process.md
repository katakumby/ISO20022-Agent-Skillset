---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p197-intra-balance-movement-modification-cancellation-process"
title: "Intra-Balance Movement Modification/Cancellation Process"
source_locations: [{"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Modification/Cancellation Process"], "locator": "/w:document/w:body/w:p[197]", "paragraph_id": "P197", "table_id": null}, {"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Modification/Cancellation Process"], "locator": "/w:document/w:body/w:p[198]", "paragraph_id": "P198", "table_id": null}, {"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Modification/Cancellation Process"], "locator": "/w:document/w:body/w:tbl[22]", "paragraph_id": null, "table_id": "T22"}]
participants: ["participant-src-000359-servicing-executing-party", "participant-src-000359-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[17]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["camt.072.001.02", "camt.073.001.02", "camt.074.001.02", "camt.075.001.02"]
message_families: ["camt.066"]
search_terms: ["Intra-Balance Movement Modification/Cancellation Process", "Servicing/Executing Party", "Instructing Party", "camt.066"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000359-account-owner", "participant-src-000359-instructing-party", "participant-src-000359-servicing-executing-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0012.md"]
---



# Intra-Balance Movement Modification/Cancellation Process

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Servicing/Executing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0012](../documents/src-000359/diagrams/fig-0012.md). Mermaid reconstruction and visual review are pending.

Source table [T22](../documents/src-000359/tables/tbl-0022.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Manage Liquidity | External process resulting in need for liquidity movements within sub balances. | Instructing Party |
| Request Intra-Balance Movement Modification/Cancellation  | Actual request for liquidity reservation (intra-balance movement) modification or cancellation. | Instructing Party |
| Process Instruction | Validation of the movement request. | Servicing/Executing Party |
| Validate | Validated If YES, i.e., the request is valid, go to the Advice Status choice and to the Modify/Cancel Intra-Balance Movement Request choice.<br>If NO, then Advice Status. | Servicing/Executing Party |
| Modify/Cancel Intra-Balance Movement Instruction | Attempt to modify/cancel a specific liquidity reservation instruction | Servicing/Executing Party |
| Executed | Executed If YES, i.e., the request is successfully executed then respond with positive Advice Status choice. <br>If NO, then Advice Status. | Servicing/Executing Party |
| Advice Status | Routes status report to communication layer. | Servicing/Executing Party |
| Monitor | Check for incoming communications associated with original instruction. | Instructing Party |
| Reconcile | External process reconciling impact of current status of original instruction. | Instructing Party |

## Messages and alternative paths

Source-supported message family mentions: `camt.066`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: Description of BusinessActivities / Intra-Balance Movement Modification/Cancellation Process.

<!-- INTRABALANCE-FIG-12-START -->
## Curated scenario and source responsibilities

[Modification and cancellation activity — source diagram and directions](../diagrams/intrabalance/fig-0012.md)

### Narrative conditions, actions and outcomes

**src-000359 P197** — Intra-Balance Movement Modification/Cancellation Process

**src-000359 P199** — Intra-Balance Movement Modification/Cancellation Query/Report Process

### Source-defined triggers, preconditions, postconditions and activity responsibilities

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


[Complete T22 with exact source rows](../documents/src-000359/tables/tbl-0022.md)

| Source step | Description / conditions | Initiator / responsible role |
| --- | --- | --- |
| Manage Liquidity | External process resulting in need for liquidity movements within sub balances. | Instructing Party |
| Request Intra-Balance Movement Modification/Cancellation  | Actual request for liquidity reservation (intra-balance movement) modification or cancellation. | Instructing Party |
| Process Instruction | Validation of the movement request. | Servicing/Executing Party |
| Validate | Validated If YES, i.e., the request is valid, go to the Advice Status choice and to the Modify/Cancel Intra-Balance Movement Request choice.<br>If NO, then Advice Status. | Servicing/Executing Party |
| Modify/Cancel Intra-Balance Movement Instruction | Attempt to modify/cancel a specific liquidity reservation instruction | Servicing/Executing Party |
| Executed | Executed If YES, i.e., the request is successfully executed then respond with positive Advice Status choice. <br>If NO, then Advice Status. | Servicing/Executing Party |
| Advice Status | Routes status report to communication layer. | Servicing/Executing Party |
| Monitor | Check for incoming communications associated with original instruction. | Instructing Party |
| Reconcile | External process reconciling impact of current status of original instruction. | Instructing Party |


### Scoped participants

- [Account owner](../../../../../../../shared/reference/participants/participant-src-000359-account-owner.md)
- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000359-instructing-party.md)
- [Servicing/Executing Party](../../../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party.md)

### Exact supplied message definitions

| Exact definition | Binding evidence |
| --- | --- |
| [camt.072.001.02](../../../../messages/camt.072.001.02/index.md) | src-000360 file page 66: 5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 |
| [camt.073.001.02](../../../../messages/camt.073.001.02/index.md) | src-000360 file page 90: 6 camt.073.001.02 IntraBalanceMovementModificationRequestStatusAdviceV02 |
| [camt.074.001.02](../../../../messages/camt.074.001.02/index.md) | src-000360 file page 115: 7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 |
| [camt.075.001.02](../../../../messages/camt.075.001.02/index.md) | src-000360 file page 132: 8 camt.075.001.02 IntraBalanceMovementCancellationRequestStatusAdviceV02 |


Part 1 uses family identifiers or unversioned names. These exact references come separately from supplied Part 2 headings. Where no exact message is printed or otherwise established, none is invented.

### Alternatives and source limitations

- Both Executed? branches feed Advise Status. T22 distinguishes a positive advice when execution succeeds; the picture does not supply separate status-message nodes.
- Native Mermaid flowchart subgraphs retain source swimlane responsibility. Source start/end glyphs, labelled decisions and bars remain explicit. T19 defines bars as parallel actions; the original uses some bars at converging alternative paths, so no extra execution semantics are inferred.

[issue-000047 — unresolved source wording and rendered-label differences](../../../../../../../tracking/issues.md)

<!-- INTRABALANCE-FIG-12-END -->
