---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
flow_id: "flow-src-000014-p155-using-error-codes"
title: "Using Error Codes"
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Controlling the Quantity of Returned Information"], "locator": "/w:document/w:body/w:p[155]", "paragraph_id": "P155", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Controlling the Quantity of Returned Information"], "locator": "/w:document/w:body/w:p[156]", "paragraph_id": "P156", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Controlling the Quantity of Returned Information"], "locator": "/w:document/w:body/w:p[157]", "paragraph_id": "P157", "table_id": null}]
participants: []
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Using Error Codes"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Using Error Codes

Source context: Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P156** Errors may be expressed at two different levels of the Return message:

**P157** If the Get message could not be processed at all, the error code will be the only relevant information in the Return message, and no retrieved information will be returned.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000014](../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md). Heading path: BusinessTransactions / How to use the Cash Management Messages / Controlling the Quantity of Returned Information.
