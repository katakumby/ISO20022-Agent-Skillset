---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000356"]
source_editions: ["march-2024"]
message_sets: ["t2s-collateral-reporting"]
flow_id: "flow-src-000356-p144-business-transactions"
title: "BusinessTransactions"
source_locations: [{"source_id": "src-000356", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[144]", "paragraph_id": "P144", "table_id": null}, {"source_id": "src-000356", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[145]", "paragraph_id": "P145", "table_id": null}, {"source_id": "src-000356", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[146]", "paragraph_id": "P146", "table_id": null}, {"source_id": "src-000356", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[147]", "paragraph_id": "P147", "table_id": null}, {"source_id": "src-000356", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[148]", "paragraph_id": "P148", "table_id": null}, {"source_id": "src-000356", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[149]", "paragraph_id": "P149", "table_id": null}, {"source_id": "src-000356", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[150]", "paragraph_id": "P150", "table_id": null}, {"source_id": "src-000356", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[151]", "paragraph_id": "P151", "table_id": null}, {"source_id": "src-000356", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[152]", "paragraph_id": "P152", "table_id": null}, {"source_id": "src-000356", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[153]", "paragraph_id": "P153", "table_id": null}]
participants: []
message_mapping_evidence: [{"source_id": "src-000356", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Collateral Reporting"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["colr.001"]
search_terms: ["BusinessTransactions", "colr.001"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---



# BusinessTransactions

Source context: T2S CollateralReporting. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P145** This section describes the message flows based on the activity diagrams documented above. It shows the typical exchanges of information in the context of a BusinessTransaction.

Source diagram evidence: [fig-0009](../documents/src-000356/diagrams/fig-0009.md). Mermaid reconstruction and visual review are pending.

**P148** As outlined above, an NCB, CSD or directly connected Central System party sends a Collateral Value Query to the Central System (e.g. T2S platform) to request information on the current available value of securities for auto collateralisation. The value will represent the amount of intraday credit that a party may receive through collateralising of their securities. Error Response or Collateral Value Response are both exclusive.

**P150** An overview of the communication flow and sequence diagram can be found below:

Source diagram evidence: [fig-0010](../documents/src-000356/diagrams/fig-0010.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `colr.001`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000356](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralReporting_2023_2024_v2.docx`. Heading path: BusinessTransactions.

Curated reusable flow: [Collateral-value query management](flow-src-000356-p138-query-management-process.md).
