---
template: false
document_kind: "flow-context"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p617-out-of-scope"
title: "Out of Scope"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor Agent and Debtor Agent are not correspondents"], "locator": "/w:document/w:body/w:p[617]", "paragraph_id": "P617", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor Agent and Debtor Agent are not correspondents"], "locator": "/w:document/w:body/w:p[618]", "paragraph_id": "P618", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor Agent and Debtor Agent are not correspondents"], "locator": "/w:document/w:body/w:p[619]", "paragraph_id": "P619", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor Agent and Debtor Agent are not correspondents"], "locator": "/w:document/w:body/w:p[620]", "paragraph_id": "P620", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor Agent and Debtor Agent are not correspondents"], "locator": "/w:document/w:body/w:p[621]", "paragraph_id": "P621", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor Agent and Debtor Agent are not correspondents"], "locator": "/w:document/w:body/w:p[622]", "paragraph_id": "P622", "table_id": null}]
participants: ["participant-src-000162-financial-institution", "participant-src-000162-intermediary-agent", "participant-src-000162-debtor-agent", "participant-src-000162-creditor", "participant-src-000162-debtor"]
message_mapping_evidence: [{"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["pacs.009", "pacs.010"]
search_terms: ["Out of Scope", "Financial Institution", "Intermediary Agent", "Debtor agent", "Creditor", "Debtor", "pacs.009", "pacs.010"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "This source-delimited heading/context is not an additional independent flow. Follow linked canonical flows for ordered responsibilities and message directions."]
manual_curated: true
issue_ids: []
related_flows: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p607-creditor-agent-and-debtor-agent-are-not-correspondents.md"]
context_review_date: "2026-11-09"
---



# Out of Scope

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Financial Institution | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-financial-institution.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Intermediary Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-intermediary-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Creditor | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P618** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages).

**P619** Some debtor agents potentially send the instruction to the debtor(s) for information (and value added) services. (Pre)Notifications are not included. 

**P620** The mandate/agreements related to the direct debit flows are not taken into account for the purpose of this document.

**P621** If the FinancialInstitutionDirectDebit cannot be processed by the debtor agent, a negative FIToFIPaymentsStatusReport message is sent back to the creditor before settlement and no FinancialInstitutionCreditTransfer will be sent to the intermediary agent.

## Messages and alternative paths

Source-supported message family mentions: `pacs.009`, `pacs.010`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Heading path: BusinessTransactions / Direct Debit / FinancialInstitutionDirectDebit / Creditor Agent and Debtor Agent are not correspondents.

## Reviewed flow context

The source-delimited content above was checked with its complete process narrative, original picture and Word figure context. It is a contextual section, not a separate message exchange.

- [Creditor Agent and Debtor Agent are not correspondents](flow-src-000162-p607-creditor-agent-and-debtor-agent-are-not-correspondents.md)
