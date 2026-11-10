---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
flow_id: "flow-src-000371-p301-securities-account-query-securities-account-report-scenario"
title: "Securities Account Query/Securities Account Report Scenario"
source_locations: [{"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Query/Response Process", "Securities Account Query/Securities Account Report Scenario"], "locator": "/w:document/w:body/w:p[301]", "paragraph_id": "P301", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Query/Response Process", "Securities Account Query/Securities Account Report Scenario"], "locator": "/w:document/w:body/w:p[302]", "paragraph_id": "P302", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Query/Response Process", "Securities Account Query/Securities Account Report Scenario"], "locator": "/w:document/w:body/w:p[303]", "paragraph_id": "P303", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Query/Response Process", "Securities Account Query/Securities Account Report Scenario"], "locator": "/w:document/w:body/w:p[304]", "paragraph_id": "P304", "table_id": null}]
participants: []
message_mapping_evidence: [{"source_id": "src-000371", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[6]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000371", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[7]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["reda.019", "reda.021"]
search_terms: ["Securities Account Query/Securities Account Report Scenario", "reda.019", "reda.021"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Securities Account Query/Securities Account Report Scenario

Source context: T2S SecuritiesAccountReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P303** Securities Account Query (reda.019)Query/Report ProcessSecurities Account Report (reda.021): ERRORSecurities Account Report (reda.021)

Source diagram evidence: [fig-0018](../documents/src-000371/diagrams/fig-0018.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `reda.019`, `reda.021`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000371](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Heading path: BusinessTransactions / Query/Response Process / Securities Account Query/Securities Account Report Scenario.
