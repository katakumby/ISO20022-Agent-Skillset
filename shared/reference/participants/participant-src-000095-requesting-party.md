---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095", "src-000096"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
participant_id: "participant-src-000095-requesting-party"
title: "Requesting Party"
source_labels: ["Report User", "Requesting Party", "report users"]
role_type: "Functional participant in reporting"
aliases: ["Report User"]
source_locations: [{"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reconciliation (Statements)", "Custody and Accounting"], "locator": "/w:document/w:body/w:tbl[41]/w:tr[2]", "paragraph_id": null, "table_id": "T41"}, {"source_id": "src-000095", "locator": "T18 rows2–3; P211 figure11; P217 figure13; P219 figure14"}, {"source_id": "src-000096", "heading": "15 reda.004.001.07 FundReferenceDataReportV07", "file_pages": [291], "evidence_id": "src-000096-reda.004.001.07-p291-c005"}]
flows: ["flow-src-000095-p209-reporting", "flow-src-000095-p216-custody-and-accounting"]
process_sections: []
message_ids: ["reda.004.001.07"]
message_families: ["reda.004"]
search_terms: ["Requesting Party", "reda.001", "reda.002"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000095-p209-reporting", "flow-src-000095-p216-custody-and-accounting", "flow-src-000095-p322-estimated", "flow-src-000095-p325-estimated-and-confirmed", "flow-src-000095-p331-detailed-estimated", "flow-src-000095-p334-detailed-estimated-and-confirmed", "flow-src-000095-p340-confirmed-cancellation-and-new-confirmed", "flow-src-000095-p344-detailed-confirmed-cancellation-and-new-confirmed", "flow-src-000095-p351-fund-reference-data-report-solicited-requested", "flow-src-000095-p356-fund-reference-data-report-unsolicited"]
---































# Requesting Party

Business context: Investment Funds. Source classification: activity participant; classification not established.

## Definition

In reporting, the Instructing Party is the Report User or Requesting Party (T18 row2). Figure13 explicitly pairs Requesting Party/Report User; figure11 uses Report User. A report user may receive scheduled push reporting without sending a request (T41).

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Request Statement | The requesting party (where the "pull" scenario is supported), sends a request for a statement. | Initiator | [T41](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0041.md) row 2 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Reporting](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p209-reporting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Custody and Accounting](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p216-custody-and-accounting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `reda.001`, `reda.002`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Requesting Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000095](../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx).

<!-- FUNDS-REPORT-ALIASES -->
## Source-supported reporting labels

In reporting, the Instructing Party is the Report User or Requesting Party (T18 row2). Figure13 explicitly pairs Requesting Party/Report User; figure11 uses Report User. A report user may receive scheduled push reporting without sending a request (T41).

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




<!-- FUNCTIONALITY-ALIASES-src-000096 -->
## Additional literal publication labels

Plural spelling of Report User; the source quote retains the reporting context and does not assert that every report is solicited.

| Source label | Source context |
| --- | --- |
| report users | src-000096-reda.004.001.07-p291-c005 |


> in a request / response environment, with the InvestmentFundReportRequest, for example, initiated by report users (data vendors, professional investors, regulators or investment fund distributors) in enabling the user to control the flow and updates of information.

src-000096, file pages291; 15 reda.004.001.07 FundReferenceDataReportV07.

<!-- /FUNCTIONALITY-ALIASES-src-000096 -->
