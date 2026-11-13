---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_sets: ["t2s-securities-reference-data"]
flow_id: "flow-src-000377-p143-business-process-description"
title: "BusinessProcess Description"
source_locations: [{"source_id": "src-000377", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[143]", "paragraph_id": "P143", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[144]", "paragraph_id": "P144", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[145]", "paragraph_id": "P145", "table_id": null}]
participants: []
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["BusinessProcess Description"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
participant_ids: ["participant-src-000377-executing-servicing-party", "participant-src-000377-instructing-party"]
diagram_paths: ["domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0002.md"]
---







# BusinessProcess Description

Source context: T2S SecuritiesReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P144** This diagram represents the high level BusinessProcesses, used to describe the high-level scope of T2S concerning “Securities Reference Data” and is not to be exhaustive.

Source diagram evidence: [fig-0002](../documents/src-000377/diagrams/fig-0002.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000377](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Heading path: BusinessProcess Description.

<!-- SECREF-FIG-2-START -->
## Curated source-grounded flow

[Securities reference-data high-level processes](../diagrams/securities-reference/fig-0002.md)

### Source narrative, conditions and alternatives

**src-000377 P143** — BusinessProcess Description

**src-000377 P144** — This diagram represents the high level BusinessProcesses, used to describe the high-level scope of T2S concerning “Securities Reference Data” and is not to be exhaustive.

**src-000377 P146** — Create Security

**src-000377 P147** — Modify Security

**src-000377 P148** — Delete Security

**src-000377 P149** — Query

**src-000377 P150** — General Statement

### Triggers, preconditions, postconditions and activity definitions

[Complete T8](../documents/src-000377/tables/tbl-0008.md)

| Item | Description |
| --- | --- |
| Definition | When an Instructing Party would like to create a specific security that is not yet supported by the Executing/Servicing Party, an Instructing Party asks the Executing/Servicing Party to create the security in its system. |
| Trigger | The process is triggered when the Instructing Party sends a Security Creation Request message. |
| Pre-conditions | The Instructing Party is known by the Executing/Servicing Party system and has been granted the appropriate privileges. The Instructing Party identified a gap in the securities’ coverage of the Executing/Servicing Party. The Instructing Party needs this security to be set-up at the Executing /Servicing Party to perform its activities. |
| Post-conditions | The acknowledgement of the processing of the creation request. |
| Role | Instructing Party |


[Complete T9](../documents/src-000377/tables/tbl-0009.md)

| Item | Description |
| --- | --- |
| Definition | When an Instructing Party is in charge of the modification of a specific security already supported by the Executing/Servicing Party system, the Instructing Party asks the Executing/Servicing Party to modify a security in the Executing/Servicing Party system. |
| Trigger | The process is triggered when the Instructing Party sends a Security Maintenance Request message. |
| Pre-conditions | The Instructing Party is known by the Executing/Servicing Party system and has been granted the appropriate privileges. An attribute of the security has changed which requires a modification of the security in the Executing/Servicing Party system. |
| Post-conditions | The acknowledgement of the processing of the maintenance request. |
| Role | Instructing Party |


[Complete T10](../documents/src-000377/tables/tbl-0010.md)

| Item | Description |
| --- | --- |
| Definition | When an Instructing Party would like to delete a specific security already supported by the Executing/Servicing Party system, an Instructing Party asks the Executing/Servicing Party to delete the security in its system. |
| Trigger | The process is triggered when the Instructing Party sends a Security Deletion Request message. |
| Pre-conditions | The Instructing Party is known by the Executing/Servicing Party system and has been granted the appropriate privileges. The Instructing Party identified a gap in the Security’ coverage of the Executing/Servicing Party. The Instructing Party needs to remove this security at the Executing /Servicing Party. |
| Post-conditions | The acknowledgement of the processing of the deletion request. |
| Role | Instructing Party |


[Complete T11](../documents/src-000377/tables/tbl-0011.md)

| Item | Description |
| --- | --- |
| Definition | The Instructing Party asks the Executing/Servicing Party a response to a query or to an Audit Trail query. |
| Trigger | The process is triggered when the Instructing Party sends a Security Query message or a Securities Audit Trail Query message. |
| Pre-conditions | The query type must be known by the Instructing party and the Executing/Servicing Party. |
| Post-conditions | The Security Report message including all of the retrieved securities records or the Securities Audit Trail Report message with all the requested audit trail information. |
| Role | Instructing Party |


[Complete T12](../documents/src-000377/tables/tbl-0012.md)

| Item | Description |
| --- | --- |
| Definition | The Recipient Party receives a Security Activity Advice statement which has been automatically produced by the Executing/Servicing Party. |
| Trigger | The process is triggered automatically. |
| Pre-conditions | A standing instruction is in place at the Executing/Servicing Party for sending of the statement. |
| Post-conditions | The acknowledgement of the sending of the statement. |
| Role | Executing/Servicing Party |


### Scoped participants and exact message references

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000377-instructing-party.md)
- [Executing/Servicing Party](../../../../../../../shared/reference/participants/participant-src-000377-executing-servicing-party.md)

| Canonical exact definition | Same-publication identifier evidence | Companion definition |
| --- | --- | --- |



### Limits and source distinctions

- Both original terminal symbols are hollow concentric circles; they are preserved as double circles rather than silently replaced with filled UML start/end glyphs.
- The connectors share unmarked junction lines. No concurrency bar or decision is invented. P144 explicitly says this high-level scope is not exhaustive. The source paragraph P150 says General Statement, while the picture says Generate Statement.
- Source377 is June2021; companion source378 is March2024. Matching full identifiers do not erase the publication difference (issue-000010).

<!-- SECREF-FIG-2-END -->
