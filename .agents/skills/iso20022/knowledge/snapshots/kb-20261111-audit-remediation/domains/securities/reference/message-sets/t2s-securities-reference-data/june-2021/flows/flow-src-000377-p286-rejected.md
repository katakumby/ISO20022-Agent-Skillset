---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_sets: ["t2s-securities-reference-data"]
flow_id: "flow-src-000377-p286-rejected"
title: "Rejected"
source_locations: [{"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[286]", "paragraph_id": "P286", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[287]", "paragraph_id": "P287", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[288]", "paragraph_id": "P288", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[289]", "paragraph_id": "P289", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[290]", "paragraph_id": "P290", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[291]", "paragraph_id": "P291", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Deletion Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[292]", "paragraph_id": "P292", "table_id": null}]
participants: ["participant-src-000377-instructing-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Rejected", "Instructing Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Rejected

Source context: T2S SecuritiesReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000377-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P287** After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P288** the mandatory information is not present or incorrect,

**P289** the security cannot be deleted,

**P290** the Instructing Party does not have the right to delete security,

**P291** the instruction has already been received and is being processed 

**P292** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000377](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Heading path: BusinessTransactions / Deletion Process / Rejection Scenario.
