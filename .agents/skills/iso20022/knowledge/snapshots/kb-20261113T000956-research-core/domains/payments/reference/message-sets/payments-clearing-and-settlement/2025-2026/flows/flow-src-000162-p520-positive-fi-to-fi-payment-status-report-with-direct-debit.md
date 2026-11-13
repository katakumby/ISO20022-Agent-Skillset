---
template: false
document_kind: "flow-context"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p520-positive-fi-to-fi-payment-status-report-with-direct-debit"
title: "Positive FI To FI Payment Status Report with Direct Debit"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit"], "locator": "/w:document/w:body/w:p[520]", "paragraph_id": "P520", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit"], "locator": "/w:document/w:body/w:p[521]", "paragraph_id": "P521", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit"], "locator": "/w:document/w:body/w:p[522]", "paragraph_id": "P522", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit"], "locator": "/w:document/w:body/w:p[523]", "paragraph_id": "P523", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit"], "locator": "/w:document/w:body/w:p[524]", "paragraph_id": "P524", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit"], "locator": "/w:document/w:body/w:p[525]", "paragraph_id": "P525", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit"], "locator": "/w:document/w:body/w:p[526]", "paragraph_id": "P526", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit"], "locator": "/w:document/w:body/w:p[527]", "paragraph_id": "P527", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit"], "locator": "/w:document/w:body/w:p[528]", "paragraph_id": "P528", "table_id": null}]
participants: []
message_mapping_evidence: [{"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[4]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["pacs.002", "pacs.004", "pacs.007"]
search_terms: ["Positive FI To FI Payment Status Report with Direct Debit", "pacs.002", "pacs.004", "pacs.007"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "This source-delimited heading/context is not an additional independent flow. Follow linked canonical flows for ordered responsibilities and message directions."]
manual_curated: true
issue_ids: ["issue-000054"]
related_flows: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p529-fito-fipayment-status-report-to-confirm-processability-of-fito-ficusto.md"]
context_review_date: "2026-11-09"
---





# Positive FI To FI Payment Status Report with Direct Debit

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P521** The positive FIToFIPaymentStatusReport message is sent by the receiver of an instruction to inform the receiver that the instruction received (either single or grouped) is processable.

**P522** A positive FIToFIPaymentStatusReport message can also be used to confirm the processability of a PaymentReturn message or an FIToFIPaymentReversal message.

**P523** The positive FIToFIPaymentStatusReport message is also meant to be generic to ensure re-usability with other Payments Instruments.

**P524** The FIToFIPaymentStatusReport messages are exchanged, point to point between two parties, optionally and as per optional bilateral agreements and may be complemented by an BankToCustomerDebitCreditNotification message ('notification') and/or BankToCustomerAccountReport/BankToCustomerStatement message ('statement').

Source diagram evidence: [fig-0040](../documents/src-000162/diagrams/fig-0040.md). Mermaid reconstruction and visual review are pending.

**P526** The positive CustomerPaymentStatusReport and FIToFIPaymentStatusReport messages are optional.

**P527** As added value service to creditors, some banks may update CustomerPaymentStatusReport messages to inform creditors about the status of transactions during their lifecycle.

**P528** Mixed CustomerPaymentStatusReport and FIToFIPaymentStatusReport messages may be exchanged, that is, ‘partially accepted’ on group level, indicated that the group contains a mix of accepted, pending and/or rejected transactions.

## Messages and alternative paths

Source-supported message family mentions: `pacs.002`, `pacs.004`, `pacs.007`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Heading path: BusinessTransactions / Direct Debit / Positive FI To FI Payment Status Report with Direct Debit.

<!-- CLEARING-CONTEXT -->
[Curated full process context, participants, alternatives and source evidence](flow-src-000162-p529-fito-fipayment-status-report-to-confirm-processability-of-fito-ficusto.md)
<!-- /CLEARING-CONTEXT -->

## Reviewed flow context

The source-delimited content above was checked with its complete process narrative, original picture and Word figure context. It is a contextual section, not a separate message exchange.

- [FIToFIPaymentStatusReport to confirm Processability of FIToFICustomerDirectDebit instruction](flow-src-000162-p529-fito-fipayment-status-report-to-confirm-processability-of-fito-ficusto.md)
