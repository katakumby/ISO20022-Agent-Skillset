---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p292-debtor-agent-sends-fito-fipayment-status-request"
title: "Debtor Agent sends FIToFIPaymentStatusRequest"
source_locations: [{"source_id": "src-000162", "locator": "/w:document/w:body/w:p[170]", "paragraph_id": "P170", "heading_path": ["BusinessTransactions", "Credit Transfer", "FIToFICustomerCreditTransfer"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[171]", "paragraph_id": "P171", "heading_path": ["BusinessTransactions", "Credit Transfer", "FIToFICustomerCreditTransfer"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[172]", "paragraph_id": "P172", "heading_path": ["BusinessTransactions", "Credit Transfer", "FIToFICustomerCreditTransfer"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[173]", "paragraph_id": "P173", "heading_path": ["BusinessTransactions", "Credit Transfer", "FIToFICustomerCreditTransfer"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[174]", "paragraph_id": "P174", "heading_path": ["BusinessTransactions", "Credit Transfer", "FIToFICustomerCreditTransfer"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[175]", "paragraph_id": "P175", "heading_path": ["BusinessTransactions", "Credit Transfer", "FIToFICustomerCreditTransfer"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[176]", "paragraph_id": "P176", "heading_path": ["BusinessTransactions", "Credit Transfer", "FIToFICustomerCreditTransfer"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[292]", "paragraph_id": "P292", "heading_path": ["BusinessTransactions", "Credit Transfer", "Debtor Agent sends FIToFIPaymentStatusRequest "]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[293]", "paragraph_id": "P293", "heading_path": ["BusinessTransactions", "Credit Transfer", "Debtor Agent sends FIToFIPaymentStatusRequest "]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[294]", "paragraph_id": "P294", "heading_path": ["BusinessTransactions", "Credit Transfer", "Debtor Agent sends FIToFIPaymentStatusRequest "]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[295]", "paragraph_id": "P295", "heading_path": ["BusinessTransactions", "Credit Transfer", "Debtor Agent sends FIToFIPaymentStatusRequest "]}]
participants: ["participant-src-000162-account-owner", "participant-src-000162-account-servicer", "participant-src-000162-branch", "participant-src-000162-clearing-agent", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-head-office", "participant-src-000162-intermediary-agent", "participant-src-000162-settlement-agent"]
message_mapping_evidence: [{"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[4]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[5]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["pacs.002", "pacs.008", "pacs.028", "pain.001"]
search_terms: ["Debtor Agent sends FIToFIPaymentStatusRequest", "Debtor agent", "pacs.002", "pacs.008", "pacs.028"]
limitations: ["Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.", "P293: if expected report is not received within scheme timeframe, send status request; response refers to original instruction. P295 permits all prior scenarios when no final status received. Middle actor unused.", "Source message names establish family-level flow context; supplied exact schema versions are separately identified.", "Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible."]
manual_curated: true
participant_ids: ["participant-src-000162-account-owner", "participant-src-000162-account-servicer", "participant-src-000162-branch", "participant-src-000162-clearing-agent", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-head-office", "participant-src-000162-intermediary-agent", "participant-src-000162-settlement-agent"]
related_diagrams: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/diagrams/clearing/fig-0021.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and whole Word figure pages compared; source tables retain independent review."}
message_reference_scope: "Part1 name/family flow; no exact version inferred from picture."
---

# Debtor Agent sends FIToFIPaymentStatusRequest

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

**P171** An FIToFICustomerCreditTransfer message is the inter-bank movement of an amount from a party bank account (the debtor account) to a beneficiary party (the creditor).

**P172** FIToFICustomerCreditTransfer messages result in one or more cash transfers between debtors and creditors through correspondent banks or infrastructures. They may be exchanged as single or grouped instructions following certain common characteristics and, for convenience or efficiency reasons, exchanged in a batch mode. The processing of credit transfers may differ from country to country and system to system.

**P173** Depending on the scenario, there might be an agent between the debtor agent and the creditor agent. This agent can be an intermediary agent or a reimbursement agent. The narrative will describe more in detail the agent role.

**P174** In scenarios where the receiving agent services an account for the sending agent, the scenario also includes the case where the sending agent has an account with a branch/head office of the receiving agent and will indicate that the receiving agent can reimburse itself at this institution. The sending agent has to be aware of an intra-group agreement allowing this.

**P175** A payment clearing and settlement system could occur between debtor agent and creditor agent (or between any other agents). The clearing process where the clearing agent after being informed on the transaction prepares and sends the payment information to the settlement agent (if different) is out of scope and will not be described. This process includes the calculation of the settlement positions and transmission of files to the settlement agent. The settlement agent transfers the funds from the debtor agent to the creditor agent in accordance with the settlement cycle and based on the settlement report provided by the clearing agent.

**P176** Only messages concerning the interbank credit transfer are illustrated in the sequence diagrams. The original contracts between the debtor and the creditor (for example order and invoice) and the CustomerCreditTransferInitiation message by the debtor are out of scope and are therefore not included in the diagram.

**P293** In the previous scenarios, the (optional) possibility of confirming the processability of the FIToFICustomerCreditTransfer via a FIToFIPaymentStatusReport was always mentioned/included. In some schemes, especially referring to real-time payments, the receipt of this FIToFIPaymentStatusReport is crucial within a certain timeframe. In the case the FIToFIPaymentStatusReport is not received within the required timeframe, a reminder shall be launched by sending an FIToFIPaymentStatusRequest. This message requests to receive a FITFIPaymentStatusReport message. The reply message to the FIToFIPaymentStatusRequest shall be a FIToFIPaymentStatusReport referring to the original payment instruction.

**P295** Sending an FIToFIPaymentStatusRequest is possible in all FIToFICustomerCreditTransfer scenarios described before (section 6.1.1, 6.1.2 and 6.1.3), if no 'final' status is received yet in a FIToFIPaymentStatusReport message.

### fig-0021

[Source reconstruction and actual review](../diagrams/clearing/fig-0021.md); direct-body paragraph P294; Word page34.

| Step | Sender and depicted roles | Receiver and depicted roles | Literal exchange |
| --- | --- | --- | --- |
| 1 | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | FIToFICustomerCreditTransfer |
| 2 | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | FIToFIPaymentStatusRequest |
| 3 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | FIToFIPaymentStatusReport |



## Outcomes, optional paths and source limitations

Source-defined optional acknowledgements, repair/resubmission, account reporting, rejection/return and settlement conditions are retained below. Positive processability status is not by itself settlement.

- Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.
- P293: if expected report is not received within scheme timeframe, send status request; response refers to original instruction. P295 permits all prior scenarios when no final status received. Middle actor unused.
- Source message names establish family-level flow context; supplied exact schema versions are separately identified.
- Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible.

## Supplied exact message references

| Family | Exact supplied definition | Scope |
| --- | --- | --- |
| pacs.002 | [pacs.002.001.16](../../../../messages/pacs.002.001.16/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pacs.008 | [pacs.008.001.14](../../../../messages/pacs.008.001.14/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pacs.028 | [pacs.028.001.07](../../../../messages/pacs.028.001.07/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pain.001 | [pain.001.001.13](../../../../messages/pain.001.001.13/index.md) | Retrieval name match; schema definition version remains separately scoped. |


## Review

Source text, original image and complete Word-rendered figure context checked on 2026-11-09. No unresolved conflict in this bounded diagram/narrative view. Activity tables and schemas retain their own review status.
