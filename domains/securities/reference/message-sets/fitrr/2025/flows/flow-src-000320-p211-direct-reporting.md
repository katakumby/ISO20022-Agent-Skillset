---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p211-direct-reporting"
title: "Transparency data — direct reporting"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Transparency Data Report BusinessTransaction ", "Direct Reporting"], "locator": "/w:document/w:body/w:p[211]", "paragraph_id": "P211", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Transparency Data Report BusinessTransaction ", "Direct Reporting"], "locator": "/w:document/w:body/w:p[212]", "paragraph_id": "P212", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Transparency Data Report BusinessTransaction ", "Direct Reporting"], "locator": "/w:document/w:body/w:p[213]", "paragraph_id": "P213", "table_id": null}]
participants: ["participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: ["auth.032.001.01", "auth.033.001.03", "auth.031.001.01"]
message_families: ["auth.032", "auth.033", "auth.031"]
search_terms: ["Direct Reporting", "RE", "SA"]
limitations: ["Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.", "The described flow is scoped to this publication; it is not advice on current regulation."]
participant_ids: ["participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
manual_curated: true
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0026.md"]
---

# Transparency data — direct reporting

[src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx); BusinessTransactions / Transparency Data Report BusinessTransaction  / Direct Reporting.

## Purpose, trigger, preconditions and outcomes

Source process definition [T16](../documents/src-000320/tables/tbl-0016.md) (the overall process conditions also apply to its reporting variant):

| Item | Description |
| --- | --- |
| Definition | To support correct implementation of the transparency regime, specific transparency reference data must be submitted by a Reporting Entity (RM, MTF, OTF, APA, CTP) to ESMA. |
| Trigger | Data is submitted when the financial instrument is first traded or requested to trade has occurred<br>or<br>On a change to the data reported as part of the Transparency Reference Data |
| Pre-conditions | The financial instrument is registered on the reporting entities system. |
| Post-conditions | The reporting entity has submitted appropriate MiFIR specific additional reference data to ESMA. |
| Role | Reporting Entity |


## Participants and responsibilities

- [Reporting Entity](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md)
- [Supervisory Authority](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md)

The RE initiates its data submission; the CA or SA performs the checks assigned by the chosen reporting model. The ordered exchanges and source narrative below retain the actual responsible party.

## Ordered exchanges and decision points

| Order | Sender | Receiver | Literal source message / exchange | Source condition or fragment |
| --- | --- | --- | --- | --- |
| 1 | Reporting Entity | Supervisory Authority | FinancialInstrumentReportingEquityTransparencyDataReport OR FinancialInstrumentReportingNonEquityTransparencyDataReport | Outside conditional frame |
| 2 | Supervisory Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Outside conditional frame |


[Reconstructed sequence and retained original](../diagrams/fitrr-sequences/fig-0026.md)

## Source narrative and additional participants

**P210** For Transparency Data Report, two types of similar data will be submitted by the venues - Equity specific information and Non-Equity specific information. The overall flow is the same regardless of the type of instrument transparency reference data that is being submitted. Distinct messages were used as differences exist in the level of information captured per message. Within the submitted messages, a single Reporting Entity is not expected to submit both messages as they may not operate instruments in scope of a specific message e.g. they may trade only Equity or Non-Equity but not both.

**P212** This flow describes an RE submitting either an Equity or Non-Equity Transparency Data Reporting message directly to the SA. For each message submitted to the SA, a Status Advice message is generated.

## Supplied message definitions

- [auth.032.001.01 — FinancialInstrumentReportingEquityTransparencyDataReportV01](../../../../messages/auth.032.001.01/index.md)
- [auth.033.001.03 — FinancialInstrumentReportingNonEquityTransparencyDataReportV03](../../../../messages/auth.033.001.03/index.md)
- [auth.031.001.01 — FinancialInstrumentReportingStatusAdviceV01](../../../../messages/auth.031.001.01/index.md)

Family mappings are grounded in Part1 tables T4–T9 and the matching supplied message catalog. The figure names remain literal; a family link does not turn an unversioned diagram into evidence for a particular schema version.

## Alternative and exceptional paths

The source conditions and narrative above define the applicable alternatives. Repeated arrows and all error branches are retained; no additional cancellation or reversal route is invented.

## Limitations

- Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.
- The described flow is scoped to this publication; it is not advice on current regulation.
