---
template: false
document_kind: "flow-context"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p195-out-of-scope"
title: "Out of Scope"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "FIToFICustomerCreditTransfer", "Debtor Agent and Creditor Agent are not Correspondents - 1 "], "locator": "/w:document/w:body/w:p[195]", "paragraph_id": "P195", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "FIToFICustomerCreditTransfer", "Debtor Agent and Creditor Agent are not Correspondents - 1 "], "locator": "/w:document/w:body/w:p[196]", "paragraph_id": "P196", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "FIToFICustomerCreditTransfer", "Debtor Agent and Creditor Agent are not Correspondents - 1 "], "locator": "/w:document/w:body/w:p[197]", "paragraph_id": "P197", "table_id": null}]
participants: ["participant-src-000162-intermediary-agent", "participant-src-000162-debtor-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Out of Scope", "Intermediary Agent", "Debtor agent"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "This source-delimited heading/context is not an additional independent flow. Follow linked canonical flows for ordered responsibilities and message directions."]
manual_curated: true
issue_ids: []
related_flows: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p186-debtor-agent-and-creditor-agent-are-not-correspondents-1.md"]
context_review_date: "2026-11-09"
---



# Out of Scope

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Intermediary Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-intermediary-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P196** The intermediary agent may send a status update to the debtor agent.

**P197** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Heading path: BusinessTransactions / Credit Transfer / FIToFICustomerCreditTransfer / Debtor Agent and Creditor Agent are not Correspondents - 1 .

## Reviewed flow context

The source-delimited content above was checked with its complete process narrative, original picture and Word figure context. It is a contextual section, not a separate message exchange.

- [Debtor Agent and Creditor Agent are not Correspondents - 1](flow-src-000162-p186-debtor-agent-and-creditor-agent-are-not-correspondents-1.md)
