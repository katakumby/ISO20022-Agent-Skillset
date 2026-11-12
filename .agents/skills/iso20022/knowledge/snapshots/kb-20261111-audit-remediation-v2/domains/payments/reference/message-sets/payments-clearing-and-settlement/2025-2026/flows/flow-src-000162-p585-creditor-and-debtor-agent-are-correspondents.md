---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p585-creditor-and-debtor-agent-are-correspondents"
title: "Creditor and Debtor Agent are correspondents"
source_locations: [{"source_id": "src-000162", "locator": "/w:document/w:body/w:p[580]", "paragraph_id": "P580", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[581]", "paragraph_id": "P581", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[582]", "paragraph_id": "P582", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[583]", "paragraph_id": "P583", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[584]", "paragraph_id": "P584", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[585]", "paragraph_id": "P585", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor and Debtor Agent are correspondents"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[586]", "paragraph_id": "P586", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor and Debtor Agent are correspondents"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[587]", "paragraph_id": "P587", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor and Debtor Agent are correspondents"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[588]", "paragraph_id": "P588", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor and Debtor Agent are correspondents"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[589]", "paragraph_id": "P589", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor and Debtor Agent are correspondents"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[590]", "paragraph_id": "P590", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor and Debtor Agent are correspondents"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[591]", "paragraph_id": "P591", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor and Debtor Agent are correspondents"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[592]", "paragraph_id": "P592", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor and Debtor Agent are correspondents"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[593]", "paragraph_id": "P593", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor and Debtor Agent are correspondents"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[594]", "paragraph_id": "P594", "heading_path": ["BusinessTransactions", "Direct Debit", "FinancialInstitutionDirectDebit", "Creditor and Debtor Agent are correspondents"]}]
participants: ["participant-src-000162-account-owner", "participant-src-000162-account-servicer", "participant-src-000162-clearing-house", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-exchange", "participant-src-000162-financial-institution", "participant-src-000162-intermediary-agent"]
message_mapping_evidence: [{"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[4]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["camt.052", "camt.053", "camt.054", "pacs.002", "pacs.010"]
search_terms: ["Creditor and Debtor Agent are correspondents", "Financial Institution", "Debtor agent", "Creditor", "Debtor", "pacs.002", "pacs.010"]
limitations: ["Creditor picture label includes Exchange or Clearing House as examples, not universal aliases. P586 debtor agent services creditor and debtor accounts; one debtor shown for simplicity. P594 unprocessable instruction is rejected before settlement; mandates/reporting not drawn.", "Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.", "Source message names establish family-level flow context; supplied exact schema versions are separately identified.", "Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible."]
manual_curated: true
participant_ids: ["participant-src-000162-account-owner", "participant-src-000162-account-servicer", "participant-src-000162-clearing-house", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-exchange", "participant-src-000162-financial-institution", "participant-src-000162-intermediary-agent"]
related_diagrams: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/diagrams/clearing/fig-0044.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and whole Word figure pages compared; source tables retain independent review."}
message_reference_scope: "Part1 name/family flow; no exact version inferred from picture."
---

# Creditor and Debtor Agent are correspondents

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Purpose, trigger and preconditions

Collect a financial-institution direct debit and route funds to creditor account.

The cited source paragraphs define the account relationship, processing/settlement state and initiation event; no additional scheme precondition is inferred.

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

**P586** The scenario covers the case where the debtor agent services an account for the creditor and for the debtor(s).  For sake of simplicity, only 1 Debtor is represented in the sequence diagram.

**P588** The creditor sends the FinancialInstitutionDirectDebit message to the debtor agent. Creditor and debtor agent are correspondents in the currency of the transaction and by sending the message the creditor requests to credit the amount on his account with the debtor agent

**P589** The debtor agent (optionally) confirms the processability of the FinancialInstitutionDirectDebit by sending a positive FIToFIPaymentStatusReport.

**P590** Out of Scope

**P591** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages).

**P592** Some debtor agents potentially send the instruction to the debtor(s) for information (and value added) services. (Pre)Notifications are not included.

**P593** The mandate/agreements related to the direct debit flows are not taken into account for the purpose of this document.

**P594** If the FinancialInstitutionDirectDebit cannot be processed by the debtor agent, a negative FIToFIPaymentsStatusReport message is sent back to the creditor before settlement.

### fig-0044

[Source reconstruction and actual review](../diagrams/clearing/fig-0044.md); direct-body paragraph P587; Word page58.

| Step | Sender and depicted roles | Receiver and depicted roles | Literal exchange |
| --- | --- | --- | --- |
| 1 | [Creditor<br/>Exchange or<br/>Clearing House / creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md); [Creditor<br/>Exchange or<br/>Clearing House / exchange](../../../../../../../shared/reference/participants/participant-src-000162-exchange.md); [Creditor<br/>Exchange or<br/>Clearing House / clearing-house](../../../../../../../shared/reference/participants/participant-src-000162-clearing-house.md) | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | FinancialInstitutionDirectDebit |
| 2 | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | [Creditor<br/>Exchange or<br/>Clearing House / creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md); [Creditor<br/>Exchange or<br/>Clearing House / exchange](../../../../../../../shared/reference/participants/participant-src-000162-exchange.md); [Creditor<br/>Exchange or<br/>Clearing House / clearing-house](../../../../../../../shared/reference/participants/participant-src-000162-clearing-house.md) | FIToFIPaymentStatusReport |



## Outcomes, optional paths and source limitations

Source-defined optional acknowledgements, repair/resubmission, account reporting, rejection/return and settlement conditions are retained below. Positive processability status is not by itself settlement.

- Creditor picture label includes Exchange or Clearing House as examples, not universal aliases. P586 debtor agent services creditor and debtor accounts; one debtor shown for simplicity. P594 unprocessable instruction is rejected before settlement; mandates/reporting not drawn.
- Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.
- Source message names establish family-level flow context; supplied exact schema versions are separately identified.
- Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible.

## Supplied exact message references

| Family | Exact supplied definition | Scope |
| --- | --- | --- |
| camt.052 | [camt.052.001.14](../../../../messages/camt.052.001.14/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| camt.053 | [camt.053.001.14](../../../../messages/camt.053.001.14/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| camt.054 | [camt.054.001.14](../../../../messages/camt.054.001.14/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pacs.002 | [pacs.002.001.16](../../../../messages/pacs.002.001.16/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pacs.010 | [pacs.010.001.06](../../../../messages/pacs.010.001.06/index.md) | Retrieval name match; schema definition version remains separately scoped. |


## Review

Source text, original image and complete Word-rendered figure context checked on 2026-11-09. No unresolved conflict in this bounded diagram/narrative view. Activity tables and schemas retain their own review status.
