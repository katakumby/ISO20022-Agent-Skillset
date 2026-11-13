---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
flow_id: "flow-src-000014-p152-controlling-the-quantity-of-returned-information"
title: "Controlling the Quantity of Returned Information"
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Controlling the Quantity of Returned Information"], "locator": "/w:document/w:body/w:p[152]", "paragraph_id": "P152", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Controlling the Quantity of Returned Information"], "locator": "/w:document/w:body/w:p[153]", "paragraph_id": "P153", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Controlling the Quantity of Returned Information"], "locator": "/w:document/w:body/w:p[154]", "paragraph_id": "P154", "table_id": null}]
participants: []
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Controlling the Quantity of Returned Information"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Controlling the Quantity of Returned Information

Source context: Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P153** In all Get messages, an element QueryType makes it possible to limit the returned information to changes compared to the information returned in a preceding Return message. 

**P154** This option should only be used in relation to a query sent previously with the same search criteria/same query name.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000014](../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md). Heading path: BusinessTransactions / How to use the Cash Management Messages / Controlling the Quantity of Returned Information.
