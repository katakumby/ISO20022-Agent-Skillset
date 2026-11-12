---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_sets: ["t2s-securities-and-penalty-reporting"]
flow_id: "flow-src-000374-p247-business-transactions"
title: "BusinessTransactions"
source_locations: [{"source_id": "src-000374", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[247]", "paragraph_id": "P247", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[248]", "paragraph_id": "P248", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[249]", "paragraph_id": "P249", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[250]", "paragraph_id": "P250", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[251]", "paragraph_id": "P251", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[252]", "paragraph_id": "P252", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[253]", "paragraph_id": "P253", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[254]", "paragraph_id": "P254", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[255]", "paragraph_id": "P255", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[256]", "paragraph_id": "P256", "table_id": null}]
participants: []
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["BusinessTransactions"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---



# BusinessTransactions

Source context: T2S SecuritiesAndPenaltyReporting. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P248** This section describes the message flows based on the activity diagrams documented above. It shows the typical exchanges of information in the context of a Business Transaction.

**P250** In the context of a Business Transaction, the process enables the reconciliation of (pending and posted) transactions and their computed penalties (if any) by providing the associated data. The main processes are highlighted in green, the surrounding processes in blue.

**P252** The reconciliation communication flows can be represented as follows:

Source diagram evidence: [fig-0013](../documents/src-000374/diagrams/fig-0013.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000374](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`. Heading path: BusinessTransactions.

Reusable mode references: [position query/response](flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp.md), [settlement query/response](flow-src-000374-p239-securities-settlement-transaction-query-and-securities-settlement-tran.md), [penalty report](flow-src-000374-p243-securities-transaction-penalties-report.md).
