---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p160-interbank-clearing-and-settlement-between-debtor-agent-and-creditor-ag"
title: "Interbank clearing and settlement between debtor agent and creditor agent"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation"], "locator": "/w:document/w:body/w:p[160]", "paragraph_id": "P160", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation"], "locator": "/w:document/w:body/w:p[161]", "paragraph_id": "P161", "table_id": null}]
participants: ["participant-src-000173-creditor-agent", "participant-src-000173-debtor-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Interbank clearing and settlement between debtor agent and creditor agent", "Creditor Agent", "Debtor Agent"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---



# Interbank clearing and settlement between debtor agent and creditor agent

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Creditor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P161** Depending on the interbank clearing and settlement method chosen, a number of messages may be exchanged between the agent parties in the payment chain.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Heading path: BusinessTransactions / CustomerCreditTransferInitiation.

<!-- INITIATION-CONTEXT -->
[Reviewed full flow context, literal directions, participants and source qualifications](flow-src-000173-p170-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor-s.md)
<!-- /INITIATION-CONTEXT -->
