---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p529-fito-fipayment-status-report-to-confirm-processability-of-fito-ficusto"
title: "FIToFIPaymentStatusReport to confirm Processability of FIToFICustomerDirectDebit instruction"
source_locations: [{"source_id": "src-000162", "locator": "/w:document/w:body/w:p[520]", "paragraph_id": "P520", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[521]", "paragraph_id": "P521", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[522]", "paragraph_id": "P522", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[523]", "paragraph_id": "P523", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[524]", "paragraph_id": "P524", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[525]", "paragraph_id": "P525", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[526]", "paragraph_id": "P526", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[527]", "paragraph_id": "P527", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[528]", "paragraph_id": "P528", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[529]", "paragraph_id": "P529", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit", "FIToFIPaymentStatusReport to confirm Processability of FIToFICustomerDirectDebit instruction"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[530]", "paragraph_id": "P530", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit", "FIToFIPaymentStatusReport to confirm Processability of FIToFICustomerDirectDebit instruction"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[531]", "paragraph_id": "P531", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit", "FIToFIPaymentStatusReport to confirm Processability of FIToFICustomerDirectDebit instruction"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[532]", "paragraph_id": "P532", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit", "FIToFIPaymentStatusReport to confirm Processability of FIToFICustomerDirectDebit instruction"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[533]", "paragraph_id": "P533", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit", "FIToFIPaymentStatusReport to confirm Processability of FIToFICustomerDirectDebit instruction"]}, {"source_id": "src-000162", "locator": "/w:document/w:body/w:p[534]", "paragraph_id": "P534", "heading_path": ["BusinessTransactions", "Direct Debit", "Positive FI To FI Payment Status Report with Direct Debit", "FIToFIPaymentStatusReport to confirm Processability of FIToFICustomerDirectDebit instruction"]}]
participants: ["participant-src-000162-clearing-and-settlement-agent", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-initiating-party"]
message_mapping_evidence: [{"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[4]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["camt.052", "camt.053", "camt.054", "pacs.002", "pacs.003", "pacs.004", "pacs.007", "pain.002", "pain.008"]
search_terms: ["FIToFIPaymentStatusReport to confirm Processability of FIToFICustomerDirectDebit instruction", "Settlement Agent", "Creditor Agent", "Debtor agent", "pacs.002", "pacs.003"]
limitations: ["Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.", "P524/P526 positive status optional under bilateral agreement. P528 mixed group statuses allowed. P521 receiver-informs-receiver wording conflicts with P532/P534 and picture direction (issue-000054).", "Source message names establish family-level flow context; supplied exact schema versions are separately identified.", "Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible."]
manual_curated: true
participant_ids: ["participant-src-000162-clearing-and-settlement-agent", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-initiating-party"]
related_diagrams: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/diagrams/clearing/fig-0040.md"]
issue_ids: ["issue-000054"]
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and whole Word figure pages compared; source tables retain independent review."}
message_reference_scope: "Part1 name/family flow; no exact version inferred from picture."
---

# FIToFIPaymentStatusReport to confirm Processability of FIToFICustomerDirectDebit instruction

[src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Purpose, trigger and preconditions

Confirm processability of a direct-debit instruction.

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

**P521** The positive FIToFIPaymentStatusReport message is sent by the receiver of an instruction to inform the receiver that the instruction received (either single or grouped) is processable.

**P522** A positive FIToFIPaymentStatusReport message can also be used to confirm the processability of a PaymentReturn message or an FIToFIPaymentReversal message.

**P523** The positive FIToFIPaymentStatusReport message is also meant to be generic to ensure re-usability with other Payments Instruments.

**P524** The FIToFIPaymentStatusReport messages are exchanged, point to point between two parties, optionally and as per optional bilateral agreements and may be complemented by an BankToCustomerDebitCreditNotification message ('notification') and/or BankToCustomerAccountReport/BankToCustomerStatement message ('statement').

**P526** The positive CustomerPaymentStatusReport and FIToFIPaymentStatusReport messages are optional.

**P527** As added value service to creditors, some banks may update CustomerPaymentStatusReport messages to inform creditors about the status of transactions during their lifecycle.

**P528** Mixed CustomerPaymentStatusReport and FIToFIPaymentStatusReport messages may be exchanged, that is, ‘partially accepted’ on group level, indicated that the group contains a mix of accepted, pending and/or rejected transactions.

**P530** In this scenario, the FIToFIPaymentStatusReport message is used to confirm the processability of a FIToFICustomerDirectDebit instruction.

**P531** The creditor agent sends an FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

**P532** The clearing and settlement agent confirms the processability of the FIToFICustomerDirectDebit instruction by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

**P533** The clearing and settlement agent sends an FIToFICustomerDirectDebit message, together with potentially the Mandate Related Information (MRI) to the debtor agent immediately for information purposes only.

**P534** The debtor agent sends a positive FIToFIPaymentStatusReport message to the clearing and settlement agent. This positive status message may subsequently be forwarded to the creditor agent.

### fig-0040

[Source reconstruction and actual review](../diagrams/clearing/fig-0040.md); direct-body paragraph P525; Word page52.

| Step | Sender and depicted roles | Receiver and depicted roles | Literal exchange |
| --- | --- | --- | --- |
| 1 | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md); [Creditor / initiating-party](../../../../../../../shared/reference/participants/participant-src-000162-initiating-party.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | CustomerDirectDebitInitiation |
| 2 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md); [Creditor / initiating-party](../../../../../../../shared/reference/participants/participant-src-000162-initiating-party.md) | CustomerPaymentStatusReport |
| 3 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000162-clearing-and-settlement-agent.md) | FIToFICustomerDirectDebit |
| 4 | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000162-clearing-and-settlement-agent.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md) | FIToFIPaymentStatusReport |
| 5 | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000162-clearing-and-settlement-agent.md) | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | FIToFICustomerDirectDebit |
| 6 | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000162-clearing-and-settlement-agent.md) | FIToFIPaymentStatusReport |



## Outcomes, optional paths and source limitations

Source-defined optional acknowledgements, repair/resubmission, account reporting, rejection/return and settlement conditions are retained below. Positive processability status is not by itself settlement.

- Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.
- P524/P526 positive status optional under bilateral agreement. P528 mixed group statuses allowed. P521 receiver-informs-receiver wording conflicts with P532/P534 and picture direction (issue-000054).
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
| pacs.007 | [pacs.007.001.14](../../../../messages/pacs.007.001.14/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pain.002 | [pain.002.001.15](../../../../messages/pain.002.001.15/index.md) | Retrieval name match; schema definition version remains separately scoped. |
| pain.008 | [pain.008.001.12](../../../../messages/pain.008.001.12/index.md) | Retrieval name match; schema definition version remains separately scoped. |


## Review

Source text, original image and complete Word-rendered figure context checked on 2026-11-09. Source issues: issue-000054. Activity tables and schemas retain their own review status.
