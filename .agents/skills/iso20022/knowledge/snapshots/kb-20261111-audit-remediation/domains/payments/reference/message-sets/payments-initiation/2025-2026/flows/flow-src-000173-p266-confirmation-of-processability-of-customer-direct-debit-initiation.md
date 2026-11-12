---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p266-confirmation-of-processability-of-customer-direct-debit-initiation"
title: "Confirmation of Processability of CustomerDirectDebitInitiation"
source_locations: [{"source_id": "src-000173", "locator": "/w:document/w:body/w:p[261]", "paragraph_id": "P261", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[262]", "paragraph_id": "P262", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[263]", "paragraph_id": "P263", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[264]", "paragraph_id": "P264", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[265]", "paragraph_id": "P265", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[266]", "paragraph_id": "P266", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit", "Confirmation of Processability of CustomerDirectDebitInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[267]", "paragraph_id": "P267", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit", "Confirmation of Processability of CustomerDirectDebitInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[268]", "paragraph_id": "P268", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit", "Confirmation of Processability of CustomerDirectDebitInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[269]", "paragraph_id": "P269", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit", "Confirmation of Processability of CustomerDirectDebitInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[270]", "paragraph_id": "P270", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit", "Confirmation of Processability of CustomerDirectDebitInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[271]", "paragraph_id": "P271", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit", "Confirmation of Processability of CustomerDirectDebitInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[272]", "paragraph_id": "P272", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit", "Confirmation of Processability of CustomerDirectDebitInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[273]", "paragraph_id": "P273", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit", "Confirmation of Processability of CustomerDirectDebitInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[274]", "paragraph_id": "P274", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit", "Confirmation of Processability of CustomerDirectDebitInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[275]", "paragraph_id": "P275", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit", "Confirmation of Processability of CustomerDirectDebitInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[276]", "paragraph_id": "P276", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit", "Confirmation of Processability of CustomerDirectDebitInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[277]", "paragraph_id": "P277", "heading_path": ["BusinessTransactions", "Positive Customer and FIToFIPaymentStatusReport with Direct Debit", "Confirmation of Processability of CustomerDirectDebitInitiation"]}]
participants: ["participant-src-000173-clearing-and-settlement-agent", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-initiating-party"]
message_mapping_evidence: [{"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["camt.052", "camt.053", "camt.054", "pacs.002", "pacs.003", "pacs.004", "pain.002", "pain.008"]
search_terms: ["Confirmation of Processability of CustomerDirectDebitInitiation", "Creditor Agent", "Debtor Agent", "Creditor", "pain.002", "pain.008"]
limitations: ["Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.", "P265/P269: point-to-point positive reports are optional under bilateral agreement; P271 allows partially accepted groups. P262 literally says receiver informs receiver, whereas arrows/P273/P275/P277 report to the prior sender (issue-000044).", "Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling."]
manual_curated: true
participant_ids: ["participant-src-000173-clearing-and-settlement-agent", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-initiating-party"]
related_diagrams: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/diagrams/initiation/fig-0023.md"]
issue_ids: ["issue-000044"]
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and rendered page context compared; tables retain independent review status."}
message_reference_scope: "Family/name-level Part1 flows; supplied exact definitions linked separately."
---



# Confirmation of Processability of CustomerDirectDebitInitiation

[src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Purpose and trigger

Confirm processability along direct-debit chain.

P265/P269: optional point-to-point status reports under bilateral agreement.

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

**P262** The positive CustomerPaymentStatusReport message (single or grouped) and FIToFIPaymentStatusReport message (single or grouped) is sent by the receiver of an instruction to inform the receiver that the instruction received is processable.

**P263** A positive CustomerPaymentStatusReport message or FIToFIPaymentStatusReport message can also be used to confirm the processability of a PaymentReturn message (in case of FIToFI) or a PaymentReversal message.

**P264** The positive CustomerPaymentStatusReport message and FIToFIPaymentStatusReport message are also meant to be generic to ensure re-usability with other Payments Instruments.

**P265** The CustomerPaymentStatusReport and FIToFIPaymentStatusReport messages are exchanged, point to point between two parties, optionally and as per bilateral agreements and may be complemented by a BankToCustomerDebitCreditNotification message ('notification') and/or BankToCustomerAccountReport/ BankToCustomerStatement message ('statement').

**P267** This scenario shows the use of the CustomerPaymentStatusReport message and FIToFIPaymentStatusReport message to confirm the processability of a CustomerDirectDebitInitiation instruction, followed by an FIToFICustomerDirectDebit message (only the messages that are part of the scope of the direct debit are illustrated in the diagram):

**P269** The positive CustomerPaymentStatusReport and FIToFIPaymentStateReport messages are optional.

**P270** To provide added value to its creditor, a bank may send a CustomerPaymentStatusReport message with an updated status to inform the creditor about the status of the transaction. The status updates may be provided throughout the life-cycle of the transaction.

**P271** A ‘mixed’ CustomerPaymentStatusReport or FIToFIPaymentStatusReport message may be exchanged, that is, the status is ‘partially accepted’ at group level, indicating that the group contains a mix of accepted, pending or rejected transactions.

**P272** The creditor sends the CustomerDirectDebitInitiation message to its Agent (the creditor agent).

**P273** The creditor agent confirms the processability of the CustomerDirectDebitInitiation instruction by sending a positive CustomerPaymentStatusReport message to the creditor.

**P274** The creditor agent sends an FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

**P275** The clearing and settlement agent confirms the processability of the FIToFICustomerDirectDebit instruction by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

**P276** The clearing and settlement agent sends an FIToFICustomerDirectDebit message, optionally with the Mandate Related Information (MRI) to the debtor agent immediately for information purposes only.

**P277** The debtor agent sends a positive FIToFIPaymentStatusReport message to the clearing and settlement agent. This positive status message may subsequently be forwarded to the creditor agent.

### fig-0023

[Source reconstruction and review](../diagrams/initiation/fig-0023.md); direct-body paragraph P268; Word file page36.

| Step | Sender and roles | Receiver and roles | Literal exchange |
| --- | --- | --- | --- |
| 1 | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md); [Creditor / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | CustomerDirectDebitInitiation |
| 2 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md); [Creditor / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | CustomerPaymentStatusReport |
| 3 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | FIToFICustomerDirectDebit |
| 4 | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | FIToFIPaymentStatusReport |
| 5 | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | FIToFICustomerDirectDebit |
| 6 | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | [Clearing and Settlement Agent / clearing-and-settlement-agent](../../../../../../../shared/reference/participants/participant-src-000173-clearing-and-settlement-agent.md) | FIToFIPaymentStatusReport |



## Outcomes, alternatives and related processes

Processability status is not settlement. Updated/mixed status reports may follow (P270–271). P262 receiver wording conflicts with literal message directions.

- Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.
- P265/P269: point-to-point positive reports are optional under bilateral agreement; P271 allows partially accepted groups. P262 literally says receiver informs receiver, whereas arrows/P273/P275/P277 report to the prior sender (issue-000044).
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

Compared source narrative, picture labels/directions and complete figure page context on 2026-11-09. Unresolved source claims: issue-000044. This bounded flow evidence has been reviewed; participant classification/schema/table references keep their own review status.
