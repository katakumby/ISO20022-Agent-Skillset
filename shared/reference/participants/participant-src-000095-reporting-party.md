---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
participant_id: "participant-src-000095-reporting-party"
title: "Reporting Party"
source_labels: ["Report Provider", "Reporting Party"]
role_type: "Functional participant in reporting"
aliases: ["Report Provider"]
source_locations: [{"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reporting"], "locator": "/w:document/w:body/w:tbl[39]/w:tr[2]", "paragraph_id": null, "table_id": "T39"}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reporting"], "locator": "/w:document/w:body/w:tbl[39]/w:tr[3]", "paragraph_id": null, "table_id": "T39"}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reporting"], "locator": "/w:document/w:body/w:tbl[39]/w:tr[4]", "paragraph_id": null, "table_id": "T39"}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reconciliation (Statements)", "Custody and Accounting"], "locator": "/w:document/w:body/w:tbl[41]/w:tr[3]", "paragraph_id": null, "table_id": "T41"}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reconciliation (Statements)", "Custody and Accounting"], "locator": "/w:document/w:body/w:tbl[41]/w:tr[4]", "paragraph_id": null, "table_id": "T41"}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reconciliation (Statements)", "Custody and Accounting"], "locator": "/w:document/w:body/w:tbl[41]/w:tr[5]", "paragraph_id": null, "table_id": "T41"}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reconciliation (Statements)", "Custody and Accounting"], "locator": "/w:document/w:body/w:tbl[41]/w:tr[6]", "paragraph_id": null, "table_id": "T41"}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reconciliation (Statements)", "Transparency of Holdings"], "locator": "/w:document/w:body/w:tbl[42]/w:tr[2]", "paragraph_id": null, "table_id": "T42"}, {"source_id": "src-000095", "locator": "T18 rows2–3; P211 figure11; P217 figure13; P219 figure14"}]
flows: ["flow-src-000095-p209-reporting", "flow-src-000095-p216-custody-and-accounting", "flow-src-000095-p218-transparency-of-holdings"]
process_sections: []
message_ids: []
message_families: ["reda.001", "reda.002", "semt.002"]
search_terms: ["Reporting Party", "reda.001", "reda.002", "semt.002"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000095-p209-reporting", "flow-src-000095-p216-custody-and-accounting", "flow-src-000095-p218-transparency-of-holdings", "flow-src-000095-p322-estimated", "flow-src-000095-p325-estimated-and-confirmed", "flow-src-000095-p331-detailed-estimated", "flow-src-000095-p334-detailed-estimated-and-confirmed", "flow-src-000095-p340-confirmed-cancellation-and-new-confirmed", "flow-src-000095-p344-detailed-confirmed-cancellation-and-new-confirmed", "flow-src-000095-p351-fund-reference-data-report-solicited-requested", "flow-src-000095-p356-fund-reference-data-report-unsolicited"]
---























# Reporting Party

Business context: Investment Funds. Source classification: activity participant; classification not established.

## Definition

In reporting, the Executing Party is the Reporting Party or Report Provider (T18 row3). Source activity lanes explicitly pair Reporting Party/Report Provider (figures11,13,14).

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Send Price Report | The reporting party sends a price report to the receiving party at the agreed frequency or in response to a request. | Initiator | [T39](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0039.md) row 2 |
| Send Cancellation | If a price report is found to have been issued in error or contains incorrect information, a price report cancellation message is sent by the reporting party to the requesting party specifying the reason for cancellation. | Initiator | [T39](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0039.md) row 3 |
| Send New Price Report | If the cancellation is because the price report contained incorrect information, the reporting party sends a new price report to the receiving party. | Initiator | [T39](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0039.md) row 4 |
| Status Received | If the request is not accepted by the reporting party, it sends a status message to the requesting party rejecting the request and specifying the reason for the rejection. | Initiator | [T41](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0041.md) row 3 |
| Send Statement | If the request is accepted by the reporting party, it sends a statement report to the requesting party in response to the request. In the "push" scenario, the reporting party sends a statement to the receiving party at the agreed frequency. | Initiator | [T41](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0041.md) row 4 |
| Send Cancellation | If the statement is found to have been issued in error or contains incorrect information, a statement cancellation message is sent by the reporting party to the requesting/receiving party specifying the reason for cancellation. | Initiator | [T41](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0041.md) row 5 |
| Send Statement | If the cancellation is because the statement contained incorrect information, the reporting party sends a new statement to the requesting/receiving party. | Initiator | [T41](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0041.md) row 6 |
| Generate Transparency Statement | The reporting party generates a statement of the holdings containing all holdings reported <br>from customers to their custodian, “downstream” in the custody chain, providing transparency of holdings of customers of the customers and compiled with the customers’ inbound statements “upstream” in the custody chain, like a regular custody statement of holdings, from a custodian to their customers, aggregated with the inbound statements received from the respective customers and enriched with the same customer data as is reported to the fund company/transfer agent.<br>The purposes that the transparency of holdings statement has been designed for include:<br>Disclosure of information about customers of customers<br>Verify/validate claims for retrocessions, rebates and commissions<br>Check compliance with laws, regulations and general terms and conditions.<br>Perform data analysis throughout custody chains, to identify geographic distribution patterns, measure the effects of targeted advertisement initiatives, and so on. | Initiator | [T42](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0042.md) row 2 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Reporting](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p209-reporting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Custody and Accounting](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p216-custody-and-accounting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transparency of Holdings](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p218-transparency-of-holdings.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `reda.001`, `reda.002`, `semt.002`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Reporting Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000095](../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx).

