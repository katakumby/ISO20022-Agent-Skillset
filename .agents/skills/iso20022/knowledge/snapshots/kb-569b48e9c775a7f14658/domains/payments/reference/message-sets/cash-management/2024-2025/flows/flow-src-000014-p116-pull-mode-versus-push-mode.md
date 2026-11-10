---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
flow_id: "flow-src-000014-p116-pull-mode-versus-push-mode"
title: "Pull Mode versus Push Mode"
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Pull Mode versus Push Mode"], "locator": "/w:document/w:body/w:p[116]", "paragraph_id": "P116", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Pull Mode versus Push Mode"], "locator": "/w:document/w:body/w:p[117]", "paragraph_id": "P117", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Pull Mode versus Push Mode"], "locator": "/w:document/w:body/w:p[118]", "paragraph_id": "P118", "table_id": null}]
participants: []
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Pull Mode versus Push Mode"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Pull Mode versus Push Mode

Source context: Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P117** The Get/Return messages have been designed in pairs: a Get message is replied to by a Return message. This concept implies that the interaction between the transaction administrator and the member is normally in pull mode where the member initiates the information flow by sending a request in the form of a Get message.

**P118** Return messages can however also be sent without a previous Get message. This is called push mode. The push of information can take place either at pre-agreed times or as a warning or alarm when a problem has occurred.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000014](../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md). Heading path: BusinessTransactions / How to use the Cash Management Messages / Pull Mode versus Push Mode.
