---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
message_sets: ["t2s-billing"]
flow_id: "flow-src-000347-p160-billing-report"
title: "Billing Report"
source_locations: [{"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Billing Report"], "locator": "/w:document/w:body/w:p[160]", "paragraph_id": "P160", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Billing Report"], "locator": "/w:document/w:body/w:p[161]", "paragraph_id": "P161", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Billing Report"], "locator": "/w:document/w:body/w:p[162]", "paragraph_id": "P162", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Billing Report"], "locator": "/w:document/w:body/w:p[163]", "paragraph_id": "P163", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Billing Report"], "locator": "/w:document/w:body/w:p[164]", "paragraph_id": "P164", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Billing Report"], "locator": "/w:document/w:body/w:p[165]", "paragraph_id": "P165", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Billing Report"], "locator": "/w:document/w:body/w:p[166]", "paragraph_id": "P166", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Billing Report"], "locator": "/w:document/w:body/w:p[167]", "paragraph_id": "P167", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Billing Report"], "locator": "/w:document/w:body/w:p[168]", "paragraph_id": "P168", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Billing Report"], "locator": "/w:document/w:body/w:p[169]", "paragraph_id": "P169", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Billing Report"], "locator": "/w:document/w:body/w:p[170]", "paragraph_id": "P170", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Billing Report"], "locator": "/w:document/w:body/w:p[171]", "paragraph_id": "P171", "table_id": null}]
participants: ["participant-src-000347-executing-servicing-party", "participant-src-000347-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000347", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Billing"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["camt.077"]
search_terms: ["Billing Report", "Executing / Servicing Party", "Instructing Party", "camt.077"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Billing Report

Source context: T2S Billing. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000347-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000347-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P161** The Executing/Servicing Party sends the report to the Instructing Party to communicate:

**P162** An official invoice

**P163** Consumption data (for NCBs only)

**P164** whenever a specific event is reached in the business day.

**P166** The Executing/Servicing Party sends the report to the Instructing Party to communicate:

**P167** the cancellation status of an invoice

**P168** At the end of the processing of a previously sent cancellation request submitted by the operator.

## Messages and alternative paths

Source-supported message family mentions: `camt.077`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000347](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`. Heading path: BusinessTransactions / Billing Report.