<!-- FUNDS-REPORT-ALIASES -->
## Source-supported reporting labels

In reporting, the Executing Party is the Reporting Party or Report Provider (T18 row3). Source activity lanes explicitly pair Reporting Party/Report Provider (figures11,13,14).

[T18 participant definitions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0018.md); these source-supported reporting aliases do not equate institutional roles.
<!-- /FUNDS-REPORT-ALIASES -->

<!-- FUNDS-CURATED-FLOW-0129-START -->
[Price report](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p904-price-report.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0129.md)
<!-- FUNDS-CURATED-FLOW-0129-END -->

<!-- FUNDS-CURATED-FLOW-0130-START -->
[Complete price report cancellation](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p907-price-report-cancellation-complete.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0130.md)
<!-- FUNDS-CURATED-FLOW-0130-END -->

<!-- FUNDS-CURATED-FLOW-0131-START -->
[Partial price cancellation and correction](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p911-price-report-cancellation-partial-and-correction.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0131.md)
<!-- FUNDS-CURATED-FLOW-0131-END -->

<!-- FUNDS-PROCESS-fig-0011 -->
[Reporting Flow](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0011.md) · [Flow responsibilities](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p209-reporting.md)
<!-- /FUNDS-PROCESS-fig-0011 -->

<!-- FUNDS-PROCESS-fig-0013 -->
[Statement Flow](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0013.md) · [Flow responsibilities](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p216-custody-and-accounting.md)
<!-- /FUNDS-PROCESS-fig-0013 -->

<!-- FUNDS-PROCESS-fig-0014 -->
[Report Transparency of Holdings](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0014.md) · [Flow responsibilities](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p218-transparency-of-holdings.md)
<!-- /FUNDS-PROCESS-fig-0014 -->

<!-- FUNDS-EARLY-FLOW-322 -->
[Fund Cash Forecast Reporting / Estimated and Confirmed Reporting  / Estimated](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p322-estimated.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-322 -->

<!-- FUNDS-EARLY-FLOW-325 -->
[Fund Cash Forecast Reporting / Estimated and Confirmed Reporting  / Estimated and Confirmed ](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p325-estimated-and-confirmed.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-325 -->

<!-- FUNDS-EARLY-FLOW-331 -->
[Fund Cash Forecast Reporting / Detailed Estimated and Confirmed  / Detailed Estimated](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p331-detailed-estimated.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-331 -->

<!-- FUNDS-EARLY-FLOW-334 -->
[Fund Cash Forecast Reporting / Detailed Estimated and Confirmed  / Detailed Estimated and Confirmed](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p334-detailed-estimated-and-confirmed.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-334 -->

<!-- FUNDS-EARLY-FLOW-340 -->
[Fund Cash Forecast Reporting / Cancellation and New / Confirmed, Cancellation and New Confirmed](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p340-confirmed-cancellation-and-new-confirmed.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-340 -->

<!-- FUNDS-EARLY-FLOW-344 -->
[Fund Cash Forecast Reporting / Cancellation and New / Detailed Confirmed, Cancellation and New Confirmed ](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p344-detailed-confirmed-cancellation-and-new-confirmed.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-344 -->

<!-- FUNDS-EARLY-FLOW-356 -->
[Fund Reference Data Reporting / Fund Reference Data Report – Unsolicited](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p356-fund-reference-data-report-unsolicited.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-356 -->

<!-- FUNDS-EARLY-FLOW-351 -->
[Fund Reference Data Reporting / Fund Reference Data Report – Solicited (requested)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p351-fund-reference-data-report-solicited-requested.md) — source figure sender/receiver.
<!-- /FUNDS-EARLY-FLOW-351 -->
