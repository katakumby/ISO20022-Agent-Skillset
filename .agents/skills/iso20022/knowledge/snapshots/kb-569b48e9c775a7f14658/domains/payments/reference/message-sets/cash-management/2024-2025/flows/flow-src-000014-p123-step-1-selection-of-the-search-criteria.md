---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
flow_id: "flow-src-000014-p123-step-1-selection-of-the-search-criteria"
title: "Step 1 - Selection of the Search Criteria"
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Building a Get Message"], "locator": "/w:document/w:body/w:p[123]", "paragraph_id": "P123", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Building a Get Message"], "locator": "/w:document/w:body/w:p[124]", "paragraph_id": "P124", "table_id": null}]
participants: []
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Step 1 - Selection of the Search Criteria"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Step 1 - Selection of the Search Criteria

Source context: Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P124** Each Get message definition describes a potential set of search criteria. These search criteria can be combined. The more search criteria used, the more refined the Get message will be. When different search criteria are combined, these have to be interpreted as an 'AND' operator, for example, if balance information is requested based on the currency of the account AND on the value date, only the balances meeting both criteria at the same time will be returned.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000014](../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md). Heading path: BusinessTransactions / How to use the Cash Management Messages / Building a Get Message.
