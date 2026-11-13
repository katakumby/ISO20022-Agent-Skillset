---
template: false
document_kind: "flow-context"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p492-out-of-scope"
title: "Out of scope"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "FIToFICustomerDirectDebit"], "locator": "/w:document/w:body/w:p[492]", "paragraph_id": "P492", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "FIToFICustomerDirectDebit"], "locator": "/w:document/w:body/w:p[493]", "paragraph_id": "P493", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "FIToFICustomerDirectDebit"], "locator": "/w:document/w:body/w:p[494]", "paragraph_id": "P494", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "FIToFICustomerDirectDebit"], "locator": "/w:document/w:body/w:p[495]", "paragraph_id": "P495", "table_id": null}]
participants: ["participant-src-000162-settlement-agent", "participant-src-000162-debtor-agent", "participant-src-000162-debtor"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Out of scope", "Settlement Agent", "Debtor agent", "Debtor"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "This source-delimited heading/context is not an additional independent flow. Follow linked canonical flows for ordered responsibilities and message directions."]
manual_curated: true
issue_ids: []
related_flows: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p468-fito-ficustomer-direct-debit.md"]
context_review_date: "2026-11-09"
---



# Out of scope

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Settlement Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-settlement-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P493** The debtor agent could optionally forward the direct debit instruction (simplified version) to the debtor (for example, in case pre-notifications are not used in a Scheme).

**P494** If clearing and settlement is carried out by two parties, the clearing agent prepares and sends the payment information for the settlement agent (in accordance with the agreed and published settlement cycle). The process includes the calculation of the settlement positions and transmission of the files to the settlement agent.

**P495** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages) to the debtors and creditors. Timing may vary depending on market practices and value added services provided by some agents that are before or after settlement.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Heading path: BusinessTransactions / Direct Debit / FIToFICustomerDirectDebit.

## Reviewed flow context

The source-delimited content above was checked with its complete process narrative, original picture and Word figure context. It is a contextual section, not a separate message exchange.

- [FIToFICustomerDirectDebit](flow-src-000162-p468-fito-ficustomer-direct-debit.md)
