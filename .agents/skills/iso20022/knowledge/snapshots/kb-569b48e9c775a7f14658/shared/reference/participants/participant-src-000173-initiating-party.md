---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
participant_id: "participant-src-000173-initiating-party"
title: "Initiating Party"
source_labels: ["Initiating Party"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[9]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000173", "locator": "T6 row9; T9–T10; T23; P156; P165–178; P180–197; P202"}, {"source_id": "src-000173", "locator": "T8 row9"}]
flows: ["flow-src-000173-p116-order-customer-to-bank-payment", "flow-src-000173-p117-authorise-customer-to-bank-payment", "flow-src-000173-p119-check-authorisation-customer-to-bank-payment", "flow-src-000173-p128-initiate-collection-of-direct-debit", "flow-src-000173-p140-complex-scenario"]
process_sections: ["flow-src-000173-p155-customer-credit-transfer-initiation", "flow-src-000173-p158-account-information-from-debtor-agent-to-initiating-party", "flow-src-000173-p162-account-information-from-creditor-agent-to-creditor", "flow-src-000173-p170-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor-s", "flow-src-000173-p173-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play", "flow-src-000173-p176-three-different-actors-play-the-roles-of-initiating-party-debtor-and-u", "flow-src-000173-p179-customer-credit-transfer-initiation-relay", "flow-src-000173-p189-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor", "flow-src-000173-p192-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play", "flow-src-000173-p195-one-actor-plays-roles-of-initiating-party-and-ultimate-debtor-second-a", "flow-src-000173-p198-customer-direct-debit-initiation-and-fito-ficustomer-direct-debit"]
message_ids: []
message_families: ["pain.001", "pain.002", "pain.008"]
search_terms: ["Initiating Party", "pain.001", "pain.002", "pain.008"]
limitations: ["Scoped to supplied Payments Initiation source. Terminology conflict remains issue-000044.", "No cross-source equivalence or fixed institution/functional-role identity is inferred."]
issue_ids: ["issue-000044"]
manual_curated: true
definition_review: {"date": "2026-11-09", "result": "pass", "scope": "T6 definition/T8 mapping and cited narrative reviewed; classification ambiguity remains."}
flow_ids: ["flow-src-000173-p107-customer-to-bank-payment-order", "flow-src-000173-p125-customer-to-bank-direct-debit", "flow-src-000173-p136-customer-to-bank-payment-order", "flow-src-000173-p140-complex-scenario", "flow-src-000173-p170-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor-s", "flow-src-000173-p173-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play", "flow-src-000173-p176-three-different-actors-play-the-roles-of-initiating-party-debtor-and-u", "flow-src-000173-p189-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor", "flow-src-000173-p192-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play", "flow-src-000173-p195-one-actor-plays-roles-of-initiating-party-and-ultimate-debtor-second-a", "flow-src-000173-p198-customer-direct-debit-initiation-and-fito-ficustomer-direct-debit", "flow-src-000173-p234-negative-customer-payment-status-report-creditor-agent", "flow-src-000173-p239-negative-customer-payment-status-report-clearing-and-settlement-agent", "flow-src-000173-p249-negative-fito-fipayment-status-report-debtor-agent", "flow-src-000173-p266-confirmation-of-processability-of-customer-direct-debit-initiation", "flow-src-000173-p280-payment-return-initiated-by-debtor-agent", "flow-src-000173-p298-customer-payment-reversal-with-direct-debit"]
---







































































# Initiating Party

Business context: Payments Initiation. Source classification: functional participant role.

## Definition

Party initiating the payment to an agent. In the payment context, this can either be the debtor (in a credit transfer), the creditor (in a direct debit), or a party that initiates the payment on behalf of the debtor or creditor. 

Evidence: [T6](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/documents/src-000173/tables/tbl-0006.md), source row 9.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Order Customer-to-bank payment](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p116-order-customer-to-bank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Authorise Customer-to-Bank Payment](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p117-authorise-customer-to-bank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Check Authorisation Customer-to-Bank Payment](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p119-check-authorisation-customer-to-bank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Initiate Collection of Direct Debit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p128-initiate-collection-of-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Complex scenario:](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p140-complex-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [CustomerCreditTransferInitiation](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p155-customer-credit-transfer-initiation.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Account information from debtor agent to initiating party](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p158-account-information-from-debtor-agent-to-initiating-party.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Account information from creditor agent to creditor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p162-account-information-from-creditor-agent-to-creditor.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [One Actor plays roles of Initiating Party, Debtor and Ultimate Debtor, Second actor plays roles of Creditor and Ultimate Creditor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p170-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor-s.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [One actor plays roles of Initiating Party and Debtor, second actor plays role of Ultimate Debtor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p173-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Three Different actors play the roles of Initiating Party, Debtor and Ultimate Debtor:](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p176-three-different-actors-play-the-roles-of-initiating-party-debtor-and-u.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [CustomerCreditTransferInitiation - Relay](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p179-customer-credit-transfer-initiation-relay.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [One actor plays roles of Initiating Party, Debtor and Ultimate Debtor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p189-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [One actor plays roles of Initiating Party and Debtor, Second Actor plays role of Ultimate Debtor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p192-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [One actor plays roles of Initiating Party and Ultimate Debtor, Second Actor plays role of Debtor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p195-one-actor-plays-roles-of-initiating-party-and-ultimate-debtor-second-a.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [CustomerDirectDebitInitiation and FIToFICustomerDirectDebit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p198-customer-direct-debit-initiation-and-fito-ficustomer-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `pain.001`, `pain.002`, `pain.008`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Initiating Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000173](../../../evidence/omitted/baf7abf3460122a33db6052d.md).

<!-- INITIATION-ROLE-REVIEW -->
## Curated responsibilities and role relationships

Creates/authorises the initiation and sends it to agent; may be debtor for a credit transfer, creditor for a direct debit, or another party acting on their behalf. (T6 row9; T9–T10; T23; P156; P165–178; P180–197; P202)

T8 row9 marks the participant under: BusinessRole / Party. This source mapping does not make the functional participant identical to a particular institution.

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

<!-- INITIATION-FLOW-170 -->
[One Actor plays roles of Initiating Party, Debtor and Ultimate Debtor, Second actor plays roles of Creditor and Ultimate Creditor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p170-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor-s.md)
<!-- /INITIATION-FLOW-170 -->

<!-- INITIATION-FLOW-173 -->
[One actor plays roles of Initiating Party and Debtor, second actor plays role of Ultimate Debtor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p173-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play.md)
<!-- /INITIATION-FLOW-173 -->

<!-- INITIATION-FLOW-176 -->
[Three Different actors play the roles of Initiating Party, Debtor and Ultimate Debtor:](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p176-three-different-actors-play-the-roles-of-initiating-party-debtor-and-u.md)
<!-- /INITIATION-FLOW-176 -->

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

<!-- INITIATION-FLOW-234 -->
[Negative CustomerPaymentStatusReport - Creditor Agent](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p234-negative-customer-payment-status-report-creditor-agent.md)
<!-- /INITIATION-FLOW-234 -->

<!-- INITIATION-FLOW-239 -->
[Negative CustomerPaymentStatusReport - Clearing And Settlement Agent](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p239-negative-customer-payment-status-report-clearing-and-settlement-agent.md)
<!-- /INITIATION-FLOW-239 -->

<!-- INITIATION-FLOW-249 -->
[Negative FIToFIPaymentStatusReport - Debtor Agent](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p249-negative-fito-fipayment-status-report-debtor-agent.md)
<!-- /INITIATION-FLOW-249 -->

<!-- INITIATION-FLOW-266 -->
[Confirmation of Processability of CustomerDirectDebitInitiation](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p266-confirmation-of-processability-of-customer-direct-debit-initiation.md)
<!-- /INITIATION-FLOW-266 -->

<!-- INITIATION-FLOW-280 -->
[PaymentReturn Initiated by Debtor Agent](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p280-payment-return-initiated-by-debtor-agent.md)
<!-- /INITIATION-FLOW-280 -->

<!-- INITIATION-FLOW-298 -->
[Customer Payment Reversal with Direct Debit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p298-customer-payment-reversal-with-direct-debit.md)
<!-- /INITIATION-FLOW-298 -->
