---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
flow_id: "flow-src-000014-p170-liquidity-management"
title: "Liquidity Management"
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "Liquidity Management"], "locator": "/w:document/w:body/w:p[170]", "paragraph_id": "P170", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "Liquidity Management"], "locator": "/w:document/w:body/w:p[171]", "paragraph_id": "P171", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "Liquidity Management"], "locator": "/w:document/w:body/w:p[172]", "paragraph_id": "P172", "table_id": null}]
participants: []
message_mapping_evidence: [{"source_id": "src-000014", "heading_path": ["Scope and Functionality", "Scope", "Groups", "System Status Management "], "locator": "/w:document/w:body/w:tbl[8]/w:tr[8]", "paragraph_id": null, "table_id": "T8"}, {"source_id": "src-000014", "heading_path": ["Scope and Functionality", "Scope", "Groups", "Liquidity Management "], "locator": "/w:document/w:body/w:tbl[10]/w:tr[2]", "paragraph_id": null, "table_id": "T10"}]
message_ids: []
message_families: ["camt.025", "camt.050"]
search_terms: ["Liquidity Management", "camt.025", "camt.050"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Liquidity Management

Source context: Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P171** Transfers are processed only when the balance in the account to be debited is sufficient to pass the liquidity transfer instruction and remain positive. Based on the criteria received within the LiquidityCreditTransfer message, the transaction administrator will execute or reject the requested transfer through the Receipt (camt.025) message.

**P172** In principle, the transaction administrator may send a Receipt message as a reply to the liquidity transfer request. To verify the outcome of the request, the member may submit a request to query on the status of the transaction and / or the account message with the appropriate search criteria.

## Messages and alternative paths

Source-supported message family mentions: `camt.025`, `camt.050`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000014](../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md). Heading path: BusinessTransactions / Liquidity Management.
