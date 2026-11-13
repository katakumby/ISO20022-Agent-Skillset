---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_sets: ["t2s-securities-reference-data"]
flow_id: "flow-src-000377-p299-security-report"
title: "Security Report"
source_locations: [{"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Query/Response Process", "Security Query/Security Report Scenario"], "locator": "/w:document/w:body/w:p[299]", "paragraph_id": "P299", "table_id": null}, {"source_id": "src-000377", "heading_path": ["BusinessTransactions", "Query/Response Process", "Security Query/Security Report Scenario"], "locator": "/w:document/w:body/w:p[300]", "paragraph_id": "P300", "table_id": null}]
participants: ["participant-src-000377-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000377", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Securities Reference Data message "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[9]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["reda.012"]
search_terms: ["Security Report", "Instructing Party", "reda.012"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Security Report

Source context: T2S SecuritiesReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000377-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P300** Depending on the query criteria, it is possible that the processing will take more than a certain time or that the result of the query will be empty due to wrong combination of criteria or no result set. In this case, an error message within a query response message is sent to the Instructing Party.

## Messages and alternative paths

Source-supported message family mentions: `reda.012`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000377](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Heading path: BusinessTransactions / Query/Response Process / Security Query/Security Report Scenario.
