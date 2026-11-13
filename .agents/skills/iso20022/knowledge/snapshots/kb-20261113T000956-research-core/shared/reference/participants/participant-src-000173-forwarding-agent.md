---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
participant_id: "participant-src-000173-forwarding-agent"
title: "Forwarding Agent"
source_labels: ["Forwarding Agent"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[8]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000173", "locator": "T6 row8; T23; P180–194; figures9/16–18"}, {"source_id": "src-000173", "locator": "T8 row8"}]
flows: ["flow-src-000173-p116-order-customer-to-bank-payment", "flow-src-000173-p119-check-authorisation-customer-to-bank-payment", "flow-src-000173-p120-validate-customer-to-bank-payment", "flow-src-000173-p140-complex-scenario"]
process_sections: ["flow-src-000173-p179-customer-credit-transfer-initiation-relay", "flow-src-000173-p189-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor", "flow-src-000173-p192-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play", "flow-src-000173-p195-one-actor-plays-roles-of-initiating-party-and-ultimate-debtor-second-a", "flow-src-000173-p198-customer-direct-debit-initiation-and-fito-ficustomer-direct-debit"]
message_ids: []
message_families: ["pain.001", "pain.002", "pain.008"]
search_terms: ["Forwarding Agent", "pain.001", "pain.002", "pain.008"]
limitations: ["Scoped to supplied Payments Initiation source. Terminology conflict remains issue-000044.", "No cross-source equivalence or fixed institution/functional-role identity is inferred."]
issue_ids: ["issue-000044"]
manual_curated: true
definition_review: {"date": "2026-11-09", "result": "pass", "scope": "T6 definition/T8 mapping and cited narrative reviewed; classification ambiguity remains."}
flow_ids: ["flow-src-000173-p107-customer-to-bank-payment-order", "flow-src-000173-p125-customer-to-bank-direct-debit", "flow-src-000173-p136-customer-to-bank-payment-order", "flow-src-000173-p140-complex-scenario", "flow-src-000173-p189-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor", "flow-src-000173-p192-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play", "flow-src-000173-p195-one-actor-plays-roles-of-initiating-party-and-ultimate-debtor-second-a", "flow-src-000173-p198-customer-direct-debit-initiation-and-fito-ficustomer-direct-debit"]
---



































# Forwarding Agent

Business context: Payments Initiation. Source classification: functional participant role.

## Definition

Financial institution that receives the instruction from the initiating party and forwards it to the next agent in the payment chain for execution.

Evidence: [T6](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/documents/src-000173/tables/tbl-0006.md), source row 8.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Order Customer-to-bank payment](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p116-order-customer-to-bank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Check Authorisation Customer-to-Bank Payment](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p119-check-authorisation-customer-to-bank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Validate Customer-to-Bank-payment](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p120-validate-customer-to-bank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Complex scenario:](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p140-complex-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [CustomerCreditTransferInitiation - Relay](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p179-customer-credit-transfer-initiation-relay.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [One actor plays roles of Initiating Party, Debtor and Ultimate Debtor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p189-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [One actor plays roles of Initiating Party and Debtor, Second Actor plays role of Ultimate Debtor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p192-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [One actor plays roles of Initiating Party and Ultimate Debtor, Second Actor plays role of Debtor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p195-one-actor-plays-roles-of-initiating-party-and-ultimate-debtor-second-a.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [CustomerDirectDebitInitiation and FIToFICustomerDirectDebit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p198-customer-direct-debit-initiation-and-fito-ficustomer-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `pain.001`, `pain.002`, `pain.008`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Forwarding Agent`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000173](../../../evidence/omitted/baf7abf3460122a33db6052d.md).

<!-- INITIATION-ROLE-REVIEW -->
## Curated responsibilities and role relationships

Receives initiation, checks and forwards to execution agent. Relay requires service agreements among involved parties specifying obligations and responsibilities; status reporting depends on agreement. (T6 row8; T23; P180–194; figures9/16–18)

T8 row8 marks the participant under: BusinessRole / Financial Institution, BusinessRole / Clearing System. This source mapping does not make the functional participant identical to a particular institution.

T1 and P98–100 use BusinessRole/Participant terminology inconsistently (issue-000044). The literal T6 definitions and T8 mapping are preserved. No identifier scheme is asserted beyond a source requirement.
<!-- /INITIATION-ROLE-REVIEW -->

<!-- INITIATION-FLOW-107 -->
[Customer-to-Bank Payment Order](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p107-customer-to-bank-payment-order.md)
<!-- /INITIATION-FLOW-107 -->

<!-- INITIATION-FLOW-125 -->
[Customer-to-Bank Direct Debit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p125-customer-to-bank-direct-debit.md)
<!-- /INITIATION-FLOW-125 -->

<!-- INITIATION-FLOW-140 -->
[Complex scenario:](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p140-complex-scenario.md)
<!-- /INITIATION-FLOW-140 -->

<!-- INITIATION-FLOW-136 -->
[Customer to Bank Payment Order](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p136-customer-to-bank-payment-order.md)
<!-- /INITIATION-FLOW-136 -->

<!-- INITIATION-FLOW-189 -->
[One actor plays roles of Initiating Party, Debtor and Ultimate Debtor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p189-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor.md)
<!-- /INITIATION-FLOW-189 -->

<!-- INITIATION-FLOW-192 -->
[One actor plays roles of Initiating Party and Debtor, Second Actor plays role of Ultimate Debtor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p192-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play.md)
<!-- /INITIATION-FLOW-192 -->

<!-- INITIATION-FLOW-195 -->
[One actor plays roles of Initiating Party and Ultimate Debtor, Second Actor plays role of Debtor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p195-one-actor-plays-roles-of-initiating-party-and-ultimate-debtor-second-a.md)
<!-- /INITIATION-FLOW-195 -->

<!-- INITIATION-FLOW-198 -->
[CustomerDirectDebitInitiation and FIToFICustomerDirectDebit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p198-customer-direct-debit-initiation-and-fito-ficustomer-direct-debit.md)
<!-- /INITIATION-FLOW-198 -->
