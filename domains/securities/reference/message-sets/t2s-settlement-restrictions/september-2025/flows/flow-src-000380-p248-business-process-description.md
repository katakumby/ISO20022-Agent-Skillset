---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_sets: ["t2s-settlement-restrictions"]
flow_id: "flow-src-000380-p248-business-process-description"
title: "BusinessProcess Description"
source_locations: [{"source_id": "src-000380", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[248]", "paragraph_id": "P248", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[249]", "paragraph_id": "P249", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[250]", "paragraph_id": "P250", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[251]", "paragraph_id": "P251", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[252]", "paragraph_id": "P252", "table_id": null}]
participants: []
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["BusinessProcess Description"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000380-executing-servicing-party", "participant-src-000380-instructing-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/diagrams/settlement-restrictions/fig-0005.md"]
---





# BusinessProcess Description

Source context: T2S SettlementRestrictions. This reference preserves the source-defined segment and its evidence.

The curated section below links this segment to its source-defined process conditions and activity responsibilities.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P249** This diagram represents the high level BusinessProcesses. The main processes are highlighted in green, the surrounding processes in blue.

Source diagram evidence: [fig-0005](../documents/src-000380/diagrams/fig-0005.md). See the maintained canonical reconstruction and review evidence below.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000380](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`. Heading path: BusinessProcess Description.

<!-- SETTLEMENT-RESTRICTIONS-FIG-5-START -->
## Curated source-grounded flow

[Settlement and reconciliation high-level process relationships](../diagrams/settlement-restrictions/fig-0005.md)

### Source narrative and mode conditions

**src-000380 P248** — BusinessProcess Description

**src-000380 P249** — This diagram represents the high level BusinessProcesses. The main processes are highlighted in green, the surrounding processes in blue.

**src-000380 P253** — Query Report Process

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

- Native Mermaid12 use-case notation preserves the source process ellipses and rectangular root. Ordinary directed associations retain the source arrow direction; no include/extend or inheritance relation is invented.
- Green reconciliation/reporting/query-response are in scope; the other blue processes provide context (P249). Confirmation connects to Reversal and Status reporting. Cancellation request connects to Status reporting; it is not equated with Reversal.
- T8 gives query and scheduled-system-event triggers, existing instructions within the party’s scope and matching criteria, and Static Data privileges for reports. It states postconditions None, rather than an inferred settlement outcome.

<!-- SETTLEMENT-RESTRICTIONS-FIG-5-END -->
