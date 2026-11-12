---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p195-one-actor-plays-roles-of-initiating-party-and-ultimate-debtor-second-a"
title: "One actor plays roles of Initiating Party and Ultimate Debtor, Second Actor plays role of Debtor"
source_locations: [{"source_id": "src-000173", "locator": "/w:document/w:body/w:p[179]", "paragraph_id": "P179", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[180]", "paragraph_id": "P180", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[181]", "paragraph_id": "P181", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[182]", "paragraph_id": "P182", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[183]", "paragraph_id": "P183", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[184]", "paragraph_id": "P184", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[185]", "paragraph_id": "P185", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[186]", "paragraph_id": "P186", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[187]", "paragraph_id": "P187", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[188]", "paragraph_id": "P188", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[195]", "paragraph_id": "P195", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay", "One actor plays roles of Initiating Party and Ultimate Debtor, Second Actor plays role of Debtor"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[196]", "paragraph_id": "P196", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay", "One actor plays roles of Initiating Party and Ultimate Debtor, Second Actor plays role of Debtor"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[197]", "paragraph_id": "P197", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay", "One actor plays roles of Initiating Party and Ultimate Debtor, Second Actor plays role of Debtor"]}]
participants: ["participant-src-000173-account-owner", "participant-src-000173-account-servicer", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-forwarding-agent", "participant-src-000173-head-office", "participant-src-000173-initiating-party", "participant-src-000173-subsidiary", "participant-src-000173-ultimate-debtor"]
message_mapping_evidence: []
message_ids: []
message_families: ["pacs.008", "pain.001", "pain.002"]
search_terms: ["One actor plays roles of Initiating Party and Ultimate Debtor, Second Actor plays role of Debtor", "Forwarding Agent", "Initiating Party", "Ultimate Debtor", "Debtor Agent", "Debtor"]
limitations: ["Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.", "P197 source example: head office initiates a payment using its foreign subsidiary account. Notifications/statements go to the depicted Debtor, distinct from initiating Ultimate Debtor.", "Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling."]
manual_curated: true
participant_ids: ["participant-src-000173-account-owner", "participant-src-000173-account-servicer", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-forwarding-agent", "participant-src-000173-head-office", "participant-src-000173-initiating-party", "participant-src-000173-subsidiary", "participant-src-000173-ultimate-debtor"]
related_diagrams: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/diagrams/initiation/fig-0018.md"]
issue_ids: ["issue-000044"]
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and rendered page context compared; tables retain independent review status."}
message_reference_scope: "Family/name-level Part1 flows; supplied exact definitions linked separately."
---



# One actor plays roles of Initiating Party and Ultimate Debtor, Second Actor plays role of Debtor

[src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Purpose and trigger

Relay a head-office initiation using a subsidiary debtor account.

P183 service agreements; P197 initiating party and ultimate debtor are head office, debtor is separate subsidiary.

## Participants and responsibilities

| Scoped participant | Participation evidence |
| --- | --- |
| [account owner](../../../../../../../shared/reference/participants/participant-src-000173-account-owner.md) | Narrative-only participant/example; omitted as a separate figure lifeline. |
| [account servicer](../../../../../../../shared/reference/participants/participant-src-000173-account-servicer.md) | Narrative-only participant/example; omitted as a separate figure lifeline. |
| [creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [creditor agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debtor](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debtor agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [forwarding agent](../../../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [head office](../../../../../../../shared/reference/participants/participant-src-000173-head-office.md) | Narrative-only participant/example; omitted as a separate figure lifeline. |
| [initiating party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | Source figure occurrence; exact action/message direction is shown below. |
| [subsidiary](../../../../../../../shared/reference/participants/participant-src-000173-subsidiary.md) | Narrative-only participant/example; omitted as a separate figure lifeline. |
| [ultimate debtor](../../../../../../../shared/reference/participants/participant-src-000173-ultimate-debtor.md) | Source figure occurrence; exact action/message direction is shown below. |


## Source-defined conditions and activities

**P180** The CustomerCreditTransferInitiation message is sent from the initiating party to the forwarding agent.

**P181** Depending on the service level agreed between the forwarding agent and the initiating party, the forwarding agent may send a CustomerPaymentStatusReport message to inform the initiating party of the status of the initiation.

**P182** After performing a series of checks, the forwarding agent will forward the CustomerCreditTransferInitiation message to the relevant debtor agent, that is, the agent that will debit the debtor account.

**P183** A relay scenario always requires service level agreements between all parties involved, in which obligations and responsibilities for each party are stipulated.

**P184** A number of additional message flows have been included to illustrate the complete end-to-end execution of the payment initiation. However, these messages are out of scope.

**P185** The below scenarios show the different customer roles that can be played on the initiating side of the credit transfer initiation, and on the receiving side of the cash transfer.

**P186** On the initiating side, up to three customer roles can be specified: the initiating party, that is., the party sending the message, the debtor, that is, the debit account owner, and the ultimate debtor, that is, the party that owes the cash to the creditor, as a result of receipt of goods or services.

**P187** These three roles can be played by one and the same actor, or they can be played by different actors. The CustomerCreditTransferInitiation message allows inclusion of the three different roles on the initiating side.

**P188** On the receiving side, up to two customer roles can be specified: the creditor, that is, the credit account owner, and the creditor, that is, the party that is the ultimate beneficiary of the cash transfer. These two roles can be played by one and the same actor, or they can be played by different actors. The CustomerCreditTransferInitiation message allows inclusion of the two different roles on the receiving side.

**P197** The message is sent by an initiating party to the forwarding agent. The actor playing the role of initiating party is the same as the actor playing the role of ultimate debtor, but the role of the debtor is played by a different actor. This illustrates the scenario in which, for example, a head office initiates the payment, but has agreed with its subsidiary abroad to use the account of the subsidiary for certain payments. After performing a series of checks, the forwarding agent will forward the message to the debtor agent.

### fig-0018

[Source reconstruction and review](../diagrams/initiation/fig-0018.md); direct-body paragraph P196; Word file page30.

| Step | Sender and roles | Receiver and roles | Literal exchange |
| --- | --- | --- | --- |
| 1 | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | [Ultimate Debtor (initiating party) / ultimate-debtor](../../../../../../../shared/reference/participants/participant-src-000173-ultimate-debtor.md); [Ultimate Debtor (initiating party) / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | Invoice |
| 2 | [Ultimate Debtor (initiating party) / ultimate-debtor](../../../../../../../shared/reference/participants/participant-src-000173-ultimate-debtor.md); [Ultimate Debtor (initiating party) / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | [Forwarding Agent / forwarding-agent](../../../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md) | CustomerCreditTransferInitiation |
| 3 | [Forwarding Agent / forwarding-agent](../../../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md) | [Ultimate Debtor (initiating party) / ultimate-debtor](../../../../../../../shared/reference/participants/participant-src-000173-ultimate-debtor.md); [Ultimate Debtor (initiating party) / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | CustomerPaymentStatusReport |
| 4 | [Forwarding Agent / forwarding-agent](../../../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md) | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | CustomerCreditTransferInitiation |
| 5 | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | [Forwarding Agent / forwarding-agent](../../../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md) | CustomerPaymentStatusReport |
| 6 | [Forwarding Agent / forwarding-agent](../../../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md) | [Ultimate Debtor (initiating party) / ultimate-debtor](../../../../../../../shared/reference/participants/participant-src-000173-ultimate-debtor.md); [Ultimate Debtor (initiating party) / initiating-party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | CustomerPaymentStatusReport |
| 7 | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | FIToFICustomerCreditTransfer |
| 8 | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | [Debtor / debtor](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md) | Notification |
| 9 | [Debtor Agent / debtor-agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | [Debtor / debtor](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md) | Statement |
| 10 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Notification |
| 11 | [Creditor Agent / creditor-agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | [Creditor / creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Statement |



## Outcomes, alternatives and related processes

Notification and statement arrows go directly to debtor in this source picture; status is returned to initiating ultimate debtor through forwarding agent.

- Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.
- P197 source example: head office initiates a payment using its foreign subsidiary account. Notifications/statements go to the depicted Debtor, distinct from initiating Ultimate Debtor.
- Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling.

## Supplied message definitions

| Family | Exact supplied reference | Scope |
| --- | --- | --- |
| pacs.008 | [pacs.008.001.14](../../../../messages/pacs.008.001.14/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pain.001 | [pain.001.001.13](../../../../messages/pain.001.001.13/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |
| pain.002 | [pain.002.001.15](../../../../messages/pain.002.001.15/index.md) | Name match for retrieval; no exact-version assertion from Part1 diagram. |



## Review

Compared source narrative, picture labels/directions and complete figure page context on 2026-11-09. Unresolved source claims: issue-000044. This bounded flow evidence has been reviewed; participant classification/schema/table references keep their own review status.
