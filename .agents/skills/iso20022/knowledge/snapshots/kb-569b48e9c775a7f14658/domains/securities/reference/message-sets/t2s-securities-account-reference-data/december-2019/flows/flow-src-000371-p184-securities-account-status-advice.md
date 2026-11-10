---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
flow_id: "flow-src-000371-p184-securities-account-status-advice"
title: "Securities Account Status Advice"
source_locations: [{"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[184]", "paragraph_id": "P184", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[185]", "paragraph_id": "P185", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[186]", "paragraph_id": "P186", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[187]", "paragraph_id": "P187", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[188]", "paragraph_id": "P188", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[189]", "paragraph_id": "P189", "table_id": null}]
participants: ["participant-src-000371-executing-servicing-party", "participant-src-000371-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000371", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000371", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["reda.018", "reda.020"]
search_terms: ["Securities Account Status Advice", "Executing/Servicing Party", "Instructing Party", "reda.018", "reda.020"]
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

**P185** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P187** Queued
The Executing/Servicing Party might inform the Instructing party that the processing of Securities Account Creation Request has been delayed. In case of e.g. a night-time cycle is running.

**P189** Completed
The Executing/Servicing Party informs the Instructing party that the Securities Account Creation Request has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the Securities Account that has been processed.

## Messages and alternative paths

Source-supported message family mentions: `reda.018`, `reda.020`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000371](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Heading path: BusinessTransactions / Creation Process / Confirmation Scenario.
