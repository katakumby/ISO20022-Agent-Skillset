---
template: false
document_kind: "flow-context"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p166-business-transactions"
title: "BusinessTransactions"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[166]", "paragraph_id": "P166", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[167]", "paragraph_id": "P167", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[168]", "paragraph_id": "P168", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:tbl[27]", "paragraph_id": null, "table_id": "T27"}]
participants: []
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["BusinessTransactions"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "This source-delimited heading/context is not an additional independent flow. Follow linked canonical flows for ordered responsibilities and message directions."]
manual_curated: true
issue_ids: []
related_flows: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p177-debtor-agent-and-creditor-agent-are-correspondents.md", "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p303-debtor-and-creditor-are-correspondents.md", "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p468-fito-ficustomer-direct-debit.md", "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p585-creditor-and-debtor-agent-are-correspondents.md"]
context_review_date: "2026-11-09"
---



# BusinessTransactions

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P167** This section describes the message flows based on the activity diagrams documented above. It shows the typical exchanges of information in the context of a BusinessTransaction.

**P168** When relevant, messages from other business areas, which are necessary for a complete understanding of the transaction, are shown on the BusinessTransaction diagrams:

Source table [T27](../documents/src-000162/tables/tbl-0027.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Heading path: BusinessTransactions.

## Reviewed flow context

The source-delimited content above was checked with its complete process narrative, original picture and Word figure context. It is a contextual section, not a separate message exchange.

- [Debtor Agent and Creditor Agent are Correspondents](flow-src-000162-p177-debtor-agent-and-creditor-agent-are-correspondents.md)
- [Debtor and Creditor are Correspondents](flow-src-000162-p303-debtor-and-creditor-are-correspondents.md)
- [FIToFICustomerDirectDebit](flow-src-000162-p468-fito-ficustomer-direct-debit.md)
- [Creditor and Debtor Agent are correspondents](flow-src-000162-p585-creditor-and-debtor-agent-are-correspondents.md)
