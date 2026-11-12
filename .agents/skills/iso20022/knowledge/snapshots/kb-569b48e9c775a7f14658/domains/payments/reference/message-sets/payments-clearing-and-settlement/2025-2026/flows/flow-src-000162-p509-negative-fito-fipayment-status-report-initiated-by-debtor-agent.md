---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p509-negative-fito-fipayment-status-report-initiated-by-debtor-agent"
title: "Negative FIToFIPaymentStatusReport Initiated by Debtor Agent"
source_locations: [{"source_id": "src-000162", "locator": "/w:document/w:body/w:p[496]", "paragraph_id": "P496", "heading_path": ["BusinessTransactions", "Direct Debit", "FIToFIPaymentStatusReport with Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[497]", "paragraph_id": "P497", "heading_path": ["BusinessTransactions", "Direct Debit", "FIToFIPaymentStatusReport with Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[498]", "paragraph_id": "P498", "heading_path": ["BusinessTransactions", "Direct Debit", "FIToFIPaymentStatusReport with Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[509]", "paragraph_id": "P509", "heading_path": ["BusinessTransactions", "Direct Debit", "FIToFIPaymentStatusReport with Direct Debit", "Negative FIToFIPaymentStatusReport Initiated by Debtor Agent"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[510]", "paragraph_id": "P510", "heading_path": ["BusinessTransactions", "Direct Debit", "FIToFIPaymentStatusReport with Direct Debit", "Negative FIToFIPaymentStatusReport Initiated by Debtor Agent"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[511]", "paragraph_id": "P511", "heading_path": ["BusinessTransactions", "Direct Debit", "FIToFIPaymentStatusReport with Direct Debit", "Negative FIToFIPaymentStatusReport Initiated by Debtor Agent"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[512]", "paragraph_id": "P512", "heading_path": ["BusinessTransactions", "Direct Debit", "FIToFIPaymentStatusReport with Direct Debit", "Negative FIToFIPaymentStatusReport Initiated by Debtor Agent"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[513]", "paragraph_id": "P513", "heading_path": ["BusinessTransactions", "Direct Debit", "FIToFIPaymentStatusReport with Direct Debit", "Negative FIToFIPaymentStatusReport Initiated by Debtor Agent"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[514]", "paragraph_id": "P514", "heading_path": ["BusinessTransactions", "Direct Debit", "FIToFIPaymentStatusReport with Direct Debit", "Negative FIToFIPaymentStatusReport Initiated by Debtor Agent"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[515]", "paragraph_id": "P515", "heading_path": ["BusinessTransactions", "Direct Debit", "FIToFIPaymentStatusReport with Direct Debit", "Negative FIToFIPaymentStatusReport Initiated by Debtor Agent"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[516]", "paragraph_id": "P516", "heading_path": ["BusinessTransactions", "Direct Debit", "FIToFIPaymentStatusReport with Direct Debit", "Negative FIToFIPaymentStatusReport Initiated by Debtor Agent"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[517]", "paragraph_id": "P517", "heading_path": ["BusinessTransactions", "Direct Debit", "FIToFIPaymentStatusReport with Direct Debit", "Negative FIToFIPaymentStatusReport Initiated by Debtor Agent"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[518]", "paragraph_id": "P518", "heading_path": ["BusinessTransactions", "Direct Debit", "FIToFIPaymentStatusReport with Direct Debit", "Negative FIToFIPaymentStatusReport Initiated by Debtor Agent"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[519]", "paragraph_id": "P519", "heading_path": ["BusinessTransactions", "Direct Debit", "FIToFIPaymentStatusReport with Direct Debit", "Negative FIToFIPaymentStatusReport Initiated by Debtor Agent"]}]
participants: ["participant-src-000162-clearing-and-settlement-agent", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-initiating-party"]
message_mapping_evidence: [{"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[4]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["camt.052", "camt.053", "camt.054", "pacs.002", "pacs.003", "pacs.004", "pain.002", "pain.008"]
search_terms: ["Negative FIToFIPaymentStatusReport Initiated by Debtor Agent", "Settlement Agent", "Creditor Agent", "Debtor agent", "Creditor", "pacs.002", "pacs.003", "pacs.004"]
limitations: ["Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.", "P519 debtor-agent status is negative before settlement; prior positive statuses do not imply final outcome. P513 asterisk depends on creditor booking; P511 permits repair and optional customer update.", "Source message names establish family-level flow context; supplied exact schema versions are separately identified.", "Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible."]
manual_curated: true
participant_ids: ["participant-src-000162-clearing-and-settlement-agent", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-initiating-party"]
related_diagrams: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/diagrams/clearing/fig-0039.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and whole Word figure pages compared; source tables retain independent review."}
message_reference_scope: "Part1 name/family flow; no exact version inferred from picture."
---

# Negative FIToFIPaymentStatusReport Initiated by Debtor Agent

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Purpose, trigger and preconditions

Reject an interbank direct-debit instruction before settlement.

The cited source paragraphs define the account relationship, processing/settlement state and initiation event; no additional scheme precondition is inferred.

## Participants and responsibilities

| Scoped participant | Evidence role |
| --- | --- |
| [clearing and settlement agent](../../../../../../../shared/reference/participants/participant-src-000162-clearing-and-settlement-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [creditor agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [debtor](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [debtor agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | Figure occurrence: see literal sender/receiver or activity steps. |
| [initiating party](../../../../../../../shared/reference/participants/participant-src-000162-initiating-party.md) | Figure occurrence: see literal sender/receiver or activity steps. |


## Source-defined activities and conditions

**P497** The negative FIToFIPaymentStatusReport message is sent by the receiver of an instruction to inform the sender of the instruction about the negative processability of the instruction.

**P498** The negative FIToFIPaymentStatusReport message is to be sent before settlement. Indeed, after settlement, the correct message to be used is the PaymentReturn message.

**P510** A negative FIToFIPaymentStatusReport message is initiated by the debtor agent to reject the FIToFICustomerDirectDebit message. (After settlement the correct message to be used by the debtor agent is the PaymentReturn message.

**P511** Whenever possible the creditor agent will correct/complement the instruction and re-submit. Consequently he would not send a negative CustomerPaymentStatusReport to the creditor. However, depending on what has been agreed between the creditor and its agent, the creditor agent may inform its customer about the repair, for example, value date.

**P513** * Information: If the creditor agent books after collection, for example, the cycle is 3 days, then the CustomerPaymentStatusReport message is to be used. If the creditor agent books immediately and the instruction is rejected in the interbank leg, then the creditor needs to be informed of a payment return.

**P514** The creditor sends a CustomerDirectDebitInitiation message to its agent (the creditor agent).

**P515** The creditor agent confirms the processability of the CustomerDirectDebitInitiation instruction by sending a CustomerPaymentStatusReport message to the creditor.

**P516** The creditor agent sends an FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

**P517** The clearing and settlement agent confirms the processability of the FIToFICustomerDirectDebit instruction by sending an FIToFIPaymentStatusReport message to the creditor agent.

**P518** The clearing and settlement agent sends an FIToFICustomerDirectDebit message, optionally with  the Mandate Related Reference (MRI) to the debtor agent immediately for information purposes only.

**P519** If settlement has not yet taken place, the debtor agent may send a negative FIToFIPaymentStatusReport message to the clearing and settlement agent, to inform it about the rejection of the FIToFICustomerDirectDebit instruction. This negative FIToFIPaymentStatusReport message may subsequently be forwarded to the creditor agent. The creditor agent may inform its customer, the creditor, about the negative processing of the CustomerDirectDebitInitiation instruction by using a CustomerPaymentStatusReport message, a BankToCustomerDebitCreditNotification message ('notification') or through a BankToCustomerAccountReport/ BankToCustomerStatement message ('statement').

### fig-0039

[Source reconstruction and actual review](../diagrams/clearing/fig-0039.md); direct-body paragraph P512; Word page51.

| Step | Sender and depicted roles | Receiver and depicted roles | Literal exchange |
| --- | --- | --- | --- |
| 1 | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md); [Creditor / initiating-party](../../../../../../../shared/reference/participants/participant-src-000162-initiating-party.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | CustomerDirectDebitInitiation |
| 2 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md); [Creditor / initiating-party](../../../../../../../shared/reference/participants/participant-src-000162-initiating-party.md) | CustomerPaymentStatusReport |
| 3 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000162-clearing-and-settlement-agent.md) | FIToFICustomerDirectDebit |
| 4 | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000162-clearing-and-settlement-agent.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | FIToFIPaymentStatusReport |
| 5 | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000162-clearing-and-settlement-agent.md) | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | FIToFICustomerDirectDebit |
| 6 | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000162-clearing-and-settlement-agent.md) | FIToFIPaymentStatusReport |
| 7 | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000162-clearing-and-settlement-agent.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | FIToFIPaymentStatusReport |
| 8 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md); [Creditor / initiating-party](../../../../../../../shared/reference/participants/participant-src-000162-initiating-party.md) | Information* |



## Outcomes, optional paths and source limitations

Source-defined optional acknowledgements, repair/resubmission, account reporting, rejection/return and settlement conditions are retained below. Positive processability status is not by itself settlement.

- Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.
- P519 debtor-agent status is negative before settlement; prior positive statuses do not imply final outcome. P513 asterisk depends on creditor booking; P511 permits repair and optional customer update.
- Source message names establish family-level flow context; supplied exact schema versions are separately identified.
- Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible.

## Supplied exact message references

| Family | Exact supplied definition | Scope |
| --- | --- | --- |
| camt.052 | [camt.052.001.14](../../../../messages/camt.052.001.14/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| camt.053 | [camt.053.001.14](../../../../messages/camt.053.001.14/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| camt.054 | [camt.054.001.14](../../../../messages/camt.054.001.14/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pacs.002 | [pacs.002.001.16](../../../../messages/pacs.002.001.16/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pacs.003 | [pacs.003.001.12](../../../../messages/pacs.003.001.12/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pacs.004 | [pacs.004.001.15](../../../../messages/pacs.004.001.15/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pain.002 | [pain.002.001.15](../../../../messages/pain.002.001.15/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pain.008 | [pain.008.001.12](../../../../messages/pain.008.001.12/index.md) | Retrieval name match; schema definition version remains separately scoped. |


## Review

Source text, original image and complete Word-rendered figure context checked on 2026-11-09. No unresolved conflict in this bounded diagram/narrative view. Activity tables and schemas retain their own review status.
