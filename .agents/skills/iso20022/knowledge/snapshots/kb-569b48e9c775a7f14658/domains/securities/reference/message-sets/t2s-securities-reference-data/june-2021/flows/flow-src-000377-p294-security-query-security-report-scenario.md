---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_sets: ["t2s-securities-reference-data"]
flow_id: "flow-src-000377-p294-security-query-security-report-scenario"
title: "Security Query/Security Report Scenario"
source_locations: [{"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Query/Response Process", "Security Query/Security Report Scenario"], "locator": "/w:document/w:body/w:p[294]", "paragraph_id": "P294", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Query/Response Process", "Security Query/Security Report Scenario"], "locator": "/w:document/w:body/w:p[295]", "paragraph_id": "P295", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Query/Response Process", "Security Query/Security Report Scenario"], "locator": "/w:document/w:body/w:p[296]", "paragraph_id": "P296", "table_id": null}]
participants: []
message_mapping_evidence: [{"source_id": "src-000377", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Securities Reference Data message "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[8]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000377", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Securities Reference Data message "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[9]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.010.001.01", "reda.012.001.01"]
message_families: ["reda.010", "reda.012"]
search_terms: ["Security Query/Security Report Scenario", "reda.010", "reda.012"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000377-executing-servicing-party", "participant-src-000377-instructing-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0018.md"]
---







# Security Query/Security Report Scenario

Source context: T2S SecuritiesReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P296** Security Query (reda.010)Query/Report ProcessSecurity Report (reda.012): ERRORSecurity Report (reda.012)Security Query (reda.010)Query/Report ProcessSecurity Report (reda.012): ERRORSecurity Report (reda.012)

Source diagram evidence: [fig-0018](../documents/src-000377/diagrams/fig-0018.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `reda.010`, `reda.012`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000377](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Heading path: BusinessTransactions / Query/Response Process / Security Query/Security Report Scenario.

<!-- SECREF-FIG-18-START -->
## Curated source-grounded flow

[Security query and report exchange](../diagrams/securities-reference/fig-0018.md)

| Picture step | Sender / responsible transmitter | Receiver | Source message |
| --- | --- | --- | --- |
| 1 | Instructing Party | Executing/Servicing Party | Security Query (reda.010) |
| 2 | Executing/Servicing Party | Instructing Party | Security Report (reda.012): ERROR |
| 3 | Executing/Servicing Party | Instructing Party | Security Report (reda.012) |


### Source narrative, conditions and alternatives

**src-000377 P294** — Security Query/Security Report Scenario

**src-000377 P297** — Security Query

**src-000377 P298** — The Instructing Party sends an instruction to the Executing/Servicing Party to run a query according to specified criteria.

**src-000377 P299** — Security Report 

**src-000377 P300** — Depending on the query criteria, it is possible that the processing will take more than a certain time or that the result of the query will be empty due to wrong combination of criteria or no result set. In this case, an error message within a query response message is sent to the Instructing Party.

**src-000377 P301** — Security Report 

**src-000377 P302** — The Executing/Servicing Party sends a query response that meets the specified criteria to the Instructing Party.

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
- [Executing/Servicing Party](../../../../../../../shared/reference/participants/participant-src-000377-executing-servicing-party.md)

| Canonical exact definition | Same-publication identifier evidence | Companion definition |
| --- | --- | --- |
| [reda.010.001.01](../../../../messages/reda.010.001.01/index.md) | src-000377 heading(s) P744 | src-000378 March2024 file page 77 |
| [reda.012.001.01](../../../../messages/reda.012.001.01/index.md) | src-000377 heading(s) P774 | src-000378 March2024 file page 94 |



### Limits and source distinctions

- The error path is conditional on excessive processing time, an unsuitable criteria combination or no result set (P300). The picture does not use an alt frame, so both literal arrows remain without declaring both responses mandatory. No timeout threshold is supplied.
- Source377 is June2021; companion source378 is March2024. Matching full identifiers do not erase the publication difference (issue-000010).
- The original figure is assembled from native Word connector/text objects and institutional pictograms. The retained full Word page is the complete composite; its pictograms alone are not counted as diagrams.
- Native Mermaid participant boxes replace the institutional drawings; sender and receiver roles, solid/dashed lines and visible arrow direction remain explicit. No institution is equated with a functional role.

<!-- SECREF-FIG-18-END -->
