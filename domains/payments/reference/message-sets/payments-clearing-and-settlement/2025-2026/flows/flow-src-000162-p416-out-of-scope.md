---
template: false
document_kind: "flow-context"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p416-out-of-scope"
title: "Out of Scope"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "PaymentReturn with FinancialInstitutionCreditTransfer ", "Debtor and Creditor are direct Correspondents"], "locator": "/w:document/w:body/w:p[416]", "paragraph_id": "P416", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "PaymentReturn with FinancialInstitutionCreditTransfer ", "Debtor and Creditor are direct Correspondents"], "locator": "/w:document/w:body/w:p[417]", "paragraph_id": "P417", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "PaymentReturn with FinancialInstitutionCreditTransfer ", "Debtor and Creditor are direct Correspondents"], "locator": "/w:document/w:body/w:p[418]", "paragraph_id": "P418", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "PaymentReturn with FinancialInstitutionCreditTransfer ", "Debtor and Creditor are direct Correspondents"], "locator": "/w:document/w:body/w:p[419]", "paragraph_id": "P419", "table_id": null}]
participants: ["participant-src-000162-creditor-agent", "participant-src-000162-debtor"]
message_mapping_evidence: [{"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[4]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["pacs.002"]
search_terms: ["Out of Scope", "Creditor Agent", "Debtor", "pacs.002"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "This source-delimited heading/context is not an additional independent flow. Follow linked canonical flows for ordered responsibilities and message directions."]
manual_curated: true
issue_ids: []
related_flows: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p409-debtor-and-creditor-are-direct-correspondents.md"]
context_review_date: "2026-11-09"
---



# Out of Scope

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Creditor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P417** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

**P418** The case where the debtor and the creditor agent are correspondents is very similar. Therefore, it is not illustrated. The scenario would cover the case where the debtor services an account for the creditor agent and the case where the debtor and the creditor agent are linked through a clearing and settlement system.

**P419** If the creditor agent services an account for the debtor, the creditor agent will inform about the non- processability of the instruction by using a negative FIToFIPaymentStatusReport message to reject the instruction.

## Messages and alternative paths

Source-supported message family mentions: `pacs.002`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Heading path: BusinessTransactions / Credit Transfer / PaymentReturn with FinancialInstitutionCreditTransfer  / Debtor and Creditor are direct Correspondents.

## Reviewed flow context

The source-delimited content above was checked with its complete process narrative, original picture and Word figure context. It is a contextual section, not a separate message exchange.

- [Debtor and Creditor are direct Correspondents](flow-src-000162-p409-debtor-and-creditor-are-direct-correspondents.md)
