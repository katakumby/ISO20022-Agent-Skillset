---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
participant_id: "participant-src-000173-debtor-agent-forwarding-agent"
title: "Debtor Agent / Forwarding Agent"
source_labels: ["Debtor Agent / Forwarding Agent"]
role_type: "activity participant; classification not established"
aliases: []
source_locations: [{"source_id": "src-000173", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"], "locator": "/w:document/w:body/w:tbl[23]/w:tr[6]", "paragraph_id": null, "table_id": "T23"}, {"source_id": "src-000173", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"], "locator": "/w:document/w:body/w:tbl[23]/w:tr[9]", "paragraph_id": null, "table_id": "T23"}, {"source_id": "src-000173", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"], "locator": "/w:document/w:body/w:tbl[23]/w:tr[13]", "paragraph_id": null, "table_id": "T23"}]
flows: ["flow-src-000173-p118-accept-customer-to-bank-payment", "flow-src-000173-p140-complex-scenario"]
process_sections: []
message_ids: []
message_families: []
search_terms: ["Debtor Agent / Forwarding Agent"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# Debtor Agent / Forwarding Agent

Business context: Payments Initiation. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Confirm acceptance (5.1) and send (5.2), receive and/or forward (5.3) acceptance acknowledgement. | This acceptance acknowledgement signifies that the payment order (subject to prior information received through the various payment status reports) will be processed by the debtor agent and will trigger accounting entries on the debtor/initiating party account maintained at the debtor agent. | Initiator | [T23](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/documents/src-000173/tables/tbl-0023.md) row 6 |
| Send, receive and/or forward debit advice (7.1) | The debit advice, prepared by the debtor agent, notifies the initiating party that the settlement has been performed, that is, that the debit entry has been passed on the account of the debtor/initiating party. The initiating party uses it for the reconciliation of entries vis-à-vis payment orders received/remitted.<br>The initiating party receives a notification from the debtor agent, (possibly through the forwarding agent - if any), that the debit entry has been passed on the account of the debtor (which may or may not be equal to the initiating party).<br>This debit advice will be further used for the reconciliation of entries vis-à-vis payment orders received/remitted. <br>The forwarding agent forwards to the initiating party a notification received from the debtor agent that the debit entry has been passed on the account of the debtor/initiating party.<br>This debit advice will be further used by the initiating party for the reconciliation of entries vis-à-vis payment orders received/remitted. | Initiator | [T23](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/documents/src-000173/tables/tbl-0023.md) row 9 |
| Send (11) / receive and forward (11.1) execution status | The initiating party optionally receives an execution status report from the debtor agent (possibly through the forwarding agent - if any). <br>The forwarding agent forwards to the initiating party a notification received from the debtor agent that the payment order file has been executed. Depending on the payment method requested and depending on the routing information contained in the payment order:<br>the creditor(s) has/have been credited in the books of the debtor agent (for 'on-us' payments)<br>the debtor agent has printed and sent cheques<br>the debtor agent has sent off the payment orders which need to be further routed in the payment chain (for 'not on-us' payments)<br>If the creditor has an account in the books of the debtor agent (which is same as creditor agent then), this execution status is a 'final' execution status (that is, the creditor has been credited by his agent). In the other cases ('receive cheques'/and when the creditor has an account at a different agent than the debtor agent), the execution status is not yet 'final' - that is, the execution status does not include the actual confirmation of credit of the creditor by his agent - or cashing of cheque by the beneficiary. | Initiator | [T23](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/documents/src-000173/tables/tbl-0023.md) row 13 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Accept Customer-to-Bank Payment](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p118-accept-customer-to-bank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Complex scenario:](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p140-complex-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Debtor Agent / Forwarding Agent`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000173](../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx).
