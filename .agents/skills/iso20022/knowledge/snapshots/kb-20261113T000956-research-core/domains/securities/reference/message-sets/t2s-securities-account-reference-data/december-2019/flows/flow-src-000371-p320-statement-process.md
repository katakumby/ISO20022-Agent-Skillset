---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
flow_id: "flow-src-000371-p320-statement-process"
title: "Statement Process"
source_locations: [{"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Statement Process"], "locator": "/w:document/w:body/w:p[320]", "paragraph_id": "P320", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Statement Process"], "locator": "/w:document/w:body/w:p[321]", "paragraph_id": "P321", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Statement Process"], "locator": "/w:document/w:body/w:p[322]", "paragraph_id": "P322", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Statement Process"], "locator": "/w:document/w:body/w:p[323]", "paragraph_id": "P323", "table_id": null}]
participants: []
message_mapping_evidence: [{"source_id": "src-000371", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[8]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["reda.035"]
search_terms: ["Statement Process", "reda.035"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Statement Process

Source context: T2S SecuritiesAccountReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P322** Securities Account Activity Advice (reda.035)Statement Process

Source diagram evidence: [fig-0020](../documents/src-000371/diagrams/fig-0020.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `reda.035`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000371](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Heading path: BusinessTransactions / Statement Process.
