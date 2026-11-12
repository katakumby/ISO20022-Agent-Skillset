---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
flow_id: "flow-src-000014-p141-building-a-return-message"
title: "Building a Return Message"
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Building a Return Message"], "locator": "/w:document/w:body/w:p[141]", "paragraph_id": "P141", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Building a Return Message"], "locator": "/w:document/w:body/w:p[142]", "paragraph_id": "P142", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Building a Return Message"], "locator": "/w:document/w:body/w:p[143]", "paragraph_id": "P143", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Building a Return Message"], "locator": "/w:document/w:body/w:p[144]", "paragraph_id": "P144", "table_id": null}]
participants: []
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Building a Return Message"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Building a Return Message

Source context: Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P142** The Return message contains the result of the Get message processing. Depending on the success or failure of the processing, the Return message may or may not contain an error notification.

**P143** As explained earlier, Return messages could also be sent spontaneously by the transaction administrator.

**P144** The agreement between the parties may stipulate, where relevant, the size and the maximum number of items to be returned within the Return message. The maximum size of the Return message, or the maximum number of occurrences allowed, have to take into account technical constraints, such as the maximum payload size on the communication network. These characteristics are considered external to the standards design and are therefore not explained in this document.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000014](../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md). Heading path: BusinessTransactions / How to use the Cash Management Messages / Building a Return Message.
