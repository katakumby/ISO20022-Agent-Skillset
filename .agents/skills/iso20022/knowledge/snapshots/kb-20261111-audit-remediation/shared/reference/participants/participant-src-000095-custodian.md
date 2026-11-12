---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
participant_id: "participant-src-000095-custodian"
title: "Custodian"
source_labels: ["Custodian"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[19]/w:tr[2]", "paragraph_id": null, "table_id": "T19"}]
flows: ["flow-src-000095-p191-payment-execution-pay-out-arrears", "flow-src-000095-p218-transparency-of-holdings", "flow-src-000095-p221-stock-transfers-single-leg-transfer", "flow-src-000095-p226-portfolio-and-stock-transfers-single-leg", "flow-src-000095-p230-portfolio-and-stock-transfers-double-matched-leg"]
process_sections: ["flow-src-000095-p236-account-management", "flow-src-000095-p940-transparency-of-holdings-statement"]
message_ids: []
message_families: ["semt.002", "semt.041", "semt.042", "sese.001", "sese.003", "sese.005", "sese.007", "sese.011", "sese.012", "sese.018", "sese.019"]
search_terms: ["Custodian", "semt.002", "semt.041", "semt.042", "sese.001", "sese.003", "sese.005", "sese.007", "sese.011", "sese.012", "sese.018", "sese.019"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000095-p240-direct", "flow-src-000095-p245-intermediary", "flow-src-000095-p251-rejection-direct", "flow-src-000095-p256-rejection-intermediary", "flow-src-000095-p262-direct", "flow-src-000095-p266-intermediary", "flow-src-000095-p269-rejection-direct", "flow-src-000095-p274-rejection-intermediary", "flow-src-000095-p279-status-of-account-opening-direct", "flow-src-000095-p284-status-of-account-modification-direct", "flow-src-000095-p290-status-of-account-opening-intermediary", "flow-src-000095-p296-status-of-account-modification-intermediary", "flow-src-000095-p302-request-for-account-management-status-rejection-direct", "flow-src-000095-p308-account-closure-direct", "flow-src-000095-p311-account-closure-and-reactivation-direct"]
---



































# Custodian

Business context: Investment Funds. Source classification: business role.

## Definition

Party that safekeeps and administers assets on behalf of the owner and that has a network of sub-custodians.

Evidence: [T19](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0019.md), source row 2.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Instructing Party](participant-src-000095-instructing-party.md) | [T20](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0020.md) row 2, column 2 |
| Can play the functional participant role in this source context | [Intermediary](participant-src-000095-intermediary.md) | [T20](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0020.md) row 2, column 3 |
| Can play the functional participant role in this source context | [Executing Party](participant-src-000095-executing-party.md) | [T20](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0020.md) row 2, column 4 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Payment Execution - Pay Out Arrears](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p191-payment-execution-pay-out-arrears.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transparency of Holdings](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p218-transparency-of-holdings.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Stock Transfers (Single Leg Transfer)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p221-stock-transfers-single-leg-transfer.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Portfolio and Stock Transfers (Single Leg)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p226-portfolio-and-stock-transfers-single-leg.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Portfolio and Stock Transfers (Double/Matched Leg)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p230-portfolio-and-stock-transfers-double-matched-leg.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Account Management](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p236-account-management.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transparency of Holdings Statement](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p940-transparency-of-holdings-statement.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `semt.002`, `semt.041`, `semt.042`, `sese.001`, `sese.003`, `sese.005`, `sese.007`, `sese.011`, `sese.012`, `sese.018`, `sese.019`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Custodian`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000095](../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md).

<!-- FUNDS-CURATED-FLOW-0138-START -->
[Transparency holdings statement aggregation and status](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p940-transparency-of-holdings-statement.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0138.md)
<!-- FUNDS-CURATED-FLOW-0138-END -->

<!-- FUNDS-PROCESS-fig-0001 -->
[Investment Funds communication scope](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0001.md)
<!-- /FUNDS-PROCESS-fig-0001 -->

<!-- FUNDS-PROCESS-fig-0002 -->
[Business roles and functional participants](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0002.md)
<!-- /FUNDS-PROCESS-fig-0002 -->

<!-- FUNDS-EARLY-FLOW-240 -->
[Account Management / Account Opening / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p240-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-240 -->

<!-- FUNDS-EARLY-FLOW-245 -->
[Account Management / Account Opening / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p245-intermediary.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-245 -->

<!-- FUNDS-EARLY-FLOW-251 -->
[Account Management / Account Opening / Rejection - Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p251-rejection-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-251 -->

<!-- FUNDS-EARLY-FLOW-256 -->
[Account Management / Account Opening / Rejection - Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p256-rejection-intermediary.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-256 -->

<!-- FUNDS-EARLY-FLOW-262 -->
[Account Management / Account Modification / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p262-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-262 -->

<!-- FUNDS-EARLY-FLOW-266 -->
[Account Management / Account Modification / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p266-intermediary.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-266 -->

<!-- FUNDS-EARLY-FLOW-269 -->
[Account Management / Account Modification / Rejection - Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p269-rejection-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-269 -->

<!-- FUNDS-EARLY-FLOW-274 -->
[Account Management / Account Modification / Rejection - Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p274-rejection-intermediary.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-274 -->

<!-- FUNDS-EARLY-FLOW-279 -->
[Account Management / Status of Account Opening - Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p279-status-of-account-opening-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-279 -->

<!-- FUNDS-EARLY-FLOW-284 -->
[Account Management / Status of Account Modification – Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p284-status-of-account-modification-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-284 -->

<!-- FUNDS-EARLY-FLOW-290 -->
[Account Management / Status of Account Opening - Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p290-status-of-account-opening-intermediary.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-290 -->

<!-- FUNDS-EARLY-FLOW-296 -->
[Account Management / Status of Account Modification - Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p296-status-of-account-modification-intermediary.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-296 -->

<!-- FUNDS-EARLY-FLOW-302 -->
[Account Management / Request for Account Management Status Rejection - Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p302-request-for-account-management-status-rejection-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-302 -->

<!-- FUNDS-EARLY-FLOW-308 -->
[Account Management / Account Closure - Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p308-account-closure-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-308 -->

<!-- FUNDS-EARLY-FLOW-311 -->
[Account Management / Account Closure and Reactivation - Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p311-account-closure-and-reactivation-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-311 -->
