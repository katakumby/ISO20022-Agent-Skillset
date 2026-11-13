---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_sets: ["bank-to-customer-cash-management"]
participant_id: "participant-src-000004-recipient"
title: "Recipient"
source_labels: ["Recipient"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000004", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[4]", "paragraph_id": null, "table_id": "T6"}]
flows: ["flow-src-000004-p137-scenario-3", "flow-src-000004-p140-reporting-through-a-forwarding-agent"]
process_sections: ["flow-src-000004-p128-reporting", "flow-src-000004-p137-scenario-3", "flow-src-000004-p140-reporting-through-a-forwarding-agent"]
message_ids: ["camt.052.001.14", "camt.053.001.14", "camt.054.001.14"]
message_families: []
search_terms: ["Recipient"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---









# Recipient

Business context: Bank-to-Customer Cash Management. Source classification: functional participant role.

## Definition

Party authorised by the account owner to receive information about movements on the account.

Evidence: [T6](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0006.md), source row 4.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Reporting](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p128-reporting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Scenario 3](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p137-scenario-3.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Reporting through a Forwarding Agent](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p140-reporting-through-a-forwarding-agent.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Recipient`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000004](../../../evidence/omitted/52f543e2b58f688bc16fa140.md).

Bank-to-customer source context: [Bank-to-customer roles and contextual generalisations](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0001.md). .

Bank-to-customer source context: [Reporting scenario 3: authorised recipient relays information](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0013.md). [flow Scenario 3](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p137-scenario-3.md).

Bank-to-customer source context: [Reporting through a forwarding agent](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0014.md). [flow Reporting through a Forwarding Agent](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p140-reporting-through-a-forwarding-agent.md).
