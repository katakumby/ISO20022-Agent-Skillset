---
template: false
document_kind: "participant"
review_status: "reviewed"
manual_curated: true
domain: "shared"
domains: ["securities"]
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
participant_id: "participant-src-000095-account-owner"
title: "Account Owner"
source_labels: ["Account Owner"]
role_type: "Functional account relationship role"
aliases: []
source_locations: [{"source_id": "src-000095", "locator": "P237–P241; T21; Account Management"}, {"source_id": "src-000095", "locator": "P241–P260; P263–P276"}]
flow_ids: ["flow-src-000095-p236-account-management", "flow-src-000095-p240-direct", "flow-src-000095-p245-intermediary", "flow-src-000095-p251-rejection-direct", "flow-src-000095-p256-rejection-intermediary", "flow-src-000095-p262-direct", "flow-src-000095-p266-intermediary", "flow-src-000095-p269-rejection-direct", "flow-src-000095-p274-rejection-intermediary", "flow-src-000095-p279-status-of-account-opening-direct", "flow-src-000095-p284-status-of-account-modification-direct", "flow-src-000095-p290-status-of-account-opening-intermediary", "flow-src-000095-p296-status-of-account-modification-intermediary", "flow-src-000095-p302-request-for-account-management-status-rejection-direct", "flow-src-000095-p308-account-closure-direct", "flow-src-000095-p311-account-closure-and-reactivation-direct"]
message_ids: []
limitations: ["Scoped to the supplied Investment Funds source; same-name roles in other publications are not merged.", "No identifier scheme is specified in the cited evidence."]
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative/table/figure labels inspected; no independent institutional equivalence inferred."}
---































# Account Owner

[src-000095](../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx)

## Definition and context

Account-side party that opens or maintains an investment-fund account with an account servicer. The source gives an investor or its designated agent as examples; these examples do not make the function a fixed institution. (P237–P241; T21; Account Management)

Source classification: Functional account relationship role. A functional role varies with the relationship; institutional examples do not fix the role for every process.

## Responsibilities and actions

Instructs opening, including supplementary accounts; instructs insertions, deletions or updates to account details. Receives confirmations and status/rejection messages directly or through one or more intermediaries. (P241–P260; P263–P276)

## Relationships

- [account servicer](participant-src-000095-account-servicer.md)
- [intermediary](participant-src-000095-intermediary.md)

## Flows and messages

- [flow-src-000095-p236-account-management](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p236-account-management.md)
- [flow-src-000095-p240-direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p240-direct.md)
- [flow-src-000095-p245-intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p245-intermediary.md)
- [flow-src-000095-p251-rejection-direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p251-rejection-direct.md)
- [flow-src-000095-p256-rejection-intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p256-rejection-intermediary.md)
- [flow-src-000095-p262-direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p262-direct.md)
- [flow-src-000095-p266-intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p266-intermediary.md)
- [flow-src-000095-p269-rejection-direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p269-rejection-direct.md)
- [flow-src-000095-p274-rejection-intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p274-rejection-intermediary.md)

Message names in the cited source identify business exchanges; exact definitions are resolved through the message-set index.

## Identification and limitations

- Scoped to the supplied Investment Funds source; same-name roles in other publications are not merged.
- No identifier scheme is specified in the cited evidence.

[Separate message-functionality evidence in Part2](participant-narrative-src-000096-account-owner.md) is cross-linked by context; no unqualified cross-publication identity is asserted.

<!-- FUNDS-CURATED-FLOW-0132-START -->
[Accounting holdings statement](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p920-accounting-statement-of-holdings.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0132.md)
<!-- FUNDS-CURATED-FLOW-0132-END -->

<!-- FUNDS-CURATED-FLOW-0133-START -->
[Accounting holdings statement query](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p923-accounting-statement-of-holdings-request.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0133.md)
<!-- FUNDS-CURATED-FLOW-0133-END -->

<!-- FUNDS-CURATED-FLOW-0134-START -->
[Accounting holdings statement cancellation](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p926-accounting-statement-of-holdings-cancellation.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0134.md)
<!-- FUNDS-CURATED-FLOW-0134-END -->

