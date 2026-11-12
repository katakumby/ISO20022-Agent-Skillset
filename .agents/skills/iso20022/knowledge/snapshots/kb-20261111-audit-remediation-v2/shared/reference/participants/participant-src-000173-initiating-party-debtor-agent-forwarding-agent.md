---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
participant_id: "participant-src-000173-initiating-party-debtor-agent-forwarding-agent"
title: "Initiating Party/ Debtor Agent / Forwarding Agent"
source_labels: ["Initiating Party/ Debtor Agent / Forwarding Agent"]
role_type: "activity participant; classification not established"
aliases: []
source_locations: [{"source_id": "src-000173", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"], "locator": "/w:document/w:body/w:tbl[23]/w:tr[5]", "paragraph_id": null, "table_id": "T23"}]
flows: ["flow-src-000173-p140-complex-scenario"]
process_sections: []
message_ids: []
message_families: []
search_terms: ["Initiating Party/ Debtor Agent / Forwarding Agent"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# Initiating Party/ Debtor Agent / Forwarding Agent

Business context: Payments Initiation. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Receive (and forward) status report (4) | The initiating party can receive from the forwarding and/or debtor agent different status reports for the payment order.<br>The payment status report can be produced at different stages of the processing and may have a different business value (depending on the checks performed, for example, payment authentication, syntax validation, risk assessment.). <br>In the case of a relay scenario, there may be a duplication of payment status reports when, for example, a first risk analysis report is produced by the agent acting as a forwarding agent and a second risk analysis report be produced by the debtor agent (acting as the executing agent in that case). A payment status report can only cover the rejected items for a given payment order group or encompass both positive and negative, that is, rejections, acknowledgement for the items in the payment order group. It may optionally report on pre-agreed repair action taken by the bank.<br>At any stage, the payment status report expresses whether the payment order is accepted for further processing (that is, valid from a syntax, business content, risk analysis point of view) or rejected and the reason for rejection or whether the payment has been repaired and how. <br>Depending on the agreement between the initiating party and the debtor agent (or forwarding agent in relay scenario), the payment orders may be rejected as a whole or partially. The rejection criteria can be fixed as a percentage or an absolute number of individual rejected orders or other agreed criteria.<br>Consequently, if all the payment orders are rejected, a global status can be returned with the global reason. <br>In the case of a relay scenario, where the debtor agent generates the status report, it will first be the forwarding agent that receives the status report. The forwarding agent will then forward the status report to the initiating party.<br>'Send negative status report' and 'Send positive status reports' are subsets of 'send status report'. A negative status report will only include rejected items; a positive status report will include accepted items and repaired items. A 'generic' status report can include a combination of negative and positive status reports.<br>When the initiating party receives a negative status report (containing rejected items), based on the negative status message (reject) from the first or forwarding agent, the initiating party analyses the reason for rejection, corrects the information causing this reject and reverses the payment: he removes the payment from remittance in transit and resets the underlying invoices to payable again. | Initiator | [T23](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/documents/src-000173/tables/tbl-0023.md) row 5 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Complex scenario:](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p140-complex-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Initiating Party/ Debtor Agent / Forwarding Agent`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000173](../../../evidence/omitted/baf7abf3460122a33db6052d.md).
