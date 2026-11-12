---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
flow_id: "flow-src-000014-p146-reconciling-get-and-return-messages"
title: "Reconciling Get and Return Messages"
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Features of Get and Return Messages"], "locator": "/w:document/w:body/w:p[146]", "paragraph_id": "P146", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Features of Get and Return Messages"], "locator": "/w:document/w:body/w:p[147]", "paragraph_id": "P147", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Features of Get and Return Messages"], "locator": "/w:document/w:body/w:p[148]", "paragraph_id": "P148", "table_id": null}]
participants: []
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Reconciling Get and Return Messages"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Reconciling Get and Return Messages

Source context: Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P147** The reconciliation of the Get and Return messages takes place via the QueryReference element of the Return message.

**P148** This element contains the message identification of the Get message to which it is replying and, optionally the name of the query.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000014](../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md). Heading path: BusinessTransactions / How to use the Cash Management Messages / Features of Get and Return Messages.
