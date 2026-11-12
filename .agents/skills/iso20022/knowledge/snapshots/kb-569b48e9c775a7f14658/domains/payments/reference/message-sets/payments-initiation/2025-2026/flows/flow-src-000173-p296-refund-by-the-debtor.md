---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p296-refund-by-the-debtor"
title: "Refund by the Debtor"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit", "Refund by the Debtor"], "locator": "/w:document/w:body/w:p[296]", "paragraph_id": "P296", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "PaymentReturn with Direct Debit", "Refund by the Debtor"], "locator": "/w:document/w:body/w:p[297]", "paragraph_id": "P297", "table_id": null}]
participants: ["participant-src-000173-debtor-agent", "participant-src-000173-debtor"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Refund by the Debtor", "Debtor Agent", "Debtor"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---



# Refund by the Debtor

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Debtor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P297** This scenario is similar to the previous scenario, except that the PaymentReturn message by the debtor agent to the clearing and settlement agent is triggered by a Refund Request by the debtor to his agent, the debtor agent (in a non-automated manner). In this case, the PaymentReturn message will contain a code indicating that it was triggered by a request for refund by the debtor.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Heading path: BusinessTransactions / PaymentReturn with Direct Debit / Refund by the Debtor.

<!-- INITIATION-CONTEXT -->
[Reviewed full flow context, literal directions, participants and source qualifications](flow-src-000173-p280-payment-return-initiated-by-debtor-agent.md)
<!-- /INITIATION-CONTEXT -->
