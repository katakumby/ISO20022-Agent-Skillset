---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p463-debtor-sends-fito-fipayment-status-request"
title: "Debtor sends FIToFIPaymentStatusRequest"
source_locations: [{"source_id": "src-000162", "locator": "/w:document/w:body/w:p[296]", "paragraph_id": "P296", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer "]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[297]", "paragraph_id": "P297", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer "]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[298]", "paragraph_id": "P298", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer "]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[299]", "paragraph_id": "P299", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer "]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[300]", "paragraph_id": "P300", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer "]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[301]", "paragraph_id": "P301", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer "]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[302]", "paragraph_id": "P302", "heading_path": ["BusinessTransactions", "Credit Transfer", "FinancialInstitutionCreditTransfer "]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[463]", "paragraph_id": "P463", "heading_path": ["BusinessTransactions", "Credit Transfer", "Debtor sends FIToFIPaymentStatusRequest"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[464]", "paragraph_id": "P464", "heading_path": ["BusinessTransactions", "Credit Transfer", "Debtor sends FIToFIPaymentStatusRequest"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[465]", "paragraph_id": "P465", "heading_path": ["BusinessTransactions", "Credit Transfer", "Debtor sends FIToFIPaymentStatusRequest"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[466]", "paragraph_id": "P466", "heading_path": ["BusinessTransactions", "Credit Transfer", "Debtor sends FIToFIPaymentStatusRequest"]}]
participants: ["participant-src-000162-account-owner", "participant-src-000162-account-servicer", "participant-src-000162-branch", "participant-src-000162-clearing-agent", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-head-office", "participant-src-000162-intermediary-agent", "participant-src-000162-settlement-agent"]
message_mapping_evidence: [{"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[4]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[5]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["pacs.002", "pacs.009", "pacs.028"]
search_terms: ["Debtor sends FIToFIPaymentStatusRequest", "Financial Institution", "Debtor", "pacs.002", "pacs.009", "pacs.028"]
limitations: ["Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.", "P464 reminder when expected status absent in required scheme timeframe; reply refers to original instruction. P465 applies to all preceding FI transfer scenarios lacking final status.", "Source message names establish family-level flow context; supplied exact schema versions are separately identified.", "Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible."]
manual_curated: true
participant_ids: ["participant-src-000162-account-owner", "participant-src-000162-account-servicer", "participant-src-000162-branch", "participant-src-000162-clearing-agent", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-head-office", "participant-src-000162-intermediary-agent", "participant-src-000162-settlement-agent"]
related_diagrams: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/diagrams/clearing/fig-0036.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and whole Word figure pages compared; source tables retain independent review."}
message_reference_scope: "Part1 name/family flow; no exact version inferred from picture."
---

# Debtor sends FIToFIPaymentStatusRequest

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Purpose, trigger and preconditions

Request a missing processability status for the original payment.

Expected status has not arrived within required scheme timeframe, with no final status yet.

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

**P464** In the previous scenarios, the (optional) possibility of confirming the processability of the FinancialInstitutionCreditTransfer via a FIToFIPaymentStatusReport was always mentioned/included. In some schemes, especially referring to real-time payments, the receipt of this FIToFIPaymentStatusReport is crucial within a certain timeframe. In this case, if the FIToFIPaymentStatusReport is not received within the required timeframe, a reminder shall be launched by sending an FIToFIPaymentStatusRequest. The reply message to the FIToFIPaymentStatusRequest shall be a FIToFIPaymentStatusReport referring to the original payment instruction.

**P465** Sending an FIToFIPaymentStatusRequest is possible in all FinancialInstitutionCreditTransfer scenarios described before (section 6.1.5, 6.1.6, 6.1.7), if no 'final' status is received yet in a FIToFIPaymentStatusReport message.

### fig-0036

[Source reconstruction and actual review](../diagrams/clearing/fig-0036.md); direct-body paragraph P464; Word page47.

| Step | Sender and depicted roles | Receiver and depicted roles | Literal exchange |
| --- | --- | --- | --- |
| 1 | [Debtor / debtor](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md) | FinancialInstitutionCreditTransfer |
| 2 | [Debtor / debtor](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md) | FIToFIPaymentStatusRequest |
| 3 | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md) | [Debtor / debtor](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | FIToFIPaymentStatusReport |



## Outcomes, optional paths and source limitations

Source-defined optional acknowledgements, repair/resubmission, account reporting, rejection/return and settlement conditions are retained below. Positive processability status is not by itself settlement.

- Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.
- P464 reminder when expected status absent in required scheme timeframe; reply refers to original instruction. P465 applies to all preceding FI transfer scenarios lacking final status.
- Source message names establish family-level flow context; supplied exact schema versions are separately identified.
- Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible.

## Supplied exact message references

| Family | Exact supplied definition | Scope |
| --- | --- | --- |
| pacs.002 | [pacs.002.001.16](../../../../messages/pacs.002.001.16/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pacs.009 | [pacs.009.001.13](../../../../messages/pacs.009.001.13/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pacs.028 | [pacs.028.001.07](../../../../messages/pacs.028.001.07/index.md) | Retrieval name match; schema definition version remains separately scoped. |


## Review

Source text, original image and complete Word-rendered figure context checked on 2026-11-09. No unresolved conflict in this bounded diagram/narrative view. Activity tables and schemas retain their own review status.
