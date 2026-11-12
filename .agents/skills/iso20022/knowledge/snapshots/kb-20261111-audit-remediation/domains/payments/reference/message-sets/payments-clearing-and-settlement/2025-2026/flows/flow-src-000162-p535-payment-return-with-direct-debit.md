---
template: false
document_kind: "flow-context"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p535-payment-return-with-direct-debit"
title: "PaymentReturn with Direct Debit"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "PaymentReturn with Direct Debit"], "locator": "/w:document/w:body/w:p[535]", "paragraph_id": "P535", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "PaymentReturn with Direct Debit"], "locator": "/w:document/w:body/w:p[536]", "paragraph_id": "P536", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "PaymentReturn with Direct Debit"], "locator": "/w:document/w:body/w:p[537]", "paragraph_id": "P537", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "PaymentReturn with Direct Debit"], "locator": "/w:document/w:body/w:p[538]", "paragraph_id": "P538", "table_id": null}]
participants: ["participant-src-000162-debtor-agent", "participant-src-000162-debtor", "participant-src-000162-party"]
message_mapping_evidence: [{"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["pacs.004"]
search_terms: ["PaymentReturn with Direct Debit", "Debtor agent", "Debtor", "Party", "pacs.004"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "This source-delimited heading/context is not an additional independent flow. Follow linked canonical flows for ordered responsibilities and message directions."]
manual_curated: true
issue_ids: []
related_flows: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p539-payment-return-initiated-by-debtor-agent.md", "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p553-refund-by-the-debtor.md"]
context_review_date: "2026-11-09"
---





# PaymentReturn with Direct Debit

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Debtor agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P536**  A PaymentReturn message is initiated by the debtor agent and sent to the previous party in the payment chain when a debit cannot be executed due to an administrative reason (for example non existing/closed account) or due to a banking reason (for example insufficient funds).

**P537** The PaymentReturn message is also the message to be used by the debtor agent following the receipt of a refund request by the debtor (out of scope) as it is assumed that the refund request will be done through a non-automated tool (for example phone/fax) and is not part of the scope.

**P538** In this case, the PaymentReturn message will contain a code to indicate that it is triggered by a request for refund by the debtor. 

## Messages and alternative paths

Source-supported message family mentions: `pacs.004`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Heading path: BusinessTransactions / Direct Debit / PaymentReturn with Direct Debit.

<!-- CLEARING-CONTEXT -->
[Curated full process context, participants, alternatives and source evidence](flow-src-000162-p539-payment-return-initiated-by-debtor-agent.md)
<!-- /CLEARING-CONTEXT -->

## Reviewed flow context

The source-delimited content above was checked with its complete process narrative, original picture and Word figure context. It is a contextual section, not a separate message exchange.

- [PaymentReturn Initiated by Debtor Agent](flow-src-000162-p539-payment-return-initiated-by-debtor-agent.md)
- [Refund by the Debtor](flow-src-000162-p553-refund-by-the-debtor.md)
