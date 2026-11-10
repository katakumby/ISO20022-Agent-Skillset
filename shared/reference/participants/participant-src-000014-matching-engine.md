---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
participant_id: "participant-src-000014-matching-engine"
title: "Matching engine"
domain: "shared"
domains: ["payments"]
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
source_labels: ["Matching engine"]
aliases: []
role_kind: "functional system role"
source_locations: [{"source_id": "src-000014", "paragraph_id": "P174", "xml_path": "/w:document/w:body/w:p[174]", "heading_path": ["BusinessTransactions", "Liquidity Management", "Liquidity Credit Transfer"]}, {"source_id": "src-000014", "paragraph_id": "P187", "xml_path": "/w:document/w:body/w:p[187]", "heading_path": ["BusinessTransactions", "Transaction", "Get/Return Transaction"]}]
limitations: ["Scoped to the Cash Management publication; no equivalence with same labels elsewhere assumed.", "These passages specify no identifier scheme."]
flow_ids: ["flow-src-000014-p118-unsolicited-push-reporting", "flow-src-000014-p173-liquidity-credit-transfer", "flow-src-000014-p177-liquidity-debit-transfer", "flow-src-000014-p181-backup-payment-scenario", "flow-src-000014-p186-get-return-transaction", "flow-src-000014-p190-get-return-transaction-receipt", "flow-src-000014-p194-cancel-transaction-scenario", "flow-src-000014-p198-modify-transaction-scenario", "flow-src-000014-p207-get-return-limit", "flow-src-000014-p212-get-return-limit-receipt", "flow-src-000014-p217-create-limit-scenario", "flow-src-000014-p221-delete-limit-scenario", "flow-src-000014-p225-modify-limit-scenario", "flow-src-000014-p236-get-return-reservation-scenario", "flow-src-000014-p241-get-return-reservation-receipt", "flow-src-000014-p247-create-reservation-scenario", "flow-src-000014-p251-modify-reservation-scenario", "flow-src-000014-p255-delete-reservation-scenario", "flow-src-000014-p261-get-return-account", "flow-src-000014-p266-get-return-account-receipt", "flow-src-000014-p277-get-return-business-day-information", "flow-src-000014-p281-get-return-business-day-information-receipt", "flow-src-000014-p294-get-return-currency-exchange-rate", "flow-src-000014-p299-get-return-currency-exchange-rate-receipt", "flow-src-000014-p308-get-return-general-business-information-scenario", "flow-src-000014-p313-get-return-general-business-information-receipt", "flow-src-000014-p319-get-return-member-scenario", "flow-src-000014-p323-get-return-member-receipt", "flow-src-000014-p329-create-member-scenario", "flow-src-000014-p333-modify-member-scenario", "flow-src-000014-p341-get-return-standing-order-scenario", "flow-src-000014-p346-get-return-standing-order-receipt", "flow-src-000014-p352-create-standing-order-scenario", "flow-src-000014-p357-modify-standing-order-scenario", "flow-src-000014-p363-delete-standing-order-scenario"]
message_ids: ["camt.003.001.08", "camt.004.001.10", "camt.005.001.11", "camt.006.001.11", "camt.007.001.10", "camt.008.001.11", "camt.009.001.08", "camt.010.001.09", "camt.011.001.08", "camt.012.001.08", "camt.013.001.04", "camt.014.001.05", "camt.015.001.04", "camt.016.001.04", "camt.017.001.05", "camt.018.001.05", "camt.019.001.07", "camt.020.001.04", "camt.021.001.06", "camt.023.001.07", "camt.024.001.08", "camt.025.001.09", "camt.046.001.08", "camt.047.001.08", "camt.048.001.07", "camt.049.001.07", "camt.050.001.07", "camt.051.001.07", "camt.069.001.05", "camt.070.001.06", "camt.071.001.05", "camt.101.001.02", "camt.102.001.03", "camt.103.001.03", "camt.104.001.01"]
---



# Matching engine

One possible transaction administrator in the liquidity and transaction scenarios. No independent legal-institution identity is asserted.

## Source-grounded responsibilities and relationships

**P174** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with the ability to manage their liquidity.

**P187** At any time during operating hours of a system, a (direct) member can query the transaction administrator (which can be a financial institution, a matching engine or a settlement engine) to get information about payment instructions held at the transaction administrator.

Related scoped role: [system transaction administrator](participant-src-000014-system-transaction-administrator.md).

[src-000014](../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx)

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
