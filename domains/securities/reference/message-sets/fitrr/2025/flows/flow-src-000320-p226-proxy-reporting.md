---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p226-proxy-reporting"
title: "Trading activity — proxy reporting"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Trading Activity Report BusinessTransaction", "Proxy Reporting"], "locator": "/w:document/w:body/w:p[226]", "paragraph_id": "P226", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Trading Activity Report BusinessTransaction", "Proxy Reporting"], "locator": "/w:document/w:body/w:p[227]", "paragraph_id": "P227", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Trading Activity Report BusinessTransaction", "Proxy Reporting"], "locator": "/w:document/w:body/w:p[228]", "paragraph_id": "P228", "table_id": null}]
participants: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: ["auth.040.001.01", "auth.041.001.01", "auth.031.001.01"]
message_families: ["auth.040", "auth.041", "auth.031"]
search_terms: ["Proxy Reporting", "RE", "CA", "SA"]
limitations: ["Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.", "The described flow is scoped to this publication; it is not advice on current regulation."]
participant_ids: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
manual_curated: true
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0030.md"]
---

# Trading activity — proxy reporting

[src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx); BusinessTransactions / Trading Activity Report BusinessTransaction / Proxy Reporting.

## Purpose, trigger, preconditions and outcomes

Source process definition [T17](../documents/src-000320/tables/tbl-0017.md) (the overall process conditions also apply to its reporting variant):

| Item | Description |
| --- | --- |
| Definition | A Reporting Entity (RM, MTF, OTF, APA, CTP) must submit aggregated quantitative data in relation to the trading activity on the venue for each instrument admitted to trading and each trading day. |
| Trigger | Data is submitted daily. |
| Pre-conditions | Data is submitted with a 7 day lag (calendar days) to ensure cancelations and other operations have been processed as best as possible. |
| Post-conditions | Data related to all financial instruments traded on the venue pertaining to Transparency have been submitted to the CA / ESMA. |
| Role | Reporting Entity |


## Participants and responsibilities

- [Reporting Entity](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md)
- [Competent Authority](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md)
- [Supervisory Authority](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md)

The RE initiates its data submission; the CA or SA performs the checks assigned by the chosen reporting model. The ordered exchanges and source narrative below retain the actual responsible party.

## Ordered exchanges and decision points

| Order | Sender | Receiver | Literal source message / exchange | Source condition or fragment |
| --- | --- | --- | --- | --- |
| 1 | Reporting Entity | Competent Authority | FinancialInstrumentReportingEquityTradingActivityReport OR FinancialInstrumentReportingNonEquityTradingActivityReport | Outside conditional frame |
| 2 | Competent Authority | Supervisory Authority | FinancialInstrumentReportingEquityTradingActivityReport OR FinancialInstrumentReportingNonEquityTradingActivityReport | Competent Authority Validation Checks (Schema; Filename; Reporting Entity) — Validation Successful |
| 3 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingStatusAdvice | Competent Authority Validation Checks (Schema; Filename; Reporting Entity) — Validation Successful |
| 4 | Competent Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Competent Authority Validation Checks (Schema; Filename; Reporting Entity) — Validation Successful |
| 5 | Competent Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Validation Failure |


[Reconstructed sequence and retained original](../diagrams/fitrr-sequences/fig-0030.md)

## Source narrative and additional participants

**P222** For Transparency Trading Activity Report, two types of similar data will be submitted by the venues - Equity specific information and Non-Equity specific information. The information captured in these messages is quantitative in nature reflecting that it relates to the specific trading activity on instruments reported as part of Reference Data and Transparency Data Reporting. Within the submitted messages, a single Reporting Entity is not expected to submit both messages as they may not operate instruments in scope of a specific message e.g. they may trade only Equity or Non-Equity but not both.

**P227** This flow describes an RE submitting either an Equity or Non-Equity Transparency Trading Activity report to the SA via a CA. In this case, the CA performs high level checks ranging from naming convention checks through to schema validations. The CA is expected to either find the message conforms or it does not, it is not expected to perform detailed operations and message parsing. Once a message conforms, it is submitted to the SA resulting in a one-to-one mapping of conforming files to submitted files. Where a submission has been made to the SA, the CA shall expect a Status Advice detailing the results from the in-depth operations that are performed on the message. Where a message does not conform, the CA is to create the Status Advice to the submitting RE.

## Supplied message definitions

- [auth.040.001.01 — FinancialInstrumentReportingEquityTradingActivityReportV01](../../../../messages/auth.040.001.01/index.md)
- [auth.041.001.01 — FinancialInstrumentReportingNonEquityTradingActivityReportV01](../../../../messages/auth.041.001.01/index.md)
- [auth.031.001.01 — FinancialInstrumentReportingStatusAdviceV01](../../../../messages/auth.031.001.01/index.md)

Family mappings are grounded in Part1 tables T4–T9 and the matching supplied message catalog. The figure names remain literal; a family link does not turn an unversioned diagram into evidence for a particular schema version.

## Alternative and exceptional paths

The CA returns a failure status instead of forwarding a failed message. Successful validation forwards the report to the SA and returns the SA status through the CA.

## Limitations

- Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.
- The described flow is scoped to this publication; it is not advice on current regulation.
