---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p261-positive-customer-and-fito-fipayment-status-report-with-direct-debit"
title: "Positive Customer and FIToFIPaymentStatusReport with Direct Debit"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit"], "locator": "/w:document/w:body/w:p[261]", "paragraph_id": "P261", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit"], "locator": "/w:document/w:body/w:p[262]", "paragraph_id": "P262", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit"], "locator": "/w:document/w:body/w:p[263]", "paragraph_id": "P263", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit"], "locator": "/w:document/w:body/w:p[264]", "paragraph_id": "P264", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit"], "locator": "/w:document/w:body/w:p[265]", "paragraph_id": "P265", "table_id": null}]
participants: []
message_mapping_evidence: [{"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["pain.002"]
search_terms: ["Positive Customer and FIToFIPaymentStatusReport with Direct Debit", "pain.002"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---



# Positive Customer and FIToFIPaymentStatusReport with Direct Debit

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P262** The positive CustomerPaymentStatusReport message (single or grouped) and FIToFIPaymentStatusReport message (single or grouped) is sent by the receiver of an instruction to inform the receiver that the instruction received is processable.

**P263** A positive CustomerPaymentStatusReport message or FIToFIPaymentStatusReport message can also be used to confirm the processability of a PaymentReturn message (in case of FIToFI) or a PaymentReversal message.

**P264** The positive CustomerPaymentStatusReport message and FIToFIPaymentStatusReport message are also meant to be generic to ensure re-usability with other Payments Instruments.

**P265** The CustomerPaymentStatusReport and FIToFIPaymentStatusReport messages are exchanged, point to point between two parties, optionally and as per bilateral agreements and may be complemented by a BankToCustomerDebitCreditNotification message ('notification') and/or BankToCustomerAccountReport/ BankToCustomerStatement message ('statement').

## Messages and alternative paths

Source-supported message family mentions: `pain.002`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Heading path: BusinessTransactions / Positive Customer and FIToFIPaymentStatusReport with Direct Debit.

<!-- INITIATION-CONTEXT -->
[Reviewed full flow context, literal directions, participants and source qualifications](flow-src-000173-p266-confirmation-of-processability-of-customer-direct-debit-initiation.md)
<!-- /INITIATION-CONTEXT -->
