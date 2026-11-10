---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
flow_id: "flow-src-000368-p254-party-status-advice"
title: "Party Status Advice"
source_locations: [{"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[254]", "paragraph_id": "P254", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[255]", "paragraph_id": "P255", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[256]", "paragraph_id": "P256", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[257]", "paragraph_id": "P257", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[258]", "paragraph_id": "P258", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[259]", "paragraph_id": "P259", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[260]", "paragraph_id": "P260", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[261]", "paragraph_id": "P261", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[262]", "paragraph_id": "P262", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[263]", "paragraph_id": "P263", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[264]", "paragraph_id": "P264", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[265]", "paragraph_id": "P265", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[266]", "paragraph_id": "P266", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[267]", "paragraph_id": "P267", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[268]", "paragraph_id": "P268", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[269]", "paragraph_id": "P269", "table_id": null}]
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

**P255** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:


**P256** Rejected
The instruction did not pass validation, some reasons could be:

**P257** the mandatory information is not present or incorrect;

**P258** the Instructing Party does not have the right to delete Party;

**P259** the instruction has already been received and is being processed;

**P260** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status


**P261** Queued
The Executing/Servicing Party might inform the Instructing party that the processing of the Delete Party instruction has been delayed. In case of e.g. a night-time cycle is running.  

**P263** Rejected after dequeuing
After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P264**  the mandatory information is not present or incorrect;

**P265**  the Party cannot be deleted;

**P266**  the Instructing Party does not have the right to delete Party;

**P267**  the instruction has already been received and is being processed;

**P268** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

## Messages and alternative paths

Source-supported message family mentions: `reda.016`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000368](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`. Heading path: BusinessTransactions / Deletion Process / Rejection Scenario.
