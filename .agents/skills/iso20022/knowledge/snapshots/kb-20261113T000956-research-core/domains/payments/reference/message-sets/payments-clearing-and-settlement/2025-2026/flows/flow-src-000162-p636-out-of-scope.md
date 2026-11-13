---
template: false
document_kind: "flow-context"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p636-out-of-scope"
title: "Out of Scope"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Payment Return in a FinancialInstitutionDirectDebit scenario"], "locator": "/w:document/w:body/w:p[636]", "paragraph_id": "P636", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Payment Return in a FinancialInstitutionDirectDebit scenario"], "locator": "/w:document/w:body/w:p[637]", "paragraph_id": "P637", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Payment Return in a FinancialInstitutionDirectDebit scenario"], "locator": "/w:document/w:body/w:p[638]", "paragraph_id": "P638", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Payment Return in a FinancialInstitutionDirectDebit scenario"], "locator": "/w:document/w:body/w:p[639]", "paragraph_id": "P639", "table_id": null}]
participants: ["participant-src-000162-debtor"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Out of Scope", "Debtor"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "This source-delimited heading/context is not an additional independent flow. Follow linked canonical flows for ordered responsibilities and message directions."]
manual_curated: true
issue_ids: []
related_flows: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p623-payment-return-in-a-financial-institution-direct-debit-scenario.md"]
context_review_date: "2026-11-09"
---



# Out of Scope

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Debtor | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P637** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages).

**P638** Some debtor agents potentially send the instruction to the debtor(s) for information (and value added) services. (Pre)Notifications are not included. 

**P639** The mandate/agreements related to the direct debit flows are not taken into account for the purpose of this document.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Heading path: BusinessTransactions / Direct Debit / FinancialInstitutionDirectDebit / Payment Return in a FinancialInstitutionDirectDebit scenario.

## Reviewed flow context

The source-delimited content above was checked with its complete process narrative, original picture and Word figure context. It is a contextual section, not a separate message exchange.

- [Payment Return in a FinancialInstitutionDirectDebit scenario](flow-src-000162-p623-payment-return-in-a-financial-institution-direct-debit-scenario.md)
