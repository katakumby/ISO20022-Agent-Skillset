---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p198-data-distribution-business-transaction"
title: "Reference data distribution"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Data Distribution BusinessTransaction "], "locator": "/w:document/w:body/w:p[198]", "paragraph_id": "P198", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Data Distribution BusinessTransaction "], "locator": "/w:document/w:body/w:p[199]", "paragraph_id": "P199", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Data Distribution BusinessTransaction "], "locator": "/w:document/w:body/w:p[200]", "paragraph_id": "P200", "table_id": null}]
participants: ["participant-src-000320-competent-authority", "participant-src-000320-public", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority", "participant-src-000320-third-party-systems"]
message_mapping_evidence: []
message_ids: ["auth.017.001.02", "auth.036.001.03", "auth.043.001.01", "auth.042.001.02", "auth.039.001.01", "auth.047.001.01", "auth.048.001.01", "auth.050.001.01", "auth.049.001.02"]
message_families: ["auth.017", "auth.036", "auth.043", "auth.042", "auth.039", "auth.047", "auth.048", "auth.050", "auth.049"]
search_terms: ["Data Distribution BusinessTransaction", "Supervisory Authority", "ESMA"]
limitations: ["The source consider operator has no native Mermaid sequence equivalent. A shaded group plus an explicit note retains the exact operator and label; it is not recast as opt or a mandatory publication schedule.", "ReferenceDataIndexReport occurs twice from SA to CA and both arrows are retained. The two final arrows go to Public (full report, then delta report). The Reporting Entity lifeline is present but has no connected arrow in this picture.", "Request Data and Download Data are explicitly out of scope. No ISO message identifier is assigned to those arrows.", "Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.", "The described flow is scoped to this publication; it is not advice on current regulation."]
participant_ids: ["participant-src-000320-competent-authority", "participant-src-000320-public", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority", "participant-src-000320-third-party-systems"]
manual_curated: true
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0023.md"]
---

# Reference data distribution

[src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx); BusinessTransactions / Data Distribution BusinessTransaction .

## Purpose, trigger, preconditions and outcomes

Source process definition [T14](../documents/src-000320/tables/tbl-0014.md) (the overall process conditions also apply to its reporting variant):

| Item | Description |
| --- | --- |
| Definition | A Supervisory Authority receives instruments reference data and shares it with other Business Participants. |
| Trigger | Daily upon reception of data from Entities reporting instruments reference data. |
| Pre-conditions | ESMA has received and generated a complete list of all instruments admitted to trading that are still valid or where a request for admission to trading has been made in the EEA. ESMA has generated all appropriate additional files. |
| Post-conditions | All data has been distributed to CAs for them to integrate within their systems as required. |
| Role | Supervisory Authority |


## Participants and responsibilities

- [Public](../../../../../../../shared/reference/participants/participant-src-000320-public.md)
- [Reporting Entity](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md)
- [Competent Authority](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md)
- [Supervisory Authority](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md)
- [3rd Party Systems](../../../../../../../shared/reference/participants/participant-src-000320-third-party-systems.md)

Initiation and responsibility follow the explicit message directions and narrative below; a participant appearing on a lifeline is not automatically a sender.

## Ordered exchanges and decision points

| Order | Sender | Receiver | Literal source message / exchange | Source condition or fragment |
| --- | --- | --- | --- | --- |
| 1 | Supervisory Authority | 3rd Party Systems | Request Data (Out of Scope) | Outside conditional frame |
| 2 | 3rd Party Systems | Supervisory Authority | Download Data (Out of Scope) | Outside conditional frame |
| 3 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingReferenceDataReport | Outside conditional frame |
| 4 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingReferenceDataDeltaReport | Outside conditional frame |
| 5 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingReferenceDataIndexReport | Outside conditional frame |
| 6 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingInvalidReferenceDataReport | Outside conditional frame |
| 7 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingReferenceDataIndexReport | Outside conditional frame |
| 8 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingNonWorkingDayReport | rgb(248, 245, 235) |
| 9 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingCountryCodeReport | rgb(248, 245, 235) |
| 10 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingCurrencyCodeReport | rgb(248, 245, 235) |
| 11 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingInstrumentClassificationReport | rgb(248, 245, 235) |
| 12 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingMarketIdentificationCodeReport | rgb(248, 245, 235) |
| 13 | Supervisory Authority | Public | FinancialInstrumentReportingReferenceDataReport | Outside conditional frame |
| 14 | Supervisory Authority | Public | FinancialInstrumentReportingReferenceDataDeltaReport | Outside conditional frame |


[Reconstructed sequence and retained original](../diagrams/fitrr-sequences/fig-0023.md)

## Source narrative and additional participants

**P199** To ensure the correct operation of transparency, transaction reporting and trading / double volume cap, the supervisory authority, ESMA, distributes to the CAs an amalgamated version of the reference data (removing duplicates, instrument inconsistencies, etc.) along with additional data sets that ESMA has used as part of its message validation operations. The additional datasets are expected to change infrequently so it is possible to consider distributing these at a different frequency to the reference data. As per the MiFIR / MiFID II directive, ESMA makes the data available to the Public (IFs, REs, academics, etc.). This can be in the form of a download on a website or a webservice query.

## Supplied message definitions

- [auth.017.001.02 — FinancialInstrumentReportingReferenceDataReportV02](../../../../messages/auth.017.001.02/index.md)
- [auth.036.001.03 — FinancialInstrumentReportingReferenceDataDeltaReportV03](../../../../messages/auth.036.001.03/index.md)
- [auth.043.001.01 — FinancialInstrumentReportingReferenceDataIndexReportV01](../../../../messages/auth.043.001.01/index.md)
- [auth.042.001.02 — FinancialInstrumentReportingInvalidReferenceDataReportV02](../../../../messages/auth.042.001.02/index.md)
- [auth.039.001.01 — FinancialInstrumentReportingNonWorkingDayReportV01](../../../../messages/auth.039.001.01/index.md)
- [auth.047.001.01 — FinancialInstrumentReportingCountryCodeReportV01](../../../../messages/auth.047.001.01/index.md)
- [auth.048.001.01 — FinancialInstrumentReportingCurrencyCodeReportV01](../../../../messages/auth.048.001.01/index.md)
- [auth.050.001.01 — FinancialInstrumentReportingInstrumentClassificationReportV01](../../../../messages/auth.050.001.01/index.md)
- [auth.049.001.02 — FinancialInstrumentReportingMarketIdentificationCodeReportV02](../../../../messages/auth.049.001.02/index.md)

Family mappings are grounded in Part1 tables T4–T9 and the matching supplied message catalog. The figure names remain literal; a family link does not turn an unversioned diagram into evidence for a particular schema version.

## Alternative and exceptional paths

The source conditions and narrative above define the applicable alternatives. Repeated arrows and all error branches are retained; no additional cancellation or reversal route is invented.

## Limitations

- The source consider operator has no native Mermaid sequence equivalent. A shaded group plus an explicit note retains the exact operator and label; it is not recast as opt or a mandatory publication schedule.
- ReferenceDataIndexReport occurs twice from SA to CA and both arrows are retained. The two final arrows go to Public (full report, then delta report). The Reporting Entity lifeline is present but has no connected arrow in this picture.
- Request Data and Download Data are explicitly out of scope. No ISO message identifier is assigned to those arrows.
- Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.
- The described flow is scoped to this publication; it is not advice on current regulation.
