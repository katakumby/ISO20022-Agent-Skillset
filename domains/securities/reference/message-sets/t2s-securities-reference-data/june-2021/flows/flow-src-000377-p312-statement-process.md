---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_sets: ["t2s-securities-reference-data"]
flow_id: "flow-src-000377-p312-statement-process"
title: "Statement Process"
source_locations: [{"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Statement Process"], "locator": "/w:document/w:body/w:p[312]", "paragraph_id": "P312", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Statement Process"], "locator": "/w:document/w:body/w:p[313]", "paragraph_id": "P313", "table_id": null}]
participants: []
message_mapping_evidence: [{"source_id": "src-000377", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Securities Reference Data message "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[10]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.009.001.01"]
message_families: ["reda.009"]
search_terms: ["Statement Process", "reda.009"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000377-executing-servicing-party", "participant-src-000377-instructing-party", "participant-src-000377-recipient-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0020.md"]
---







# Statement Process

Source context: T2S SecuritiesReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P313** Security Activity Advice (reda.009)Statement ProcessSecurity Activity Advice (reda.009)Statement Process

Source diagram evidence: [fig-0020](../documents/src-000377/diagrams/fig-0020.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `reda.009`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000377](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Heading path: BusinessTransactions / Statement Process.

<!-- SECREF-FIG-20-START -->
## Curated source-grounded flow

[Unsolicited security activity advice](../diagrams/securities-reference/fig-0020.md)

| Picture step | Sender / responsible transmitter | Receiver | Source message |
| --- | --- | --- | --- |
| 1 | Executing/Servicing Party | Instructing Party | Security Activity Advice (reda.009) |


### Source narrative, conditions and alternatives

**src-000377 P312** — Statement Process

**src-000377 P314** — Security Activity Advice 

**src-000377 P315** — The Executing/Servicing Party sends a statement to the Instructing Party containing information on changes occurred for securities reference data during the business day.

**src-000377 P316** — The statement is sent unilaterally in an unsolicited manner.

### Triggers, preconditions, postconditions and activity definitions

[Complete T12](../documents/src-000377/tables/tbl-0012.md)

| Item | Description |
| --- | --- |
| Definition | The Recipient Party receives a Security Activity Advice statement which has been automatically produced by the Executing/Servicing Party. |
| Trigger | The process is triggered automatically. |
| Pre-conditions | A standing instruction is in place at the Executing/Servicing Party for sending of the statement. |
| Post-conditions | The acknowledgement of the sending of the statement. |
| Role | Executing/Servicing Party |


[Complete T18](../documents/src-000377/tables/tbl-0018.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Instruction | Instructing Party might instruct Executing/Servicing Party to run a statement.<br>This is not covered by the current process as NO message will be created to cover this. | Instructing Party |
| Process statement | Executing/Servicing Party processes the statement. | Executing/Servicing Party |
| Response | Executing/Servicing Party sends the statement to the Instructing Party. | Executing/Servicing Party |
| Monitor Process | Instructing Party monitors the status of the instruction. | Instructing Party |


### Scoped participants and exact message references

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000377-instructing-party.md)
- [Executing/Servicing Party](../../../../../../../shared/reference/participants/participant-src-000377-executing-servicing-party.md)
- [Recipient Party](../../../../../../../shared/reference/participants/participant-src-000377-recipient-party.md)

| Canonical exact definition | Same-publication identifier evidence | Companion definition |
| --- | --- | --- |
| [reda.009.001.01](../../../../messages/reda.009.001.01/index.md) | src-000377 heading(s) P859 | src-000378 March2024 file page 71 |



### Limits and source distinctions

- The source statement covers securities-reference-data changes during the business day and is sent unilaterally in an unsolicited manner (P315–P316). T12 requires a standing instruction; T18 says an initiating instruction is outside the message scope.
- Source377 is June2021; companion source378 is March2024. Matching full identifiers do not erase the publication difference (issue-000010).
- The original figure is assembled from native Word connector/text objects and institutional pictograms. The retained full Word page is the complete composite; its pictograms alone are not counted as diagrams.
- Native Mermaid participant boxes replace the institutional drawings; sender and receiver roles, solid/dashed lines and visible arrow direction remain explicit. No institution is equated with a functional role.

<!-- SECREF-FIG-20-END -->
