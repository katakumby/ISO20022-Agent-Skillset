---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320", "src-000321"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
participant_id: "participant-src-000320-nca"
title: "NCA"
source_labels: ["NCA", "all national competent authorities", "national competent authorities", "national competent authority"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[3]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000321", "heading": "3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02", "file_pages": [15], "evidence_id": "src-000321-auth.017.001.02-p15-c001"}, {"source_id": "src-000321", "heading": "4 auth.031.001.01 FinancialInstrumentReportingStatusAdviceV01", "file_pages": [39], "evidence_id": "src-000321-auth.031.001.01-p39-c001"}, {"source_id": "src-000321", "heading": "5 auth.032.001.01 FinancialInstrumentReportingEquityTransparencyDataReportV01", "file_pages": [48], "evidence_id": "src-000321-auth.032.001.01-p48-c001"}, {"source_id": "src-000321", "heading": "6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "file_pages": [55], "evidence_id": "src-000321-auth.033.001.03-p55-c001"}, {"source_id": "src-000321", "heading": "7 auth.035.001.01 FinancialInstrumentReportingTradingVolumeCapDataReportV01", "file_pages": [85], "evidence_id": "src-000321-auth.035.001.01-p85-c001"}, {"source_id": "src-000321", "heading": "8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03", "file_pages": [91], "evidence_id": "src-000321-auth.036.001.03-p91-c001"}, {"source_id": "src-000321", "heading": "10 auth.040.001.01 FinancialInstrumentReportingEquityTradingActivityReportV01", "file_pages": [170], "evidence_id": "src-000321-auth.040.001.01-p170-c001"}, {"source_id": "src-000321", "heading": "11 auth.041.001.01 FinancialInstrumentReportingNonEquityTradingActivityReportV01", "file_pages": [178], "evidence_id": "src-000321-auth.041.001.01-p178-c001"}, {"source_id": "src-000321", "heading": "12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02", "file_pages": [184], "evidence_id": "src-000321-auth.042.001.02-p184-c001"}, {"source_id": "src-000321", "heading": "13 auth.043.001.01 FinancialInstrumentReportingReferenceDataIndexReportV01", "file_pages": [211], "evidence_id": "src-000321-auth.043.001.01-p211-c001"}, {"source_id": "src-000321", "heading": "15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03", "file_pages": [227], "evidence_id": "src-000321-auth.045.001.03-p227-c001"}, {"source_id": "src-000321", "heading": "19 auth.050.001.01 FinancialInstrumentReportingInstrumentClassificationReportV01", "file_pages": [259], "evidence_id": "src-000321-auth.050.001.01-p259-c001"}, {"source_id": "src-000321", "heading": "21 auth.102.001.01 FinancialInstrumentReportingCancellationReportV01", "file_pages": [268], "evidence_id": "src-000321-auth.102.001.01-p268-c001"}, {"source_id": "src-000321", "heading": "16 auth.047.001.01 FinancialInstrumentReportingCountryCodeReportV01", "file_pages": [244], "evidence_id": "src-000321-auth.047.001.01-p244-c001"}, {"source_id": "src-000321", "heading": "17 auth.048.001.01 FinancialInstrumentReportingCurrencyCodeReportV01", "file_pages": [247], "evidence_id": "src-000321-auth.048.001.01-p247-c001"}, {"source_id": "src-000321", "heading": "18 auth.049.001.02 FinancialInstrumentReportingMarketIdentificationCodeReportV02", "file_pages": [252], "evidence_id": "src-000321-auth.049.001.02-p252-c002"}]
flows: []
process_sections: []
message_ids: ["auth.017.001.02", "auth.031.001.01", "auth.032.001.01", "auth.033.001.03", "auth.035.001.01", "auth.036.001.03", "auth.040.001.01", "auth.041.001.01", "auth.042.001.02", "auth.043.001.01", "auth.045.001.03", "auth.047.001.01", "auth.048.001.01", "auth.049.001.02", "auth.050.001.01", "auth.102.001.01"]
message_families: ["auth.017", "auth.031", "auth.032", "auth.033", "auth.035", "auth.036", "auth.040", "auth.041", "auth.042", "auth.043", "auth.045", "auth.047", "auth.048", "auth.049", "auth.050", "auth.102"]
search_terms: ["NCA"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---









# NCA

Business context: Transactions and Financial Instruments Data Reporting. Source classification: business role.

## Definition

National Competent Authority of each EEA member state.

Evidence: [T11](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0011.md), source row 3.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Reporting Entity](participant-src-000320-reporting-entity.md) | [T12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0012.md) row 10, column 2 |
| Can play the functional participant role in this source context | [Competent Authority](participant-src-000320-competent-authority.md) | [T12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0012.md) row 10, column 3 |
| Can play the functional participant role in this source context | [Supervisory Authority](participant-src-000320-supervisory-authority.md) | [T12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0012.md) row 10, column 4 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `NCA`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000320](../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx).




<!-- FUNCTIONALITY-ALIASES-src-000321 -->
## Additional literal publication labels

T11 row3 of source320 explicitly expands NCA as National Competent Authority. Source321 uses the full singular/plural labels; the quantifier all remains a qualifier in the quoted distribution scope.

