---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p249-negative-fito-fipayment-status-report-debtor-agent"
title: "Negative FIToFIPaymentStatusReport - Debtor Agent"
source_locations: [{"source_id": "src-000173", "locator": "/w:document/w:body/w:p[231]", "paragraph_id": "P231", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[232]", "paragraph_id": "P232", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[233]", "paragraph_id": "P233", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[249]", "paragraph_id": "P249", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative FIToFIPaymentStatusReport - Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[250]", "paragraph_id": "P250", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative FIToFIPaymentStatusReport - Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[251]", "paragraph_id": "P251", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative FIToFIPaymentStatusReport - Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[252]", "paragraph_id": "P252", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative FIToFIPaymentStatusReport - Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[253]", "paragraph_id": "P253", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative FIToFIPaymentStatusReport - Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[254]", "paragraph_id": "P254", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative FIToFIPaymentStatusReport - Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[255]", "paragraph_id": "P255", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative FIToFIPaymentStatusReport - Debtor Agent"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[256]", "paragraph_id": "P256", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "CustomerPaymentStatusReport message to the Creditor "]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[257]", "paragraph_id": "P257", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "CustomerPaymentStatusReport message to the Creditor "]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[258]", "paragraph_id": "P258", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "CustomerPaymentStatusReport message to the Creditor "]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[259]", "paragraph_id": "P259", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "CustomerPaymentStatusReport message to the Creditor "]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[260]", "paragraph_id": "P260", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "CustomerPaymentStatusReport message to the Creditor "]}]
participants: ["participant-src-000173-clearing-and-settlement-agent", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-initiating-party"]
message_mapping_evidence: [{"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["camt.052", "camt.053", "camt.054", "pacs.002", "pacs.003", "pacs.004", "pain.002", "pain.008"]
search_terms: ["Negative FIToFIPaymentStatusReport - Debtor Agent", "Creditor Agent", "Debtor Agent", "Creditor", "pain.002", "pain.008"]
limitations: ["Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.", "First two status exchanges are positive; debtor-agent status is negative, then relayed. P252–260 supply timing, repair and optional customer-information qualifications.", "Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling."]
manual_curated: true
participant_ids: ["participant-src-000173-clearing-and-settlement-agent", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-initiating-party"]
related_diagrams: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/diagrams/initiation/fig-0022.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and rendered page context compared; tables retain independent review status."}
message_reference_scope: "Family/name-level Part1 flows; supplied exact definitions linked separately."
---



# Negative FIToFIPaymentStatusReport - Debtor Agent

[src-000173](../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx)

## Purpose and trigger

Debtor agent rejects an interbank direct-debit instruction.

P260: settlement has not occurred. Initial positive statuses do not prevent later rejection.

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

**P250** A negative FIToFIPaymentStatusReport message is initiated by the debtor agent to reject the FIToFICustomerDirectDebit message (only the messages that are part of the scope of the direct debit are illustrated in the diagram):

**P252** Whenever possible, the creditor agent will correct or complement the instruction and re-submit. If this is the case, the creditor agent would not send a negative CustomerPaymentStatusReport to the creditor. However, depending on what has been agreed between the creditor and its agent, the creditor agent may inform its customer about the repair, for example, value date.

**P253** With respect to ‘Information’ above: if the creditor agent books after collection, for example, cycle is 3 days, then the CustomerPaymentStatusReport message is to be used. If the creditor agent books immediately and the instruction is rejected in the interbank leg, then the creditor needs to be informed of a payment return.

**P254** The creditor sends a CustomerDirectDebitInitiation message to its Agent (the creditor agent).

**P255** The creditor agent confirms the processability of the CustomerDirectDebitInitiation message by sending a positive

**P257** The creditor agent sends an FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

**P258** The clearing and settlement agent confirms the processability of the FIToFICustomerDirectDebit message by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

**P259** The clearing and settlement agent sends an FIToFICustomerDirectDebit message, optionally with the Mandate Related Reference (MRI), to the debtor agent immediately for information purposes only.

**P260** If settlement has not yet taken place, the debtor agent may send a negative FIToFIPaymentStatusReport message to the clearing and settlement agent, to inform him about the rejection of the FIToFICustomerDirectDebitinstruction. This negative FIToFIPaymentStatusReport message may subsequently be forwarded to the creditor agent. The creditor agent may inform (but not necessarily) his customer, the creditor, about the negative processing of the CustomerDirectDebitInitiation instruction by using a CustomerPaymentStatusReport message, a BankToCustomerDebitCreditNotification message ('notification') or through a BankToCustomerAccountReport and/or BankToCustomerStatement message ('statement').

### fig-0022

[Source reconstruction and review](../diagrams/initiation/fig-0022.md); direct-body paragraph P251; Word file page34.

| Step | Sender and roles | Receiver and roles | Literal exchange |
| --- | --- | --- | --- |
| 1 | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md); [Creditor / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | CustomerDirectDebitInitiation |
| 2 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md); [Creditor / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | CustomerPaymentStatusReport |
| 3 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | FIToFICustomerDirectDebit |
| 4 | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | FIToFIPaymentStatusReport |
| 5 | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | FIToFICustomerDirectDebit |
| 6 | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | FIToFIPaymentStatusReport |
| 7 | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | FIToFIPaymentStatusReport |
| 8 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md); [Creditor / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | Information |



## Outcomes, alternatives and related processes

Negative interbank status may be relayed to creditor agent; creditor information/repair remain conditional (P252–260).

- Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.
- First two status exchanges are positive; debtor-agent status is negative, then relayed. P252–260 supply timing, repair and optional customer-information qualifications.
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
