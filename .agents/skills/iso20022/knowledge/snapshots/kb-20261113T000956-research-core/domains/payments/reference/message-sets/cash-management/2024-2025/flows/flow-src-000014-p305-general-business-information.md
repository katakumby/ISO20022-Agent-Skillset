---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
flow_id: "flow-src-000014-p305-general-business-information"
title: "General Business Information"
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "System Status ", "General Business Information"], "locator": "/w:document/w:body/w:p[305]", "paragraph_id": "P305", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "System Status ", "General Business Information"], "locator": "/w:document/w:body/w:p[306]", "paragraph_id": "P306", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "System Status ", "General Business Information"], "locator": "/w:document/w:body/w:p[307]", "paragraph_id": "P307", "table_id": null}]
participants: []
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["General Business Information"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# General Business Information

Source context: Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P306** The transaction administrator can send general business information messages to the members, which may request further action from them. General business information can contain either, static data announcing foreseen events affecting the system, or dynamic data, warning or notifying about unexpected events.

**P307** This type of information can be transmitted in either of the two following ways:

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000014](../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md). Heading path: BusinessTransactions / System Status  / General Business Information.
