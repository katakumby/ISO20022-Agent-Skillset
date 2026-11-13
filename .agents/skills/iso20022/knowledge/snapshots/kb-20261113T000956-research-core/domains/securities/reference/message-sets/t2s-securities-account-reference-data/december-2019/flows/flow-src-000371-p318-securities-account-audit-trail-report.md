---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
flow_id: "flow-src-000371-p318-securities-account-audit-trail-report"
title: "Securities Account Audit Trail Report"
source_locations: [{"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Query/Response Process", "Securities Account Audit Trail Query/Securities Account Audit Trail Report Scenario"], "locator": "/w:document/w:body/w:p[318]", "paragraph_id": "P318", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Query/Response Process", "Securities Account Audit Trail Query/Securities Account Audit Trail Report Scenario"], "locator": "/w:document/w:body/w:p[319]", "paragraph_id": "P319", "table_id": null}]
participants: ["participant-src-000371-executing-servicing-party", "participant-src-000371-instructing-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Securities Account Audit Trail Report", "Executing/Servicing Party", "Instructing Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Securities Account Audit Trail Report

Source context: T2S SecuritiesAccountReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing/Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000371-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000371-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P319** The Executing/Servicing Party sends a query response that meets the specified criteria to the Instructing Party.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000371](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Heading path: BusinessTransactions / Query/Response Process / Securities Account Audit Trail Query/Securities Account Audit Trail Report Scenario.
