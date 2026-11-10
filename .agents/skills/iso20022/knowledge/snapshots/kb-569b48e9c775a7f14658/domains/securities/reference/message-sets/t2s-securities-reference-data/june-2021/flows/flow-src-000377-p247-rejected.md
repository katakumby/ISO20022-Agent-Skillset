---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_sets: ["t2s-securities-reference-data"]
flow_id: "flow-src-000377-p247-rejected"
title: "Rejected"
source_locations: [{"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[247]", "paragraph_id": "P247", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[248]", "paragraph_id": "P248", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[249]", "paragraph_id": "P249", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[250]", "paragraph_id": "P250", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[251]", "paragraph_id": "P251", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[252]", "paragraph_id": "P252", "table_id": null}]
participants: []
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Rejected"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Rejected

Source context: T2S SecuritiesReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P248** After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P249** the mandatory information is not present or incorrect,

**P250** the data cannot be updated,

**P251** the instruction has already been received and is being processed. 

**P252** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000377](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Heading path: BusinessTransactions / Modification Process / Rejection Scenario.