<!-- FUNDS-CURATED-FLOW-0135-START -->
[Custody holdings statement](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p930-custody-statement-of-holdings.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0135.md)
<!-- FUNDS-CURATED-FLOW-0135-END -->

<!-- FUNDS-CURATED-FLOW-0136-START -->
[Custody holdings statement query](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p933-custody-statement-of-holdings-request.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0136.md)
<!-- FUNDS-CURATED-FLOW-0136-END -->

<!-- FUNDS-CURATED-FLOW-0137-START -->
[Custody holdings statement cancellation](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p936-custody-statement-of-holdings-cancellation.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0137.md)
<!-- FUNDS-CURATED-FLOW-0137-END -->

<!-- FUNDS-CURATED-FLOW-0138-START -->
[Transparency holdings statement aggregation and status](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p940-transparency-of-holdings-statement.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0138.md)
<!-- FUNDS-CURATED-FLOW-0138-END -->

<!-- FUNDS-CURATED-FLOW-0139-START -->
[Investment fund transaction statement](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p945-statement-of-investment-fund-transactions.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0139.md)
<!-- FUNDS-CURATED-FLOW-0139-END -->

<!-- FUNDS-CURATED-FLOW-0140-START -->
[Investment fund transaction statement query](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p948-statement-of-investment-fund-transactions-request.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0140.md)
<!-- FUNDS-CURATED-FLOW-0140-END -->

<!-- FUNDS-CURATED-FLOW-0141-START -->
[Investment fund transaction statement cancellation](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p951-statement-of-investment-fund-transactions-cancellation.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0141.md)
<!-- FUNDS-CURATED-FLOW-0141-END -->

<!-- FUNDS-EARLY-FLOW-240 -->
[Account Management / Account Opening / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p240-direct.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-240 -->

<!-- FUNDS-EARLY-FLOW-245 -->
[Account Management / Account Opening / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p245-intermediary.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-245 -->

<!-- FUNDS-EARLY-FLOW-251 -->
[Account Management / Account Opening / Rejection - Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p251-rejection-direct.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-251 -->

<!-- FUNDS-EARLY-FLOW-256 -->
[Account Management / Account Opening / Rejection - Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p256-rejection-intermediary.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-256 -->

<!-- FUNDS-EARLY-FLOW-262 -->
[Account Management / Account Modification / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p262-direct.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-262 -->

<!-- FUNDS-EARLY-FLOW-266 -->
[Account Management / Account Modification / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p266-intermediary.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-266 -->

<!-- FUNDS-EARLY-FLOW-269 -->
[Account Management / Account Modification / Rejection - Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p269-rejection-direct.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-269 -->

<!-- FUNDS-EARLY-FLOW-274 -->
[Account Management / Account Modification / Rejection - Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p274-rejection-intermediary.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-274 -->

<!-- FUNDS-EARLY-FLOW-279 -->
[Account Management / Status of Account Opening - Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p279-status-of-account-opening-direct.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-279 -->

<!-- FUNDS-EARLY-FLOW-284 -->
[Account Management / Status of Account Modification – Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p284-status-of-account-modification-direct.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-284 -->

<!-- FUNDS-EARLY-FLOW-290 -->
[Account Management / Status of Account Opening - Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p290-status-of-account-opening-intermediary.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-290 -->

<!-- FUNDS-EARLY-FLOW-296 -->
[Account Management / Status of Account Modification - Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p296-status-of-account-modification-intermediary.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-296 -->

<!-- FUNDS-EARLY-FLOW-302 -->
[Account Management / Request for Account Management Status Rejection - Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p302-request-for-account-management-status-rejection-direct.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-302 -->

<!-- FUNDS-EARLY-FLOW-308 -->
[Account Management / Account Closure - Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p308-account-closure-direct.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-308 -->

<!-- FUNDS-EARLY-FLOW-311 -->
[Account Management / Account Closure and Reactivation - Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p311-account-closure-and-reactivation-direct.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-311 -->
