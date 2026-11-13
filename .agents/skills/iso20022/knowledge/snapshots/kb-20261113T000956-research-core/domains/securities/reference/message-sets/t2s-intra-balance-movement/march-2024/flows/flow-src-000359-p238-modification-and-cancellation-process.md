---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p238-modification-and-cancellation-process"
title: "Modification and Cancellation Process"
source_locations: [{"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Modification and Cancellation Process "], "locator": "/w:document/w:body/w:p[238]", "paragraph_id": "P238", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Modification and Cancellation Process "], "locator": "/w:document/w:body/w:p[239]", "paragraph_id": "P239", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Modification and Cancellation Process "], "locator": "/w:document/w:body/w:p[240]", "paragraph_id": "P240", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Modification and Cancellation Process "], "locator": "/w:document/w:body/w:p[241]", "paragraph_id": "P241", "table_id": null}]
participants: ["participant-src-000359-servicing-executing-party-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[17]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[18]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[6]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[7]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[8]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["camt.066.001.02", "camt.067.001.02", "camt.072.001.02", "camt.073.001.02", "camt.074.001.02", "camt.075.001.02"]
message_families: ["camt.066", "camt.067", "camt.072", "camt.073", "camt.074", "camt.075"]
search_terms: ["Modification and Cancellation Process", "Servicing/Executing Party Instructing Party", "camt.066", "camt.067", "camt.072", "camt.073", "camt.074", "camt.075"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000359-account-owner", "participant-src-000359-instructing-party", "participant-src-000359-servicing-executing-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0019.md"]
---



# Modification and Cancellation Process

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Servicing/Executing Party Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P240** Servicing/Executing PartyInstructing Party IntraBalanceMovementStatusAdvice (camt.067) IntraBalanceMovementInstruction (camt.066)IntraBalanceMovementModificationRequest (camt.072)IntraBalanceMovementModificationRequestStatusAdvice (camt.073)IntraBalanceMovementCancellationRequest (camt.074)IntraBalanceMovementCancellationRequestStatusAdvice (camt.075)Servicing/Executing PartyInstructing Party IntraBalanceMovementStatusAdvice (camt.067) IntraBalanceMovementInstruction (camt.066)IntraBalanceMovementModificationRequest (camt.072)IntraBalanceMovementModificationRequestStatusAdvice (camt.073)IntraBalanceMovementCancellationRequest (camt.074)IntraBalanceMovementCancellationRequestStatusAdvice (camt.075)

Source diagram evidence: [fig-0019](../documents/src-000359/diagrams/fig-0019.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `camt.066`, `camt.067`, `camt.072`, `camt.073`, `camt.074`, `camt.075`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: BusinessTransactions / Modification and Cancellation Process .

<!-- INTRABALANCE-FIG-19-START -->
## Curated scenario and source responsibilities

[Modification and cancellation transaction exchange — source diagram and directions](../diagrams/intrabalance/fig-0019.md)

| Step | Sender / transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party | Servicing/Executing Party | IntraBalanceMovementInstruction (camt.066) |
| 2 | Servicing/Executing Party | Instructing Party | IntraBalanceMovementStatusAdvice (camt.067) |
| 3 | Instructing Party | Servicing/Executing Party | IntraBalanceMovementModificationRequest (camt.072) |
| 4 | Servicing/Executing Party | Instructing Party | IntraBalanceMovementModificationRequestStatusAdvice (camt.073) |
| 5 | Instructing Party | Servicing/Executing Party | IntraBalanceMovementCancellationRequest (camt.074) |
| 6 | Servicing/Executing Party | Instructing Party | IntraBalanceMovementCancellationRequestStatusAdvice (camt.075) |


### Narrative conditions, actions and outcomes

**src-000359 P238** — Modification and Cancellation Process 

**src-000359 P242** — IntraBalance Movement Instruction

**src-000359 P243** — The Instructing Party sends the instruction to the Servicing/Executing Party to allocate money from a specific cash account. This instruction contains all the information needed for the movement of cash between balances. 

**src-000359 P244** — IntraBalance Movement Status Advice

**src-000359 P245** — The Servicing/Executing Party informs the Instructing Party about the lifecycle of its instruction with its actual status.

**src-000359 P246** — IntraBalance Movement Modification Request

**src-000359 P247** — The instructing Party requests the modification of a processing indicator or other information of the intra-balance movement instruction previously sent.

**src-000359 P248** — IntraBalance Movement Modification Request Status Advice

**src-000359 P249** — The Servicing/Executing Party informs the Instructing Party about the status of the intra-balance movement modification request previously sent.

**src-000359 P250** — IntraBalance Movement Cancellation Request

**src-000359 P251** — The instructing Party requests the cancellation of the intra-balance movement instruction previously sent.

**src-000359 P252** — IntraBalance Movement Cancellation Request Status Advice

**src-000359 P253** — The Servicing/Executing Party informs the Instructing Party about the status of the intra-balance movement cancellation request previously sent.

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
| [camt.066.001.02](../../../../messages/camt.066.001.02/index.md) | src-000360 file page 10: 2 camt.066.001.02 IntraBalanceMovementInstructionV02 |
| [camt.067.001.02](../../../../messages/camt.067.001.02/index.md) | src-000360 file page 31: 3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 |
| [camt.072.001.02](../../../../messages/camt.072.001.02/index.md) | src-000360 file page 66: 5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 |
| [camt.073.001.02](../../../../messages/camt.073.001.02/index.md) | src-000360 file page 90: 6 camt.073.001.02 IntraBalanceMovementModificationRequestStatusAdviceV02 |
| [camt.074.001.02](../../../../messages/camt.074.001.02/index.md) | src-000360 file page 115: 7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 |
| [camt.075.001.02](../../../../messages/camt.075.001.02/index.md) | src-000360 file page 132: 8 camt.075.001.02 IntraBalanceMovementCancellationRequestStatusAdviceV02 |


Part 1 uses family identifiers or unversioned names. These exact references come separately from supplied Part 2 headings. Where no exact message is printed or otherwise established, none is invented.

### Alternatives and source limitations

- Long labels and some code suffixes are clipped in the local Word rendering. Their complete source text is preserved in the drawing text at P240; reconstructed labels recover that text. The picture supplies no alt frame making modification and cancellation alternatives, so none is invented.
- Source-native text boxes and connector objects form a complete figure. The retained Word page is the complete composite; the small WMF bank pictograms are not treated as standalone diagrams.
- Solid/dashed connectors and their directions are preserved. Source colours are recorded per message step below; colours distinguish pictured context without asserting extra protocol semantics.
- Native Mermaid boxes replace institutional pictograms; labels define the functional participants and do not bind a role to one institution.

[issue-000047 — unresolved source wording and rendered-label differences](../../../../../../../tracking/issues.md)

<!-- INTRABALANCE-FIG-19-END -->
