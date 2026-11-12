---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p298-customer-payment-reversal-with-direct-debit"
title: "Customer Payment Reversal with Direct Debit"
source_locations: [{"source_id": "src-000173", "locator": "/w:document/w:body/w:p[298]", "paragraph_id": "P298", "heading_path": ["BusinessTransactions", "Customer Payment Reversal with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[299]", "paragraph_id": "P299", "heading_path": ["BusinessTransactions", "Customer Payment Reversal with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[300]", "paragraph_id": "P300", "heading_path": ["BusinessTransactions", "Customer Payment Reversal with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[301]", "paragraph_id": "P301", "heading_path": ["BusinessTransactions", "Customer Payment Reversal with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[302]", "paragraph_id": "P302", "heading_path": ["BusinessTransactions", "Customer Payment Reversal with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[303]", "paragraph_id": "P303", "heading_path": ["BusinessTransactions", "Customer Payment Reversal with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[304]", "paragraph_id": "P304", "heading_path": ["BusinessTransactions", "Customer Payment Reversal with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[305]", "paragraph_id": "P305", "heading_path": ["BusinessTransactions", "Customer Payment Reversal with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[306]", "paragraph_id": "P306", "heading_path": ["BusinessTransactions", "Customer Payment Reversal with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[307]", "paragraph_id": "P307", "heading_path": ["BusinessTransactions", "Customer Payment Reversal with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[308]", "paragraph_id": "P308", "heading_path": ["BusinessTransactions", "Customer Payment Reversal with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[309]", "paragraph_id": "P309", "heading_path": ["BusinessTransactions", "Customer Payment Reversal with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[310]", "paragraph_id": "P310", "heading_path": ["BusinessTransactions", "Customer Payment Reversal with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[311]", "paragraph_id": "P311", "heading_path": ["BusinessTransactions", "Customer Payment Reversal with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[312]", "paragraph_id": "P312", "heading_path": ["BusinessTransactions", "Customer Payment Reversal with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[313]", "paragraph_id": "P313", "heading_path": ["BusinessTransactions", "Customer Payment Reversal with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[314]", "paragraph_id": "P314", "heading_path": ["BusinessTransactions", "Customer Payment Reversal with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[315]", "paragraph_id": "P315", "heading_path": ["BusinessTransactions", "Customer Payment Reversal with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[316]", "paragraph_id": "P316", "heading_path": ["BusinessTransactions", "Customer Payment Reversal with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[317]", "paragraph_id": "P317", "heading_path": ["BusinessTransactions", "Customer Payment Reversal with Direct Debit"]}]
participants: ["participant-src-000173-clearing-agent", "participant-src-000173-clearing-and-settlement-agent", "participant-src-000173-credit-party", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debit-party", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-initiating-party", "participant-src-000173-scheme-manager", "participant-src-000173-settlement-agent"]
message_mapping_evidence: [{"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["pacs.002", "pacs.003", "pacs.004", "pacs.007", "pain.002", "pain.007", "pain.008"]
search_terms: ["Customer Payment Reversal with Direct Debit", "Creditor Agent", "Debtor Agent", "Creditor", "Debtor", "Party", "pain.002", "pain.007", "pain.008"]
limitations: ["Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.", "P299: after settlement, a paid direct debit should not have been processed. P301 permits creditor agent originating the reversal. P313–315 separate settlement is outside picture; P317 warns return and reversal may cross.", "Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling."]
manual_curated: true
participant_ids: ["participant-src-000173-clearing-agent", "participant-src-000173-clearing-and-settlement-agent", "participant-src-000173-credit-party", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debit-party", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-initiating-party", "participant-src-000173-scheme-manager", "participant-src-000173-settlement-agent"]
related_diagrams: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/diagrams/initiation/fig-0025.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and rendered page context compared; tables retain independent review status."}
message_reference_scope: "Family/name-level Part1 flows; supplied exact definitions linked separately."
---



# Customer Payment Reversal with Direct Debit

[src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Purpose and trigger

Reverse a paid direct debit that should not have been processed.

P299: after settlement; P309 example is duplicated instruction and reversal refers to original with reasons.

## Participants and responsibilities

| Scoped participant | Participation evidence |
| --- | --- |
| [clearing agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-agent.md) | Narrative-only participant/example; omitted as a separate figure lifeline. |
| [clearing and settlement agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [credit party](../../../../../../../shared/reference/participants/participant-src-000173-credit-party.md) | Narrative-only participant/example; omitted as a separate figure lifeline. |
| [creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [creditor agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debit party](../../../../../../../shared/reference/participants/participant-src-000173-debit-party.md) | Narrative-only participant/example; omitted as a separate figure lifeline. |
| [debtor](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debtor agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [initiating party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | Source figure occurrence; exact action/message direction is shown below. |
| [scheme manager](../../../../../../../shared/reference/participants/participant-src-000173-scheme-manager.md) | Narrative-only participant/example; omitted as a separate figure lifeline. |
| [settlement agent](../../../../../../../shared/reference/participants/participant-src-000173-settlement-agent.md) | Narrative-only participant/example; omitted as a separate figure lifeline. |


## Source-defined conditions and activities

**P299** The creditor will initiate a CustomerPaymentReversal message, after settlement, when a paid direct debit should not have been processed.

**P300** The creditor agent will, in turn, initiate an FIToFIPaymentReversal message for the next agent in the payment chain. Consequently, the debtor will be credited.

**P301** The creditor agent may be the originator of a payment reversal - he will in this case initiate an FIToFIPaymentReversal message (only the potential messages that are part of the scope of the direct debit are illustrated in the diagram):

**P304** The creditor sends a CustomerDirectDebitInitiation message to its agent (the creditor agent).

**P305** The creditor agent confirms the processability of the CustomerDirectDebitInitiation instruction by sending a positive CustomerPaymentStatusReport message to the creditor.

**P306** The creditor agent sends an FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

**P307** The clearing and settlement agent confirms the processability of the FIToFICustomerDirectDebit instruction by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

**P308** The clearing and settlement agent sends an FIToFICustomerDirectDebit message, optionally with the Mandate Related Reference (MRI), to the debtor agent immediately for information purposes only.

**P309** The debtor agent sends a positive FIToFIPaymentStatusReport message to the clearing and settlement agent. The creditor realises this was a duplicated CustomerDirectDebitInitiation instruction. He now wants to send a CustomerPaymentReversal message. He identifies the original CustomerDirectDebitInitiation message (or a file of direct debit instructions) and generates an offsetting transaction in favour of the debtor, under the quotation of the reversal reasons. The creditor agent may confirm the receipt of the CustomerPaymentReversal message by sending a positive CustomerPaymentStatusReport message to the creditor.

**P310** An FIToFIPaymentReversal message is submitted by the creditor agent to the clearing and settlement agent for settlement, under quotation of the original direct debit reference and the reason for the reversal.

**P311** The Clearing Agent confirms the processability of the reversal by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

**P312** The clearing and settlement agent forwards the FIToFIPaymentReversal message to the debtor agent immediately for information purposes only.

**P313** In case the clearing and settlement agent are two parties the Clearing Agent prepares the payment information for the Settlement Agent (in accordance with the agreed and published settlement cycle). That process includes the calculation of the settlement positions.

**P314** The information provided to the Settlement Agent is the net position to be debited, the party to be debited, the net position to the credited, the party to be credited and the value date (Out of Scope).

**P315** The Settlement Agent performs the transfer of funds from the Credit Party to the Debit Party (in accordance with the agreed and published settlement cycle) (Out of Scope).

**P316** A positive FIToFIPaymentStatusReport message can optionally be initiated by the debtor agent and sent to the clearing and settlement agent to confirm the processability of the reversal message.

**P317** It may exceptionally occur that a PaymentReturn message and a CustomerPaymentReversal message would cross each other, this could only be avoided through value-added monitoring services that could be offered by the scheme manager and/or this might provoke exceptions/investigation handling.

### fig-0025

[Source reconstruction and review](../diagrams/initiation/fig-0025.md); direct-body paragraph P303; Word file page39.

| Step | Sender and roles | Receiver and roles | Literal exchange |
| --- | --- | --- | --- |
| 1 | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md); [Creditor / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | CustomerDirectDebitInitiation |
| 2 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md); [Creditor / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | CustomerPaymentStatusReport |
| 3 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | FIToFICustomerDirectDebit |
| 4 | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | FIToFIPaymentStatusReport |
| 5 | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | FIToFICustomerDirectDebit |
| 6 | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | FIToFIPaymentStatusReport |
| 7 | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md); [Creditor / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | CustomerPaymentReversal |
| 8 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md); [Creditor / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | CustomerPaymentStatusReport |
| 9 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | FIToFIPaymentReversal |
| 10 | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | FIToFIPaymentStatusReport |
| 11 | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | FIToFIPaymentReversal |
| 12 | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | FIToFIPaymentStatusReport |



## Outcomes, alternatives and related processes

Creditor or creditor agent may initiate; debtor is credited. Optional status confirmations and separate settlement remain explicit. Return/reversal may cross and require monitoring or investigation (P317).

- Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.
- P299: after settlement, a paid direct debit should not have been processed. P301 permits creditor agent originating the reversal. P313–315 separate settlement is outside picture; P317 warns return and reversal may cross.
- Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling.

| Process | Reference |
| --- | --- |
| Direct-debit return activity | [Direct-debit return activity](flow-src-000173-p149-return-direct-debit.md) |
| Debtor refund request | [Debtor refund request](flow-src-000173-p151-request-refund-of-direct-debit.md) |
| PaymentReturn exchange | [PaymentReturn exchange](flow-src-000173-p280-payment-return-initiated-by-debtor-agent.md) |
| Post-settlement CustomerPaymentReversal | [Post-settlement CustomerPaymentReversal](flow-src-000173-p298-customer-payment-reversal-with-direct-debit.md) |


## Supplied message definitions

| Family | Exact supplied reference | Scope |
| --- | --- | --- |
| pacs.002 | [pacs.002.001.16](../../../../messages/pacs.002.001.16/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pacs.003 | [pacs.003.001.12](../../../../messages/pacs.003.001.12/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pacs.004 | [pacs.004.001.15](../../../../messages/pacs.004.001.15/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pacs.007 | [pacs.007.001.14](../../../../messages/pacs.007.001.14/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pain.002 | [pain.002.001.15](../../../../messages/pain.002.001.15/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pain.007 | [pain.007.001.13](../../../../messages/pain.007.001.13/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pain.008 | [pain.008.001.12](../../../../messages/pain.008.001.12/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |



## Review

Compared source narrative, picture labels/directions and complete figure page context on 2026-11-09. This bounded flow evidence has been reviewed; participant classification/schema/table references keep their own review status.
