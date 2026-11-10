---
template: false
document_kind: "flow-context"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p407-payment-return-with-financial-institution-credit-transfer"
title: "PaymentReturn with FinancialInstitutionCreditTransfer"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "PaymentReturn with FinancialInstitutionCreditTransfer "], "locator": "/w:document/w:body/w:p[407]", "paragraph_id": "P407", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "PaymentReturn with FinancialInstitutionCreditTransfer "], "locator": "/w:document/w:body/w:p[408]", "paragraph_id": "P408", "table_id": null}]
participants: ["participant-src-000162-financial-institution", "participant-src-000162-party"]
message_mapping_evidence: [{"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["pacs.004", "pacs.009"]
search_terms: ["PaymentReturn with FinancialInstitutionCreditTransfer", "Financial Institution", "Party", "pacs.004", "pacs.009"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "This source-delimited heading/context is not an additional independent flow. Follow linked canonical flows for ordered responsibilities and message directions."]
manual_curated: true
issue_ids: []
related_flows: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p409-debtor-and-creditor-are-direct-correspondents.md", "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p420-debtor-agent-and-creditor-are-correspondents.md", "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p433-debtor-agent-and-creditor-agent-are-correspondents.md", "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p445-debtor-agent-and-creditor-agent-are-not-correspondents.md"]
context_review_date: "2026-11-09"
---





# PaymentReturn with FinancialInstitutionCreditTransfer

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Financial Institution | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-financial-institution.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P408** The PaymentReturn message is sent by an instructed agent to the previous party in the payment chain when a payment cannot be executed due to an administrative reason (for example, non existing/closed account) or banking reason (for example, insufficient funds).

## Messages and alternative paths

Source-supported message family mentions: `pacs.004`, `pacs.009`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Heading path: BusinessTransactions / Credit Transfer / PaymentReturn with FinancialInstitutionCreditTransfer .

<!-- CLEARING-CONTEXT -->
[Curated full process context, participants, alternatives and source evidence](flow-src-000162-p409-debtor-and-creditor-are-direct-correspondents.md)
<!-- /CLEARING-CONTEXT -->

## Reviewed flow context

The source-delimited content above was checked with its complete process narrative, original picture and Word figure context. It is a contextual section, not a separate message exchange.

- [Debtor and Creditor are direct Correspondents](flow-src-000162-p409-debtor-and-creditor-are-direct-correspondents.md)
- [Debtor Agent and Creditor are Correspondents](flow-src-000162-p420-debtor-agent-and-creditor-are-correspondents.md)
- [Debtor Agent and Creditor Agent are Correspondents](flow-src-000162-p433-debtor-agent-and-creditor-agent-are-correspondents.md)
- [Debtor Agent and Creditor Agent are Not Correspondents](flow-src-000162-p445-debtor-agent-and-creditor-agent-are-not-correspondents.md)
