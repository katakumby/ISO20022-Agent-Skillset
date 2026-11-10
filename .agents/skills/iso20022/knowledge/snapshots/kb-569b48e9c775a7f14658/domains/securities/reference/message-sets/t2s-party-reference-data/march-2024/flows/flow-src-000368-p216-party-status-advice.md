---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
flow_id: "flow-src-000368-p216-party-status-advice"
title: "Party Status Advice"
source_locations: [{"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[216]", "paragraph_id": "P216", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[217]", "paragraph_id": "P217", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[218]", "paragraph_id": "P218", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[219]", "paragraph_id": "P219", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[220]", "paragraph_id": "P220", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[221]", "paragraph_id": "P221", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[222]", "paragraph_id": "P222", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[223]", "paragraph_id": "P223", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[224]", "paragraph_id": "P224", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[225]", "paragraph_id": "P225", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[226]", "paragraph_id": "P226", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[227]", "paragraph_id": "P227", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[228]", "paragraph_id": "P228", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[229]", "paragraph_id": "P229", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[230]", "paragraph_id": "P230", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[231]", "paragraph_id": "P231", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[232]", "paragraph_id": "P232", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[233]", "paragraph_id": "P233", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[234]", "paragraph_id": "P234", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[235]", "paragraph_id": "P235", "table_id": null}]
participants: ["participant-src-000368-executing-servicing-party", "participant-src-000368-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000368", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Party Reference Data"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["reda.016"]
search_terms: ["Party Status Advice", "Executing / Servicing Party", "Instructing Party", "reda.016"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Party Status Advice

Source context: T2S PartyReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000368-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000368-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P217** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:


**P218** Rejected:
The instruction did not pass validation, some reasons could be:

**P219** the mandatory information is not present or incorrect,

**P220** the data cannot be updated,

**P221** the party cannot be blocked/unblocked,

**P222** the Instructing Party does not have the right to (un)block party

**P223** the instruction has already been received and is being processed 

**P224** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.


**P225** Queued:
The Executing/Servicing Party might inform the Instructing party that the processing of the Modify Party instruction has been delayed. In case of e.g. a night-time cycle is running.  

**P227** Rejected after dequeuing:
After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P228** the mandatory information is not present or incorrect,

**P229** the data cannot be updated,

**P230** the party cannot be blocked,

**P231** the Instructing Party does not have the right to block/unblock Party

**P232** the instruction has already been received and is being processed 

**P234** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

## Messages and alternative paths

Source-supported message family mentions: `reda.016`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000368](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`. Heading path: BusinessTransactions / Modification Process / Rejection Scenario.
