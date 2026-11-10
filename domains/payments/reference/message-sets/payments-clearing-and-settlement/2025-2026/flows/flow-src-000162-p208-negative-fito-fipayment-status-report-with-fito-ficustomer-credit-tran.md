---
template: false
document_kind: "flow-context"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p208-negative-fito-fipayment-status-report-with-fito-ficustomer-credit-tran"
title: "Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer"], "locator": "/w:document/w:body/w:p[208]", "paragraph_id": "P208", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer"], "locator": "/w:document/w:body/w:p[209]", "paragraph_id": "P209", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer"], "locator": "/w:document/w:body/w:p[210]", "paragraph_id": "P210", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer"], "locator": "/w:document/w:body/w:p[211]", "paragraph_id": "P211", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer"], "locator": "/w:document/w:body/w:p[212]", "paragraph_id": "P212", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Credit Transfer", "Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer"], "locator": "/w:document/w:body/w:p[213]", "paragraph_id": "P213", "table_id": null}]
participants: ["participant-src-000162-financial-institution"]
message_mapping_evidence: [{"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[4]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["pacs.002", "pacs.004", "pacs.008", "pacs.009"]
search_terms: ["Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer", "Financial Institution", "pacs.002", "pacs.004", "pacs.008", "pacs.009"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "This source-delimited heading/context is not an additional independent flow. Follow linked canonical flows for ordered responsibilities and message directions."]
manual_curated: true
issue_ids: []
related_flows: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p214-debtor-agent-and-creditor-agent-are-direct-correspondents.md", "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p221-debtor-agent-and-creditor-agent-are-not-correspondents-1.md", "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p236-debtor-agent-and-creditor-agent-are-not-correspondents-2.md"]
context_review_date: "2026-11-09"
---





# Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Financial Institution | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-financial-institution.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P209** The negative FIToFIPaymentStatusReport message is used, point to point between two parties, to report about the negative processability of an instruction, that is, to report about the rejection of the instruction, and is used to:

**P210** Reject an FIToFICustomerCreditTransfer

**P211** Reject a FinancialInstitutionCreditTransfer

**P212** The negative FIToFIPaymentStatusReport message is sent before settlement.

**P213** After settlement, the correct message to be used is the PaymentReturn message, the BankToCustomerDebitCreditNotification message ('notification') and/or the BankToCustomerAccountReport/ BankToCustomerStatement message ('statement'). Different options are illustrated in the sequence diagram.

## Messages and alternative paths

Source-supported message family mentions: `pacs.002`, `pacs.004`, `pacs.008`, `pacs.009`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Heading path: BusinessTransactions / Credit Transfer / Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer.

<!-- CLEARING-CONTEXT -->
[Curated full process context, participants, alternatives and source evidence](flow-src-000162-p214-debtor-agent-and-creditor-agent-are-direct-correspondents.md)
<!-- /CLEARING-CONTEXT -->

## Reviewed flow context

The source-delimited content above was checked with its complete process narrative, original picture and Word figure context. It is a contextual section, not a separate message exchange.

- [Debtor Agent and Creditor Agent are Direct Correspondents](flow-src-000162-p214-debtor-agent-and-creditor-agent-are-direct-correspondents.md)
- [Debtor Agent and Creditor Agent are not Correspondents - 1](flow-src-000162-p221-debtor-agent-and-creditor-agent-are-not-correspondents-1.md)
- [Debtor Agent and Creditor Agent are not Correspondents - 2](flow-src-000162-p236-debtor-agent-and-creditor-agent-are-not-correspondents-2.md)
