---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
participant_id: "participant-src-000173-clearing-system"
title: "Clearing System"
source_labels: ["Clearing System"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[3]", "paragraph_id": null, "table_id": "T7"}]
flows: []
process_sections: ["flow-src-000173-p198-customer-direct-debit-initiation-and-fito-ficustomer-direct-debit"]
message_ids: []
message_families: ["pain.008"]
search_terms: ["Clearing System", "pain.008"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# Clearing System

Business context: Payments Initiation. Source classification: business role.

## Definition

Specifies the system which plays a role in the clearing process.

Evidence: [T7](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/documents/src-000173/tables/tbl-0007.md), source row 3.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [CustomerDirectDebitInitiation and FIToFICustomerDirectDebit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p198-customer-direct-debit-initiation-and-fito-ficustomer-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `pain.008`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Clearing System`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000173](../../../evidence/omitted/baf7abf3460122a33db6052d.md).
