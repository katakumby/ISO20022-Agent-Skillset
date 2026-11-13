---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
participant_id: "participant-src-000095-executing-party"
title: "Executing Party"
source_labels: ["Executing Party"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[18]/w:tr[3]", "paragraph_id": null, "table_id": "T18"}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Order Processing"], "locator": "/w:document/w:body/w:tbl[40]/w:tr[6]", "paragraph_id": null, "table_id": "T40"}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Order Processing"], "locator": "/w:document/w:body/w:tbl[40]/w:tr[9]", "paragraph_id": null, "table_id": "T40"}]
flows: ["flow-src-000095-p187-order-execution", "flow-src-000095-p205-account-opening", "flow-src-000095-p207-account-modification", "flow-src-000095-p212-order-processing", "flow-src-000095-p221-stock-transfers-single-leg-transfer", "flow-src-000095-p226-portfolio-and-stock-transfers-single-leg", "flow-src-000095-p230-portfolio-and-stock-transfers-double-matched-leg"]
process_sections: ["flow-src-000095-p360-order-and-confirmation", "flow-src-000095-p368-direct", "flow-src-000095-p374-intermediary", "flow-src-000095-p381-bulk", "flow-src-000095-p388-direct", "flow-src-000095-p394-intermediary", "flow-src-000095-p400-bulk", "flow-src-000095-p407-direct", "flow-src-000095-p411-intermediary", "flow-src-000095-p415-order-instruction-status-reporting", "flow-src-000095-p425-direct", "flow-src-000095-p429-intermediary", "flow-src-000095-p436-bulk", "flow-src-000095-p445-direct", "flow-src-000095-p449-intermediary", "flow-src-000095-p456-bulk", "flow-src-000095-p465-direct", "flow-src-000095-p469-intermediary", "flow-src-000095-p476-request-status-of-subscription", "flow-src-000095-p481-request-status-of-redemption", "flow-src-000095-p486-request-status-of-switch", "flow-src-000095-p491-scenarios-for-confirmations-when-multiple-orders-specified-in-a-single", "flow-src-000095-p504-order-cancellation-and-status", "flow-src-000095-p515-request-and-status-direct", "flow-src-000095-p519-request-and-status-intermediary", "flow-src-000095-p524-request-and-status-bulk", "flow-src-000095-p534-request-and-status-direct", "flow-src-000095-p539-request-and-status-intermediary", "flow-src-000095-p544-request-and-status-bulk", "flow-src-000095-p554-request-and-status-direct", "flow-src-000095-p558-request-and-status-intermediary", "flow-src-000095-p563-order-cancellation-status-request", "flow-src-000095-p569-request-status-of-subscription", "flow-src-000095-p575-request-status-of-redemption", "flow-src-000095-p581-status-request-rejected", "flow-src-000095-p586-request-status-of-switch", "flow-src-000095-p592-order-confirmation-status-reporting", "flow-src-000095-p597-subscription", "flow-src-000095-p602-redemption", "flow-src-000095-p607-switch", "flow-src-000095-p612-order-confirmation-amendment", "flow-src-000095-p619-direct", "flow-src-000095-p624-intermediary", "flow-src-000095-p630-bulk", "flow-src-000095-p639-direct", "flow-src-000095-p644-intermediary", "flow-src-000095-p650-bulk", "flow-src-000095-p659-direct", "flow-src-000095-p664-intermediary", "flow-src-000095-p670-order-confirmation-cancellation", "flow-src-000095-p677-direct", "flow-src-000095-p682-intermediary", "flow-src-000095-p687-bulk", "flow-src-000095-p696-direct", "flow-src-000095-p701-intermediary", "flow-src-000095-p707-bulk", "flow-src-000095-p716-direct", "flow-src-000095-p720-intermediary", "flow-src-000095-p726-order-confirmation-status-request", "flow-src-000095-p731-subscription", "flow-src-000095-p738-redemption", "flow-src-000095-p745-switch", "flow-src-000095-p752-message-rejection", "flow-src-000095-p764-discovery", "flow-src-000095-p768-portfolio-transfer-instruction", "flow-src-000095-p779-rejected", "flow-src-000095-p783-request-status", "flow-src-000095-p789-cancellation", "flow-src-000095-p794-rejected-cancellation-invalid-reference", "flow-src-000095-p799-rejected-cancellation-already-executed", "flow-src-000095-p805-individual-asset-transfer", "flow-src-000095-p811-own-account-direct", "flow-src-000095-p816-two-account-owners-direct-double-leg", "flow-src-000095-p822-two-account-owners-direct-single-leg", "flow-src-000095-p837-two-account-owners-intermediary-double-leg", "flow-src-000095-p843-transfer-out-reversal", "flow-src-000095-p848-transfer-in-reversal", "flow-src-000095-p853-transfer-out-cancellation", "flow-src-000095-p857-transfer-in-cancellation", "flow-src-000095-p861-request-for-transfer-status-and-transfer-status", "flow-src-000095-p867-request-for-status", "flow-src-000095-p871-request-for-status-rejection", "flow-src-000095-p876-status-direct", "flow-src-000095-p881-status-intermediary", "flow-src-000095-p886-cancellation-status-direct", "flow-src-000095-p893-transfer-cancellation-status-intermediary"]
message_ids: []
message_families: ["acmt.001", "acmt.003", "semt.001", "sese.001", "sese.002", "sese.003", "sese.004", "sese.005", "sese.006", "sese.007", "sese.008", "sese.009", "sese.010", "sese.011", "sese.012", "sese.013", "sese.014", "sese.018", "sese.019", "sese.043", "setr.001", "setr.002", "setr.003", "setr.004", "setr.005", "setr.006", "setr.007", "setr.008", "setr.009", "setr.010", "setr.011", "setr.012", "setr.013", "setr.014", "setr.015", "setr.016", "setr.017", "setr.018", "setr.047", "setr.048", "setr.049", "setr.051", "setr.052", "setr.053", "setr.055", "setr.056", "setr.057", "setr.058"]
search_terms: ["Executing Party", "acmt.001", "acmt.003", "semt.001", "sese.001", "sese.002", "sese.003", "sese.004", "sese.005", "sese.006", "sese.007", "sese.008", "sese.009", "sese.010", "sese.011", "sese.012", "sese.013", "sese.014", "sese.018", "sese.019", "sese.043", "setr.001", "setr.002", "setr.003", "setr.004", "setr.005", "setr.006", "setr.007", "setr.008", "setr.009", "setr.010", "setr.011", "setr.012", "setr.013", "setr.014", "setr.015", "setr.016", "setr.017", "setr.018", "setr.047", "setr.048", "setr.049", "setr.051", "setr.052", "setr.053", "setr.055", "setr.056", "setr.057", "setr.058"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000095-p205-account-opening", "flow-src-000095-p207-account-modification", "flow-src-000095-p212-order-processing", "flow-src-000095-p368-direct", "flow-src-000095-p374-intermediary", "flow-src-000095-p381-bulk", "flow-src-000095-p388-direct", "flow-src-000095-p394-intermediary", "flow-src-000095-p400-bulk", "flow-src-000095-p407-direct", "flow-src-000095-p411-intermediary", "flow-src-000095-p425-direct", "flow-src-000095-p429-intermediary", "flow-src-000095-p436-bulk", "flow-src-000095-p445-direct", "flow-src-000095-p449-intermediary", "flow-src-000095-p456-bulk", "flow-src-000095-p465-direct", "flow-src-000095-p469-intermediary", "flow-src-000095-p476-request-status-of-subscription", "flow-src-000095-p481-request-status-of-redemption", "flow-src-000095-p486-request-status-of-switch", "flow-src-000095-p491-scenarios-for-confirmations-when-multiple-orders-specified-in-a-single", "flow-src-000095-p515-request-and-status-direct", "flow-src-000095-p519-request-and-status-intermediary", "flow-src-000095-p524-request-and-status-bulk"]
---























































# Executing Party

Business context: Investment Funds. Source classification: functional participant role.

## Definition

Party that receives an instruction or request and acts accordingly, for example, registers the instruction (for example, transfer agent, fund manager order desk). In the context of reporting this is the reporting party or report provider.

Evidence: [T18](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0018.md), source row 3.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Validation | The instruction (subscription/redemption) order is validated; the executing party can optionally send one or more status messages to the intermediary to keep the intermediary updated on progress so far. | Initiator | [T40](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0040.md) row 6 |
| Confirmation | If the instruction (subscription/redemption) order is accepted by the executing party, the details of the unit shares/price are notified by the executing party to the intermediary. | Initiator | [T40](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0040.md) row 9 |

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [Custodian](participant-src-000095-custodian.md) | [T20](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0020.md) row 2, column 4 |
| Business role listed for this functional participant | [ICSD](participant-src-000095-icsd.md) | [T20](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0020.md) row 3, column 4 |
| Business role listed for this functional participant | [CSD](participant-src-000095-csd.md) | [T20](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0020.md) row 4, column 4 |
| Business role listed for this functional participant | [Market Data Provider](participant-src-000095-market-data-provider.md) | [T20](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0020.md) row 5, column 4 |
| Business role listed for this functional participant | [Distributor](participant-src-000095-distributor.md) | [T20](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0020.md) row 9, column 4 |
| Business role listed for this functional participant | [Concentrator](participant-src-000095-concentrator.md) | [T20](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0020.md) row 10, column 4 |
| Business role listed for this functional participant | [Transfer Agent](participant-src-000095-transfer-agent.md) | [T20](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0020.md) row 11, column 4 |
| Business role listed for this functional participant | [Fund Accountant](participant-src-000095-fund-accountant.md) | [T20](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0020.md) row 12, column 4 |
| Business role listed for this functional participant | [Paying Agent](participant-src-000095-paying-agent.md) | [T20](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0020.md) row 13, column 4 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Order Execution](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p187-order-execution.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Account Opening](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p205-account-opening.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Account Modification](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p207-account-modification.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order Processing](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p212-order-processing.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Stock Transfers (Single Leg Transfer)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p221-stock-transfers-single-leg-transfer.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Portfolio and Stock Transfers (Single Leg)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p226-portfolio-and-stock-transfers-single-leg.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Portfolio and Stock Transfers (Double/Matched Leg)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p230-portfolio-and-stock-transfers-double-matched-leg.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order and Confirmation](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p360-order-and-confirmation.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p368-direct.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p374-intermediary.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p381-bulk.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p388-direct.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p394-intermediary.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p400-bulk.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p407-direct.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p411-intermediary.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order Instruction Status Reporting](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p415-order-instruction-status-reporting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p425-direct.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p429-intermediary.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p436-bulk.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p445-direct.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p449-intermediary.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p456-bulk.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p465-direct.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p469-intermediary.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Request Status of Subscription](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p476-request-status-of-subscription.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Request Status of Redemption](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p481-request-status-of-redemption.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Request Status of Switch](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p486-request-status-of-switch.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p491-scenarios-for-confirmations-when-multiple-orders-specified-in-a-single.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order Cancellation and Status](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p504-order-cancellation-and-status.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Request and Status - Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p515-request-and-status-direct.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Request and Status - Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p519-request-and-status-intermediary.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Request and Status - Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p524-request-and-status-bulk.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Request and Status - Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p534-request-and-status-direct.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Request and Status - Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p539-request-and-status-intermediary.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Request and Status - Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p544-request-and-status-bulk.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Request and Status - Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p554-request-and-status-direct.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Request and Status - Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p558-request-and-status-intermediary.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order Cancellation Status Request](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p563-order-cancellation-status-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Request Status of Subscription](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p569-request-status-of-subscription.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Request Status of Redemption](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p575-request-status-of-redemption.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Status Request Rejected](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p581-status-request-rejected.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Request Status of Switch](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p586-request-status-of-switch.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order Confirmation Status Reporting](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p592-order-confirmation-status-reporting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Subscription](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p597-subscription.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Redemption](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p602-redemption.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Switch](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p607-switch.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order Confirmation Amendment](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p612-order-confirmation-amendment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p619-direct.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p624-intermediary.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p630-bulk.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p639-direct.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p644-intermediary.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p650-bulk.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p659-direct.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p664-intermediary.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order Confirmation Cancellation](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p670-order-confirmation-cancellation.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p677-direct.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p682-intermediary.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p687-bulk.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p696-direct.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p701-intermediary.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p707-bulk.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p716-direct.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p720-intermediary.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order Confirmation Status Request](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p726-order-confirmation-status-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Subscription](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p731-subscription.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Redemption](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p738-redemption.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Switch](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p745-switch.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Message Rejection](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p752-message-rejection.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Discovery](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p764-discovery.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Portfolio Transfer Instruction](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p768-portfolio-transfer-instruction.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Rejected](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p779-rejected.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Request Status](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p783-request-status.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Cancellation](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p789-cancellation.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Rejected Cancellation - Invalid Reference](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p794-rejected-cancellation-invalid-reference.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Rejected Cancellation – Already Executed](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p799-rejected-cancellation-already-executed.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Individual Asset Transfer](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p805-individual-asset-transfer.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Own Account - Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p811-own-account-direct.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Two Account Owners – Direct – Double Leg](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p816-two-account-owners-direct-double-leg.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Two Account Owners – Direct – Single Leg](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p822-two-account-owners-direct-single-leg.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Two Account Owners – Intermediary - Double Leg](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p837-two-account-owners-intermediary-double-leg.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transfer Out Reversal](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p843-transfer-out-reversal.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transfer In Reversal](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p848-transfer-in-reversal.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transfer Out Cancellation](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p853-transfer-out-cancellation.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transfer In Cancellation](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p857-transfer-in-cancellation.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Request for Transfer Status and Transfer Status](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p861-request-for-transfer-status-and-transfer-status.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Request for Status](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p867-request-for-status.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Request for Status Rejection](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p871-request-for-status-rejection.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Status - Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p876-status-direct.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Status - Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p881-status-intermediary.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Cancellation Status – Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p886-cancellation-status-direct.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transfer Cancellation Status – Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p893-transfer-cancellation-status-intermediary.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `acmt.001`, `acmt.003`, `semt.001`, `sese.001`, `sese.002`, `sese.003`, `sese.004`, `sese.005`, `sese.006`, `sese.007`, `sese.008`, `sese.009`, `sese.010`, `sese.011`, `sese.012`, `sese.013`, `sese.014`, `sese.018`, `sese.019`, `sese.043`, `setr.001`, `setr.002`, `setr.003`, `setr.004`, `setr.005`, `setr.006`, `setr.007`, `setr.008`, `setr.009`, `setr.010`, `setr.011`, `setr.012`, `setr.013`, `setr.014`, `setr.015`, `setr.016`, `setr.017`, `setr.018`, `setr.047`, `setr.048`, `setr.049`, `setr.051`, `setr.052`, `setr.053`, `setr.055`, `setr.056`, `setr.057`, `setr.058`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Executing Party`. No external identifier scheme or alias equivalence has been inferred.

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

<!-- FUNDS-CURATED-FLOW-0080-START -->
[Subscription cancellation status query](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p569-request-status-of-subscription.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0080.md)
<!-- FUNDS-CURATED-FLOW-0080-END -->

<!-- FUNDS-CURATED-FLOW-0081-START -->
[Redemption cancellation status query](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p575-request-status-of-redemption.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0081.md)
<!-- FUNDS-CURATED-FLOW-0081-END -->

<!-- FUNDS-CURATED-FLOW-0082-START -->
[Redemption cancellation request rejected for invalid reference](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p581-status-request-rejected.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0082.md)
<!-- FUNDS-CURATED-FLOW-0082-END -->

<!-- FUNDS-CURATED-FLOW-0083-START -->
[Switch cancellation status query](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p586-request-status-of-switch.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0083.md)
<!-- FUNDS-CURATED-FLOW-0083-END -->

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

<!-- FUNDS-CURATED-FLOW-0106-START -->
[Transfer status request rejected for an unknown reference](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p752-message-rejection.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0106.md)
<!-- FUNDS-CURATED-FLOW-0106-END -->

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

<!-- FUNDS-PROCESS-fig-0002 -->
[Business roles and functional participants](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0002.md)
<!-- /FUNDS-PROCESS-fig-0002 -->

<!-- FUNDS-PROCESS-fig-0009 -->
[Account Opening Flow](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0009.md) · [Flow responsibilities](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p205-account-opening.md)
<!-- /FUNDS-PROCESS-fig-0009 -->

<!-- FUNDS-PROCESS-fig-0010 -->
[Account Modification Flow](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0010.md) · [Flow responsibilities](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p207-account-modification.md)
<!-- /FUNDS-PROCESS-fig-0010 -->

<!-- FUNDS-PROCESS-fig-0012 -->
[Order Flow with Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0012.md) · [Flow responsibilities](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p212-order-processing.md)
<!-- /FUNDS-PROCESS-fig-0012 -->

<!-- FUNDS-EARLY-FLOW-368 -->
[Order and Confirmation / Subscription  / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p368-direct.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-368 -->

<!-- FUNDS-EARLY-FLOW-374 -->
[Order and Confirmation / Subscription  / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p374-intermediary.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-374 -->

<!-- FUNDS-EARLY-FLOW-381 -->
[Order and Confirmation / Subscription  / Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p381-bulk.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-381 -->

<!-- FUNDS-EARLY-FLOW-388 -->
[Order and Confirmation / Redemption / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p388-direct.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-388 -->

<!-- FUNDS-EARLY-FLOW-394 -->
[Order and Confirmation / Redemption / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p394-intermediary.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-394 -->

<!-- FUNDS-EARLY-FLOW-400 -->
[Order and Confirmation / Redemption / Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p400-bulk.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-400 -->

<!-- FUNDS-EARLY-FLOW-407 -->
[Order and Confirmation / Switch  / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p407-direct.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-407 -->

<!-- FUNDS-EARLY-FLOW-411 -->
[Order and Confirmation / Switch  / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p411-intermediary.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-411 -->

<!-- FUNDS-EARLY-FLOW-425 -->
[Order Instruction Status Reporting / Subscription / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p425-direct.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-425 -->

<!-- FUNDS-EARLY-FLOW-445 -->
[Order Instruction Status Reporting / Redemption / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p445-direct.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-445 -->

<!-- FUNDS-EARLY-FLOW-465 -->
[Order Instruction Status Reporting / Switch / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p465-direct.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-465 -->

<!-- FUNDS-EARLY-FLOW-429 -->
[Order Instruction Status Reporting / Subscription / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p429-intermediary.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-429 -->

<!-- FUNDS-EARLY-FLOW-449 -->
[Order Instruction Status Reporting / Redemption / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p449-intermediary.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-449 -->

<!-- FUNDS-EARLY-FLOW-469 -->
[Order Instruction Status Reporting / Switch / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p469-intermediary.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-469 -->

<!-- FUNDS-EARLY-FLOW-436 -->
[Order Instruction Status Reporting / Subscription / Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p436-bulk.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-436 -->

<!-- FUNDS-EARLY-FLOW-456 -->
[Order Instruction Status Reporting / Redemption / Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p456-bulk.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-456 -->

<!-- FUNDS-EARLY-FLOW-476 -->
[Order Instruction Status Reporting / Order Instruction Status Request / Request Status of Subscription ](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p476-request-status-of-subscription.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-476 -->

<!-- FUNDS-EARLY-FLOW-481 -->
[Order Instruction Status Reporting / Order Instruction Status Request / Request Status of Redemption ](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p481-request-status-of-redemption.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-481 -->

<!-- FUNDS-EARLY-FLOW-486 -->
[Order Instruction Status Reporting / Order Instruction Status Request / Request Status of Switch](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p486-request-status-of-switch.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-486 -->

<!-- FUNDS-EARLY-FLOW-491 -->
[Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p491-scenarios-for-confirmations-when-multiple-orders-specified-in-a-single.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-491 -->

<!-- FUNDS-EARLY-FLOW-515 -->
[Order Cancellation and Status  / Subscription  / Request and Status - Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p515-request-and-status-direct.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-515 -->

<!-- FUNDS-EARLY-FLOW-519 -->
[Order Cancellation and Status  / Subscription  / Request and Status - Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p519-request-and-status-intermediary.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-519 -->

<!-- FUNDS-EARLY-FLOW-524 -->
[Order Cancellation and Status  / Subscription  / Request and Status - Bulk ](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p524-request-and-status-bulk.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-524 -->
