---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_sets: ["t2s-securities-reference-data"]
flow_id: "flow-src-000377-p303-securities-audit-trail-query-and-report-scenario"
title: "Securities Audit Trail Query and Report Scenario"
source_locations: [{"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Query/Response Process", "Securities Audit Trail Query and Report Scenario"], "locator": "/w:document/w:body/w:p[303]", "paragraph_id": "P303", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Query/Response Process", "Securities Audit Trail Query and Report Scenario"], "locator": "/w:document/w:body/w:p[304]", "paragraph_id": "P304", "table_id": null}]
participants: []
message_mapping_evidence: [{"source_id": "src-000377", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Securities Reference Data message "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[11]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000377", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Securities Reference Data message "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[12]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.033.001.01", "reda.034.001.01"]
message_families: ["reda.033", "reda.034"]
search_terms: ["Securities Audit Trail Query and Report Scenario", "reda.033", "reda.034"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000377-executing-servicing-party", "participant-src-000377-instructing-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0019.md"]
---







# Securities Audit Trail Query and Report Scenario

Source context: T2S SecuritiesReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P304** Securities Audit Trail Query (reda.033)Query/Response ProcessSecurities Audit Trail Report (reda.034): ERRORSecurities Audit Trail Report (reda.034)Securities Audit Trail Query (reda.033)Query/Response ProcessSecurities Audit Trail Report (reda.034): ERRORSecurities Audit Trail Report (reda.034)

Source diagram evidence: [fig-0019](../documents/src-000377/diagrams/fig-0019.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `reda.033`, `reda.034`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000377](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Heading path: BusinessTransactions / Query/Response Process / Securities Audit Trail Query and Report Scenario.

<!-- SECREF-FIG-19-START -->
## Curated source-grounded flow

[Securities audit-trail query and report exchange](../diagrams/securities-reference/fig-0019.md)

| Picture step | Sender / responsible transmitter | Receiver | Source message |
| --- | --- | --- | --- |
| 1 | Instructing Party | Executing/Servicing Party | Securities Audit Trail Query (reda.033) |
| 2 | Executing/Servicing Party | Instructing Party | Securities Audit Trail Report (reda.034): ERROR |
| 3 | Executing/Servicing Party | Instructing Party | Securities Audit Trail Report (reda.034) |


### Source narrative, conditions and alternatives

**src-000377 P303** — Securities Audit Trail Query and Report Scenario

**src-000377 P305** — Securities Audit Trail Query

**src-000377 P306** — The Instructing Party sends an instruction to the Executing/Servicing Party to run a query according to specified criteria’s to retrieve the complete audit trail on a specific security.

**src-000377 P307** — Securities Audit Trail Report

**src-000377 P308** — Depending on the query criteria, it is possible that the processing will take more than a certain time or that the result of the query will be empty due to wrong combination of criteria or no result set. In this case, an error message within a query response message is sent to the Instructing Party.

**src-000377 P309** — Securities Audit Trail Report

**src-000377 P310** — The Executing/Servicing Party sends a query response that meets the specified criteria to the Instructing Party.

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
| [reda.033.001.01](../../../../messages/reda.033.001.01/index.md) | src-000377 heading(s) P892 | src-000378 March2024 file page 129 |
| [reda.034.001.01](../../../../messages/reda.034.001.01/index.md) | src-000377 heading(s) P915 | src-000378 March2024 file page 134 |



### Limits and source distinctions

- The query retrieves the complete audit trail on a specific security (P306). Error conditions and successful-result descriptions are alternatives in P308/P310, without a numeric timeout. No mandatory dual response is inferred.
- Source377 is June2021; companion source378 is March2024. Matching full identifiers do not erase the publication difference (issue-000010).
- The original figure is assembled from native Word connector/text objects and institutional pictograms. The retained full Word page is the complete composite; its pictograms alone are not counted as diagrams.
- Native Mermaid participant boxes replace the institutional drawings; sender and receiver roles, solid/dashed lines and visible arrow direction remain explicit. No institution is equated with a functional role.

<!-- SECREF-FIG-19-END -->
