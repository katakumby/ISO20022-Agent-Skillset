---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p179-customer-credit-transfer-initiation-relay"
title: "CustomerCreditTransferInitiation - Relay"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay"], "locator": "/w:document/w:body/w:p[179]", "paragraph_id": "P179", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay"], "locator": "/w:document/w:body/w:p[180]", "paragraph_id": "P180", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay"], "locator": "/w:document/w:body/w:p[181]", "paragraph_id": "P181", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay"], "locator": "/w:document/w:body/w:p[182]", "paragraph_id": "P182", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay"], "locator": "/w:document/w:body/w:p[183]", "paragraph_id": "P183", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay"], "locator": "/w:document/w:body/w:p[184]", "paragraph_id": "P184", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay"], "locator": "/w:document/w:body/w:p[185]", "paragraph_id": "P185", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay"], "locator": "/w:document/w:body/w:p[186]", "paragraph_id": "P186", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay"], "locator": "/w:document/w:body/w:p[187]", "paragraph_id": "P187", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation - Relay"], "locator": "/w:document/w:body/w:p[188]", "paragraph_id": "P188", "table_id": null}]
participants: ["participant-src-000173-forwarding-agent", "participant-src-000173-initiating-party", "participant-src-000173-ultimate-debtor", "participant-src-000173-account-owner", "participant-src-000173-debtor-agent", "participant-src-000173-creditor", "participant-src-000173-debtor", "participant-src-000173-party"]
message_mapping_evidence: [{"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["pain.001", "pain.002"]
search_terms: ["CustomerCreditTransferInitiation - Relay", "Forwarding Agent", "Initiating Party", "Ultimate Debtor", "Account Owner", "Debtor Agent", "Creditor", "Debtor", "Party", "pain.001", "pain.002"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---



# CustomerCreditTransferInitiation - Relay

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Forwarding Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Initiating Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Ultimate Debtor | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-ultimate-debtor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Creditor | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P180** The CustomerCreditTransferInitiation message is sent from the initiating party to the forwarding agent.

**P181** Depending on the service level agreed between the forwarding agent and the initiating party, the forwarding agent may send a CustomerPaymentStatusReport message to inform the initiating party of the status of the initiation.

**P182** After performing a series of checks, the forwarding agent will forward the CustomerCreditTransferInitiation message to the relevant debtor agent, that is, the agent that will debit the debtor account.

**P183** A relay scenario always requires service level agreements between all parties involved, in which obligations and responsibilities for each party are stipulated.

**P184** A number of additional message flows have been included to illustrate the complete end-to-end execution of the payment initiation. However, these messages are out of scope.

**P185** The below scenarios show the different customer roles that can be played on the initiating side of the credit transfer initiation, and on the receiving side of the cash transfer.

**P186** On the initiating side, up to three customer roles can be specified: the initiating party, that is., the party sending the message, the debtor, that is, the debit account owner, and the ultimate debtor, that is, the party that owes the cash to the creditor, as a result of receipt of goods or services.

**P187** These three roles can be played by one and the same actor, or they can be played by different actors. The CustomerCreditTransferInitiation message allows inclusion of the three different roles on the initiating side.

**P188** On the receiving side, up to two customer roles can be specified: the creditor, that is, the credit account owner, and the creditor, that is, the party that is the ultimate beneficiary of the cash transfer. These two roles can be played by one and the same actor, or they can be played by different actors. The CustomerCreditTransferInitiation message allows inclusion of the two different roles on the receiving side.

## Messages and alternative paths

Source-supported message family mentions: `pain.001`, `pain.002`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Heading path: BusinessTransactions / CustomerCreditTransferInitiation - Relay.

<!-- INITIATION-CONTEXT -->
[Reviewed full flow context, literal directions, participants and source qualifications](flow-src-000173-p189-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor.md)
<!-- /INITIATION-CONTEXT -->
