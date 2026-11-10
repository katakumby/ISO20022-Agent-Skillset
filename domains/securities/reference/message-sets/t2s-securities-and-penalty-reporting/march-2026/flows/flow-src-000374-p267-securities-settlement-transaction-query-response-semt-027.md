---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_sets: ["t2s-securities-and-penalty-reporting"]
flow_id: "flow-src-000374-p267-securities-settlement-transaction-query-response-semt-027"
title: "Securities Settlement Transaction Query Response (semt.027)"
source_locations: [{"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Settlement Transaction Query Response (semt.027)"], "locator": "/w:document/w:body/w:p[267]", "paragraph_id": "P267", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Settlement Transaction Query Response (semt.027)"], "locator": "/w:document/w:body/w:p[268]", "paragraph_id": "P268", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Settlement Transaction Query Response (semt.027)"], "locator": "/w:document/w:body/w:p[269]", "paragraph_id": "P269", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Settlement Transaction Query Response (semt.027)"], "locator": "/w:document/w:body/w:p[270]", "paragraph_id": "P270", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Settlement Transaction Query Response (semt.027)"], "locator": "/w:document/w:body/w:p[271]", "paragraph_id": "P271", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Settlement Transaction Query Response (semt.027)"], "locator": "/w:document/w:body/w:p[272]", "paragraph_id": "P272", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Settlement Transaction Query Response (semt.027)"], "locator": "/w:document/w:body/w:p[273]", "paragraph_id": "P273", "table_id": null}]
participants: []
message_mapping_evidence: [{"source_id": "src-000374", "heading_path": ["Scope and Functionality", "Scope", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000374", "heading_path": ["Scope and Functionality", "Scope", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["semt.026", "semt.027"]
search_terms: ["Securities Settlement Transaction Query Response (semt.027)", "semt.026", "semt.027"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---



# Securities Settlement Transaction Query Response (semt.027)

Source context: T2S SecuritiesAndPenaltyReporting. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P268** The Securities Settlement Transaction Query Response message is sent by T2S to a Central Securities Depository or a directly connected T2S participant (e.g. payment bank/settlement bank). This message is used to provide information on Settlement Instructions based on the criteria as defined within the query message.

**P270** To request the Securities Settlement Transaction Query Response message, the sender sends a semt.026 message containing search criteria to restrict the query. This message is sent by T2S in the following message usages:

**P271** Settlement Instruction Query Response.

**P272** Settlement Instruction Current Status Query Response.

**P273** Settlement Instruction Status Audit Trail Query Response.

## Messages and alternative paths

Source-supported message family mentions: `semt.026`, `semt.027`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000374](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`. Heading path: BusinessTransactions / Securities Settlement Transaction Query Response (semt.027).

Reusable mode references: [position query/response](flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp.md), [settlement query/response](flow-src-000374-p239-securities-settlement-transaction-query-and-securities-settlement-tran.md), [penalty report](flow-src-000374-p243-securities-transaction-penalties-report.md).
