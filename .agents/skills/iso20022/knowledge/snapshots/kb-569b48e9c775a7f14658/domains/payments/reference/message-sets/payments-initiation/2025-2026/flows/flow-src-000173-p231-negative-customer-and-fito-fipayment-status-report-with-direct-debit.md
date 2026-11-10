---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p231-negative-customer-and-fito-fipayment-status-report-with-direct-debit"
title: "Negative Customer and FIToFIPaymentStatusReport with Direct Debit"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit"], "locator": "/w:document/w:body/w:p[231]", "paragraph_id": "P231", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit"], "locator": "/w:document/w:body/w:p[232]", "paragraph_id": "P232", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit"], "locator": "/w:document/w:body/w:p[233]", "paragraph_id": "P233", "table_id": null}]
participants: []
message_mapping_evidence: [{"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["pain.002"]
search_terms: ["Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "pain.002"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---



# Negative Customer and FIToFIPaymentStatusReport with Direct Debit

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P232** The negative CustomerPaymentStatusReport message (single or grouped) or FItoFIPaymentStatusReport message (single or grouped) is sent by the receiver of an instruction to inform the sender of the instruction about the negative processability of the instruction.

**P233** The negative CustomerPaymentStatusReport message FIToFIPaymentStatusReport message used to reject a direct debit instruction, is to be sent before settlement. After settlement, the correct message to be used is the PaymentReturn message.

## Messages and alternative paths

Source-supported message family mentions: `pain.002`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Heading path: BusinessTransactions / Negative Customer and FIToFIPaymentStatusReport with Direct Debit.

<!-- INITIATION-CONTEXT -->
[Reviewed full flow context, literal directions, participants and source qualifications](flow-src-000173-p234-negative-customer-payment-status-report-creditor-agent.md)
<!-- /INITIATION-CONTEXT -->
