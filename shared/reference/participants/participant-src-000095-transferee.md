---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
participant_id: "participant-src-000095-transferee"
title: "Transferee"
source_labels: ["Transferee"]
role_type: "activity participant; classification not established"
aliases: []
source_locations: [{"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", " Portfolio and Stock Transfers (Single Leg)"], "locator": "/w:document/w:body/w:tbl[44]/w:tr[5]", "paragraph_id": null, "table_id": "T44"}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", " Portfolio and Stock Transfers (Single Leg)"], "locator": "/w:document/w:body/w:tbl[44]/w:tr[7]", "paragraph_id": null, "table_id": "T44"}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Portfolio and Stock Transfers (Double/Matched Leg)"], "locator": "/w:document/w:body/w:tbl[45]/w:tr[3]", "paragraph_id": null, "table_id": "T45"}]
flows: ["flow-src-000095-p221-stock-transfers-single-leg-transfer", "flow-src-000095-p226-portfolio-and-stock-transfers-single-leg", "flow-src-000095-p230-portfolio-and-stock-transfers-double-matched-leg"]
process_sections: ["flow-src-000095-p759-portfolio-transfer-management", "flow-src-000095-p764-discovery", "flow-src-000095-p768-portfolio-transfer-instruction", "flow-src-000095-p779-rejected", "flow-src-000095-p783-request-status", "flow-src-000095-p789-cancellation", "flow-src-000095-p794-rejected-cancellation-invalid-reference", "flow-src-000095-p799-rejected-cancellation-already-executed", "flow-src-000095-p828-two-account-owners-direct-slt-market-practice"]
message_ids: []
message_families: ["semt.001", "sese.001", "sese.003", "sese.005", "sese.007", "sese.009", "sese.010", "sese.011", "sese.012", "sese.013", "sese.014", "sese.018", "sese.019", "sese.043"]
search_terms: ["Transferee", "semt.001", "sese.001", "sese.003", "sese.005", "sese.007", "sese.009", "sese.010", "sese.011", "sese.012", "sese.013", "sese.014", "sese.018", "sese.019", "sese.043"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000095-p226-portfolio-and-stock-transfers-single-leg", "flow-src-000095-p230-portfolio-and-stock-transfers-double-matched-leg"]
---







# Transferee

Business context: Investment Funds. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Record Asserts to be Received | The assets to be received are recorded by the transferee. The transferee requests its intermediary for the receiving chain account holding information. | Initiator | [T44](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0044.md) row 5 |
| Advice Receiving Account Information | The transferee notifies the transferor of the receiving chain account holding information. | Initiator | [T44](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0044.md) row 7 |
| Instruct Transfer | The transfer in instruction is sent by the transferee to its transfer agent. | Initiator | [T45](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0045.md) row 3 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Stock Transfers (Single Leg Transfer)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p221-stock-transfers-single-leg-transfer.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Portfolio and Stock Transfers (Single Leg)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p226-portfolio-and-stock-transfers-single-leg.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Portfolio and Stock Transfers (Double/Matched Leg)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p230-portfolio-and-stock-transfers-double-matched-leg.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Portfolio Transfer Management](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p759-portfolio-transfer-management.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Discovery](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p764-discovery.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Portfolio Transfer Instruction](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p768-portfolio-transfer-instruction.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Rejected](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p779-rejected.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Request Status](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p783-request-status.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Cancellation](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p789-cancellation.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Rejected Cancellation - Invalid Reference](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p794-rejected-cancellation-invalid-reference.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Rejected Cancellation – Already Executed](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p799-rejected-cancellation-already-executed.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Two Account Owners – Direct – SLT Market Practice](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p828-two-account-owners-direct-slt-market-practice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `semt.001`, `sese.001`, `sese.003`, `sese.005`, `sese.007`, `sese.009`, `sese.010`, `sese.011`, `sese.012`, `sese.013`, `sese.014`, `sese.018`, `sese.019`, `sese.043`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Transferee`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000095](../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx).








<!-- FUNDS-CURATED-FLOW-0107-START -->
[Portfolio transfer discovery](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p764-discovery.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0107.md)
<!-- FUNDS-CURATED-FLOW-0107-END -->

<!-- FUNDS-CURATED-FLOW-0108-START -->
[Portfolio transfer instruction and completion](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p768-portfolio-transfer-instruction.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0108.md)
<!-- FUNDS-CURATED-FLOW-0108-END -->

<!-- FUNDS-CURATED-FLOW-0109-START -->
[Portfolio transfer instruction rejected](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p779-rejected.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0109.md)
<!-- FUNDS-CURATED-FLOW-0109-END -->

<!-- FUNDS-CURATED-FLOW-0110-START -->
[Portfolio transfer status query](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p783-request-status.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0110.md)
<!-- FUNDS-CURATED-FLOW-0110-END -->

<!-- FUNDS-CURATED-FLOW-0111-START -->
[Portfolio transfer cancellation accepted](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p789-cancellation.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0111.md)
<!-- FUNDS-CURATED-FLOW-0111-END -->

<!-- FUNDS-CURATED-FLOW-0112-START -->
[Portfolio transfer cancellation rejected for invalid reference](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p794-rejected-cancellation-invalid-reference.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0112.md)
<!-- FUNDS-CURATED-FLOW-0112-END -->

<!-- FUNDS-CURATED-FLOW-0113-START -->
[Portfolio transfer cancellation rejected after execution](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p799-rejected-cancellation-already-executed.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0113.md)
<!-- FUNDS-CURATED-FLOW-0113-END -->

<!-- FUNDS-CURATED-FLOW-0117-START -->
[Two-owner asset transfer — SLT market practice](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p828-two-account-owners-direct-slt-market-practice.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0117.md)
<!-- FUNDS-CURATED-FLOW-0117-END -->

<!-- FUNDS-PROCESS-fig-0001 -->
[Investment Funds communication scope](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0001.md)
<!-- /FUNDS-PROCESS-fig-0001 -->

<!-- FUNDS-PROCESS-fig-0016 -->
[Transfer — Single Leg (Transferor instructing)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0016.md) · [Flow responsibilities](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p226-portfolio-and-stock-transfers-single-leg.md)
<!-- /FUNDS-PROCESS-fig-0016 -->

<!-- FUNDS-PROCESS-fig-0017 -->
[Transfer Flow — Double Leg (institution to institution)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0017.md) · [Flow responsibilities](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p230-portfolio-and-stock-transfers-double-matched-leg.md)
<!-- /FUNDS-PROCESS-fig-0017 -->
