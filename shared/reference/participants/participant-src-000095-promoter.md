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
participant_id: "participant-src-000095-promoter"
title: "Promoter"
source_labels: ["Promoter"]
role_type: "Institutional source example"
aliases: []
source_locations: [{"source_id": "src-000095", "locator": "P109 figure1"}, {"source_id": "src-000095", "locator": "P109 figure1"}]
flow_ids: []
message_ids: []
limitations: ["Scoped to the supplied Investment Funds source; same-name roles in other publications are not merged.", "No identifier scheme is specified in the cited evidence."]
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative/table/figure labels inspected; no independent institutional equivalence inferred."}
---



# Promoter

[src-000095](../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx)

## Definition and context

Promoter is named alongside Fund Management Company and Transfer Agent in the communication-scope figure. A standalone definition is not supplied in this view. (P109 figure1)

Source classification: Institutional source example. A functional role varies with the relationship; institutional examples do not fix the role for every process.

## Responsibilities and actions

Appears within the source endpoint for FundReferenceData; the figure does not allocate separate responsibilities among the three labels. (P109 figure1)

## Relationships

- [fund management company](participant-src-000095-fund-management-company.md)
- [transfer agent](participant-src-000095-transfer-agent.md)

## Flows and messages



Message names in the cited source identify business exchanges; exact definitions are resolved through the message-set index.

## Identification and limitations

- Scoped to the supplied Investment Funds source; same-name roles in other publications are not merged.
- No identifier scheme is specified in the cited evidence.

<!-- FUNDS-PROCESS-fig-0001 -->
[Investment Funds communication scope](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0001.md)
<!-- /FUNDS-PROCESS-fig-0001 -->
