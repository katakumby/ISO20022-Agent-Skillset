---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
flow_id: "flow-src-000371-p279-securities-account-status-advice"
title: "Securities Account Status Advice"
source_locations: [{"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[279]", "paragraph_id": "P279", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[280]", "paragraph_id": "P280", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[281]", "paragraph_id": "P281", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[282]", "paragraph_id": "P282", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[283]", "paragraph_id": "P283", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[284]", "paragraph_id": "P284", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[285]", "paragraph_id": "P285", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[286]", "paragraph_id": "P286", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[287]", "paragraph_id": "P287", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[288]", "paragraph_id": "P288", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[289]", "paragraph_id": "P289", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[290]", "paragraph_id": "P290", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[291]", "paragraph_id": "P291", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[292]", "paragraph_id": "P292", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[293]", "paragraph_id": "P293", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[294]", "paragraph_id": "P294", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[295]", "paragraph_id": "P295", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[296]", "paragraph_id": "P296", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[297]", "paragraph_id": "P297", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[298]", "paragraph_id": "P298", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[299]", "paragraph_id": "P299", "table_id": null}]
participants: ["participant-src-000371-executing-servicing-party", "participant-src-000371-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000371", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["reda.020"]
search_terms: ["Securities Account Status Advice", "Executing/Servicing Party", "Instructing Party", "reda.020"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Securities Account Status Advice

Source context: T2S SecuritiesAccountReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing/Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000371-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000371-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P280** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P282** Rejected

**P283** The instruction did not pass validation, some reasons could be:

**P284** the mandatory information is not present or incorrect,

**P285** the Instructing Party does not have the right to delete securities account,

**P286** the instruction has already been received and is being processed. 

**P287** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

**P289** Queued

**P290** The Executing/Servicing Party might inform the Instructing party that the processing of the Delete Securities Account instruction has been delayed. In case of e.g. a night-time cycle is running.

**P292** Rejected

**P293** After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P294** the mandatory information is not present or incorrect,

**P295** the securities account cannot be deleted,

**P296** the Instructing Party does not have the right to delete securities account,

**P297** the instruction has already been received and is being processed 

**P298** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

## Messages and alternative paths

Source-supported message family mentions: `reda.020`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000371](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Heading path: BusinessTransactions / Deletion Process / Rejection Scenario.
