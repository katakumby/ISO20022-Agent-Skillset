---
template: false
document_kind: "participant"
review_status: "reviewed"
manual_curated: true
domain: "shared"
domains: ["securities"]
source_ids: ["src-000095", "src-000096"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
participant_id: "participant-src-000095-professional-investor"
title: "professional investor"
source_labels: ["professional investor", "professional investors"]
role_type: "Narrative example of a functional reporting/account role"
aliases: []
flow_ids: ["flow-src-000095-p351-fund-reference-data-report-solicited-requested", "flow-src-000095-p356-fund-reference-data-report-unsolicited"]
message_ids: ["reda.004.001.07"]
source_locations: [{"source_id": "src-000095", "locator": "P350; Fund Reference Data Reporting"}, {"source_id": "src-000096", "heading": "15 reda.004.001.07 FundReferenceDataReportV07", "file_pages": [291], "evidence_id": "src-000096-reda.004.001.07-p291-c005"}]
limitations: ["No institutional identity or identifier scheme is established beyond the cited narrative.", "Example participation does not assign the same function in every relationship."]
review_evidence: {"date": "2026-11-09", "scope": "Cited source narrative inspected."}
message_families: ["reda.004"]
---













# professional investor

[src-000095](../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md); P350; Fund Reference Data Reporting.

## Definition and context

Example of a report user receiving investment-fund reference data. This label is not automatically equated with Institutional Investor.

## Responsibilities and relationships

The source presents this participant as an example of [requesting party](participant-src-000095-requesting-party.md). Actual sender/receiver responsibility is assigned by the flow, not by the institutional label alone.

## Flows and messages

Applicable account-management/reporting flows cite the narrative. No direction is inferred solely from this example label.

## Identification and limitations

No identifier scheme is specified in this cited scope; source-supported examples are kept separate from functional definitions.

<!-- FUNDS-EARLY-FLOW-356 -->
[Fund Reference Data Reporting / Fund Reference Data Report – Unsolicited](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p356-fund-reference-data-report-unsolicited.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-356 -->

<!-- FUNDS-EARLY-FLOW-351 -->
[Fund Reference Data Reporting / Fund Reference Data Report – Solicited (requested)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p351-fund-reference-data-report-solicited-requested.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-351 -->




<!-- FUNCTIONALITY-ALIASES-src-000096 -->
## Additional literal publication labels

Plural spelling of the same source-defined business-role label in report-recipient examples.

| Source label | Source context |
| --- | --- |
| professional investors | src-000096-reda.004.001.07-p291-c005 |


> in a request / response environment, with the InvestmentFundReportRequest, for example, initiated by report users (data vendors, professional investors, regulators or investment fund distributors) in enabling the user to control the flow and updates of information.

src-000096, file pages291; 15 reda.004.001.07 FundReferenceDataReportV07.

<!-- /FUNCTIONALITY-ALIASES-src-000096 -->
