---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_sets: ["t2s-securities-and-penalty-reporting"]
flow_id: "flow-src-000374-p276-securities-transaction-penalties-report-semt-044"
title: "Securities Transaction Penalties Report (semt.044)"
source_locations: [{"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Transaction Penalties Report (semt.044)"], "locator": "/w:document/w:body/w:p[276]", "paragraph_id": "P276", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Transaction Penalties Report (semt.044)"], "locator": "/w:document/w:body/w:p[277]", "paragraph_id": "P277", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Transaction Penalties Report (semt.044)"], "locator": "/w:document/w:body/w:p[278]", "paragraph_id": "P278", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Transaction Penalties Report (semt.044)"], "locator": "/w:document/w:body/w:p[279]", "paragraph_id": "P279", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Transaction Penalties Report (semt.044)"], "locator": "/w:document/w:body/w:p[280]", "paragraph_id": "P280", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Transaction Penalties Report (semt.044)"], "locator": "/w:document/w:body/w:p[281]", "paragraph_id": "P281", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Transaction Penalties Report (semt.044)"], "locator": "/w:document/w:body/w:p[282]", "paragraph_id": "P282", "table_id": null}]
participants: []
message_mapping_evidence: [{"source_id": "src-000374", "heading_path": ["Scope and Functionality", "Scope", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[6]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["semt.044"]
search_terms: ["Securities Transaction Penalties Report (semt.044)", "semt.044"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---



# Securities Transaction Penalties Report (semt.044)

Source context: T2S SecuritiesAndPenaltyReporting. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P277** The Securities Transaction Penalties Report message is sent by T2S to T2S Actors, i.e. CSDs or CSD participants, to provide them with the Daily Penalty List, the List of Modified Penalties and the Monthly Aggregated Amounts of penalties for the previous month. T2S shall allow the relevant T2S Actor to receive penalties information under its default data scope.

**P278** In case of a CSD, the information shall include the penalties that are either imposed or credited to all the parties belonging to the CSD data scope.

**P279** In case of a CSD participant (or an External CSD), the information shall include the penalties that are either imposed or credited to the CSD participant (or the External CSD).


## Messages and alternative paths

Source-supported message family mentions: `semt.044`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000374](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`. Heading path: BusinessTransactions / Securities Transaction Penalties Report (semt.044).

Reusable mode references: [position query/response](flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp.md), [settlement query/response](flow-src-000374-p239-securities-settlement-transaction-query-and-securities-settlement-tran.md), [penalty report](flow-src-000374-p243-securities-transaction-penalties-report.md).
