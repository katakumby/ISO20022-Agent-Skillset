---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p645-creditor-sends-fito-fipayment-status-request"
title: "Creditor sends FIToFIPaymentStatusRequest"
source_locations: [{"source_id": "src-000162", "locator": "/w:document/w:body/w:p[580]", "paragraph_id": "P580", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[581]", "paragraph_id": "P581", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[582]", "paragraph_id": "P582", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[583]", "paragraph_id": "P583", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[584]", "paragraph_id": "P584", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[645]", "paragraph_id": "P645", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor sends FIToFIPaymentStatusRequest"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[646]", "paragraph_id": "P646", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor sends FIToFIPaymentStatusRequest"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[647]", "paragraph_id": "P647", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor sends FIToFIPaymentStatusRequest"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[648]", "paragraph_id": "P648", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor sends FIToFIPaymentStatusRequest"]}]
participants: ["participant-src-000162-account-owner", "participant-src-000162-account-servicer", "participant-src-000162-clearing-and-settlement-agent", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-financial-institution"]
message_mapping_evidence: [{"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[4]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[5]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["pacs.002", "pacs.009", "pacs.010", "pacs.028"]
search_terms: ["Creditor sends FIToFIPaymentStatusRequest", "Financial Institution", "Creditor", "pacs.002", "pacs.009", "pacs.010", "pacs.028"]
limitations: ["Literal middle lifeline is Clearing and Settlement Agent, unlike intermediary in figures44–48, and remains unused. P646 requires status response but no reply arrow drawn. P648 names FinancialInstitutionCreditTransfer and repeats section6.2.7.2 despite FI direct-debit context (issue-000054).", "Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.", "Source message names establish family-level flow context; supplied exact schema versions are separately identified.", "Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible."]
manual_curated: true
participant_ids: ["participant-src-000162-account-owner", "participant-src-000162-account-servicer", "participant-src-000162-clearing-and-settlement-agent", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-financial-institution"]
related_diagrams: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/diagrams/clearing/fig-0049.md"]
issue_ids: ["issue-000054"]
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and whole Word figure pages compared; source tables retain independent review."}
message_reference_scope: "Part1 name/family flow; no exact version inferred from picture."
---

# Creditor sends FIToFIPaymentStatusRequest

[src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Purpose, trigger and preconditions

Request a missing processability status for the original payment.

Expected status has not arrived within required scheme timeframe, with no final status yet.

## Participants and responsibilities

| Scoped participant | Evidence role |
| --- | --- |
| [account owner](../../../../../../../shared/reference/participants/participant-src-000162-account-owner.md) | Source narrative/table participant, possibly outside bounded picture. |
| [account servicer](../../../../../../../shared/reference/participants/participant-src-000162-account-servicer.md) | Source narrative/table participant, possibly outside bounded picture. |
| [clearing and settlement agent](../../../../../../../shared/reference/participants/participant-src-000162-clearing-and-settlement-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [creditor agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [debtor](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [debtor agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [financial institution](../../../../../../../shared/reference/participants/participant-src-000162-financial-institution.md) | Source narrative/table participant, possibly outside bounded picture. |


## Source-defined activities and conditions

**P581** A FinancialInstitutionDirectDebit message is the interbank instruction to collect an amount via direct debit from (one or more) party bank account(s) (the Debtor Account(s)) in favour of one or more beneficiary party(ies) (the creditor(s)) where all parties are financial institutions.

**P582** FinancialInstitutionDirectDebits result in cash transfers between Debtor(s) and creditor(s) in the books of the debtor agent or through correspondent banks. 
If there are different transactions, they can be grouped per creditor in a CreditInstruction, but one message can potentially contain multiple credit instructions  for different creditors.

**P583** This is represented in the message by putting the creditor and debtor details on a different level (CreditInstruction block can contain multiple DirectDebitTransactionInformation blocks).  This makes the FinancialInstitutionDirectDebit message different from the other (pacs) messages in this business area, but is necessary to have the equivalent of the MT 204 (allowing for 1 beneficiary institution, but multiple debit institutions).

**P584** The FinancialInstitutionDirectDebit message is sent to the debtor agent. It is used to clear direct debit instructions, initiated by a financial institution creditor.

**P646** In the previous scenarios, the (optional) possibility of confirming the processability of the FinancialInstitutionDirectDebit via a FIToFIPaymentStatusReport was always mentioned/included. In some payment schemes, especially referring to real-time payments, the receipt of this FIToFIPaymentStatusReport is crucial within a certain timeframe. In this case, if the FIToFIPaymentStatusReport is not received within the required timeframe, a reminder shall be launched by sending an FIToFIPaymentStatusRequest. The reply message to the FIToFIPaymentStatusRequest shall be a FIToFIPaymentStatusReport referring to the original payment instruction.

**P648** Sending an FIToFIPaymentStatusRequest is possible in all FinancialInstitutionCreditTransfer scenarios described before (section 6.2.7.2, 6.2.7.2, 6.2.7.3, 6.2.7.4), if no 'final' status is received yet in a FIToFIPaymentStatusReport message.

### fig-0049

[Source reconstruction and actual review](../diagrams/clearing/fig-0049.md); direct-body paragraph P647; Word page63.

| Step | Sender and depicted roles | Receiver and depicted roles | Literal exchange |
| --- | --- | --- | --- |
| 1 | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md) | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | FinancialInstitutionDirectDebit |
| 2 | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md) | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | FIToFIPaymentStatusRequest |



### Narrative-only message path

[debtor-agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) → [creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md): FIToFIPaymentStatusReport (P646). Reply to the request, referring to original instruction; intentionally absent from drawn response arrows.

## Outcomes, optional paths and source limitations

Source-defined optional acknowledgements, repair/resubmission, account reporting, rejection/return and settlement conditions are retained below. Positive processability status is not by itself settlement.

- Literal middle lifeline is Clearing and Settlement Agent, unlike intermediary in figures44–48, and remains unused. P646 requires status response but no reply arrow drawn. P648 names FinancialInstitutionCreditTransfer and repeats section6.2.7.2 despite FI direct-debit context (issue-000054).
- Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.
- Source message names establish family-level flow context; supplied exact schema versions are separately identified.
- Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible.

## Supplied exact message references

| Family | Exact supplied definition | Scope |
| --- | --- | --- |
| pacs.002 | [pacs.002.001.16](../../../../messages/pacs.002.001.16/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pacs.009 | [pacs.009.001.13](../../../../messages/pacs.009.001.13/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pacs.010 | [pacs.010.001.06](../../../../messages/pacs.010.001.06/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pacs.028 | [pacs.028.001.07](../../../../messages/pacs.028.001.07/index.md) | Retrieval name match; schema definition version remains separately scoped. |


## Review

Source text, original image and complete Word-rendered figure context checked on 2026-11-09. Source issues: issue-000054. Activity tables and schemas retain their own review status.
