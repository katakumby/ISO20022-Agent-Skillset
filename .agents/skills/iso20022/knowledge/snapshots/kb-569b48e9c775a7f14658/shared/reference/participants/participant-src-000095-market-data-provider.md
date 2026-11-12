---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
participant_id: "participant-src-000095-market-data-provider"
title: "Market Data Provider"
source_labels: ["Market Data Provider"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[19]/w:tr[4]", "paragraph_id": null, "table_id": "T19"}]
flows: []
process_sections: ["flow-src-000095-p315-fund-cash-forecast-reporting", "flow-src-000095-p348-fund-reference-data-reporting", "flow-src-000095-p900-price-reporting"]
message_ids: []
message_families: ["reda.001", "reda.004"]
search_terms: ["Market Data Provider", "reda.001", "reda.004"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000095-p322-estimated", "flow-src-000095-p325-estimated-and-confirmed", "flow-src-000095-p331-detailed-estimated", "flow-src-000095-p334-detailed-estimated-and-confirmed", "flow-src-000095-p340-confirmed-cancellation-and-new-confirmed", "flow-src-000095-p344-detailed-confirmed-cancellation-and-new-confirmed", "flow-src-000095-p351-fund-reference-data-report-solicited-requested", "flow-src-000095-p356-fund-reference-data-report-unsolicited"]
---



















# Market Data Provider

Business context: Investment Funds. Source classification: business role.

## Definition

Source of financial information. It provides financial news and data (for example, facts, statistics and analysis), for professional and individual investors through various media (for example, the Internet, magazine).

Evidence: [T19](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0019.md), source row 4.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Executing Party](participant-src-000095-executing-party.md) | [T20](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0020.md) row 5, column 4 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Fund Cash Forecast Reporting](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p315-fund-cash-forecast-reporting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Fund Reference Data Reporting](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p348-fund-reference-data-reporting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Price Reporting](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p900-price-reporting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `reda.001`, `reda.004`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Market Data Provider`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000095](../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md).

<!-- FUNDS-CURATED-FLOW-0129-START -->
[Price report](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p904-price-report.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0129.md)
<!-- FUNDS-CURATED-FLOW-0129-END -->

<!-- FUNDS-CURATED-FLOW-0130-START -->
[Complete price report cancellation](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p907-price-report-cancellation-complete.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0130.md)
<!-- FUNDS-CURATED-FLOW-0130-END -->

<!-- FUNDS-CURATED-FLOW-0131-START -->
[Partial price cancellation and correction](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p911-price-report-cancellation-partial-and-correction.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0131.md)
<!-- FUNDS-CURATED-FLOW-0131-END -->

<!-- FUNDS-PROCESS-fig-0002 -->
[Business roles and functional participants](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0002.md)
<!-- /FUNDS-PROCESS-fig-0002 -->

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
