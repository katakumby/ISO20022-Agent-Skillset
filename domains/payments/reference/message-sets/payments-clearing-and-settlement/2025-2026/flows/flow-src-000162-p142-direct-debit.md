---
template: false
document_kind: "flow-context"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p142-direct-debit"
title: "Direct Debit"
source_locations: [{"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Direct Debit"], "locator": "/w:document/w:body/w:p[142]", "paragraph_id": "P142", "table_id": null}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Direct Debit"], "locator": "/w:document/w:body/w:p[143]", "paragraph_id": "P143", "table_id": null}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Direct Debit"], "locator": "/w:document/w:body/w:p[144]", "paragraph_id": "P144", "table_id": null}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Direct Debit"], "locator": "/w:document/w:body/w:p[145]", "paragraph_id": "P145", "table_id": null}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Direct Debit"], "locator": "/w:document/w:body/w:p[146]", "paragraph_id": "P146", "table_id": null}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Direct Debit"], "locator": "/w:document/w:body/w:p[147]", "paragraph_id": "P147", "table_id": null}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Direct Debit"], "locator": "/w:document/w:body/w:p[148]", "paragraph_id": "P148", "table_id": null}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Direct Debit"], "locator": "/w:document/w:body/w:p[149]", "paragraph_id": "P149", "table_id": null}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Direct Debit"], "locator": "/w:document/w:body/w:p[150]", "paragraph_id": "P150", "table_id": null}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Direct Debit"], "locator": "/w:document/w:body/w:p[151]", "paragraph_id": "P151", "table_id": null}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Direct Debit"], "locator": "/w:document/w:body/w:p[152]", "paragraph_id": "P152", "table_id": null}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Direct Debit"], "locator": "/w:document/w:body/w:p[153]", "paragraph_id": "P153", "table_id": null}]
participants: ["participant-src-000162-creditor", "participant-src-000162-debtor"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Direct Debit", "Creditor", "Debtor"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "This source-delimited heading/context is not an additional independent flow. Follow linked canonical flows for ordered responsibilities and message directions."]
manual_curated: true
issue_ids: []
related_flows: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p154-direct-debit-instruction.md", "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p157-return-direct-debit.md", "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p159-request-refund-direct-debit.md", "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p161-direct-debit-reversal.md"]
context_review_date: "2026-11-09"
---



# Direct Debit

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Creditor | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P143** Some base definitions of direct debit terms:

**P144** Direct Debit: Direct Debit(s) results in cash transfers between debtors and creditors through infrastructures or correspondent banks. They may be exchanged as single instructions but are traditionally grouped following some common characteristics and, for convenience or efficiency reasons, exchanged in a batch mode.

**P145** Mandate: This is the authorisation / expression of consent given by the Debtor allowing a specified creditor to originate Direct Debit instructions for debiting the specified Debtor’s account in accordance with the relevant Direct Debit scheme rules and, if applicable,  the mandate details.

**P146** Reject: Rejects are individual debits or files of debits that are rejected due to technical reasons, e.g. invalid format, wrong IBAN check digit. Rejects take place prior to interbank settlement if the creditor’s agent, the debtor’s agent or any other agent in the chain is not able to process the individual debit or files of debits.

**P147** Request for Cancellation: A request by the creditor to cancel a Direct Debit instruction prior to the interbank settlement

**P148** Revocation: A request by the creditor to revoke a Direct Debit Payment order prior to the acceptance by the creditor’s Agent.

**P149** Reversal: The creditor initiates a reversal instruction after settlement, when a paid Direct Debit should not have been processed. Consequently, the debtor will be credited back.

**P150** Refusal by the Debtor: One of the Debtor’s right to refuse either any Direct Debit transaction to be debited on its account, or one Direct Debit, once pre-noticed by a creditor.

**P151** Return: Returns are individual debits that have reached the Debtor’s Agent and have been settled at the interbank level, but the Debtor’s Agent is then unable to make the collection for one of a number of reasons e.g. account closed, no funds, customer dead, account does not accept Direct Debit, etc.

**P152** Refund: Refund is the process to claim for reimbursement of a Direct Debit for any reason after settlement and within a defined period ("n" days). A refund instruction is initiated by the Debtor.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Heading path: Description of BusinessActivities / Direct Debit.

## Reviewed flow context

The source-delimited content above was checked with its complete process narrative, original picture and Word figure context. It is a contextual section, not a separate message exchange.

- [Direct debit instruction](flow-src-000162-p154-direct-debit-instruction.md)
- [Return Direct Debit](flow-src-000162-p157-return-direct-debit.md)
- [Request Refund Direct Debit](flow-src-000162-p159-request-refund-direct-debit.md)
- [Direct Debit Reversal](flow-src-000162-p161-direct-debit-reversal.md)
