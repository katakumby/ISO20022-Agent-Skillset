---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p640-fito-fipayment-reversal-with-direct-debit"
title: "FIToFIPaymentReversal with Direct Debit"
source_locations: [{"source_id": "src-000162", "locator": "/w:document/w:body/w:p[580]", "paragraph_id": "P580", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[581]", "paragraph_id": "P581", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[582]", "paragraph_id": "P582", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[583]", "paragraph_id": "P583", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[584]", "paragraph_id": "P584", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[640]", "paragraph_id": "P640", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "FIToFIPaymentReversal with Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[641]", "paragraph_id": "P641", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "FIToFIPaymentReversal with Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[642]", "paragraph_id": "P642", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "FIToFIPaymentReversal with Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[643]", "paragraph_id": "P643", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "FIToFIPaymentReversal with Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[644]", "paragraph_id": "P644", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "FIToFIPaymentReversal with Direct Debit"]}]
participants: ["participant-src-000162-account-owner", "participant-src-000162-account-servicer", "participant-src-000162-clearing-house", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-exchange", "participant-src-000162-financial-institution", "participant-src-000162-intermediary-agent"]
message_mapping_evidence: [{"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["pacs.002", "pacs.007", "pacs.010"]
search_terms: ["FIToFIPaymentReversal with Direct Debit", "Financial Institution", "Debtor agent", "Creditor", "pacs.007", "pacs.010"]
limitations: ["Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.", "P641 duplicate original example; P643 reversal after settlement; P644 positive confirmation. All parties in this FI direct-debit scope are financial institutions; this does not redefine Debtor/Creditor across other flows.", "Source message names establish family-level flow context; supplied exact schema versions are separately identified.", "Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible."]
manual_curated: true
participant_ids: ["participant-src-000162-account-owner", "participant-src-000162-account-servicer", "participant-src-000162-clearing-house", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-exchange", "participant-src-000162-financial-institution", "participant-src-000162-intermediary-agent"]
related_diagrams: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/diagrams/clearing/fig-0048.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and whole Word figure pages compared; source tables retain independent review."}
message_reference_scope: "Part1 name/family flow; no exact version inferred from picture."
---

# FIToFIPaymentReversal with Direct Debit

[src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Purpose, trigger and preconditions

Reverse a paid direct debit that should not have been processed.

Original paid instruction should not have been processed, for example duplicate; reversal is after settlement.

## Participants and responsibilities

| Scoped participant | Evidence role |
| --- | --- |
| [account owner](../../../../../../../shared/reference/participants/participant-src-000162-account-owner.md) | Source narrative/table participant, possibly outside bounded picture. |
| [account servicer](../../../../../../../shared/reference/participants/participant-src-000162-account-servicer.md) | Source narrative/table participant, possibly outside bounded picture. |
| [clearing house](../../../../../../../shared/reference/participants/participant-src-000162-clearing-house.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [creditor agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [debtor](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [debtor agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [exchange](../../../../../../../shared/reference/participants/participant-src-000162-exchange.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [financial institution](../../../../../../../shared/reference/participants/participant-src-000162-financial-institution.md) | Source narrative/table participant, possibly outside bounded picture. |
| [intermediary agent](../../../../../../../shared/reference/participants/participant-src-000162-intermediary-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |


## Source-defined activities and conditions

**P581** A FinancialInstitutionDirectDebit message is the interbank instruction to collect an amount via direct debit from (one or more) party bank account(s) (the Debtor Account(s)) in favour of one or more beneficiary party(ies) (the creditor(s)) where all parties are financial institutions.

**P582** FinancialInstitutionDirectDebits result in cash transfers between Debtor(s) and creditor(s) in the books of the debtor agent or through correspondent banks. 
If there are different transactions, they can be grouped per creditor in a CreditInstruction, but one message can potentially contain multiple credit instructions  for different creditors.

**P583** This is represented in the message by putting the creditor and debtor details on a different level (CreditInstruction block can contain multiple DirectDebitTransactionInformation blocks).  This makes the FinancialInstitutionDirectDebit message different from the other (pacs) messages in this business area, but is necessary to have the equivalent of the MT 204 (allowing for 1 beneficiary institution, but multiple debit institutions).

**P584** The FinancialInstitutionDirectDebit message is sent to the debtor agent. It is used to clear direct debit instructions, initiated by a financial institution creditor.

**P641** After the scenario described in 6.2.6.1, the creditor may realises (for example) that the FinancialInstitutionDirectDebit instruction was a duplicate.

**P643** The creditor can initiate an FIToFIPaymentReversal message, after settlement, when a paid direct debit should not have been processed.

**P644** The debtor agent can confirm the processability of the FIToFIPaymentReversal  by sending a positive FITFIPaymentsStatusReport to the creditor.

### fig-0048

[Source reconstruction and actual review](../diagrams/clearing/fig-0048.md); direct-body paragraph P642; Word page62.

| Step | Sender and depicted roles | Receiver and depicted roles | Literal exchange |
| --- | --- | --- | --- |
| 1 | [Creditor<br/>Exchange or<br/>Clearing House / creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md); [Creditor<br/>Exchange or<br/>Clearing House / exchange](../../../../../../../shared/reference/participants/participant-src-000162-exchange.md); [Creditor<br/>Exchange or<br/>Clearing House / clearing-house](../../../../../../../shared/reference/participants/participant-src-000162-clearing-house.md) | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | FinancialInstitutionDirectDebit |
| 2 | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | [Creditor<br/>Exchange or<br/>Clearing House / creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md); [Creditor<br/>Exchange or<br/>Clearing House / exchange](../../../../../../../shared/reference/participants/participant-src-000162-exchange.md); [Creditor<br/>Exchange or<br/>Clearing House / clearing-house](../../../../../../../shared/reference/participants/participant-src-000162-clearing-house.md) | FIToFIPaymentStatusReport |
| 3 | [Creditor<br/>Exchange or<br/>Clearing House / creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md); [Creditor<br/>Exchange or<br/>Clearing House / exchange](../../../../../../../shared/reference/participants/participant-src-000162-exchange.md); [Creditor<br/>Exchange or<br/>Clearing House / clearing-house](../../../../../../../shared/reference/participants/participant-src-000162-clearing-house.md) | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | FIToFIPaymentReversal |
| 4 | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | [Creditor<br/>Exchange or<br/>Clearing House / creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md); [Creditor<br/>Exchange or<br/>Clearing House / exchange](../../../../../../../shared/reference/participants/participant-src-000162-exchange.md); [Creditor<br/>Exchange or<br/>Clearing House / clearing-house](../../../../../../../shared/reference/participants/participant-src-000162-clearing-house.md) | FIToFIPaymentStatusReport |



## Outcomes, optional paths and source limitations

Source-defined optional acknowledgements, repair/resubmission, account reporting, rejection/return and settlement conditions are retained below. Positive processability status is not by itself settlement.

- Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.
- P641 duplicate original example; P643 reversal after settlement; P644 positive confirmation. All parties in this FI direct-debit scope are financial institutions; this does not redefine Debtor/Creditor across other flows.
- Source message names establish family-level flow context; supplied exact schema versions are separately identified.
- Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible.

| Distinct process | Reference |
| --- | --- |
| Direct-debit return activity | [Direct-debit return activity](flow-src-000162-p157-return-direct-debit.md) |
| Debtor refund activity | [Debtor refund activity](flow-src-000162-p159-request-refund-direct-debit.md) |
| Reversal activity | [Reversal activity](flow-src-000162-p161-direct-debit-reversal.md) |
| PaymentReturn and debtor refund | [PaymentReturn and debtor refund](flow-src-000162-p539-payment-return-initiated-by-debtor-agent.md) |
| Customer direct-debit reversal | [Customer direct-debit reversal](flow-src-000162-p556-fito-fipayment-reversal-with-direct-debit.md) |
| FI direct-debit reversal | [FI direct-debit reversal](flow-src-000162-p640-fito-fipayment-reversal-with-direct-debit.md) |


## Supplied exact message references

| Family | Exact supplied definition | Scope |
| --- | --- | --- |
| pacs.002 | [pacs.002.001.16](../../../../messages/pacs.002.001.16/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pacs.007 | [pacs.007.001.14](../../../../messages/pacs.007.001.14/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pacs.010 | [pacs.010.001.06](../../../../messages/pacs.010.001.06/index.md) | Retrieval name match; schema definition version remains separately scoped. |


## Review

Source text, original image and complete Word-rendered figure context checked on 2026-11-09. No unresolved conflict in this bounded diagram/narrative view. Activity tables and schemas retain their own review status.
