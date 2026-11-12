---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_sets: ["t2s-link-reference-data"]
flow_id: "flow-src-000365-p190-reference-data-link-maintenance-request"
title: "Reference Data Link Maintenance Request"
source_locations: [{"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[190]", "paragraph_id": "P190", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[191]", "paragraph_id": "P191", "table_id": null}]
participants: ["participant-src-000365-executing-servicing-party", "participant-src-000365-instructing-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Reference Data Link Maintenance Request", "Executing / Servicing Party", "Instructing Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---



# Reference Data Link Maintenance Request

Source context: T2S LinkReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P191** The Instructing Party sends an instruction to the Executing/Servicing Party to modify data for a Reference Data Link. This instruction contains information that uniquely identify the Reference Data Link. 

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000365](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`. Heading path: BusinessTransactions / Modification Process / Confirmation Scenario.

Reusable flows: [creation](flow-src-000365-p120-link-creation-process.md), [modification](flow-src-000365-p122-link-modification-process.md).
