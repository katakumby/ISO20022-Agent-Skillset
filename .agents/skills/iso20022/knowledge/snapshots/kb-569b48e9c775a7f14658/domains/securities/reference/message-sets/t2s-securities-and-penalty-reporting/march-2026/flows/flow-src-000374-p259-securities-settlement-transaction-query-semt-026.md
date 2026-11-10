---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_sets: ["t2s-securities-and-penalty-reporting"]
flow_id: "flow-src-000374-p259-securities-settlement-transaction-query-semt-026"
title: "Securities Settlement Transaction Query (semt.026)"
source_locations: [{"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Settlement Transaction Query (semt.026)"], "locator": "/w:document/w:body/w:p[259]", "paragraph_id": "P259", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Settlement Transaction Query (semt.026)"], "locator": "/w:document/w:body/w:p[260]", "paragraph_id": "P260", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Settlement Transaction Query (semt.026)"], "locator": "/w:document/w:body/w:p[261]", "paragraph_id": "P261", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Settlement Transaction Query (semt.026)"], "locator": "/w:document/w:body/w:p[262]", "paragraph_id": "P262", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Settlement Transaction Query (semt.026)"], "locator": "/w:document/w:body/w:p[263]", "paragraph_id": "P263", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Settlement Transaction Query (semt.026)"], "locator": "/w:document/w:body/w:p[264]", "paragraph_id": "P264", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Settlement Transaction Query (semt.026)"], "locator": "/w:document/w:body/w:p[265]", "paragraph_id": "P265", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Settlement Transaction Query (semt.026)"], "locator": "/w:document/w:body/w:p[266]", "paragraph_id": "P266", "table_id": null}]
participants: []
message_mapping_evidence: [{"source_id": "src-000374", "heading_path": ["Scope and Functionality", "Scope", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000374", "heading_path": ["Scope and Functionality", "Scope", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["semt.026", "semt.027", "sese.022"]
search_terms: ["Securities Settlement Transaction Query (semt.026)", "semt.026", "semt.027", "sese.022"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---



# Securities Settlement Transaction Query (semt.026)

Source context: T2S SecuritiesAndPenaltyReporting. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P260** The Securities Settlement Transaction Query message is sent by a Central Securities Depository or a directly connected T2S participant (e.g. payment bank/settlement bank) to T2S. This message is used to request information on Settlement Instructions.

**P261** This message is sent to T2S for the following query types:

**P262** Settlement Instruction Query.

**P263** Settlement Instruction Current Status Query.

**P264** Settlement Instruction Status Audit Trail Query.

**P266** In response to the Securities Settlement Transaction Query message, T2S sends a Securities Settlement Transaction Query Response message (semt.027) with the corresponding requested settlement instructions or a Securities Status Or Statement Query Status Advice message (sese.022) in the case of a business error.

## Messages and alternative paths

Source-supported message family mentions: `semt.026`, `semt.027`, `sese.022`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000374](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`. Heading path: BusinessTransactions / Securities Settlement Transaction Query (semt.026).

Reusable mode references: [position query/response](flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp.md), [settlement query/response](flow-src-000374-p239-securities-settlement-transaction-query-and-securities-settlement-tran.md), [penalty report](flow-src-000374-p243-securities-transaction-penalties-report.md).
