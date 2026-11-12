---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_sets: ["bank-to-customer-cash-management"]
participant_id: "participant-src-000004-account-owner"
title: "Account Owner"
source_labels: ["Account Owner"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000004", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[3]", "paragraph_id": null, "table_id": "T6"}]
flows: ["flow-src-000004-p101-report", "flow-src-000004-p104-reconcile", "flow-src-000004-p107-report-on-payment-transaction", "flow-src-000004-p109-report-on-payment-transaction-status", "flow-src-000004-p115-cash-positioning", "flow-src-000004-p117-notification-to-account-owner", "flow-src-000004-p119-transaction-reconciliation-1", "flow-src-000004-p122-transaction-reconciliation-2", "flow-src-000004-p131-scenario-1", "flow-src-000004-p134-scenario-2", "flow-src-000004-p137-scenario-3", "flow-src-000004-p140-reporting-through-a-forwarding-agent", "flow-src-000004-p144-direct-scenario", "flow-src-000004-p149-relay-scenario"]
process_sections: ["flow-src-000004-p128-reporting", "flow-src-000004-p131-scenario-1", "flow-src-000004-p134-scenario-2", "flow-src-000004-p137-scenario-3", "flow-src-000004-p140-reporting-through-a-forwarding-agent", "flow-src-000004-p144-direct-scenario", "flow-src-000004-p149-relay-scenario"]
message_ids: ["camt.052.001.14", "camt.053.001.14", "camt.054.001.14", "camt.060.001.07"]
message_families: ["camt.052", "camt.053", "camt.054", "camt.060"]
search_terms: ["Account Owner", "camt.052", "camt.053", "camt.054", "camt.060"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---



























# Account Owner

Business context: Bank-to-Customer Cash Management. Source classification: functional participant role.

## Definition

Party that legally holds the account or the party in a contractual relationship with the servicer.

Evidence: [T6](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0006.md), source row 3.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [Creditor](participant-src-000004-creditor.md) | [T8](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0008.md) row 2, column 3 |
| Business role listed for this functional participant | [Debtor](participant-src-000004-debtor.md) | [T8](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0008.md) row 3, column 3 |
| Business role listed for this functional participant | [System Member](participant-src-000004-system-member.md) | [T8](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0008.md) row 7, column 3 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Reconcile](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p104-reconcile.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Notification to Account Owner](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p117-notification-to-account-owner.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transaction Reconciliation - 1](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p119-transaction-reconciliation-1.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transaction Reconciliation -2](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p122-transaction-reconciliation-2.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Reporting](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p128-reporting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Scenario 1](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p131-scenario-1.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Scenario 2](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p134-scenario-2.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Scenario 3](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p137-scenario-3.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Reporting through a Forwarding Agent](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p140-reporting-through-a-forwarding-agent.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Direct Scenario](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p144-direct-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Relay Scenario](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p149-relay-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `camt.052`, `camt.053`, `camt.054`, `camt.060`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Account Owner`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000004](../../../evidence/omitted/52f543e2b58f688bc16fa140.md).

Bank-to-customer source context: [Bank-to-customer roles and contextual generalisations](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0001.md). .

Bank-to-customer source context: [Reporting business-process actor overview](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0002.md). [flow Report](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p101-report.md), [flow Reconcile](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p104-reconcile.md), [flow Report on Payment Transaction](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p107-report-on-payment-transaction.md), [flow Report on Payment Transaction Status](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p109-report-on-payment-transaction-status.md).

Bank-to-customer source context: [Cash positioning across internal systems and account servicer](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0007.md). [flow Cash Positioning](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p115-cash-positioning.md).

Bank-to-customer source context: [Optional notifications to the account owner](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0008.md). [flow Notification to Account Owner](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p117-notification-to-account-owner.md).

Bank-to-customer source context: [Transaction reconciliation initiated by the account owner](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0009.md). [flow Transaction Reconciliation - 1](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p119-transaction-reconciliation-1.md).

Bank-to-customer source context: [Transaction reconciliation initiated by a counterparty](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0010.md). [flow Transaction Reconciliation -2](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p122-transaction-reconciliation-2.md).

Bank-to-customer source context: [Reporting scenario 1: intraday report then end-of-day statement](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0011.md). [flow Scenario 1](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p131-scenario-1.md).

Bank-to-customer source context: [Reporting scenario 2: credit threshold, intraday report and statement](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0012.md). [flow Scenario 2](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p134-scenario-2.md).

Bank-to-customer source context: [Reporting scenario 3: authorised recipient relays information](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0013.md). [flow Scenario 3](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p137-scenario-3.md).

Bank-to-customer source context: [Reporting through a forwarding agent](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0014.md). [flow Reporting through a Forwarding Agent](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p140-reporting-through-a-forwarding-agent.md).

Bank-to-customer source context: [Direct reporting request to the account servicer](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0015.md). [flow Direct Scenario](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p144-direct-scenario.md).

Bank-to-customer source context: [Relay reporting request and response](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0016.md). [flow Relay Scenario](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p149-relay-scenario.md).
