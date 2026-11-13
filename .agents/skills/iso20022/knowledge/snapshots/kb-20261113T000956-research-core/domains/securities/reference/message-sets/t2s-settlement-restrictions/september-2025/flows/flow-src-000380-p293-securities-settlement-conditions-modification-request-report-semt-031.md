---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_sets: ["t2s-settlement-restrictions"]
flow_id: "flow-src-000380-p293-securities-settlement-conditions-modification-request-report-semt-031"
title: "Securities Settlement Conditions Modification Request Report (semt.031)"
source_locations: [{"source_id": "src-000380", "heading_path": ["BusinessTransactions", "Securities Settlement Conditions Modification Request Report (semt.031)"], "locator": "/w:document/w:body/w:p[293]", "paragraph_id": "P293", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessTransactions", "Securities Settlement Conditions Modification Request Report (semt.031)"], "locator": "/w:document/w:body/w:p[294]", "paragraph_id": "P294", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessTransactions", "Securities Settlement Conditions Modification Request Report (semt.031)"], "locator": "/w:document/w:body/w:p[295]", "paragraph_id": "P295", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessTransactions", "Securities Settlement Conditions Modification Request Report (semt.031)"], "locator": "/w:document/w:body/w:p[296]", "paragraph_id": "P296", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessTransactions", "Securities Settlement Conditions Modification Request Report (semt.031)"], "locator": "/w:document/w:body/w:p[297]", "paragraph_id": "P297", "table_id": null}, {"source_id": "src-000380", "heading_path": ["BusinessTransactions", "Securities Settlement Conditions Modification Request Report (semt.031)"], "locator": "/w:document/w:body/w:p[298]", "paragraph_id": "P298", "table_id": null}]
participants: []
message_mapping_evidence: [{"source_id": "src-000380", "heading_path": ["Scope and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["semt.031.001.01"]
message_families: ["semt.030", "semt.031"]
search_terms: ["Securities Settlement Conditions Modification Request Report (semt.031)", "semt.030", "semt.031"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
participant_ids: ["participant-src-000380-account-owner", "participant-src-000380-central-securities-depositories-csd", "participant-src-000380-direct-connected-participant-dcp", "participant-src-000380-executing-servicing-party", "participant-src-000380-instructing-party", "participant-src-000380-requestor", "participant-src-000380-t2s"]
---





# Securities Settlement Conditions Modification Request Report (semt.031)

Source context: T2S SettlementRestrictions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P295** The Securities Settlement Conditions Modification Request Report message is sent by T2S to CSDs or other directly connected T2S parties. This message is used as response to the semt.030 message, containing information on Securities Settlement Conditions Modification Instructions.

**P297** The message is also sent by T2S as a report triggered by defined business and time events. The delta version returns new Securities Settlement Conditions Modification Instructions not reported to the requestor in a previous execution of the Securities Settlement Conditions Modification Request report.

## Messages and alternative paths

Source-supported message family mentions: `semt.030`, `semt.031`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000380](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`. Heading path: BusinessTransactions / Securities Settlement Conditions Modification Request Report (semt.031).

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.031-START -->
[semt.031.001.01 — exact business narrative, conditions and direction](../../../../messages/semt.031.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.031-END -->
