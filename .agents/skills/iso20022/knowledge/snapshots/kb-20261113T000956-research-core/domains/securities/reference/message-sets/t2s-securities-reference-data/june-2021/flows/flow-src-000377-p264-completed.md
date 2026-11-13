---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_sets: ["t2s-securities-reference-data"]
flow_id: "flow-src-000377-p264-completed"
title: "Completed"
source_locations: [{"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Deletion Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[264]", "paragraph_id": "P264", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Deletion Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[265]", "paragraph_id": "P265", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Deletion Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[266]", "paragraph_id": "P266", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Deletion Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[267]", "paragraph_id": "P267", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Deletion Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[268]", "paragraph_id": "P268", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Deletion Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[269]", "paragraph_id": "P269", "table_id": null}]
participants: ["participant-src-000377-executing-servicing-party", "participant-src-000377-instructing-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Completed", "Executing/Servicing Party", "Instructing Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Completed

Source context: T2S SecuritiesReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing/Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000377-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000377-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P265** The Executing/Servicing Party informs the Instructing party that the Delete Securiy instruction has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the security that has been processed.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000377](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Heading path: BusinessTransactions / Deletion Process / Confirmation Scenario.
