---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p256-customer-payment-status-report-message-to-the-creditor"
title: "CustomerPaymentStatusReport message to the Creditor"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "CustomerPaymentStatusReport message to the Creditor "], "locator": "/w:document/w:body/w:p[256]", "paragraph_id": "P256", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "CustomerPaymentStatusReport message to the Creditor "], "locator": "/w:document/w:body/w:p[257]", "paragraph_id": "P257", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "CustomerPaymentStatusReport message to the Creditor "], "locator": "/w:document/w:body/w:p[258]", "paragraph_id": "P258", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "CustomerPaymentStatusReport message to the Creditor "], "locator": "/w:document/w:body/w:p[259]", "paragraph_id": "P259", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "Negative Customer and FIToFIPaymentStatusReport with Direct Debit", "CustomerPaymentStatusReport message to the Creditor "], "locator": "/w:document/w:body/w:p[260]", "paragraph_id": "P260", "table_id": null}]
participants: ["participant-src-000173-creditor-agent", "participant-src-000173-debtor-agent", "participant-src-000173-creditor"]
message_mapping_evidence: [{"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["pain.002", "pain.008"]
search_terms: ["CustomerPaymentStatusReport message to the Creditor", "Creditor Agent", "Debtor Agent", "Creditor", "pain.002", "pain.008"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---



# CustomerPaymentStatusReport message to the Creditor

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Creditor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Creditor | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P257** The creditor agent sends an FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

**P258** The clearing and settlement agent confirms the processability of the FIToFICustomerDirectDebit message by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

**P259** The clearing and settlement agent sends an FIToFICustomerDirectDebit message, optionally with the Mandate Related Reference (MRI), to the debtor agent immediately for information purposes only.

**P260** If settlement has not yet taken place, the debtor agent may send a negative FIToFIPaymentStatusReport message to the clearing and settlement agent, to inform him about the rejection of the FIToFICustomerDirectDebitinstruction. This negative FIToFIPaymentStatusReport message may subsequently be forwarded to the creditor agent. The creditor agent may inform (but not necessarily) his customer, the creditor, about the negative processing of the CustomerDirectDebitInitiation instruction by using a CustomerPaymentStatusReport message, a BankToCustomerDebitCreditNotification message ('notification') or through a BankToCustomerAccountReport and/or BankToCustomerStatement message ('statement').

## Messages and alternative paths

Source-supported message family mentions: `pain.002`, `pain.008`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Heading path: BusinessTransactions / Negative Customer and FIToFIPaymentStatusReport with Direct Debit / CustomerPaymentStatusReport message to the Creditor .

<!-- INITIATION-CONTEXT -->
[Reviewed full flow context, literal directions, participants and source qualifications](flow-src-000173-p249-negative-fito-fipayment-status-report-debtor-agent.md)
<!-- /INITIATION-CONTEXT -->
