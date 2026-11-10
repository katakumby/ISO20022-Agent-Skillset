---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p278-payment-return-with-direct-debit"
title: "PaymentReturn with Direct Debit"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit"], "locator": "/w:document/w:body/w:p[278]", "paragraph_id": "P278", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit"], "locator": "/w:document/w:body/w:p[279]", "paragraph_id": "P279", "table_id": null}]
participants: ["participant-src-000173-debtor-agent", "participant-src-000173-debtor", "participant-src-000173-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["PaymentReturn with Direct Debit", "Debtor Agent", "Debtor", "Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---



# PaymentReturn with Direct Debit

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Debtor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P279** A PaymentReturn message is initiated by the debtor agent and sent to the previous party in the payment chain when a debit cannot be executed due to an administrative reason (such as non-existing/closed account) or due to a banking reason (such as insufficient funds). The PaymentReturn message is also the message to be used by the debtor agent following the receipt of a refund request by the debtor as it is assumed that the refund request will be done through a non-automated tool (such as phone/fax) and is not part of the scope. In this case, the PaymentReturn message will contain a code to indicate that it is triggered by a request for refund by the debtor.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Heading path: BusinessTransactions / PaymentReturn with Direct Debit.

<!-- INITIATION-CONTEXT -->
[Reviewed full flow context, literal directions, participants and source qualifications](flow-src-000173-p280-payment-return-initiated-by-debtor-agent.md)
<!-- /INITIATION-CONTEXT -->
