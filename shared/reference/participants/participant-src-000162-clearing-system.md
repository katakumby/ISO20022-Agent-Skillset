---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
participant_id: "participant-src-000162-clearing-system"
title: "Clearing System"
source_labels: ["Clearing System"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[3]", "paragraph_id": null, "table_id": "T7"}]
flows: ["flow-src-000162-p118-clear-interbank-payment", "flow-src-000162-p127-process-direct-debit", "flow-src-000162-p154-direct-debit-instruction"]
process_sections: ["flow-src-000162-p186-debtor-agent-and-creditor-agent-are-not-correspondents-1", "flow-src-000162-p214-debtor-agent-and-creditor-agent-are-direct-correspondents", "flow-src-000162-p221-debtor-agent-and-creditor-agent-are-not-correspondents-1", "flow-src-000162-p249-debtor-agent-and-the-creditor-agent-are-correspondents", "flow-src-000162-p260-debtor-agent-and-creditor-agent-are-not-correspondents-1", "flow-src-000162-p409-debtor-and-creditor-are-direct-correspondents", "flow-src-000162-p420-debtor-agent-and-creditor-are-correspondents", "flow-src-000162-p433-debtor-agent-and-creditor-agent-are-correspondents", "flow-src-000162-p445-debtor-agent-and-creditor-agent-are-not-correspondents", "flow-src-000162-p468-fito-ficustomer-direct-debit"]
message_ids: []
message_families: ["pacs.002", "pacs.003", "pacs.004", "pacs.008", "pacs.009", "pacs.010"]
search_terms: ["Clearing System", "pacs.002", "pacs.003", "pacs.004", "pacs.008", "pacs.009", "pacs.010"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000162-p111-credit-transfer", "flow-src-000162-p124-direct-debit"]
---











# Clearing System

Business context: Payments Clearing and Settlement. Source classification: business role.

## Definition

Specifies the system which plays a role in the clearing process.

Evidence: [T7](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0007.md), source row 3.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [Debtor agent](participant-src-000162-debtor-agent.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 6, column 3 |
| Business role listed for this functional participant | [Creditor Agent](participant-src-000162-creditor-agent.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 7, column 3 |
| Business role listed for this functional participant | [Forwarding Agent](participant-src-000162-forwarding-agent.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 8, column 3 |
| Business role listed for this functional participant | [Account Servicer](participant-src-000162-account-servicer.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 11, column 3 |
| Business role listed for this functional participant | [Payment Clearing Agent](participant-src-000162-payment-clearing-agent.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 12, column 3 |
| Business role listed for this functional participant | [PaymentSettlementAgent](participant-src-000162-payment-settlement-agent.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 13, column 3 |
| Business role listed for this functional participant | [Intermediary Agent](participant-src-000162-intermediary-agent.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 14, column 3 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Clear Interbank Payment](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p118-clear-interbank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Process direct debit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p127-process-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Direct debit instruction](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p154-direct-debit-instruction.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are not Correspondents - 1](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p186-debtor-agent-and-creditor-agent-are-not-correspondents-1.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are Direct Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p214-debtor-agent-and-creditor-agent-are-direct-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are not Correspondents - 1](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p221-debtor-agent-and-creditor-agent-are-not-correspondents-1.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and the Creditor Agent are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p249-debtor-agent-and-the-creditor-agent-are-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are not Correspondents - 1](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p260-debtor-agent-and-creditor-agent-are-not-correspondents-1.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor and Creditor are direct Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p409-debtor-and-creditor-are-direct-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p420-debtor-agent-and-creditor-are-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p433-debtor-agent-and-creditor-agent-are-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are Not Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p445-debtor-agent-and-creditor-agent-are-not-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [FIToFICustomerDirectDebit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p468-fito-ficustomer-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `pacs.002`, `pacs.003`, `pacs.004`, `pacs.008`, `pacs.009`, `pacs.010`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Clearing System`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000162](../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx).

<!-- CLEARING-FLOW-111 -->
[Credit Transfer](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p111-credit-transfer.md)
<!-- /CLEARING-FLOW-111 -->

<!-- CLEARING-FLOW-124 -->
[Direct Debit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p124-direct-debit.md)
<!-- /CLEARING-FLOW-124 -->

## Supplied named examples of contextual responsibilities

The following source-example flows show roles in their particular account or payment relationships. Named participants remain separate from this reusable functional role.

- [Source example flow8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-08.md)
- [Source example flow12](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-12.md)
- [Source example flow16](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-16.md)
