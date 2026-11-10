---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p173-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play"
title: "One actor plays roles of Initiating Party and Debtor, second actor plays role of Ultimate Debtor"
source_locations: [{"source_id": "src-000173", "locator": "/w:document/w:body/w:p[155]", "paragraph_id": "P155", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[156]", "paragraph_id": "P156", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[157]", "paragraph_id": "P157", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[158]", "paragraph_id": "P158", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[159]", "paragraph_id": "P159", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[160]", "paragraph_id": "P160", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[161]", "paragraph_id": "P161", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[162]", "paragraph_id": "P162", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[163]", "paragraph_id": "P163", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[164]", "paragraph_id": "P164", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[165]", "paragraph_id": "P165", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[166]", "paragraph_id": "P166", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[167]", "paragraph_id": "P167", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[168]", "paragraph_id": "P168", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[169]", "paragraph_id": "P169", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[173]", "paragraph_id": "P173", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation", "One actor plays roles of Initiating Party and Debtor, second actor plays role of Ultimate Debtor"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[174]", "paragraph_id": "P174", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation", "One actor plays roles of Initiating Party and Debtor, second actor plays role of Ultimate Debtor"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[175]", "paragraph_id": "P175", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation", "One actor plays roles of Initiating Party and Debtor, second actor plays role of Ultimate Debtor"]}]
participants: ["participant-src-000173-account-owner", "participant-src-000173-account-servicer", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-initiating-party", "participant-src-000173-ultimate-debtor"]
message_mapping_evidence: []
message_ids: []
message_families: ["camt.052", "camt.053", "camt.054", "pacs.008", "pain.001", "pain.002"]
search_terms: ["One actor plays roles of Initiating Party and Debtor, second actor plays role of Ultimate Debtor", "Initiating Party", "Ultimate Debtor", "Debtor Agent", "Debtor"]
limitations: ["Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.", "Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling.", "The picture starts with Ultimate Debtor to Debtor Invoice; it does not draw a Creditor-to-Ultimate Debtor invoice."]
manual_curated: true
participant_ids: ["participant-src-000173-account-owner", "participant-src-000173-account-servicer", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-initiating-party", "participant-src-000173-ultimate-debtor"]
related_diagrams: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/diagrams/initiation/fig-0014.md"]
issue_ids: ["issue-000044"]
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and rendered page context compared; tables retain independent review status."}
message_reference_scope: "Family/name-level Part1 flows; supplied exact definitions linked separately."
---



# One actor plays roles of Initiating Party and Debtor, second actor plays role of Ultimate Debtor

[src-000173](../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx)

## Purpose and trigger

Initiating party and debtor are one actor; ultimate debtor is separate.

P175: initiation goes from initiating party to debtor agent.

## Participants and responsibilities

| Scoped participant | Participation evidence |
| --- | --- |
| [account owner](../../../../../../../shared/reference/participants/participant-src-000173-account-owner.md) | Narrative-only participant/example; omitted as a separate figure lifeline. |
| [account servicer](../../../../../../../shared/reference/participants/participant-src-000173-account-servicer.md) | Narrative-only participant/example; omitted as a separate figure lifeline. |
| [creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [creditor agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debtor](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debtor agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [initiating party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | Source figure occurrence; exact action/message direction is shown below. |
| [ultimate debtor](../../../../../../../shared/reference/participants/participant-src-000173-ultimate-debtor.md) | Source figure occurrence; exact action/message direction is shown below. |


## Source-defined conditions and activities

**P156** The CustomerCreditTransferInitiation message is sent from the initiating party to the debtor agent. Depending on the service level agreed between the debtor agent and the initiating party, the debtor agent may send a CustomerPaymentStatusReport message to inform the initiating party of the status of the initiation.

**P157** A number of additional message flows have been included to illustrate the complete end-to-end execution of the CustomerCreditTransferInitiation. However, these messages are out of scope. These message flows are:

**P158** Account information from debtor agent to initiating party

**P159** Depending on the service level agreed, the debtor agent may provide the initiating party with a BankToCustomerDebitCreditNotification ('notification') and/or BankToCustomerAccountReport/BankToCustomerStatement ('statement') once the payment has been executed and the debit entry has been posted to the debtor account. The logical, chronological sequence for sending these messages is defined by the bank implementing and offering these services.

**P160** Interbank clearing and settlement between debtor agent and creditor agent

**P161** Depending on the interbank clearing and settlement method chosen, a number of messages may be exchanged between the agent parties in the payment chain.

**P162** Account information from creditor agent to creditor

**P163** Depending on the service level agreed, the creditor agent may provide the creditor with a BankToCustomerDebitCreditNotification ('notification') and/or BankToCustomerAccountReport/BankToCustomerStatement ('statement') once the payment has been posted to the creditor account. The logical, chronological sequence for sending these messages is defined by the bank implementing and offering these services.

**P164** The scenarios below illustrate the different customer roles that can be played on the initiating side of the credit transfer initiation, and on the receiving side of the cash transfer.

**P165** On the initiating side, up to three customer roles can be specified: the initiating party, that is, the party sending the message, the debtor, that is the debit account owner, and the ultimate debtor, that is, the party that owes the cash to the creditor as a result of receipt of goods or services.

**P166** These three roles can be played by one and the same actor, or they can be played by different actors.

**P167** The CustomerCreditTransferInitiation message allows inclusion of the three different roles on the initiating side.

**P168** On the receiving side, up to two customer roles can be specified: the creditor, that is, the credit account owner, and the creditor, that is, the party that is the ultimate beneficiary of the cash transfer. These two roles can be played by one and the same actor, or they can be played by different actors.

**P169** The CustomerCreditTransferInitiation message allows inclusion of the two different roles on the receiving side.

**P175** The message is sent by an initiating party to the debtor agent. The actor playing the role of initiating party is the same as the actor playing the role of debtor, but the role of the ultimate debtor is played by a different actor.

### fig-0014

[Source reconstruction and review](../diagrams/initiation/fig-0014.md); direct-body paragraph P174; Word file page26.

| Step | Sender and roles | Receiver and roles | Literal exchange |
| --- | --- | --- | --- |
| 1 | [Ultimate Debtor / ultimate-debtor](../../../../../../../shared/reference/participants/participant-src-000173-ultimate-debtor.md) | [Debtor (initiating party) / debtor](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md); [Debtor (initiating party) / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | Invoice |
| 2 | [Debtor (initiating party) / debtor](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md); [Debtor (initiating party) / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | CustomerCreditTransferInitiation |
| 3 | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | [Debtor (initiating party) / debtor](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md); [Debtor (initiating party) / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | CustomerPaymentStatusReport |
| 4 | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | FIToFICustomerCreditTransfer |
| 5 | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | [Debtor (initiating party) / debtor](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md); [Debtor (initiating party) / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | Notification |
| 6 | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | [Debtor (initiating party) / debtor](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md); [Debtor (initiating party) / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | Statement |
| 7 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Notification |
| 8 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Statement |



## Outcomes, alternatives and related processes

Picture and P175 retain the separate ultimate-debtor relationship; reporting and interbank qualifications are in P157–163.

- Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.
- Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling.
- The picture starts with Ultimate Debtor to Debtor Invoice; it does not draw a Creditor-to-Ultimate Debtor invoice.

## Supplied message definitions

| Family | Exact supplied reference | Scope |
| --- | --- | --- |
| camt.052 | [camt.052.001.14](../../../../messages/camt.052.001.14/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| camt.053 | [camt.053.001.14](../../../../messages/camt.053.001.14/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| camt.054 | [camt.054.001.14](../../../../messages/camt.054.001.14/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pacs.008 | [pacs.008.001.14](../../../../messages/pacs.008.001.14/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pain.001 | [pain.001.001.13](../../../../messages/pain.001.001.13/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pain.002 | [pain.002.001.15](../../../../messages/pain.002.001.15/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |



## Review

Compared source narrative, picture labels/directions and complete figure page context on 2026-11-09. Unresolved source claims: issue-000044. This bounded flow evidence has been reviewed; participant classification/schema/table references keep their own review status.
