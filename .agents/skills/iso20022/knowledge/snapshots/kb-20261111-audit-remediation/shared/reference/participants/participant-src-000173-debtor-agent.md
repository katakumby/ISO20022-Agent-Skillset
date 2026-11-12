---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
participant_id: "participant-src-000173-debtor-agent"
title: "Debtor Agent"
source_labels: ["Debtor Agent"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[6]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000173", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"], "locator": "/w:document/w:body/w:tbl[23]/w:tr[8]", "paragraph_id": null, "table_id": "T23"}, {"source_id": "src-000173", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"], "locator": "/w:document/w:body/w:tbl[23]/w:tr[12]", "paragraph_id": null, "table_id": "T23"}, {"source_id": "src-000173", "locator": "T6 row6; T23; P156–161; P182; P222; P260; P279–297; figures9–25"}, {"source_id": "src-000173", "locator": "T8 row6"}]
flows: ["flow-src-000173-p116-order-customer-to-bank-payment", "flow-src-000173-p117-authorise-customer-to-bank-payment", "flow-src-000173-p119-check-authorisation-customer-to-bank-payment", "flow-src-000173-p120-validate-customer-to-bank-payment", "flow-src-000173-p121-assess-customer-to-bank-payment-risk", "flow-src-000173-p122-generate-regulatory-reporting-information", "flow-src-000173-p123-clear-customer-to-bank-payment", "flow-src-000173-p124-settle-customer-to-bank-payment", "flow-src-000173-p140-complex-scenario"]
process_sections: ["flow-src-000173-p155-customer-credit-transfer-initiation", "flow-src-000173-p158-account-information-from-debtor-agent-to-initiating-party", "flow-src-000173-p160-interbank-clearing-and-settlement-between-debtor-agent-and-creditor-ag", "flow-src-000173-p170-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor-s", "flow-src-000173-p173-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play", "flow-src-000173-p176-three-different-actors-play-the-roles-of-initiating-party-debtor-and-u", "flow-src-000173-p179-customer-credit-transfer-initiation-relay", "flow-src-000173-p189-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor", "flow-src-000173-p192-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play", "flow-src-000173-p195-one-actor-plays-roles-of-initiating-party-and-ultimate-debtor-second-a", "flow-src-000173-p198-customer-direct-debit-initiation-and-fito-ficustomer-direct-debit", "flow-src-000173-p223-out-of-scope", "flow-src-000173-p249-negative-fito-fipayment-status-report-debtor-agent", "flow-src-000173-p256-customer-payment-status-report-message-to-the-creditor", "flow-src-000173-p266-confirmation-of-processability-of-customer-direct-debit-initiation", "flow-src-000173-p278-payment-return-with-direct-debit", "flow-src-000173-p280-payment-return-initiated-by-debtor-agent", "flow-src-000173-p296-refund-by-the-debtor", "flow-src-000173-p298-customer-payment-reversal-with-direct-debit"]
message_ids: []
message_families: ["pain.001", "pain.002", "pain.007", "pain.008"]
search_terms: ["Debtor Agent", "pain.001", "pain.002", "pain.007", "pain.008"]
limitations: ["Scoped to supplied Payments Initiation source. Terminology conflict remains issue-000044.", "No cross-source equivalence or fixed institution/functional-role identity is inferred."]
issue_ids: ["issue-000044"]
manual_curated: true
definition_review: {"date": "2026-11-09", "result": "pass", "scope": "T6 definition/T8 mapping and cited narrative reviewed; classification ambiguity remains."}
flow_ids: ["flow-src-000173-p107-customer-to-bank-payment-order", "flow-src-000173-p136-customer-to-bank-payment-order", "flow-src-000173-p138-simple-scenario", "flow-src-000173-p140-complex-scenario", "flow-src-000173-p147-customer-to-bank-direct-debit", "flow-src-000173-p149-return-direct-debit", "flow-src-000173-p151-request-refund-of-direct-debit", "flow-src-000173-p170-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor-s", "flow-src-000173-p173-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play", "flow-src-000173-p176-three-different-actors-play-the-roles-of-initiating-party-debtor-and-u", "flow-src-000173-p189-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor", "flow-src-000173-p192-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play", "flow-src-000173-p195-one-actor-plays-roles-of-initiating-party-and-ultimate-debtor-second-a", "flow-src-000173-p198-customer-direct-debit-initiation-and-fito-ficustomer-direct-debit", "flow-src-000173-p234-negative-customer-payment-status-report-creditor-agent", "flow-src-000173-p239-negative-customer-payment-status-report-clearing-and-settlement-agent", "flow-src-000173-p249-negative-fito-fipayment-status-report-debtor-agent", "flow-src-000173-p266-confirmation-of-processability-of-customer-direct-debit-initiation", "flow-src-000173-p280-payment-return-initiated-by-debtor-agent", "flow-src-000173-p298-customer-payment-reversal-with-direct-debit"]
---



















































































# Debtor Agent

Business context: Payments Initiation. Source classification: functional participant role.

## Definition

Financial institution servicing an account for the debtor.

Evidence: [T6](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/documents/src-000173/tables/tbl-0006.md), source row 6.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Debit account and credit Internal account (7) | The debtor agent debits the account stipulated as being the debit account in the payment order. This includes currency conversion and charges if needed.<br>The debtor agent, after having successfully debited the debtor's account, credits internal accounts in order to transfer the provision necessary to process the payment order further. | Initiator | [T23](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/documents/src-000173/tables/tbl-0023.md) row 8 |
| Rebuild payment order(s) (10) | The debtor agent rebuilds the payment order by:<br>subtracting the failed/invalid individual payment instructions from the payment orders he received <br>subtracting, if relevant, the 'on us' individual payment instructions from the payment orders he received <br>merging, if relevant, of several payment orders coming from different initiating parties or agents acting as forwarding agents. The merge criteria are defined by the bank<br>re-building a consistent remittance | Initiator | [T23](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/documents/src-000173/tables/tbl-0023.md) row 12 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Order Customer-to-bank payment](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p116-order-customer-to-bank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Authorise Customer-to-Bank Payment](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p117-authorise-customer-to-bank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Check Authorisation Customer-to-Bank Payment](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p119-check-authorisation-customer-to-bank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Validate Customer-to-Bank-payment](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p120-validate-customer-to-bank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Assess Customer-to-Bank-Payment Risk](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p121-assess-customer-to-bank-payment-risk.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Generate Regulatory Reporting Information](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p122-generate-regulatory-reporting-information.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Clear customer-to-bank payment](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p123-clear-customer-to-bank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Settle customer-to-bank payment](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p124-settle-customer-to-bank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Complex scenario:](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p140-complex-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [CustomerCreditTransferInitiation](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p155-customer-credit-transfer-initiation.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Account information from debtor agent to initiating party](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p158-account-information-from-debtor-agent-to-initiating-party.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Interbank clearing and settlement between debtor agent and creditor agent](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p160-interbank-clearing-and-settlement-between-debtor-agent-and-creditor-ag.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [One Actor plays roles of Initiating Party, Debtor and Ultimate Debtor, Second actor plays roles of Creditor and Ultimate Creditor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p170-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor-s.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [One actor plays roles of Initiating Party and Debtor, second actor plays role of Ultimate Debtor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p173-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Three Different actors play the roles of Initiating Party, Debtor and Ultimate Debtor:](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p176-three-different-actors-play-the-roles-of-initiating-party-debtor-and-u.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [CustomerCreditTransferInitiation - Relay](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p179-customer-credit-transfer-initiation-relay.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [One actor plays roles of Initiating Party, Debtor and Ultimate Debtor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p189-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [One actor plays roles of Initiating Party and Debtor, Second Actor plays role of Ultimate Debtor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p192-one-actor-plays-roles-of-initiating-party-and-debtor-second-actor-play.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [One actor plays roles of Initiating Party and Ultimate Debtor, Second Actor plays role of Debtor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p195-one-actor-plays-roles-of-initiating-party-and-ultimate-debtor-second-a.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [CustomerDirectDebitInitiation and FIToFICustomerDirectDebit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p198-customer-direct-debit-initiation-and-fito-ficustomer-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Out of scope](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p223-out-of-scope.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Negative FIToFIPaymentStatusReport - Debtor Agent](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p249-negative-fito-fipayment-status-report-debtor-agent.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [CustomerPaymentStatusReport message to the Creditor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p256-customer-payment-status-report-message-to-the-creditor.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Confirmation of Processability of CustomerDirectDebitInitiation](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p266-confirmation-of-processability-of-customer-direct-debit-initiation.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [PaymentReturn with Direct Debit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p278-payment-return-with-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [PaymentReturn Initiated by Debtor Agent](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p280-payment-return-initiated-by-debtor-agent.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Refund by the Debtor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p296-refund-by-the-debtor.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Customer Payment Reversal with Direct Debit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p298-customer-payment-reversal-with-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `pain.001`, `pain.002`, `pain.007`, `pain.008`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Debtor Agent`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000173](../../../evidence/omitted/baf7abf3460122a33db6052d.md).

<!-- INITIATION-ROLE-REVIEW -->
## Curated responsibilities and role relationships

Services debtor account; receives credit-transfer initiation directly or through forwarding agent, validates/risk-checks and books the debit, supplies status/account information, receives direct-debit instructions, and initiates returns or handles debtor refund requests. (T6 row6; T23; P156–161; P182; P222; P260; P279–297; figures9–25)

T8 row6 marks the participant under: BusinessRole / Financial Institution, BusinessRole / Clearing System. This source mapping does not make the functional participant identical to a particular institution.

T1 and P98–100 use BusinessRole/Participant terminology inconsistently (issue-000044). The literal T6 definitions and T8 mapping are preserved. No identifier scheme is asserted beyond a source requirement.
<!-- /INITIATION-ROLE-REVIEW -->

<!-- INITIATION-FLOW-107 -->
[Customer-to-Bank Payment Order](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p107-customer-to-bank-payment-order.md)
<!-- /INITIATION-FLOW-107 -->

<!-- INITIATION-FLOW-138 -->
[Simple scenario:](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p138-simple-scenario.md)
<!-- /INITIATION-FLOW-138 -->

<!-- INITIATION-FLOW-140 -->
[Complex scenario:](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p140-complex-scenario.md)
<!-- /INITIATION-FLOW-140 -->

<!-- INITIATION-FLOW-136 -->
[Customer to Bank Payment Order](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p136-customer-to-bank-payment-order.md)
<!-- /INITIATION-FLOW-136 -->

<!-- INITIATION-FLOW-147 -->
[Customer-to-bank Direct Debit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p147-customer-to-bank-direct-debit.md)
<!-- /INITIATION-FLOW-147 -->

<!-- INITIATION-FLOW-149 -->
[Return Direct Debit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p149-return-direct-debit.md)
<!-- /INITIATION-FLOW-149 -->

<!-- INITIATION-FLOW-151 -->
[Request Refund of Direct Debit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p151-request-refund-of-direct-debit.md)
<!-- /INITIATION-FLOW-151 -->

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
