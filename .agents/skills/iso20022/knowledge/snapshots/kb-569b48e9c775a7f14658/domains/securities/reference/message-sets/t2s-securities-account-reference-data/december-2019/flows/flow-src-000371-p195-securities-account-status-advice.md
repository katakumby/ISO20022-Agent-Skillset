---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
flow_id: "flow-src-000371-p195-securities-account-status-advice"
title: "Securities Account Status Advice"
source_locations: [{"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[195]", "paragraph_id": "P195", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[196]", "paragraph_id": "P196", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[197]", "paragraph_id": "P197", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[198]", "paragraph_id": "P198", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[199]", "paragraph_id": "P199", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[200]", "paragraph_id": "P200", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[201]", "paragraph_id": "P201", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[202]", "paragraph_id": "P202", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[203]", "paragraph_id": "P203", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[204]", "paragraph_id": "P204", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[205]", "paragraph_id": "P205", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[206]", "paragraph_id": "P206", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[207]", "paragraph_id": "P207", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[208]", "paragraph_id": "P208", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[209]", "paragraph_id": "P209", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[210]", "paragraph_id": "P210", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[211]", "paragraph_id": "P211", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[212]", "paragraph_id": "P212", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[213]", "paragraph_id": "P213", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[214]", "paragraph_id": "P214", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[215]", "paragraph_id": "P215", "table_id": null}]
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

**P196** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P197** Rejected

**P198** The instruction did not pass validation, some reasons could be:

**P199** the mandatory information is not present or incorrect,

**P200** the instruction is not a new occurrence,

**P201** the instruction has already been received and is being processed. 

**P202** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

**P204** Queued
The Executing/Servicing Party might inform the Instructing party that the processing of the Create Securities Account instruction has been delayed. In case of e.g. a night-time cycle is running.

**P206** Rejected

**P207** After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P208** the mandatory information is not present or incorrect,

**P209** the instruction is not a new occurrence,

**P210** the instruction has already been received and is being processed 

**P211** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

## Messages and alternative paths

Source-supported message family mentions: `reda.020`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000371](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Heading path: BusinessTransactions / Creation Process / Rejection Scenario.
