---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_sets: ["t2s-securities-reference-data"]
flow_id: "flow-src-000377-p162-query-query-response-process"
title: "Query/Query Response Process"
source_locations: [{"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Query/Query Response Process"], "locator": "/w:document/w:body/w:p[162]", "paragraph_id": "P162", "table_id": null}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Query/Query Response Process"], "locator": "/w:document/w:body/w:p[163]", "paragraph_id": "P163", "table_id": null}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Query/Query Response Process"], "locator": "/w:document/w:body/w:tbl[17]", "paragraph_id": null, "table_id": "T17"}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Query/Query Response Process"], "locator": "/w:document/w:body/w:p[164]", "paragraph_id": "P164", "table_id": null}]
participants: ["participant-src-000377-executing-servicing-party", "participant-src-000377-instructing-party"]
message_mapping_evidence: []
message_ids: ["reda.010.001.01", "reda.012.001.01", "reda.033.001.01", "reda.034.001.01"]
message_families: []
search_terms: ["Query/Query Response Process", "Executing/Servicing Party", "Instructing Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000377-executing-party", "participant-src-000377-executing-servicing-party", "participant-src-000377-instructing-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0010.md"]
---







# Query/Query Response Process

Source context: T2S SecuritiesReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing/Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000377-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000377-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0010](../documents/src-000377/diagrams/fig-0010.md). Mermaid reconstruction and visual review are pending.

Source table [T17](../documents/src-000377/tables/tbl-0017.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Instruction | Instructing Party instructs Executing/Servicing Party to run a query or Audit Trail Query. | Instructing Party |
| Process query | Executing/Servicing Party processes the request.<br>In case the processing of the query takes too much time or cannot give any positive response, the Executing/Servicing Party sends an error message back to the Instructing Party with the error code and the related explanation. | Executing/Servicing Party |
| Response | Executing/Services Party sends the response to the Instructing Party according to query results. | Executing/Servicing Party |
| Monitor Process | Instructing Party monitors the status of the instruction. | Instructing Party |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000377](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Heading path: Description of BusinessActivities / Query/Query Response Process.

<!-- SECREF-FIG-10-START -->
## Curated source-grounded flow

[Security query and audit-trail query activity](../diagrams/securities-reference/fig-0010.md)

### Source narrative, conditions and alternatives

**src-000377 P162** — Query/Query Response Process

### Triggers, preconditions, postconditions and activity definitions

[Complete T11](../documents/src-000377/tables/tbl-0011.md)

| Item | Description |
| --- | --- |
| Definition | The Instructing Party asks the Executing/Servicing Party a response to a query or to an Audit Trail query. |
| Trigger | The process is triggered when the Instructing Party sends a Security Query message or a Securities Audit Trail Query message. |
| Pre-conditions | The query type must be known by the Instructing party and the Executing/Servicing Party. |
| Post-conditions | The Security Report message including all of the retrieved securities records or the Securities Audit Trail Report message with all the requested audit trail information. |
| Role | Instructing Party |


[Complete T17](../documents/src-000377/tables/tbl-0017.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Instruction | Instructing Party instructs Executing/Servicing Party to run a query or Audit Trail Query. | Instructing Party |
| Process query | Executing/Servicing Party processes the request.<br>In case the processing of the query takes too much time or cannot give any positive response, the Executing/Servicing Party sends an error message back to the Instructing Party with the error code and the related explanation. | Executing/Servicing Party |
| Response | Executing/Services Party sends the response to the Instructing Party according to query results. | Executing/Servicing Party |
| Monitor Process | Instructing Party monitors the status of the instruction. | Instructing Party |


### Scoped participants and exact message references

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000377-instructing-party.md)
- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000377-executing-party.md)
- [Executing/Servicing Party](../../../../../../../shared/reference/participants/participant-src-000377-executing-servicing-party.md)

| Canonical exact definition | Same-publication identifier evidence | Companion definition |
| --- | --- | --- |
| [reda.010.001.01](../../../../messages/reda.010.001.01/index.md) | src-000377 heading(s) P744 | src-000378 March2024 file page 77 |
| [reda.012.001.01](../../../../messages/reda.012.001.01/index.md) | src-000377 heading(s) P774 | src-000378 March2024 file page 94 |
| [reda.033.001.01](../../../../messages/reda.033.001.01/index.md) | src-000377 heading(s) P892 | src-000378 March2024 file page 129 |
| [reda.034.001.01](../../../../messages/reda.034.001.01/index.md) | src-000377 heading(s) P915 | src-000378 March2024 file page 134 |



### Limits and source distinctions

- No start/end glyph or error decision is supplied in this activity picture. The linked table/narrative preserves additional error conditions without adding unseen diagram nodes.
- Source377 is June2021; companion source378 is March2024. Matching full identifiers do not erase the publication difference (issue-000010).

<!-- SECREF-FIG-10-END -->
