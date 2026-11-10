---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_sets: ["t2s-settlement-restrictions"]
flow_id: "flow-src-000380-p276-business-transactions"
title: "BusinessTransactions"
source_locations: [{"source_id": "src-000380", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[276]", "paragraph_id": "P276", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[277]", "paragraph_id": "P277", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[278]", "paragraph_id": "P278", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[279]", "paragraph_id": "P279", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[280]", "paragraph_id": "P280", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[281]", "paragraph_id": "P281", "table_id": null}]
participants: []
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["BusinessTransactions"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000380-executing-servicing-party", "participant-src-000380-instructing-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/diagrams/settlement-restrictions/fig-0014.md"]
---





# BusinessTransactions

Source context: T2S SettlementRestrictions. This reference preserves the source-defined segment and its evidence.

The curated section below links this segment to its source-defined process conditions and activity responsibilities.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P277** This section describes the message flows based on the activity diagrams documented above. It shows the typical exchanges of information in the context of a Business Transaction.

**P278** In the context of a Business Transaction, the process enables the reconciliation of (pending and posted) transactions by providing the associated data. The main processes are highlighted in green, the surrounding processes in blue. 

Source diagram evidence: [fig-0014](../documents/src-000380/diagrams/fig-0014.md). See the maintained canonical reconstruction and review evidence below.

**P281** The reconciliation communication flows can be represented as follows:

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000380](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`. Heading path: BusinessTransactions.

<!-- SETTLEMENT-RESTRICTIONS-FIG-14-START -->
## Curated source-grounded flow

[Transaction reconciliation in instruction, cancellation and modification context](../diagrams/settlement-restrictions/fig-0014.md)

### Source narrative and mode conditions

**src-000380 P276** — BusinessTransactions

**src-000380 P277** — This section describes the message flows based on the activity diagrams documented above. It shows the typical exchanges of information in the context of a Business Transaction.

**src-000380 P278** — In the context of a Business Transaction, the process enables the reconciliation of (pending and posted) transactions by providing the associated data. The main processes are highlighted in green, the surrounding processes in blue. 

**src-000380 P281** — The reconciliation communication flows can be represented as follows:

### Trigger, preconditions, postconditions and responsibilities

[Complete T8](../documents/src-000380/tables/tbl-0008.md)

| Item | Description |
| --- | --- |
| Definition | The process provides responses to queries regarding maintenance of Settlement and intra-position movement instructions (cancellation /modification request) previously sent and allows sending of reconciliation results of intra-position movement instructions (pending and posted) via query responses or via reporting. |
| Trigger | The process is triggered either by the system through a scheduled or by the receipt of a query request sent by the Instructing Party. |
| Pre-conditions | Settlement or Intra position movement instructions must exist to query within the scope of the Instructing Party and which correspond to the criteria as defined within the query and report.<br>The Instructing Party must hold necessary privileges within the Static Data configuration in order to receive reports. |
| Post-conditions | None |
| Role | Instructing Party for the query. <br>Executing Party / Servicing Party for the query response and for reporting. |


### Participants and exact definitions

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000380-instructing-party.md)
- [Executing / Servicing Party](../../../../../../../shared/reference/participants/participant-src-000380-executing-servicing-party.md)

| Canonical exact definition | Exact-definition evidence |
| --- | --- |



The exact identifiers above come from the separately cited companion Part2 in the same September2025 message-set publication. Unversioned context families are not assigned arbitrary definitions.

### Alternatives and source distinctions

- This diagram supplies transaction context, not an exact message sequence. The direct instruction-to-status path and the two request paths are distinct; it supplies no reversal node or requirement to execute both requests.
- P278 says reconciliation covers pending and posted transactions using associated data. The diagram’s bar is retained without adding execution semantics beyond the source legend. Green reconciliation is in scope; blue surrounding actions provide context.

<!-- SETTLEMENT-RESTRICTIONS-FIG-14-END -->
