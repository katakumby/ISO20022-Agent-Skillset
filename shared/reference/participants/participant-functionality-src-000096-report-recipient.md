---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["securities"]
participant_id: "participant-functionality-src-000096-report-recipient"
title: "report recipient — Investment Funds Functionality"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
source_labels: ["report recipient"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["investment-funds"]
message_ids: ["reda.001.001.05", "reda.002.001.05", "reda.004.001.07"]
message_families: ["reda.001", "reda.002", "reda.004"]
source_locations: [{"source_id": "src-000096", "heading": "13 reda.001.001.05 PriceReportV05", "file_pages": [159], "evidence_id": "src-000096-reda.001.001.05-p159-c001"}, {"source_id": "src-000096", "heading": "13 reda.001.001.05 PriceReportV05", "file_pages": [159], "evidence_id": "src-000096-reda.001.001.05-p159-c002"}, {"source_id": "src-000096", "heading": "14 reda.002.001.05 PriceReportCancellationV05", "file_pages": [222], "evidence_id": "src-000096-reda.002.001.05-p222-c001"}, {"source_id": "src-000096", "heading": "15 reda.004.001.07 FundReferenceDataReportV07", "file_pages": [291], "evidence_id": "src-000096-reda.004.001.07-p291-c001"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
---

# report recipient — Investment Funds Functionality

[src-000096](../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf)

## Definition and business context

Recipient-side reporting role in the quoted investment-funds messages, including source-defined institutional examples. It does not establish a requirement to have requested the report.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000096-reda.001.001.05-p159-c001

src-000096, file page 159; 13 reda.001.001.05 PriceReportV05.

> A report provider, for example, a transfer agent, fund accountant or market data provider, sends the PriceReport message to the report recipient, for example, a fund management company, transfer agent, market data provider, regulator or any other interested party to provide the net asset value and price information for financial instruments on specific trade dates and, optionally, to quote price variation information.

### src-000096-reda.001.001.05-p159-c002

src-000096, file page 159; 13 reda.001.001.05 PriceReportV05.

> The PriceReport message is sent by the report provider to the report recipient to:

### src-000096-reda.002.001.05-p222-c001

src-000096, file page 222; 14 reda.002.001.05 PriceReportCancellationV05.

> A report provider, for example, a transfer agent, fund accountant or market data provider, sends the PriceReportCancellation message to the report recipient, for example, a fund management company, transfer agent, market data provider, regulator or any other interested party to cancel previously sent prices.

### src-000096-reda.004.001.07-p291-c001

src-000096, file page 291; 15 reda.004.001.07 FundReferenceDataReportV07.

> The FundReferenceDataReport message is sent by a report provider, for example, a fund promoter, fund management company, transfer agent, or market data provider to the report recipient, for example, a professional investor, investment fund distributor, market data provider, regulator or other interested party, to provide the key reference data for financial instruments to facilitate trading.

## Applicable exact messages


- [reda.001.001.05](../../../domains/securities/reference/messages/reda.001.001.05/roles.md)
- [reda.002.001.05](../../../domains/securities/reference/messages/reda.002.001.05/roles.md)
- [reda.004.001.07](../../../domains/securities/reference/messages/reda.004.001.07/roles.md)

## Identity and unresolved scope

Source labels: report recipient. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.
