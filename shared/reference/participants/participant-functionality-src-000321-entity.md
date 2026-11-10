---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["securities"]
participant_id: "participant-functionality-src-000321-entity"
title: "entity — Transactions and Financial Instruments Data Reporting Functionality"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
source_labels: ["entity"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["fitrr"]
message_ids: ["auth.044.001.03"]
message_families: ["auth.044"]
source_locations: [{"source_id": "src-000321", "heading": "14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03", "file_pages": [217], "evidence_id": "src-000321-auth.044.001.03-p217-c001"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
---

# entity — Transactions and Financial Instruments Data Reporting Functionality

[src-000321](../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf)

## Definition and business context

Entity named as a user of FinancialInstrumentReportingEquityTradingActivityResult to provide computed equity trading-activity results; its institution type remains unspecified.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000321-auth.044.001.03-p217-c001

src-000321, file page 217; 14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03.

> The FinancialInstrumentReportingEquityTradingActivityResult message is used by an entity or an authority to provide information on computed results data of an equity specific trading activity.

## Applicable exact messages


- [auth.044.001.03](../../../domains/securities/reference/messages/auth.044.001.03/roles.md)

## Identity and unresolved scope

Source labels: entity. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.
