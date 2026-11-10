---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
participant_id: "participant-src-000095-transfer-agent"
title: "Transfer Agent"
source_labels: ["Transfer Agent"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[19]/w:tr[10]", "paragraph_id": null, "table_id": "T19"}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Stock Transfers (Single Leg Transfer)"], "locator": "/w:document/w:body/w:tbl[43]/w:tr[6]", "paragraph_id": null, "table_id": "T43"}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", " Portfolio and Stock Transfers (Single Leg)"], "locator": "/w:document/w:body/w:tbl[44]/w:tr[10]", "paragraph_id": null, "table_id": "T44"}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", " Portfolio and Stock Transfers (Single Leg)"], "locator": "/w:document/w:body/w:tbl[44]/w:tr[11]", "paragraph_id": null, "table_id": "T44"}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Portfolio and Stock Transfers (Double/Matched Leg)"], "locator": "/w:document/w:body/w:tbl[45]/w:tr[4]", "paragraph_id": null, "table_id": "T45"}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Portfolio and Stock Transfers (Double/Matched Leg)"], "locator": "/w:document/w:body/w:tbl[45]/w:tr[5]", "paragraph_id": null, "table_id": "T45"}]
flows: ["flow-src-000095-p187-order-execution", "flow-src-000095-p189-payment-execution-advance-pay-in", "flow-src-000095-p191-payment-execution-pay-out-arrears", "flow-src-000095-p192-tax-accounting", "flow-src-000095-p194-commission-accounting", "flow-src-000095-p195-commission-accounting-transaction-based-commission-accounting", "flow-src-000095-p196-commission-accounting-trailer-commission-accounting", "flow-src-000095-p199-distribution", "flow-src-000095-p200-registration", "flow-src-000095-p218-transparency-of-holdings", "flow-src-000095-p221-stock-transfers-single-leg-transfer", "flow-src-000095-p226-portfolio-and-stock-transfers-single-leg", "flow-src-000095-p230-portfolio-and-stock-transfers-double-matched-leg"]
process_sections: ["flow-src-000095-p236-account-management", "flow-src-000095-p315-fund-cash-forecast-reporting", "flow-src-000095-p348-fund-reference-data-reporting", "flow-src-000095-p360-order-and-confirmation", "flow-src-000095-p381-bulk", "flow-src-000095-p415-order-instruction-status-reporting", "flow-src-000095-p504-order-cancellation-and-status", "flow-src-000095-p592-order-confirmation-status-reporting", "flow-src-000095-p612-order-confirmation-amendment", "flow-src-000095-p630-bulk", "flow-src-000095-p650-bulk", "flow-src-000095-p670-order-confirmation-cancellation", "flow-src-000095-p687-bulk", "flow-src-000095-p707-bulk", "flow-src-000095-p726-order-confirmation-status-request", "flow-src-000095-p805-individual-asset-transfer", "flow-src-000095-p828-two-account-owners-direct-slt-market-practice", "flow-src-000095-p861-request-for-transfer-status-and-transfer-status", "flow-src-000095-p871-request-for-status-rejection", "flow-src-000095-p900-price-reporting", "flow-src-000095-p915-statements"]
message_ids: []
message_families: ["reda.001", "reda.004", "semt.002", "sese.001", "sese.003", "sese.005", "sese.007", "sese.009", "sese.010", "sese.011", "sese.012", "sese.018", "sese.019", "setr.001", "setr.003", "setr.004", "setr.006", "setr.007", "setr.009", "setr.010", "setr.012", "setr.016", "setr.017", "setr.047", "setr.049", "setr.051", "setr.053", "setr.057", "setr.058"]
search_terms: ["Transfer Agent", "reda.001", "reda.004", "semt.002", "sese.001", "sese.003", "sese.005", "sese.007", "sese.009", "sese.010", "sese.011", "sese.012", "sese.018", "sese.019", "setr.001", "setr.003", "setr.004", "setr.006", "setr.007", "setr.009", "setr.010", "setr.012", "setr.016", "setr.017", "setr.047", "setr.049", "setr.051", "setr.053", "setr.057", "setr.058"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000095-p221-stock-transfers-single-leg-transfer", "flow-src-000095-p226-portfolio-and-stock-transfers-single-leg", "flow-src-000095-p230-portfolio-and-stock-transfers-double-matched-leg", "flow-src-000095-p240-direct", "flow-src-000095-p245-intermediary", "flow-src-000095-p251-rejection-direct", "flow-src-000095-p256-rejection-intermediary", "flow-src-000095-p262-direct", "flow-src-000095-p266-intermediary", "flow-src-000095-p269-rejection-direct", "flow-src-000095-p274-rejection-intermediary", "flow-src-000095-p279-status-of-account-opening-direct", "flow-src-000095-p284-status-of-account-modification-direct", "flow-src-000095-p290-status-of-account-opening-intermediary", "flow-src-000095-p296-status-of-account-modification-intermediary", "flow-src-000095-p302-request-for-account-management-status-rejection-direct", "flow-src-000095-p308-account-closure-direct", "flow-src-000095-p311-account-closure-and-reactivation-direct", "flow-src-000095-p322-estimated", "flow-src-000095-p325-estimated-and-confirmed", "flow-src-000095-p331-detailed-estimated", "flow-src-000095-p334-detailed-estimated-and-confirmed", "flow-src-000095-p340-confirmed-cancellation-and-new-confirmed", "flow-src-000095-p344-detailed-confirmed-cancellation-and-new-confirmed", "flow-src-000095-p351-fund-reference-data-report-solicited-requested", "flow-src-000095-p356-fund-reference-data-report-unsolicited", "flow-src-000095-p368-direct", "flow-src-000095-p374-intermediary", "flow-src-000095-p381-bulk", "flow-src-000095-p388-direct", "flow-src-000095-p394-intermediary", "flow-src-000095-p400-bulk", "flow-src-000095-p407-direct", "flow-src-000095-p411-intermediary", "flow-src-000095-p425-direct", "flow-src-000095-p429-intermediary", "flow-src-000095-p436-bulk", "flow-src-000095-p445-direct", "flow-src-000095-p449-intermediary", "flow-src-000095-p456-bulk", "flow-src-000095-p465-direct", "flow-src-000095-p469-intermediary", "flow-src-000095-p476-request-status-of-subscription", "flow-src-000095-p481-request-status-of-redemption", "flow-src-000095-p486-request-status-of-switch", "flow-src-000095-p515-request-and-status-direct", "flow-src-000095-p519-request-and-status-intermediary", "flow-src-000095-p524-request-and-status-bulk"]
---





































































































# Transfer Agent

Business context: Investment Funds. Source classification: business role.

## Definition

Party appointed by the fund management company. This party updates records of investor accounts to reflect the daily investor purchases, redemptions, switches, transfers, and re-registrations. It ensures the timely settlement of transactions, and may provide tax information to the investor and/or to its intermediaries. It may calculate, collect, and rebate commissions. It prepares and distributes confirmations reflecting transactions, resulting in unit or cash account movements to the investor or the investor's intermediary. It responds to inquiries concerning account status, and processes the income distribution.

Evidence: [T19](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0019.md), source row 10.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Confirm Transfer | The transfer out and transfer in confirmations are simultaneously sent by the transfer agent to the transferor’s bank and the transferee’s bank. | Initiator | [T43](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0043.md) row 6 |
| Provide Status | The transfer out instruction is validated by the transfer agent, who optionally sends a transfer instruction status report; if the transfer could not be registered immediately. | Initiator | [T44](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0044.md) row 10 |
| Confirm Transfer | The transfer out and transfer in confirmations are simultaneously sent by the transfer agent to the transferor’s intermediary and the transferee’s intermediary. | Initiator | [T44](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0044.md) row 11 |
| Provide Status | The transfer out and transfer in instructions are validated by the transfer agent, who sends first a transfer instruction status report with the status received to the transferor and transferee as soon as their instructions have been received and optionally a second transfer instruction status report with the status matched is sent to the transferor and transferee, if the transfer could not be registered immediately. | Initiator | [T45](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0045.md) row 4 |
| Confirmed | The transfer out and transfer in confirmations are simultaneously sent by the transfer agent to the transferor and the transferee to complete the transfer. | Initiator | [T45](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0045.md) row 5 |

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Executing Party](participant-src-000095-executing-party.md) | [T20](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0020.md) row 11, column 4 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Order Execution](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p187-order-execution.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Payment Execution - Advance Pay In](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p189-payment-execution-advance-pay-in.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Payment Execution - Pay Out Arrears](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p191-payment-execution-pay-out-arrears.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Tax Accounting](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p192-tax-accounting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Commission Accounting](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p194-commission-accounting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Commission Accounting / Transaction Based Commission Accounting](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p195-commission-accounting-transaction-based-commission-accounting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Commission Accounting / Trailer Commission Accounting](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p196-commission-accounting-trailer-commission-accounting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Distribution](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p199-distribution.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Registration](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p200-registration.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transparency of Holdings](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p218-transparency-of-holdings.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Stock Transfers (Single Leg Transfer)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p221-stock-transfers-single-leg-transfer.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Portfolio and Stock Transfers (Single Leg)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p226-portfolio-and-stock-transfers-single-leg.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Portfolio and Stock Transfers (Double/Matched Leg)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p230-portfolio-and-stock-transfers-double-matched-leg.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Account Management](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p236-account-management.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Fund Cash Forecast Reporting](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p315-fund-cash-forecast-reporting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Fund Reference Data Reporting](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p348-fund-reference-data-reporting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order and Confirmation](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p360-order-and-confirmation.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p381-bulk.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order Instruction Status Reporting](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p415-order-instruction-status-reporting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order Cancellation and Status](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p504-order-cancellation-and-status.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order Confirmation Status Reporting](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p592-order-confirmation-status-reporting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order Confirmation Amendment](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p612-order-confirmation-amendment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p630-bulk.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p650-bulk.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order Confirmation Cancellation](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p670-order-confirmation-cancellation.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p687-bulk.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p707-bulk.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order Confirmation Status Request](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p726-order-confirmation-status-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Individual Asset Transfer](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p805-individual-asset-transfer.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Two Account Owners – Direct – SLT Market Practice](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p828-two-account-owners-direct-slt-market-practice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Request for Transfer Status and Transfer Status](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p861-request-for-transfer-status-and-transfer-status.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Request for Status Rejection](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p871-request-for-status-rejection.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Price Reporting](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p900-price-reporting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Statements](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p915-statements.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `reda.001`, `reda.004`, `semt.002`, `sese.001`, `sese.003`, `sese.005`, `sese.007`, `sese.009`, `sese.010`, `sese.011`, `sese.012`, `sese.018`, `sese.019`, `setr.001`, `setr.003`, `setr.004`, `setr.006`, `setr.007`, `setr.009`, `setr.010`, `setr.012`, `setr.016`, `setr.017`, `setr.047`, `setr.049`, `setr.051`, `setr.053`, `setr.057`, `setr.058`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Transfer Agent`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000095](../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md).


<!-- FUNDS-CURATED-FLOW-0075-START -->
[Redemption cancellation — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p534-request-and-status-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0075.md)
<!-- FUNDS-CURATED-FLOW-0075-END -->

<!-- FUNDS-CURATED-FLOW-0076-START -->
[Redemption cancellation — intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p539-request-and-status-intermediary.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0076.md)
<!-- FUNDS-CURATED-FLOW-0076-END -->

<!-- FUNDS-CURATED-FLOW-0077-START -->
[Redemption cancellation — bulk and reinstruction](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p544-request-and-status-bulk.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0077.md)
<!-- FUNDS-CURATED-FLOW-0077-END -->

<!-- FUNDS-CURATED-FLOW-0078-START -->
[Switch cancellation — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p554-request-and-status-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0078.md)
<!-- FUNDS-CURATED-FLOW-0078-END -->

<!-- FUNDS-CURATED-FLOW-0079-START -->
[Switch cancellation — intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p558-request-and-status-intermediary.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0079.md)
<!-- FUNDS-CURATED-FLOW-0079-END -->

<!-- FUNDS-CURATED-FLOW-0084-START -->
[Subscription confirmation rejected by instructing party](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p597-subscription.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0084.md)
<!-- FUNDS-CURATED-FLOW-0084-END -->

<!-- FUNDS-CURATED-FLOW-0085-START -->
[Redemption confirmation rejected by instructing party](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p602-redemption.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0085.md)
<!-- FUNDS-CURATED-FLOW-0085-END -->

<!-- FUNDS-CURATED-FLOW-0086-START -->
[Switch confirmation rejected by instructing party](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p607-switch.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0086.md)
<!-- FUNDS-CURATED-FLOW-0086-END -->

<!-- FUNDS-CURATED-FLOW-0087-START -->
[Subscription confirmation amendment — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p619-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0087.md)
<!-- FUNDS-CURATED-FLOW-0087-END -->

<!-- FUNDS-CURATED-FLOW-0088-START -->
[Subscription confirmation amendment — intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p624-intermediary.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0088.md)
<!-- FUNDS-CURATED-FLOW-0088-END -->

<!-- FUNDS-CURATED-FLOW-0089-START -->
[Subscription confirmation amendment — bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p630-bulk.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0089.md)
<!-- FUNDS-CURATED-FLOW-0089-END -->

<!-- FUNDS-CURATED-FLOW-0090-START -->
[Redemption confirmation amendment — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p639-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0090.md)
<!-- FUNDS-CURATED-FLOW-0090-END -->

<!-- FUNDS-CURATED-FLOW-0091-START -->
[Redemption confirmation amendment — intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p644-intermediary.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0091.md)
<!-- FUNDS-CURATED-FLOW-0091-END -->

<!-- FUNDS-CURATED-FLOW-0092-START -->
[Redemption confirmation amendment — bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p650-bulk.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0092.md)
<!-- FUNDS-CURATED-FLOW-0092-END -->

<!-- FUNDS-CURATED-FLOW-0093-START -->
[Switch confirmation amendment — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p659-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0093.md)
<!-- FUNDS-CURATED-FLOW-0093-END -->

<!-- FUNDS-CURATED-FLOW-0094-START -->
[Switch confirmation amendment — intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p664-intermediary.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0094.md)
<!-- FUNDS-CURATED-FLOW-0094-END -->

<!-- FUNDS-CURATED-FLOW-0095-START -->
[Subscription confirmation cancellation — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p677-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0095.md)
<!-- FUNDS-CURATED-FLOW-0095-END -->

<!-- FUNDS-CURATED-FLOW-0096-START -->
[Subscription confirmation cancellation — intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p682-intermediary.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0096.md)
<!-- FUNDS-CURATED-FLOW-0096-END -->

<!-- FUNDS-CURATED-FLOW-0097-START -->
[Subscription confirmation cancellation — bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p687-bulk.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0097.md)
<!-- FUNDS-CURATED-FLOW-0097-END -->

<!-- FUNDS-CURATED-FLOW-0098-START -->
[Redemption confirmation cancellation — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p696-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0098.md)
<!-- FUNDS-CURATED-FLOW-0098-END -->

<!-- FUNDS-CURATED-FLOW-0099-START -->
[Redemption confirmation cancellation — intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p701-intermediary.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0099.md)
<!-- FUNDS-CURATED-FLOW-0099-END -->

<!-- FUNDS-CURATED-FLOW-0100-START -->
[Redemption confirmation cancellation — bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p707-bulk.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0100.md)
<!-- FUNDS-CURATED-FLOW-0100-END -->

<!-- FUNDS-CURATED-FLOW-0101-START -->
[Switch confirmation cancellation — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p716-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0101.md)
<!-- FUNDS-CURATED-FLOW-0101-END -->

<!-- FUNDS-CURATED-FLOW-0102-START -->
[Switch confirmation cancellation — intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p720-intermediary.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0102.md)
<!-- FUNDS-CURATED-FLOW-0102-END -->

<!-- FUNDS-CURATED-FLOW-0103-START -->
[Subscription amended-confirmation status query](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p731-subscription.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0103.md)
<!-- FUNDS-CURATED-FLOW-0103-END -->

<!-- FUNDS-CURATED-FLOW-0104-START -->
[Redemption amended-confirmation status query](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p738-redemption.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0104.md)
<!-- FUNDS-CURATED-FLOW-0104-END -->

<!-- FUNDS-CURATED-FLOW-0105-START -->
[Switch amended-confirmation status query](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p745-switch.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0105.md)
<!-- FUNDS-CURATED-FLOW-0105-END -->

<!-- FUNDS-CURATED-FLOW-0114-START -->
[Own-account asset transfer — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p811-own-account-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0114.md)
<!-- FUNDS-CURATED-FLOW-0114-END -->

<!-- FUNDS-CURATED-FLOW-0115-START -->
[Two-owner asset transfer — direct double leg](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p816-two-account-owners-direct-double-leg.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0115.md)
<!-- FUNDS-CURATED-FLOW-0115-END -->

<!-- FUNDS-CURATED-FLOW-0116-START -->
[Two-owner asset transfer — direct single leg](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p822-two-account-owners-direct-single-leg.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0116.md)
<!-- FUNDS-CURATED-FLOW-0116-END -->

<!-- FUNDS-CURATED-FLOW-0117-START -->
[Two-owner asset transfer — SLT market practice](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p828-two-account-owners-direct-slt-market-practice.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0117.md)
<!-- FUNDS-CURATED-FLOW-0117-END -->

<!-- FUNDS-CURATED-FLOW-0118-START -->
[Two-owner asset transfer — intermediary double leg](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p837-two-account-owners-intermediary-double-leg.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0118.md)
<!-- FUNDS-CURATED-FLOW-0118-END -->

<!-- FUNDS-CURATED-FLOW-0119-START -->
[Transfer-out confirmation reversal](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p843-transfer-out-reversal.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0119.md)
<!-- FUNDS-CURATED-FLOW-0119-END -->

<!-- FUNDS-CURATED-FLOW-0120-START -->
[Transfer-in confirmation reversal](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p848-transfer-in-reversal.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0120.md)
<!-- FUNDS-CURATED-FLOW-0120-END -->

<!-- FUNDS-CURATED-FLOW-0121-START -->
[Transfer-out instruction cancellation request](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p853-transfer-out-cancellation.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0121.md)
<!-- FUNDS-CURATED-FLOW-0121-END -->

<!-- FUNDS-CURATED-FLOW-0122-START -->
[Transfer-in instruction cancellation request](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p857-transfer-in-cancellation.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0122.md)
<!-- FUNDS-CURATED-FLOW-0122-END -->

<!-- FUNDS-CURATED-FLOW-0123-START -->
[Transfer instruction status query](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p867-request-for-status.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0123.md)
<!-- FUNDS-CURATED-FLOW-0123-END -->

<!-- FUNDS-CURATED-FLOW-0124-START -->
[Transfer instruction status query rejected](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p871-request-for-status-rejection.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0124.md)
<!-- FUNDS-CURATED-FLOW-0124-END -->

<!-- FUNDS-CURATED-FLOW-0125-START -->
[Unsolicited transfer instruction status — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p876-status-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0125.md)
<!-- FUNDS-CURATED-FLOW-0125-END -->

<!-- FUNDS-CURATED-FLOW-0126-START -->
[Unsolicited transfer instruction status — intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p881-status-intermediary.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0126.md)
<!-- FUNDS-CURATED-FLOW-0126-END -->

<!-- FUNDS-CURATED-FLOW-0127-START -->
[Transfer cancellation status query — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p886-cancellation-status-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0127.md)
<!-- FUNDS-CURATED-FLOW-0127-END -->

<!-- FUNDS-CURATED-FLOW-0128-START -->
[Transfer cancellation status query — intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p893-transfer-cancellation-status-intermediary.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0128.md)
<!-- FUNDS-CURATED-FLOW-0128-END -->

<!-- FUNDS-CURATED-FLOW-0129-START -->
[Price report](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p904-price-report.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0129.md)
<!-- FUNDS-CURATED-FLOW-0129-END -->

<!-- FUNDS-CURATED-FLOW-0130-START -->
[Complete price report cancellation](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p907-price-report-cancellation-complete.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0130.md)
<!-- FUNDS-CURATED-FLOW-0130-END -->

<!-- FUNDS-CURATED-FLOW-0131-START -->
[Partial price cancellation and correction](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p911-price-report-cancellation-partial-and-correction.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0131.md)
<!-- FUNDS-CURATED-FLOW-0131-END -->

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

<!-- FUNDS-PROCESS-fig-0001 -->
[Investment Funds communication scope](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0001.md)
<!-- /FUNDS-PROCESS-fig-0001 -->

<!-- FUNDS-PROCESS-fig-0002 -->
[Business roles and functional participants](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0002.md)
<!-- /FUNDS-PROCESS-fig-0002 -->

<!-- FUNDS-PROCESS-fig-0015 -->
[Transfer Flow — Single Leg (from transfer agent perspective)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0015.md) · [Flow responsibilities](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p221-stock-transfers-single-leg-transfer.md)
<!-- /FUNDS-PROCESS-fig-0015 -->

<!-- FUNDS-PROCESS-fig-0016 -->
[Transfer — Single Leg (Transferor instructing)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0016.md) · [Flow responsibilities](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p226-portfolio-and-stock-transfers-single-leg.md)
<!-- /FUNDS-PROCESS-fig-0016 -->

<!-- FUNDS-PROCESS-fig-0017 -->
[Transfer Flow — Double Leg (institution to institution)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0017.md) · [Flow responsibilities](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p230-portfolio-and-stock-transfers-double-matched-leg.md)
<!-- /FUNDS-PROCESS-fig-0017 -->

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

<!-- FUNDS-EARLY-FLOW-322 -->
[Fund Cash Forecast Reporting / Estimated and Confirmed Reporting  / Estimated](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p322-estimated.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-322 -->

<!-- FUNDS-EARLY-FLOW-325 -->
[Fund Cash Forecast Reporting / Estimated and Confirmed Reporting  / Estimated and Confirmed ](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p325-estimated-and-confirmed.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-325 -->

<!-- FUNDS-EARLY-FLOW-331 -->
[Fund Cash Forecast Reporting / Detailed Estimated and Confirmed  / Detailed Estimated](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p331-detailed-estimated.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-331 -->

<!-- FUNDS-EARLY-FLOW-334 -->
[Fund Cash Forecast Reporting / Detailed Estimated and Confirmed  / Detailed Estimated and Confirmed](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p334-detailed-estimated-and-confirmed.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-334 -->

<!-- FUNDS-EARLY-FLOW-340 -->
[Fund Cash Forecast Reporting / Cancellation and New / Confirmed, Cancellation and New Confirmed](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p340-confirmed-cancellation-and-new-confirmed.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-340 -->

<!-- FUNDS-EARLY-FLOW-344 -->
[Fund Cash Forecast Reporting / Cancellation and New / Detailed Confirmed, Cancellation and New Confirmed ](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p344-detailed-confirmed-cancellation-and-new-confirmed.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-344 -->

<!-- FUNDS-EARLY-FLOW-356 -->
[Fund Reference Data Reporting / Fund Reference Data Report – Unsolicited](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p356-fund-reference-data-report-unsolicited.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-356 -->

<!-- FUNDS-EARLY-FLOW-351 -->
[Fund Reference Data Reporting / Fund Reference Data Report – Solicited (requested)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p351-fund-reference-data-report-solicited-requested.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-351 -->

<!-- FUNDS-EARLY-FLOW-368 -->
[Order and Confirmation / Subscription  / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p368-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-368 -->

<!-- FUNDS-EARLY-FLOW-374 -->
[Order and Confirmation / Subscription  / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p374-intermediary.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-374 -->

<!-- FUNDS-EARLY-FLOW-381 -->
[Order and Confirmation / Subscription  / Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p381-bulk.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-381 -->

<!-- FUNDS-EARLY-FLOW-388 -->
[Order and Confirmation / Redemption / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p388-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-388 -->

<!-- FUNDS-EARLY-FLOW-394 -->
[Order and Confirmation / Redemption / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p394-intermediary.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-394 -->

<!-- FUNDS-EARLY-FLOW-400 -->
[Order and Confirmation / Redemption / Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p400-bulk.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-400 -->

<!-- FUNDS-EARLY-FLOW-407 -->
[Order and Confirmation / Switch  / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p407-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-407 -->

<!-- FUNDS-EARLY-FLOW-411 -->
[Order and Confirmation / Switch  / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p411-intermediary.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-411 -->

<!-- FUNDS-EARLY-FLOW-425 -->
[Order Instruction Status Reporting / Subscription / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p425-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-425 -->

<!-- FUNDS-EARLY-FLOW-445 -->
[Order Instruction Status Reporting / Redemption / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p445-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-445 -->

<!-- FUNDS-EARLY-FLOW-465 -->
[Order Instruction Status Reporting / Switch / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p465-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-465 -->

<!-- FUNDS-EARLY-FLOW-429 -->
[Order Instruction Status Reporting / Subscription / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p429-intermediary.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-429 -->

<!-- FUNDS-EARLY-FLOW-449 -->
[Order Instruction Status Reporting / Redemption / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p449-intermediary.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-449 -->

<!-- FUNDS-EARLY-FLOW-469 -->
[Order Instruction Status Reporting / Switch / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p469-intermediary.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-469 -->

<!-- FUNDS-EARLY-FLOW-436 -->
[Order Instruction Status Reporting / Subscription / Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p436-bulk.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-436 -->

<!-- FUNDS-EARLY-FLOW-456 -->
[Order Instruction Status Reporting / Redemption / Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p456-bulk.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-456 -->

<!-- FUNDS-EARLY-FLOW-476 -->
[Order Instruction Status Reporting / Order Instruction Status Request / Request Status of Subscription ](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p476-request-status-of-subscription.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-476 -->

<!-- FUNDS-EARLY-FLOW-481 -->
[Order Instruction Status Reporting / Order Instruction Status Request / Request Status of Redemption ](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p481-request-status-of-redemption.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-481 -->

<!-- FUNDS-EARLY-FLOW-486 -->
[Order Instruction Status Reporting / Order Instruction Status Request / Request Status of Switch](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p486-request-status-of-switch.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-486 -->

<!-- FUNDS-EARLY-FLOW-515 -->
[Order Cancellation and Status  / Subscription  / Request and Status - Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p515-request-and-status-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-515 -->

<!-- FUNDS-EARLY-FLOW-519 -->
[Order Cancellation and Status  / Subscription  / Request and Status - Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p519-request-and-status-intermediary.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-519 -->

<!-- FUNDS-EARLY-FLOW-524 -->
[Order Cancellation and Status  / Subscription  / Request and Status - Bulk ](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p524-request-and-status-bulk.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-524 -->
