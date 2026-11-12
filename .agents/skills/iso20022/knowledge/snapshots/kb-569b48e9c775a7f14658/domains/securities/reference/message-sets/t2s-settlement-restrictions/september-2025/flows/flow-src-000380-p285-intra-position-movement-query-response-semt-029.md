---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_sets: ["t2s-settlement-restrictions"]
flow_id: "flow-src-000380-p285-intra-position-movement-query-response-semt-029"
title: "Intra Position Movement Query Response (semt.029)"
source_locations: [{"source_id": "src-000380", "heading_path": ["BusinessTransactions", "Intra Position Movement Query Response (semt.029)"], "locator": "/w:document/w:body/w:p[285]", "paragraph_id": "P285", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessTransactions", "Intra Position Movement Query Response (semt.029)"], "locator": "/w:document/w:body/w:p[286]", "paragraph_id": "P286", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessTransactions", "Intra Position Movement Query Response (semt.029)"], "locator": "/w:document/w:body/w:p[287]", "paragraph_id": "P287", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessTransactions", "Intra Position Movement Query Response (semt.029)"], "locator": "/w:document/w:body/w:p[288]", "paragraph_id": "P288", "table_id": null}]
participants: []
message_mapping_evidence: [{"source_id": "src-000380", "heading_path": ["Scope and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000380", "heading_path": ["Scope and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["semt.029.001.01"]
message_families: ["semt.028", "semt.029"]
search_terms: ["Intra Position Movement Query Response (semt.029)", "semt.028", "semt.029"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
participant_ids: ["participant-src-000380-account-owner", "participant-src-000380-central-securities-depositories-csd", "participant-src-000380-direct-connected-participant-dcp", "participant-src-000380-executing-servicing-party", "participant-src-000380-instructing-party", "participant-src-000380-t2s"]
---





# Intra Position Movement Query Response (semt.029)

Source context: T2S SettlementRestrictions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P286** The Intra Position Movement Query Response message is sent by T2S to CSD or other directly connected T2S party. This message is used to provide information on Intra Position Movement instructions.

**P287** The Intra Position Movement Query Response is sent in response to a semt.028 message.

## Messages and alternative paths

Source-supported message family mentions: `semt.028`, `semt.029`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000380](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`. Heading path: BusinessTransactions / Intra Position Movement Query Response (semt.029).

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.029-START -->
[semt.029.001.01 — exact business narrative, conditions and direction](../../../../messages/semt.029.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.029-END -->
