---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p303-debtor-and-creditor-are-correspondents"
title: "Debtor and Creditor are Correspondents"
source_locations: [{"source_id": "src-000162", "locator": "/w:document/w:body/w:p[296]", "paragraph_id": "P296", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer "]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[297]", "paragraph_id": "P297", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer "]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[298]", "paragraph_id": "P298", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer "]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[299]", "paragraph_id": "P299", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer "]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[300]", "paragraph_id": "P300", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer "]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[301]", "paragraph_id": "P301", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer "]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[302]", "paragraph_id": "P302", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer "]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[303]", "paragraph_id": "P303", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer ", "Debtor and Creditor are Correspondents"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[304]", "paragraph_id": "P304", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer ", "Debtor and Creditor are Correspondents"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[305]", "paragraph_id": "P305", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer ", "Debtor and Creditor are Correspondents"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[306]", "paragraph_id": "P306", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer ", "Debtor and Creditor are Correspondents"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[307]", "paragraph_id": "P307", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer ", "Debtor and Creditor are Correspondents"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[308]", "paragraph_id": "P308", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer ", "Debtor and Creditor are Correspondents"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[309]", "paragraph_id": "P309", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer ", "Debtor and Creditor are Correspondents"]}]
participants: ["participant-src-000162-account-owner", "participant-src-000162-account-servicer", "participant-src-000162-branch", "participant-src-000162-clearing-agent", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-head-office", "participant-src-000162-intermediary-agent", "participant-src-000162-settlement-agent"]
message_mapping_evidence: [{"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[4]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["camt.052", "camt.053", "camt.054", "pacs.002", "pacs.009"]
search_terms: ["Debtor and Creditor are Correspondents", "Financial Institution", "Debtor agent", "Creditor", "Debtor", "pacs.002", "pacs.009"]
limitations: ["Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.", "P305 creditor services debtor account (thus acts as debtor agent). P309 reverse account service uses account reporting instead of transfer. P306 positive status optional.", "Source message names establish family-level flow context; supplied exact schema versions are separately identified.", "Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible."]
manual_curated: true
participant_ids: ["participant-src-000162-account-owner", "participant-src-000162-account-servicer", "participant-src-000162-branch", "participant-src-000162-clearing-agent", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-head-office", "participant-src-000162-intermediary-agent", "participant-src-000162-settlement-agent"]
related_diagrams: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/diagrams/clearing/fig-0022.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and whole Word figure pages compared; source tables retain independent review."}
message_reference_scope: "Part1 name/family flow; no exact version inferred from picture."
---

# Debtor and Creditor are Correspondents

[src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Purpose, trigger and preconditions

Execute a financial-institution credit transfer with contextual correspondent account relationships.

The cited source paragraphs define the account relationship, processing/settlement state and initiation event; no additional scheme precondition is inferred.

## Participants and responsibilities

| Scoped participant | Evidence role |
| --- | --- |
| [account owner](../../../../../../../shared/reference/participants/participant-src-000162-account-owner.md) | Source narrative/table participant, possibly outside bounded picture. |
| [account servicer](../../../../../../../shared/reference/participants/participant-src-000162-account-servicer.md) | Source narrative/table participant, possibly outside bounded picture. |
| [branch](../../../../../../../shared/reference/participants/participant-src-000162-branch.md) | Source narrative/table participant, possibly outside bounded picture. |
| [clearing agent](../../../../../../../shared/reference/participants/participant-src-000162-clearing-agent.md) | Source narrative/table participant, possibly outside bounded picture. |
| [creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [creditor agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [debtor](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [debtor agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [head office](../../../../../../../shared/reference/participants/participant-src-000162-head-office.md) | Source narrative/table participant, possibly outside bounded picture. |
| [intermediary agent](../../../../../../../shared/reference/participants/participant-src-000162-intermediary-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [settlement agent](../../../../../../../shared/reference/participants/participant-src-000162-settlement-agent.md) | Source narrative/table participant, possibly outside bounded picture. |


## Source-defined activities and conditions

**P297** A FinancialInstitutionCreditTransfer message is the inter-bank movement of an amount from a party bank account (the debtor) to a beneficiary party (the creditor) where all parties are financial institutions.

**P298** FinancialInstitutionCreditTransfer messages result in cash transfers between debtors and creditors through correspondent banks or infrastructures. They may be exchanged as single instructions or grouped following certain common characteristics and, for convenience or efficiency reasons, exchanged in a batch mode. The processing of credit transfers may differ from country to country and system to system.

**P299** Depending on the scenario, there might be an agent between the debtor agent and the creditor agent. This agent can be an intermediary agent or a reimbursement agent. The narrative will describe more in detail the agent role.

**P300** In scenarios where the receiving agent services an account for the sending agent, the scenario also includes the case where the sending agent has an account with a branch/head office of the receiving agent and will indicate that the receiving agent can reimburse itself at this institution. The sending agent has to be aware of an intra-group agreement allowing this.

**P301** A payment clearing and settlement system could occur between debtor agent and creditor agent (or between any other agents). The clearing process where the clearing agent after being informed on the transaction prepares and sends the payment information to the settlement agent (if different) is out of scope and will not be described. This process includes the calculation of the settlement positions and transmission of files to the settlement agent. The settlement agent transfers the funds from the debtor agent to the creditor agent in accordance with the settlement cycle and based on the settlement report provided by the clearing agent.

**P302** Only the messages in the scope of interbank credit transfer are illustrated in the BusinessTransactions (sequence diagrams). The original contracts between the debtor and the creditor, for example, forex, inter-bank loans, and securities transactions, are out of scope and are not included in the diagrams.

**P305** The scenario covers the case where the creditor services an account for the debtor, that is, the debtor agent. In scope: the debtor sends the FinancialInstitutionCreditTransfer message to the creditor.

**P306** The creditor optionally confirms the processability of the FinancialInstitutionCreditTransfer by sending a positive FIToFIPaymentStatusReport message to the debtor.

**P307** Out of Scope

**P308** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages).

**P309** If the debtor services an account for the creditor, that is, the creditor agent, then instead of sending a FinancialInstitutionCreditTransfer message, the debtor will send a BankToCustomerDebitCreditNotification message ('notification') and/or BankToCustomerAccountReport/BankToCustomerStatement message ('statement').

### fig-0022

[Source reconstruction and actual review](../diagrams/clearing/fig-0022.md); direct-body paragraph P304; Word page35.

| Step | Sender and depicted roles | Receiver and depicted roles | Literal exchange |
| --- | --- | --- | --- |
| 1 | [Debtor / debtor](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md) | FinancialInstitutionCreditTransfer |
| 2 | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md) | [Debtor / debtor](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | FIToFIPaymentStatusReport |



## Outcomes, optional paths and source limitations

Source-defined optional acknowledgements, repair/resubmission, account reporting, rejection/return and settlement conditions are retained below. Positive processability status is not by itself settlement.

- Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.
- P305 creditor services debtor account (thus acts as debtor agent). P309 reverse account service uses account reporting instead of transfer. P306 positive status optional.
- Source message names establish family-level flow context; supplied exact schema versions are separately identified.
- Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible.

## Supplied exact message references

| Family | Exact supplied definition | Scope |
| --- | --- | --- |
| camt.052 | [camt.052.001.14](../../../../messages/camt.052.001.14/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| camt.053 | [camt.053.001.14](../../../../messages/camt.053.001.14/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| camt.054 | [camt.054.001.14](../../../../messages/camt.054.001.14/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pacs.002 | [pacs.002.001.16](../../../../messages/pacs.002.001.16/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pacs.009 | [pacs.009.001.13](../../../../messages/pacs.009.001.13/index.md) | Retrieval name match; schema definition version remains separately scoped. |


## Review

Source text, original image and complete Word-rendered figure context checked on 2026-11-09. No unresolved conflict in this bounded diagram/narrative view. Activity tables and schemas retain their own review status.
