---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
participant_id: "participant-src-000014-counterparty-member"
title: "Counterparty member"
domain: "shared"
domains: ["payments"]
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
source_labels: ["Counterparty member"]
aliases: []
role_kind: "functional counterparty role"
source_locations: [{"source_id": "src-000014", "paragraph_id": "P183", "xml_path": "/w:document/w:body/w:p[183]", "heading_path": ["BusinessTransactions", "Liquidity Management", "Backup Payment Scenario"]}, {"source_id": "src-000014", "paragraph_id": "P205", "xml_path": "/w:document/w:body/w:p[205]", "heading_path": ["BusinessTransactions", "Limit management "]}, {"source_id": "src-000014", "paragraph_id": "P206", "xml_path": "/w:document/w:body/w:p[206]", "heading_path": ["BusinessTransactions", "Limit management "]}]
limitations: ["Scoped to the Cash Management publication; no equivalence with same labels elsewhere assumed.", "These passages specify no identifier scheme."]
flow_ids: ["flow-src-000014-p181-backup-payment-scenario", "flow-src-000014-p207-get-return-limit", "flow-src-000014-p212-get-return-limit-receipt", "flow-src-000014-p217-create-limit-scenario", "flow-src-000014-p221-delete-limit-scenario", "flow-src-000014-p225-modify-limit-scenario"]
message_ids: ["camt.009.001.08", "camt.010.001.09", "camt.011.001.08", "camt.012.001.08", "camt.023.001.07", "camt.025.001.09", "camt.101.001.02"]
---



# Counterparty member

Another participant can receive backup-payment funds; bilateral limits identify the particular other member. The bilateral role is not equated with an account servicer.

## Source-grounded responsibilities and relationships

**P183** At any time during the operating hours of the system, a member can request the transaction administrator to transfer funds from the member to another participant in the system in case the user is in recovery mode. The transaction administrator will reply with a Receipt message that may contain the status of the request.

**P205** Limits are set by a member of the system either with regard to another specific member (bilateral limit) or with regard to all other participants (multilateral limit). As a result, there can be a maximum of one multilateral limit and as many bilateral limits as members of the system.

**P206** For a bilateral limit, a member always needs to identify the counterparty to which it applies.

Related scoped role: [system direct member](participant-src-000014-system-direct-member.md).

[src-000014](../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx)

<!-- CASH-FLOWS -->
## Applicable flows and responsibilities

Contextual business roles may perform the linked functional role; this list does not make them additional message senders/receivers.

- [Backup Payment Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p181-backup-payment-scenario.md)
- [Get/Return Limit](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p207-get-return-limit.md)
- [Get/Return Limit Receipt](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p212-get-return-limit-receipt.md)
- [Create Limit Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p217-create-limit-scenario.md)
- [Delete Limit Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p221-delete-limit-scenario.md)
- [Modify Limit Scenario](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/flow-src-000014-p225-modify-limit-scenario.md)
