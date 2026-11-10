---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p219-in-external-scenario"
title: "In external scenario"
source_locations: [{"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Creation Process ", "In external scenario"], "locator": "/w:document/w:body/w:p[219]", "paragraph_id": "P219", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Creation Process ", "In external scenario"], "locator": "/w:document/w:body/w:p[220]", "paragraph_id": "P220", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Creation Process ", "In external scenario"], "locator": "/w:document/w:body/w:p[221]", "paragraph_id": "P221", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Creation Process ", "In external scenario"], "locator": "/w:document/w:body/w:p[222]", "paragraph_id": "P222", "table_id": null}]
participants: ["participant-src-000359-servicing-executing-party-instructing-party", "participant-src-000359-servicing-executing-party", "participant-src-000359-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[17]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[18]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[19]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["camt.066.001.02", "camt.067.001.02", "camt.068.001.02"]
message_families: ["camt.066", "camt.067", "camt.068"]
search_terms: ["In external scenario", "Servicing/Executing Party Instructing Party", "Servicing/Executing Party", "Instructing Party", "camt.066", "camt.067", "camt.068"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000359-account-owner", "participant-src-000359-instructing-party", "participant-src-000359-servicing-executing-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0017.md"]
---



# In external scenario

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Servicing/Executing Party Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Servicing/Executing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P220** It applies when the cash settlement restriction sent by the Instructing party is processed and confirmed by the Servicing/Executing party.

**P222** Servicing/Executing PartyInstructing Party IntraBalanceMovementStatusAdvice (camt.067)IntraBalanceMovementInstruction (camt.066)IntraBalanceMovementConfirmation (camt.068)Servicing/Executing PartyInstructing Party IntraBalanceMovementStatusAdvice (camt.067)IntraBalanceMovementInstruction (camt.066)IntraBalanceMovementConfirmation (camt.068)

Source diagram evidence: [fig-0017](../documents/src-000359/diagrams/fig-0017.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `camt.066`, `camt.067`, `camt.068`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: BusinessTransactions / Creation Process  / In external scenario.

<!-- INTRABALANCE-FIG-17-START -->
## Curated scenario and source responsibilities

[External cash settlement restriction creation — source diagram and directions](../diagrams/intrabalance/fig-0017.md)

| Step | Sender / transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party | Servicing/Executing Party | IntraBalanceMovementInstruction (camt.066) |
| 2 | Servicing/Executing Party | Instructing Party | IntraBalanceMovementStatusAdvice (camt.067) |
| 3 | Servicing/Executing Party | Instructing Party | IntraBalanceMovementConfirmation (camt.068) |


### Narrative conditions, actions and outcomes

**src-000359 P219** — In external scenario

**src-000359 P220** — It applies when the cash settlement restriction sent by the Instructing party is processed and confirmed by the Servicing/Executing party.

**src-000359 P223** — IntraBalance Movement Instruction

**src-000359 P224** — The Instructing Party sends the instruction to the Servicing/Executing Party to allocate money from a specific cash account. This instruction contains all the information needed for the movement of cash between balances. 

**src-000359 P225** — IntraBalance Movement Status Advice

**src-000359 P226** — The Servicing/Executing Party informs the Instructing Party about the lifecycle of its instruction with its actual status.

**src-000359 P227** —  IntraBalance Movement Confirmation

**src-000359 P228** — The Servicing/Executing Party informs the Instructing Party that the Intra-balance movement has been successfully processed either in full mode or in partials. The Servicing/Executing Party presents to the Instructing Party the unique reference number assigned that identifies the restriction.

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


[Complete T20 with exact source rows](../documents/src-000359/tables/tbl-0020.md)

| Source step | Description / conditions | Initiator / responsible role |
| --- | --- | --- |
| Manage Liquidity | External process resulting in need for liquidity movements within sub balances. | Instructing Party |
| Instruct SubBalance Movement | Actual instruction for liquidity reservation. | Instructing Party |
| Process Instruction | Validation of the movement request. | Servicing/Executing Party |
| Validate | If YES, i.e., the request is valid, go to the Settle Instruction choice.<br>If NO, then Advice Status. | Servicing/Executing Party |
| Settle Instruction | Attempt to credit and debit cash account sub balances as instructed.  | Servicing/Executing Party |
| Settled | If YES, that is the request is settled then go to the Confirm Movement choice. <br>If NO, then Advice Status. | Servicing/Executing Party |
| Confirm Movement | Routes confirmation report to communication layer | Servicing/Executing Party |
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
| [camt.068.001.02](../../../../messages/camt.068.001.02/index.md) | src-000360 file page 50: 4 camt.068.001.02 IntraBalanceMovementConfirmationV02 |


Part 1 uses family identifiers or unversioned names. These exact references come separately from supplied Part 2 headings. Where no exact message is printed or otherwise established, none is invented.

### Alternatives and source limitations

- Source-native text boxes and connector objects form a complete figure. The retained Word page is the complete composite; the small WMF bank pictograms are not treated as standalone diagrams.
- Solid/dashed connectors and their directions are preserved. Source colours are recorded per message step below; colours distinguish pictured context without asserting extra protocol semantics.
- Native Mermaid boxes replace institutional pictograms; labels define the functional participants and do not bind a role to one institution.

[issue-000047 — unresolved source wording and rendered-label differences](../../../../../../../tracking/issues.md)

<!-- INTRABALANCE-FIG-17-END -->
