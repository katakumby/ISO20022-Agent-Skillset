---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_sets: ["t2s-settlement-restrictions"]
flow_id: "flow-src-000380-p299-securities-transaction-cancellation-request-query-semt-032"
title: "Securities Transaction Cancellation Request Query (semt.032)"
source_locations: [{"source_id": "src-000380", "heading_path": ["BusinessTransactions", "Securities Transaction Cancellation Request Query (semt.032)"], "locator": "/w:document/w:body/w:p[299]", "paragraph_id": "P299", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessTransactions", "Securities Transaction Cancellation Request Query (semt.032)"], "locator": "/w:document/w:body/w:p[300]", "paragraph_id": "P300", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessTransactions", "Securities Transaction Cancellation Request Query (semt.032)"], "locator": "/w:document/w:body/w:p[301]", "paragraph_id": "P301", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessTransactions", "Securities Transaction Cancellation Request Query (semt.032)"], "locator": "/w:document/w:body/w:p[302]", "paragraph_id": "P302", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessTransactions", "Securities Transaction Cancellation Request Query (semt.032)"], "locator": "/w:document/w:body/w:p[303]", "paragraph_id": "P303", "table_id": null}]
participants: []
message_mapping_evidence: [{"source_id": "src-000380", "heading_path": ["Scope and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[6]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["semt.032.001.01"]
message_families: ["semt.032", "semt.033", "sese.022"]
search_terms: ["Securities Transaction Cancellation Request Query (semt.032)", "semt.032", "semt.033", "sese.022"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
participant_ids: ["participant-src-000380-central-securities-depositories-csd", "participant-src-000380-direct-connected-participant-dcp", "participant-src-000380-executing-servicing-party", "participant-src-000380-instructing-party", "participant-src-000380-t2s"]
---





# Securities Transaction Cancellation Request Query (semt.032)

Source context: T2S SettlementRestrictions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P300** The Securities Transaction Cancellation Request Query is sent by a CSD or other directly connected T2S party to T2S. It aims at querying either the full details or current status of Cancellation Instructions of Settlement and Intra Position Movement Instructions based on a set of search criteria business attributes. 

**P302** In response to the Securities Transaction Cancellation Request Query message, T2S sends a semt.033 with the corresponding Cancellation Instructions or a sese.022 in case an error occurs.

## Messages and alternative paths

Source-supported message family mentions: `semt.032`, `semt.033`, `sese.022`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000380](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`. Heading path: BusinessTransactions / Securities Transaction Cancellation Request Query (semt.032).

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.032-START -->
[semt.032.001.01 — exact business narrative, conditions and direction](../../../../messages/semt.032.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.032-END -->
