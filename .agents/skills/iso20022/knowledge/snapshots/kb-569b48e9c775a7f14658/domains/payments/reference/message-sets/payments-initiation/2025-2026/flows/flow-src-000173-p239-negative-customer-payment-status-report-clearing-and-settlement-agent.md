---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p239-negative-customer-payment-status-report-clearing-and-settlement-agent"
title: "Negative CustomerPaymentStatusReport - Clearing And Settlement Agent"
source_locations: [{"source_id": "src-000173", "locator": "/w:document/w:body/w:p[231]", "paragraph_id": "P231", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[232]", "paragraph_id": "P232", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[233]", "paragraph_id": "P233", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[239]", "paragraph_id": "P239", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative CustomerPaymentStatusReport - Clearing And Settlement Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[240]", "paragraph_id": "P240", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative CustomerPaymentStatusReport - Clearing And Settlement Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[241]", "paragraph_id": "P241", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative CustomerPaymentStatusReport - Clearing And Settlement Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[242]", "paragraph_id": "P242", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative CustomerPaymentStatusReport - Clearing And Settlement Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[243]", "paragraph_id": "P243", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative CustomerPaymentStatusReport - Clearing And Settlement Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[244]", "paragraph_id": "P244", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative CustomerPaymentStatusReport - Clearing And Settlement Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[245]", "paragraph_id": "P245", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative CustomerPaymentStatusReport - Clearing And Settlement Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[246]", "paragraph_id": "P246", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative CustomerPaymentStatusReport - Clearing And Settlement Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[247]", "paragraph_id": "P247", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative CustomerPaymentStatusReport - Clearing And Settlement Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[248]", "paragraph_id": "P248", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative CustomerPaymentStatusReport - Clearing And Settlement Agent"]}]
participants: ["participant-src-000173-clearing-and-settlement-agent", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-initiating-party"]
message_mapping_evidence: [{"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["camt.052", "camt.053", "camt.054", "pacs.002", "pacs.003", "pacs.004", "pain.002", "pain.008"]
search_terms: ["Negative CustomerPaymentStatusReport - Clearing And Settlement Agent", "Creditor Agent", "Creditor", "pain.002", "pain.008"]
limitations: ["Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.", "P240: clearing/settlement negative FIToFIPaymentStatusReport rejects the instruction before settlement. P242/P248 prefer correcting and resubmitting without involving creditor where possible. P243/P247 identify alternatives for the generic Information arrow based on booking/agreement.", "Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling."]
manual_curated: true
participant_ids: ["participant-src-000173-clearing-and-settlement-agent", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-initiating-party"]
related_diagrams: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/diagrams/initiation/fig-0021.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and rendered page context compared; tables retain independent review status."}
message_reference_scope: "Family/name-level Part1 flows; supplied exact definitions linked separately."
---



# Negative CustomerPaymentStatusReport - Clearing And Settlement Agent

[src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Purpose and trigger

Clearing/settlement agent rejects an interbank direct-debit instruction.

P240/P247: instruction is not processable and settlement has not occurred.

## Participants and responsibilities

| Scoped participant | Participation evidence |
| --- | --- |
| [clearing and settlement agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [creditor agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debtor](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debtor agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [initiating party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | Source figure occurrence; exact action/message direction is shown below. |


## Source-defined conditions and activities

**P232** The negative CustomerPaymentStatusReport message (single or grouped) or FItoFIPaymentStatusReport message (single or grouped) is sent by the receiver of an instruction to inform the sender of the instruction about the negative processability of the instruction.

**P233** The negative CustomerPaymentStatusReport message FIToFIPaymentStatusReport message used to reject a direct debit instruction, is to be sent before settlement. After settlement, the correct message to be used is the PaymentReturn message.

**P240** A negative FIToFIPaymentStatusReport message is initiated by the clearing and settlement agent to reject an FIToFICustomerDirectDebit message (only the messages that are part of the scope of the direct debit are illustrated in the diagram):

**P242** Whenever possible, the creditor agent will correct or complement the instruction and re-submit. If this is the case, the creditor agent would not send a negative CustomerPaymentStatusReport to the creditor. However, depending on what has been agreed between the creditor and its agent, the creditor agent may inform its customer about the repair, for example, value date.

**P243** With respect to ‘Information’ above: If the creditor agent books after collection (that is cycle is 3 days) then the CustomerPaymentStatusReport message is to be used. If the creditor agent books immediately and the instruction is rejected in the interbank leg, then the creditor needs to be informed of a payment return.

**P244** The creditor sends the CustomerDirectDebitInitiation message to its Agent (the creditor agent).

**P245** The creditor agent confirms the processability of the CustomerDirectDebitInitiation instruction by sending a positive CustomerPaymentStatusReport message to the creditor.

**P246** The creditor agent sends an FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

**P247** If information is missing and interbank settlement has not taken place yet, the clearing and settlement agent informs the creditor agent about the non processability of the FIToFICustomerDirectDebit instruction. The creditor agent may inform (but not necessarily) his customer, the creditor, about the negative processing of the CustomerDirectDebitInitiation instruction by using a negative CustomerPaymentStatusReport message, a BankToCustomerDebitCreditNotification message ('notification') or through a BankToCustomerAccountReport and/or BankToCustomerStatement message.

**P248** Before sending a negative CustomerPaymentStatusReport message to its customer, it is assumed that the creditor agent will try to correct the CustomerDirectDebitInitiation message information and re-submit an FIToFICustomerDirectDebit message to the clearing and settlement agent. In this case the creditor will not be involved.

### fig-0021

[Source reconstruction and review](../diagrams/initiation/fig-0021.md); direct-body paragraph P241; Word file page33.

| Step | Sender and roles | Receiver and roles | Literal exchange |
| --- | --- | --- | --- |
| 1 | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md); [Creditor / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | CustomerDirectDebitInitiation |
| 2 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md); [Creditor / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | CustomerPaymentStatusReport |
| 3 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | FIToFICustomerDirectDebit |
| 4 | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | FIToFIPaymentStatusReport |
| 5 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md); [Creditor / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | Information |



## Outcomes, alternatives and related processes

Creditor agent first tries repair/resubmission when possible; customer information depends on booking and agreement (P242–248).

- Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.
- P240: clearing/settlement negative FIToFIPaymentStatusReport rejects the instruction before settlement. P242/P248 prefer correcting and resubmitting without involving creditor where possible. P243/P247 identify alternatives for the generic Information arrow based on booking/agreement.
- Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling.

## Supplied message definitions

| Family | Exact supplied reference | Scope |
| --- | --- | --- |
| camt.052 | [camt.052.001.14](../../../../messages/camt.052.001.14/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| camt.053 | [camt.053.001.14](../../../../messages/camt.053.001.14/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| camt.054 | [camt.054.001.14](../../../../messages/camt.054.001.14/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pacs.002 | [pacs.002.001.16](../../../../messages/pacs.002.001.16/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pacs.003 | [pacs.003.001.12](../../../../messages/pacs.003.001.12/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pacs.004 | [pacs.004.001.15](../../../../messages/pacs.004.001.15/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pain.002 | [pain.002.001.15](../../../../messages/pain.002.001.15/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pain.008 | [pain.008.001.12](../../../../messages/pain.008.001.12/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |



## Review

Compared source narrative, picture labels/directions and complete figure page context on 2026-11-09. This bounded flow evidence has been reviewed; participant classification/schema/table references keep their own review status.
