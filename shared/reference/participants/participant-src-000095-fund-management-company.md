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
participant_id: "participant-src-000095-fund-management-company"
title: "Fund Management Company"
source_labels: ["Fund Management Company"]
role_type: "Institutional source example"
aliases: []
source_locations: [{"source_id": "src-000095", "locator": "P109 figure1"}, {"source_id": "src-000095", "locator": "P109 figure1; T19 Transfer Agent row"}]
flow_ids: ["flow-src-000095-p322-estimated", "flow-src-000095-p325-estimated-and-confirmed", "flow-src-000095-p331-detailed-estimated", "flow-src-000095-p334-detailed-estimated-and-confirmed", "flow-src-000095-p340-confirmed-cancellation-and-new-confirmed", "flow-src-000095-p344-detailed-confirmed-cancellation-and-new-confirmed", "flow-src-000095-p351-fund-reference-data-report-solicited-requested", "flow-src-000095-p356-fund-reference-data-report-unsolicited"]
message_ids: []
limitations: ["Scoped to the supplied Investment Funds source; same-name roles in other publications are not merged.", "No identifier scheme is specified in the cited evidence."]
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative/table/figure labels inspected; no independent institutional equivalence inferred."}
---



















# Fund Management Company

[src-000095](../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx)

## Definition and context

Institution named together with Promoter and Transfer Agent in the communication-scope figure; the source does not give this grouping a merged participant identity. (P109 figure1)

Source classification: Institutional source example. A functional role varies with the relationship; institutional examples do not fix the role for every process.

## Responsibilities and actions

Appears as a source endpoint for FundReferenceData sent to the institutional-investor/custodian/distributor grouping. T19 states that the transfer agent is appointed by the fund management company. (P109 figure1; T19 Transfer Agent row)

## Relationships

- [transfer agent](participant-src-000095-transfer-agent.md)

## Flows and messages



Message names in the cited source identify business exchanges; exact definitions are resolved through the message-set index.

## Identification and limitations

- Scoped to the supplied Investment Funds source; same-name roles in other publications are not merged.
- No identifier scheme is specified in the cited evidence.

<!-- FUNDS-CURATED-FLOW-0129-START -->
[Price report](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p904-price-report.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0129.md)
<!-- FUNDS-CURATED-FLOW-0129-END -->

<!-- FUNDS-CURATED-FLOW-0130-START -->
[Complete price report cancellation](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p907-price-report-cancellation-complete.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0130.md)
<!-- FUNDS-CURATED-FLOW-0130-END -->

<!-- FUNDS-CURATED-FLOW-0131-START -->
[Partial price cancellation and correction](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p911-price-report-cancellation-partial-and-correction.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0131.md)
<!-- FUNDS-CURATED-FLOW-0131-END -->

<!-- FUNDS-PROCESS-fig-0001 -->
[Investment Funds communication scope](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0001.md)
<!-- /FUNDS-PROCESS-fig-0001 -->

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
