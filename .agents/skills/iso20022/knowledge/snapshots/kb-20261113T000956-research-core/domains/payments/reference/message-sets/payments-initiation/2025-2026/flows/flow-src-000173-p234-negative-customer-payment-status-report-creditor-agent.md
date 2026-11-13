---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p234-negative-customer-payment-status-report-creditor-agent"
title: "Negative CustomerPaymentStatusReport - Creditor Agent"
source_locations: [{"source_id": "src-000173", "locator": "/w:document/w:body/w:p[231]", "paragraph_id": "P231", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[232]", "paragraph_id": "P232", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[233]", "paragraph_id": "P233", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[234]", "paragraph_id": "P234", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative CustomerPaymentStatusReport - Creditor Agent "]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[235]", "paragraph_id": "P235", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative CustomerPaymentStatusReport - Creditor Agent "]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[236]", "paragraph_id": "P236", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative CustomerPaymentStatusReport - Creditor Agent "]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[237]", "paragraph_id": "P237", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative CustomerPaymentStatusReport - Creditor Agent "]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[238]", "paragraph_id": "P238", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "Negative CustomerPaymentStatusReport - Creditor Agent "]}]
participants: ["participant-src-000173-clearing-and-settlement-agent", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-initiating-party"]
message_mapping_evidence: [{"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["pacs.002", "pacs.004", "pain.002", "pain.008"]
search_terms: ["Negative CustomerPaymentStatusReport - Creditor Agent", "Creditor Agent", "Creditor", "pain.002", "pain.008"]
limitations: ["Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.", "P235/P238: creditor agent rejects initiation for non-processability, for example missing information. Unused lifelines are retained.", "Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling."]
manual_curated: true
participant_ids: ["participant-src-000173-clearing-and-settlement-agent", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-initiating-party"]
related_diagrams: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/diagrams/initiation/fig-0020.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and rendered page context compared; tables retain independent review status."}
message_reference_scope: "Family/name-level Part1 flows; supplied exact definitions linked separately."
---



# Negative CustomerPaymentStatusReport - Creditor Agent

[src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Purpose and trigger

Creditor agent rejects a customer direct-debit initiation.

P232–235: instruction is not processable; negative status is sent before settlement.

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

**P235** A negative CustomerPaymentStatusReport message is initiated by the creditor agent to reject a CustomerDirectDebitInitiation message. (Only the messages that are part of the scope of the direct debit are illustrated in the diagram):

**P237** The creditor sends the CustomerDirectDebitInitiation message to its Agent (the creditor agent).

**P238** The creditor agent sends a negative CustomerPaymentStatusReport message to the creditor to inform him about the non processability of the CustomerDirectDebitInitiation instruction, for instance due to missing information.

### fig-0020

[Source reconstruction and review](../diagrams/initiation/fig-0020.md); direct-body paragraph P236; Word file page33.

| Step | Sender and roles | Receiver and roles | Literal exchange |
| --- | --- | --- | --- |
| 1 | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md); [Creditor / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | CustomerDirectDebitInitiation |
| 2 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md); [Creditor / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | CustomerPaymentStatusReport |



## Outcomes, alternatives and related processes

Creditor receives negative CustomerPaymentStatusReport, e.g. for missing information (P238). After settlement use PaymentReturn (P233).

- Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.
- P235/P238: creditor agent rejects initiation for non-processability, for example missing information. Unused lifelines are retained.
- Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling.

## Supplied message definitions

| Family | Exact supplied reference | Scope |
| --- | --- | --- |
| pacs.002 | [pacs.002.001.16](../../../../messages/pacs.002.001.16/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pacs.004 | [pacs.004.001.15](../../../../messages/pacs.004.001.15/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pain.002 | [pain.002.001.15](../../../../messages/pain.002.001.15/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pain.008 | [pain.008.001.12](../../../../messages/pain.008.001.12/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |



## Review

Compared source narrative, picture labels/directions and complete figure page context on 2026-11-09. This bounded flow evidence has been reviewed; participant classification/schema/table references keep their own review status.
