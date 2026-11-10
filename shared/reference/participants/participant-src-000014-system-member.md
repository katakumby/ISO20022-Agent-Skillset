---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
participant_id: "participant-src-000014-system-member"
title: "System Member"
source_labels: ["System Member"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[2]", "paragraph_id": null, "table_id": "T12"}]
flows: []
process_sections: []
message_ids: ["camt.003.001.08", "camt.004.001.10", "camt.005.001.11", "camt.006.001.11", "camt.007.001.10", "camt.008.001.11", "camt.009.001.08", "camt.010.001.09", "camt.011.001.08", "camt.012.001.08", "camt.013.001.04", "camt.014.001.05", "camt.015.001.04", "camt.016.001.04", "camt.017.001.05", "camt.018.001.05", "camt.019.001.07", "camt.020.001.04", "camt.021.001.06", "camt.023.001.07", "camt.024.001.08", "camt.025.001.09", "camt.046.001.08", "camt.047.001.08", "camt.048.001.07", "camt.049.001.07", "camt.050.001.07", "camt.051.001.07", "camt.069.001.05", "camt.070.001.06", "camt.071.001.05", "camt.101.001.02", "camt.102.001.03", "camt.103.001.03", "camt.104.001.01"]
message_families: []
search_terms: ["System Member"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels."]
manual_curated: true
issue_ids: ["issue-000058"]
flow_ids: ["flow-src-000014-p118-unsolicited-push-reporting", "flow-src-000014-p173-liquidity-credit-transfer", "flow-src-000014-p177-liquidity-debit-transfer", "flow-src-000014-p181-backup-payment-scenario", "flow-src-000014-p186-get-return-transaction", "flow-src-000014-p190-get-return-transaction-receipt", "flow-src-000014-p194-cancel-transaction-scenario", "flow-src-000014-p198-modify-transaction-scenario", "flow-src-000014-p207-get-return-limit", "flow-src-000014-p212-get-return-limit-receipt", "flow-src-000014-p217-create-limit-scenario", "flow-src-000014-p221-delete-limit-scenario", "flow-src-000014-p225-modify-limit-scenario", "flow-src-000014-p236-get-return-reservation-scenario", "flow-src-000014-p241-get-return-reservation-receipt", "flow-src-000014-p247-create-reservation-scenario", "flow-src-000014-p251-modify-reservation-scenario", "flow-src-000014-p255-delete-reservation-scenario", "flow-src-000014-p261-get-return-account", "flow-src-000014-p266-get-return-account-receipt", "flow-src-000014-p277-get-return-business-day-information", "flow-src-000014-p281-get-return-business-day-information-receipt", "flow-src-000014-p294-get-return-currency-exchange-rate", "flow-src-000014-p299-get-return-currency-exchange-rate-receipt", "flow-src-000014-p308-get-return-general-business-information-scenario", "flow-src-000014-p313-get-return-general-business-information-receipt", "flow-src-000014-p319-get-return-member-scenario", "flow-src-000014-p323-get-return-member-receipt", "flow-src-000014-p329-create-member-scenario", "flow-src-000014-p333-modify-member-scenario", "flow-src-000014-p341-get-return-standing-order-scenario", "flow-src-000014-p346-get-return-standing-order-receipt", "flow-src-000014-p352-create-standing-order-scenario", "flow-src-000014-p357-modify-standing-order-scenario", "flow-src-000014-p363-delete-standing-order-scenario"]
---







# System Member

Business context: Cash Management. Source classification: functional participant role.

## Definition

Party that instructs the executing/servicing party to process and maintain a standing order.

Evidence: [T12](../../../domains/payments/reference/message-sets/cash-management/2024-2025/documents/src-000014/tables/tbl-0012.md), source row 2.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [Cash Provider](participant-src-000014-cash-provider.md) | [T14](../../../domains/payments/reference/message-sets/cash-management/2024-2025/documents/src-000014/tables/tbl-0014.md) row 2, column 2 |
| Business role listed for this functional participant | [Settlement Agent](participant-src-000014-settlement-agent.md) | [T14](../../../domains/payments/reference/message-sets/cash-management/2024-2025/documents/src-000014/tables/tbl-0014.md) row 3, column 2 |
| Business role listed for this functional participant | [Corporate](participant-src-000014-corporate.md) | [T14](../../../domains/payments/reference/message-sets/cash-management/2024-2025/documents/src-000014/tables/tbl-0014.md) row 4, column 2 |
| Business role listed for this functional participant | [Market Infrastructure](participant-src-000014-market-infrastructure.md) | [T14](../../../domains/payments/reference/message-sets/cash-management/2024-2025/documents/src-000014/tables/tbl-0014.md) row 5, column 2 |
| Business role listed for this functional participant | [ACH](participant-src-000014-ach.md) | [T14](../../../domains/payments/reference/message-sets/cash-management/2024-2025/documents/src-000014/tables/tbl-0014.md) row 7, column 2 |

## Flows, source process sections and messages

Operational scenario links are recorded below.

Exact-version links below use the companion Part2 definitions.

## Aliases, identification and limitations

Source labels: `System Member`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000014](../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx).

<!-- CASH-FLOWS -->
## Applicable flows and responsibilities

Contextual business roles may perform the linked functional role; this list does not make them additional message senders/receivers.

- [Liquidity Credit Transfer](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p173-liquidity-credit-transfer.md)
- [Liquidity Debit Transfer](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p177-liquidity-debit-transfer.md)
- [Backup Payment Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p181-backup-payment-scenario.md)
- [Get/Return Transaction](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p186-get-return-transaction.md)
- [Get/Return Transaction Receipt](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p190-get-return-transaction-receipt.md)
- [Cancel Transaction Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p194-cancel-transaction-scenario.md)
- [Modify Transaction Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p198-modify-transaction-scenario.md)
- [Get/Return Limit](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p207-get-return-limit.md)
- [Get/Return Limit Receipt](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p212-get-return-limit-receipt.md)
- [Create Limit Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p217-create-limit-scenario.md)
- [Delete Limit Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p221-delete-limit-scenario.md)
- [Modify Limit Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p225-modify-limit-scenario.md)
- [Get/Return Reservation Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p236-get-return-reservation-scenario.md)
- [Get/Return Reservation Receipt](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p241-get-return-reservation-receipt.md)
- [Create Reservation Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p247-create-reservation-scenario.md)
- [Modify Reservation Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p251-modify-reservation-scenario.md)
- [Delete Reservation Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p255-delete-reservation-scenario.md)
- [Get/Return Account](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p261-get-return-account.md)
- [Get/Return Account Receipt](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p266-get-return-account-receipt.md)
- [Get/Return Business Day Information](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p277-get-return-business-day-information.md)
- [Get/Return Business Day Information Receipt](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p281-get-return-business-day-information-receipt.md)
- [Get/Return Currency Exchange Rate](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p294-get-return-currency-exchange-rate.md)
- [Get/Return Currency Exchange Rate Receipt](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p299-get-return-currency-exchange-rate-receipt.md)
- [Get/Return General Business Information Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p308-get-return-general-business-information-scenario.md)
- [Get/Return General Business Information Receipt](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p313-get-return-general-business-information-receipt.md)
- [Get/Return Member Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p319-get-return-member-scenario.md)
- [Get/Return Member Receipt](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p323-get-return-member-receipt.md)
- [Create Member Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p329-create-member-scenario.md)
- [Modify Member Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p333-modify-member-scenario.md)
- [Get/Return Standing Order Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p341-get-return-standing-order-scenario.md)
- [Get/Return Standing Order Receipt](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p346-get-return-standing-order-receipt.md)
- [Create Standing Order Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p352-create-standing-order-scenario.md)
- [Modify Standing Order Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p357-modify-standing-order-scenario.md)
- [Delete Standing Order Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p363-delete-standing-order-scenario.md)
- [Unsolicited operational cash reports and warnings](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p118-unsolicited-push-reporting.md)
