---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_sets: ["t2s-securities-and-penalty-reporting"]
flow_id: "flow-src-000374-p257-securities-account-position-query-semt-025"
title: "Securities Account Position Query (semt.025)"
source_locations: [{"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Account Position Query (semt.025)"], "locator": "/w:document/w:body/w:p[257]", "paragraph_id": "P257", "table_id": null}, {"source_id": "src-000374", "heading_path": ["BusinessTransactions", "Securities Account Position Query (semt.025)"], "locator": "/w:document/w:body/w:p[258]", "paragraph_id": "P258", "table_id": null}]
participants: []
message_mapping_evidence: [{"source_id": "src-000374", "heading_path": ["Scope and Functionality", "Scope", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["semt.025", "semt.040", "sese.022"]
search_terms: ["Securities Account Position Query (semt.025)", "semt.025", "semt.040", "sese.022"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---



# Securities Account Position Query (semt.025)

Source context: T2S SecuritiesAndPenaltyReporting. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P258** The Securities Account Position Query message returns the latest securities position at the given time of the day that the query has been requested for the specified securities accounts. In case the T2S Actor requests for a Securities Account Position History Query, he should indicate either the securities account or the account owner as search criteria. In a Securities Account Position History Query, T2S returns all closing securities positions on the dates within the specified time period for the specified securities accounts. In response to the Securities Account Position Query message, T2S sends a semt.040 message with the list of the different securities positions of a T2S Actor's securities account or a sese.022 message in case of error.

## Messages and alternative paths

Source-supported message family mentions: `semt.025`, `semt.040`, `sese.022`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000374](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`. Heading path: BusinessTransactions / Securities Account Position Query (semt.025).

Reusable mode references: [position query/response](flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp.md), [settlement query/response](flow-src-000374-p239-securities-settlement-transaction-query-and-securities-settlement-tran.md), [penalty report](flow-src-000374-p243-securities-transaction-penalties-report.md).
