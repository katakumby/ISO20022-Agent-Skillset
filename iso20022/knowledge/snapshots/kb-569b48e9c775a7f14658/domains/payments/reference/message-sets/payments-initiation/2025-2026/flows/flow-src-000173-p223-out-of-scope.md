---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p223-out-of-scope"
title: "Out of scope"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerDirectDebitInitiation and FIToFICustomerDirectDebit "], "locator": "/w:document/w:body/w:p[223]", "paragraph_id": "P223", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerDirectDebitInitiation and FIToFICustomerDirectDebit "], "locator": "/w:document/w:body/w:p[224]", "paragraph_id": "P224", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerDirectDebitInitiation and FIToFICustomerDirectDebit "], "locator": "/w:document/w:body/w:p[225]", "paragraph_id": "P225", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerDirectDebitInitiation and FIToFICustomerDirectDebit "], "locator": "/w:document/w:body/w:p[226]", "paragraph_id": "P226", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerDirectDebitInitiation and FIToFICustomerDirectDebit "], "locator": "/w:document/w:body/w:p[227]", "paragraph_id": "P227", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerDirectDebitInitiation and FIToFICustomerDirectDebit "], "locator": "/w:document/w:body/w:p[228]", "paragraph_id": "P228", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerDirectDebitInitiation and FIToFICustomerDirectDebit "], "locator": "/w:document/w:body/w:p[229]", "paragraph_id": "P229", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerDirectDebitInitiation and FIToFICustomerDirectDebit "], "locator": "/w:document/w:body/w:p[230]", "paragraph_id": "P230", "table_id": null}]
participants: ["participant-src-000173-creditor-agent", "participant-src-000173-debtor-agent", "participant-src-000173-debtor", "participant-src-000173-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Out of scope", "Creditor Agent", "Debtor Agent", "Debtor", "Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---



# Out of scope

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Creditor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P224** Optionally, the debtor agent could forward the direct debit instruction (simplified version) to the debtor (for example, if pre-notifications are not used in a scheme).

**P225** If the clearing and settlement agent are two parties the clearing agent prepares and sends the payment information for the settlement agent (in accordance with the agreed and published settlement cycle). The process includes the calculation of the settlement positions and transmission of the files to the Settlement Agent.

**P226** The information provided includes the net position to be debited, the party to be debited, the net position to be credited, the party to be credited and the value date.

**P227** The clearing agent prepares and sends the payment information for the settlement agent (in accordance with the agreed and published settlement cycle). The process includes the calculation of the settlement positions and transmission of the files to the settlement agent.

**P228** The information provided includes the net position to be debited, the party to be debited, the net position to be credited, the party to be credited and the value date.

**P229** The settlement is executed by the settlement agent, in accordance with the settlement cycle, based on the settlement report provided by the clearing agent. The settlement agent performs the transfer of funds from the debtor agent to the creditor agent.

**P230** Reporting (BankToCustomerDebitCreditNotification message ('notification') and/or BankToCustomerAccountReport/ BankToCustomerStatement message ('statement')) to the debtors and creditors is out of scope. Timing may vary depending on market practices and value added services provided by some agents, that is, before or after settlement.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Heading path: BusinessTransactions / CustomerDirectDebitInitiation and FIToFICustomerDirectDebit .

<!-- INITIATION-CONTEXT -->
[Reviewed full flow context, literal directions, participants and source qualifications](flow-src-000173-p198-customer-direct-debit-initiation-and-fito-ficustomer-direct-debit.md)
<!-- /INITIATION-CONTEXT -->
