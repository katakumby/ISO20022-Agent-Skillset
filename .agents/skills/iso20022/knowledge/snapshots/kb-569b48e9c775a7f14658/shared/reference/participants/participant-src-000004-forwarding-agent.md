---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_sets: ["bank-to-customer-cash-management"]
participant_id: "participant-src-000004-forwarding-agent"
title: "Forwarding Agent"
source_labels: ["Forwarding Agent"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000004", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[5]", "paragraph_id": null, "table_id": "T6"}]
flows: ["flow-src-000004-p101-report", "flow-src-000004-p104-reconcile", "flow-src-000004-p107-report-on-payment-transaction", "flow-src-000004-p109-report-on-payment-transaction-status", "flow-src-000004-p140-reporting-through-a-forwarding-agent", "flow-src-000004-p149-relay-scenario"]
process_sections: ["flow-src-000004-p140-reporting-through-a-forwarding-agent", "flow-src-000004-p149-relay-scenario"]
message_ids: ["camt.052.001.14", "camt.053.001.14", "camt.054.001.14", "camt.060.001.07"]
message_families: ["camt.060"]
search_terms: ["Forwarding Agent", "camt.060"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---











# Forwarding Agent

Business context: Bank-to-Customer Cash Management. Source classification: functional participant role.

## Definition

Financial institution that receives the instruction from the initiating party and forwards it to the next agent in the payment chain for execution

Evidence: [T6](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0006.md), source row 5.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Report on Payment Transaction Status](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p109-report-on-payment-transaction-status.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Reporting through a Forwarding Agent](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p140-reporting-through-a-forwarding-agent.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Relay Scenario](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p149-relay-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `camt.060`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Forwarding Agent`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000004](../../../evidence/omitted/52f543e2b58f688bc16fa140.md).

Bank-to-customer source context: [Bank-to-customer roles and contextual generalisations](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0001.md). .

Bank-to-customer source context: [Reporting business-process actor overview](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0002.md). [flow Report](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p101-report.md), [flow Reconcile](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p104-reconcile.md), [flow Report on Payment Transaction](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p107-report-on-payment-transaction.md), [flow Report on Payment Transaction Status](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p109-report-on-payment-transaction-status.md).

Bank-to-customer source context: [Reporting through a forwarding agent](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0014.md). [flow Reporting through a Forwarding Agent](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p140-reporting-through-a-forwarding-agent.md).

Bank-to-customer source context: [Relay reporting request and response](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0016.md). [flow Relay Scenario](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p149-relay-scenario.md).
