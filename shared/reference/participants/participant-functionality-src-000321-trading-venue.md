---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["securities"]
participant_id: "participant-functionality-src-000321-trading-venue"
title: "trading venue — Transactions and Financial Instruments Data Reporting Functionality"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
source_labels: ["trading venue", "trading venues"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["fitrr"]
message_ids: ["auth.017.001.02", "auth.032.001.01", "auth.033.001.03", "auth.035.001.01", "auth.036.001.03", "auth.040.001.01", "auth.041.001.01", "auth.042.001.02", "auth.045.001.03", "auth.049.001.02", "auth.102.001.01"]
message_families: ["auth.017", "auth.032", "auth.033", "auth.035", "auth.036", "auth.040", "auth.041", "auth.042", "auth.045", "auth.049", "auth.102"]
source_locations: [{"source_id": "src-000321", "heading": "3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02", "file_pages": [15], "evidence_id": "src-000321-auth.017.001.02-p15-c001"}, {"source_id": "src-000321", "heading": "5 auth.032.001.01 FinancialInstrumentReportingEquityTransparencyDataReportV01", "file_pages": [48], "evidence_id": "src-000321-auth.032.001.01-p48-c001"}, {"source_id": "src-000321", "heading": "6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "file_pages": [55], "evidence_id": "src-000321-auth.033.001.03-p55-c001"}, {"source_id": "src-000321", "heading": "7 auth.035.001.01 FinancialInstrumentReportingTradingVolumeCapDataReportV01", "file_pages": [85], "evidence_id": "src-000321-auth.035.001.01-p85-c001"}, {"source_id": "src-000321", "heading": "8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03", "file_pages": [91], "evidence_id": "src-000321-auth.036.001.03-p91-c001"}, {"source_id": "src-000321", "heading": "10 auth.040.001.01 FinancialInstrumentReportingEquityTradingActivityReportV01", "file_pages": [170], "evidence_id": "src-000321-auth.040.001.01-p170-c001"}, {"source_id": "src-000321", "heading": "11 auth.041.001.01 FinancialInstrumentReportingNonEquityTradingActivityReportV01", "file_pages": [178], "evidence_id": "src-000321-auth.041.001.01-p178-c001"}, {"source_id": "src-000321", "heading": "12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02", "file_pages": [184], "evidence_id": "src-000321-auth.042.001.02-p184-c001"}, {"source_id": "src-000321", "heading": "15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03", "file_pages": [227], "evidence_id": "src-000321-auth.045.001.03-p227-c001"}, {"source_id": "src-000321", "heading": "18 auth.049.001.02 FinancialInstrumentReportingMarketIdentificationCodeReportV02", "file_pages": [252], "evidence_id": "src-000321-auth.049.001.02-p252-c001"}, {"source_id": "src-000321", "heading": "21 auth.102.001.01 FinancialInstrumentReportingCancellationReportV01", "file_pages": [268], "evidence_id": "src-000321-auth.102.001.01-p268-c001"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
---

# trading venue — Transactions and Financial Instruments Data Reporting Functionality

[src-000321](../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf)

## Definition and business context

Reporting-side participant explicitly named for financial-instrument reference, transparency, activity, cancellation and related reporting. Its institutional type is not equated with one of the separate source business roles.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000321-auth.017.001.02-p15-c001

src-000321, file page 15; 3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02.

> This FinancialInstrumentReportingReferenceDataReport message is sent by the trading venue to the national competent authority to report on the reference data used in the securities transactions.

### src-000321-auth.032.001.01-p48-c001

src-000321, file page 48; 5 auth.032.001.01 FinancialInstrumentReportingEquityTransparencyDataReportV01.

> The FinancialInstrumentReportingEquityTransparencyDataReport message is sent by the trading venues to the national competent authority to report on the transparency data for equity financial instruments.

### src-000321-auth.033.001.03-p55-c001

src-000321, file page 55; 6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03.

> The FinancialInstrumentReportingNonEquityTransparencyDataReport message is sent by the trading venue to the national competent authority to submit non equity specific details as part of classifying and applying necessary transparency non equity computations.

### src-000321-auth.035.001.01-p85-c001

src-000321, file page 85; 7 auth.035.001.01 FinancialInstrumentReportingTradingVolumeCapDataReportV01.

> The FinancialInstrumentReportingTradingVolumeCapDataReport message is sent by the trading venue to the national competent authority to report the total volume of trading and volumes of trading under reference price waiver and negotiated transactions waiver.

### src-000321-auth.036.001.03-p91-c001

src-000321, file page 91; 8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03.

> The FinancialInstrumentReportingReferenceDataDeltaReport message is sent by the trading venues to the national competent authority to report on changes that have occurred in the base data between reference data file generation.

### src-000321-auth.040.001.01-p170-c001

src-000321, file page 170; 10 auth.040.001.01 FinancialInstrumentReportingEquityTradingActivityReportV01.

> The FinancialInstrumentReportingEquityTradingActivityReport message is sent by the trading venue to the national competent authority to report on equity specific trading activity data, used for the transparency calculations.

### src-000321-auth.041.001.01-p178-c001

src-000321, file page 178; 11 auth.041.001.01 FinancialInstrumentReportingNonEquityTradingActivityReportV01.

> The FinancialInstrumentReportingNonEquityTradingActivityReport message is sent by the trading venue to the national competent authority to report on non-equity specific trading activity aggregated quantitative data, used for the transparency calculations.

### src-000321-auth.042.001.02-p184-c001

src-000321, file page 184; 12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02.

> The FinancialInstrumentReportingInvalidReferenceDataReport message is sent by the trading venue to the national competent authority to report on all records that have become invalid based on updates that have been received or that have passed the termination date original set for the instrument.

### src-000321-auth.045.001.03-p227-c001

src-000321, file page 227; 15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03.

> The FinancialInstrumentReportingNonEquityTradingActivityResult message is sent by the trading venue to the national competent authority to report on computed results data of non-equity specific trading activity.

### src-000321-auth.049.001.02-p252-c001

src-000321, file page 252; 18 auth.049.001.02 FinancialInstrumentReportingMarketIdentificationCodeReportV02.

> The FinancialInstrumentReportingMarket IdentificationCodeReport provides the valid market identification code (MIC) of venues that are valid and registered to operate as a trading venue.

### src-000321-auth.102.001.01-p268-c001

src-000321, file page 268; 21 auth.102.001.01 FinancialInstrumentReportingCancellationReportV01.

> This FinancialInstrumentReportingCancellationReport message is sent by the trading venue to the national competent authority to cancel reference data previously reported by mistake.

## Applicable exact messages


- [auth.017.001.02](../../../domains/securities/reference/messages/auth.017.001.02/roles.md)
- [auth.032.001.01](../../../domains/securities/reference/messages/auth.032.001.01/roles.md)
- [auth.033.001.03](../../../domains/securities/reference/messages/auth.033.001.03/roles.md)
- [auth.035.001.01](../../../domains/securities/reference/messages/auth.035.001.01/roles.md)
- [auth.036.001.03](../../../domains/securities/reference/messages/auth.036.001.03/roles.md)
- [auth.040.001.01](../../../domains/securities/reference/messages/auth.040.001.01/roles.md)
- [auth.041.001.01](../../../domains/securities/reference/messages/auth.041.001.01/roles.md)
- [auth.042.001.02](../../../domains/securities/reference/messages/auth.042.001.02/roles.md)
- [auth.045.001.03](../../../domains/securities/reference/messages/auth.045.001.03/roles.md)
- [auth.049.001.02](../../../domains/securities/reference/messages/auth.049.001.02/roles.md)
- [auth.102.001.01](../../../domains/securities/reference/messages/auth.102.001.01/roles.md)

## Identity and unresolved scope

Source labels: trading venue, trading venues. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.