| Source label | Source context |
| --- | --- |
| national competent authority | src-000321-auth.017.001.02-p15-c001; src-000321-auth.031.001.01-p39-c001; src-000321-auth.032.001.01-p48-c001; src-000321-auth.033.001.03-p55-c001; src-000321-auth.035.001.01-p85-c001; src-000321-auth.036.001.03-p91-c001; src-000321-auth.040.001.01-p170-c001; src-000321-auth.041.001.01-p178-c001; src-000321-auth.042.001.02-p184-c001; src-000321-auth.045.001.03-p227-c001; src-000321-auth.102.001.01-p268-c001 |
| national competent authorities | src-000321-auth.043.001.01-p211-c001; src-000321-auth.047.001.01-p244-c001; src-000321-auth.048.001.01-p247-c001; src-000321-auth.049.001.02-p252-c002; src-000321-auth.050.001.01-p259-c001 |
| all national competent authorities | src-000321-auth.050.001.01-p259-c001 |


> This FinancialInstrumentReportingReferenceDataReport message is sent by the trading venue to the national competent authority to report on the reference data used in the securities transactions.

src-000321, file pages15; 3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02.

> The FinancialInstrumentReportingStatusAdvice message is sent by the national competent authority to the reporting agent to provide a status advice for the correctness, issues or errors that arise from the submitted report.

src-000321, file pages39; 4 auth.031.001.01 FinancialInstrumentReportingStatusAdviceV01.

> The FinancialInstrumentReportingEquityTransparencyDataReport message is sent by the trading venues to the national competent authority to report on the transparency data for equity financial instruments.

src-000321, file pages48; 5 auth.032.001.01 FinancialInstrumentReportingEquityTransparencyDataReportV01.

> The FinancialInstrumentReportingNonEquityTransparencyDataReport message is sent by the trading venue to the national competent authority to submit non equity specific details as part of classifying and applying necessary transparency non equity computations.

src-000321, file pages55; 6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03.

> The FinancialInstrumentReportingTradingVolumeCapDataReport message is sent by the trading venue to the national competent authority to report the total volume of trading and volumes of trading under reference price waiver and negotiated transactions waiver.

src-000321, file pages85; 7 auth.035.001.01 FinancialInstrumentReportingTradingVolumeCapDataReportV01.

> The FinancialInstrumentReportingReferenceDataDeltaReport message is sent by the trading venues to the national competent authority to report on changes that have occurred in the base data between reference data file generation.

src-000321, file pages91; 8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03.

> The FinancialInstrumentReportingEquityTradingActivityReport message is sent by the trading venue to the national competent authority to report on equity specific trading activity data, used for the transparency calculations.

src-000321, file pages170; 10 auth.040.001.01 FinancialInstrumentReportingEquityTradingActivityReportV01.

> The FinancialInstrumentReportingNonEquityTradingActivityReport message is sent by the trading venue to the national competent authority to report on non-equity specific trading activity aggregated quantitative data, used for the transparency calculations.

src-000321, file pages178; 11 auth.041.001.01 FinancialInstrumentReportingNonEquityTradingActivityReportV01.

> The FinancialInstrumentReportingInvalidReferenceDataReport message is sent by the trading venue to the national competent authority to report on all records that have become invalid based on updates that have been received or that have passed the termination date original set for the instrument.

src-000321, file pages184; 12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02.

> This FinancialInstrumentReportingReferenceDataIndexReport message is sent by National Competent Authorities to express an interest in receiving data on European indices.

src-000321, file pages211; 13 auth.043.001.01 FinancialInstrumentReportingReferenceDataIndexReportV01.

> The FinancialInstrumentReportingNonEquityTradingActivityResult message is sent by the trading venue to the national competent authority to report on computed results data of non-equity specific trading activity.

src-000321, file pages227; 15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03.

> The FinancialInstrumentReportingCountryCodeReport message provides the details of the two character country codes and is created by ESMA for distribution to national competent authorities.

src-000321, file pages244; 16 auth.047.001.01 FinancialInstrumentReportingCountryCodeReportV01.

> The MiFIRCurrencyCodeReport message provides the details the ISO 4217 currency codes and is created by ESMA for distribution to National Competent Authorities.

src-000321, file pages247; 17 auth.048.001.01 FinancialInstrumentReportingCurrencyCodeReportV01.

> This message is generated by ESMA for distribution to national competent authorities.

src-000321, file pages252; 18 auth.049.001.02 FinancialInstrumentReportingMarketIdentificationCodeReportV02.

> The FinancialInstrumentReportingInstrumentClassificationReport message is sent by ESMA to all national competent authorities and provides all valid combinations for classification of financial instruments (CFI) as per ISO 10962.

src-000321, file pages259; 19 auth.050.001.01 FinancialInstrumentReportingInstrumentClassificationReportV01.

> This FinancialInstrumentReportingCancellationReport message is sent by the trading venue to the national competent authority to cancel reference data previously reported by mistake.

src-000321, file pages268; 21 auth.102.001.01 FinancialInstrumentReportingCancellationReportV01.

<!-- /FUNCTIONALITY-ALIASES-src-000321 -->
