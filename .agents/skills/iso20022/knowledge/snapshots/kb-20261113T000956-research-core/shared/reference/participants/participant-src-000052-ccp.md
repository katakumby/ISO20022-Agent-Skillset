---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
participant_id: "participant-src-000052-ccp"
title: "CCP"
source_labels: ["CCP"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000052", "heading_path": ["BusinessRoles and Participants"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[10]", "paragraph_id": null, "table_id": "T10"}]
flows: ["flow-src-000052-p191-business-process-trade-management", "flow-src-000052-p194-business-process-risk-management-netting-process", "flow-src-000052-p196-business-process-risk-management-margining-process", "flow-src-000052-p198-business-process-risk-management-default-fund-contribution-process", "flow-src-000052-p201-business-process-settlement-management-settlement-netting-process", "flow-src-000052-p204-settlement-management-buy-in-process"]
process_sections: ["flow-src-000052-p113-trade-management-process", "flow-src-000052-p119-risk-management-process", "flow-src-000052-p125-netting-process", "flow-src-000052-p131-margining-process", "flow-src-000052-p137-default-fund-contribution-process", "flow-src-000052-p143-collateral-management-process-out-of-scope", "flow-src-000052-p149-settlement-management-process", "flow-src-000052-p155-settlement-netting-process", "flow-src-000052-p161-buy-in-process", "flow-src-000052-p167-reporting-process-out-of-scope", "flow-src-000052-p217-trade-leg-notification-business-transaction", "flow-src-000052-p229-margining-business-transaction", "flow-src-000052-p240-default-fund-contribution-business-transaction", "flow-src-000052-p250-buy-in-business-transaction"]
message_ids: []
message_families: []
search_terms: ["CCP"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# CCP

Business context: CCP Clearing. Source classification: business role.

## Definition

The infrastructure that will act as central counterparty.

Evidence: [T10](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0010.md), source row 10.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Central Counterparty](participant-src-000052-central-counterparty.md) | [T11](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0011.md) row 6, column 3 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Trade Management process:](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p113-trade-management-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Risk Management process:](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p119-risk-management-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Netting process:](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p125-netting-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Margining process:](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p131-margining-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Default Fund Contribution process:](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p137-default-fund-contribution-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Collateral Management process (out of scope):](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p143-collateral-management-process-out-of-scope.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Settlement Management process:](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p149-settlement-management-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Settlement Netting process:](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p155-settlement-netting-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Buy-In process:](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p161-buy-in-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Reporting process (Out of scope):](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p167-reporting-process-out-of-scope.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [BusinessProcess - Trade Management](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p191-business-process-trade-management.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [BusinessProcess - Risk Management – Netting Process](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p194-business-process-risk-management-netting-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [BusinessProcess - Risk Management – Margining Process](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p196-business-process-risk-management-margining-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [BusinessProcess - Risk Management – Default Fund Contribution Process](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p198-business-process-risk-management-default-fund-contribution-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [BusinessProcess - Settlement Management – Settlement Netting Process](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p201-business-process-settlement-management-settlement-netting-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Settlement Management – Buy-In Process](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p204-settlement-management-buy-in-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Trade Leg Notification BusinessTransaction](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p217-trade-leg-notification-business-transaction.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Margining BusinessTransaction](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p229-margining-business-transaction.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Default Fund Contribution BusinessTransaction](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p240-default-fund-contribution-business-transaction.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Buy-in BusinessTransaction](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p250-buy-in-business-transaction.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `CCP`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000052](../../../evidence/omitted/b45c53bac2be08dee677b607.md).
