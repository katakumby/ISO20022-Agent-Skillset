---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_sets: ["t2s-settlement-restrictions"]
flow_id: "flow-src-000380-p282-intra-position-movement-query-semt-028"
title: "Intra Position Movement Query (semt.028)"
source_locations: [{"source_id": "src-000380", "heading_path": ["BusinessTransactions", "Intra Position Movement Query (semt.028)"], "locator": "/w:document/w:body/w:p[282]", "paragraph_id": "P282", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessTransactions", "Intra Position Movement Query (semt.028)"], "locator": "/w:document/w:body/w:p[283]", "paragraph_id": "P283", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessTransactions", "Intra Position Movement Query (semt.028)"], "locator": "/w:document/w:body/w:p[284]", "paragraph_id": "P284", "table_id": null}]
participants: []
message_mapping_evidence: [{"source_id": "src-000380", "heading_path": ["Scope and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["semt.028.001.01"]
message_families: ["semt.028", "semt.029", "sese.022"]
search_terms: ["Intra Position Movement Query (semt.028)", "semt.028", "semt.029", "sese.022"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
participant_ids: ["participant-src-000380-central-securities-depositories-csd", "participant-src-000380-direct-connected-participant-dcp", "participant-src-000380-executing-servicing-party", "participant-src-000380-instructing-party", "participant-src-000380-t2s"]
---





# Intra Position Movement Query (semt.028)

Source context: T2S SettlementRestrictions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P283** The Intra Position Movement Query message is sent by a CSD or other directly connected T2S party to T2S. This message is used to request information on Intra-Position Movement instructions.

**P284** In response to the Intra Position Movement Query message, T2S sends a semt.029 message with the corresponding requested intra position movements or a sese.022 message in the case of a business error.

## Messages and alternative paths

Source-supported message family mentions: `semt.028`, `semt.029`, `sese.022`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000380](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`. Heading path: BusinessTransactions / Intra Position Movement Query (semt.028).

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.028-START -->
[semt.028.001.01 — exact business narrative, conditions and direction](../../../../messages/semt.028.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.028-END -->
