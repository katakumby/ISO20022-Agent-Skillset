---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p244-in-direct-reporting"
title: "Trading volume cap — indirect reporting"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Trading Volume Cap BusinessTransaction ", "In-Direct Reporting"], "locator": "/w:document/w:body/w:p[244]", "paragraph_id": "P244", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Trading Volume Cap BusinessTransaction ", "In-Direct Reporting"], "locator": "/w:document/w:body/w:p[245]", "paragraph_id": "P245", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Trading Volume Cap BusinessTransaction ", "In-Direct Reporting"], "locator": "/w:document/w:body/w:p[246]", "paragraph_id": "P246", "table_id": null}]
participants: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: ["auth.035.001.01", "auth.031.001.01"]
message_families: ["auth.035", "auth.031"]
search_terms: ["In-Direct Reporting", "RE", "CA", "SA"]
limitations: ["The source loop/first alternative covers the Reporting Entity and Competent Authority lifelines while report arrows and the inner alternative cross that frame boundary to the Supervisory Authority. Mermaid expands these frames to the participating lifelines. Conditions, all arrows, order and the crossing-frame feature are retained in text; frame geometry is not identical.", "T6 uses FinancialInstrumentsTradingVolumeCapDataReport while the picture uses FinancialInstrumentReportingTradingVolumeCapDataReport. The contextual family link auth.035 comes from T6; the source picture label is retained literally.", "Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.", "The described flow is scoped to this publication; it is not advice on current regulation."]
participant_ids: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
manual_curated: true
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0035.md"]
---

# Trading volume cap — indirect reporting

[src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx); BusinessTransactions / Trading Volume Cap BusinessTransaction  / In-Direct Reporting.

## Purpose, trigger, preconditions and outcomes

Source process definition [T19](../documents/src-000320/tables/tbl-0019.md) (the overall process conditions also apply to its reporting variant):

| Item | Description |
| --- | --- |
| Definition | For all Equity / Equity-like instruments that are traded in the EEA, Reporting Entities (RM, MTF, CTP) are to report volumes of trade per currency that they have undertaken on each instrument over the preceding period (01-15 or 16-31 of each month). The report captures total volume of trades as well as volumes of trades that have been undertaken under Negotiated Transactions and Reference Price waivers. |
| Trigger | The Reporting Entity submits data twice per month, typically on the 1st and 16th of each month. |
| Pre-conditions | The Equity / Equity like financial instruments have been previously submitted through the reference data and transparency additional reference data messages. |
| Post-conditions | The double volume cap calculations are performed taking into account a years' worth of data to establish the percentage of trades that are being performed under either Reference Price or Negotiated Transactions waiver. |
| Role | Reporting entity |


## Participants and responsibilities

- [Reporting Entity](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md)
- [Competent Authority](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md)
- [Supervisory Authority](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md)

The RE initiates its data submission; the CA or SA performs the checks assigned by the chosen reporting model. The ordered exchanges and source narrative below retain the actual responsible party.

## Ordered exchanges and decision points

| Order | Sender | Receiver | Literal source message / exchange | Source condition or fragment |
| --- | --- | --- | --- | --- |
| 1 | Reporting Entity | Competent Authority | FinancialInstrumentReportingTradingVolumeCapDataReport | Capture all Relevant Messages |
| 2 | Competent Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Capture all Relevant Messages / Message Received Correctly — All data is correct |
| 3 | Competent Authority | Supervisory Authority | FinancialInstrumentReportingTradingVolumeCapDataReport | Capture all Relevant Messages / Message Received Correctly — All data is correct |
| 4 | Competent Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Capture all Relevant Messages / Some data errors |
| 5 | Competent Authority | Supervisory Authority | FinancialInstrumentReportingTradingVolumeCapDataReport | Capture all Relevant Messages / Some data errors / Instrument with no Errors |
| 6 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingStatusAdvice | Message Received Correctly — All data is correct |
| 7 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingStatusAdvice | Some data errors |
| 8 | Competent Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Some data errors |


[Reconstructed sequence and retained original](../diagrams/fitrr-sequences/fig-0035.md)

## Source narrative and additional participants

**P245** This flow describes an RE submitting a Trading Volume Cap Data report message to the CA. The CA performs all message processing operations before submitting the same message or a new message of all valid instruments to the SA. For each message the CA checks, it generates a Status Advice message to the RE. As the RE can correct errors, the process loops until the RE has submitted all data that it wants to. In parallel to this, the CA submits either a single amalgamated message to the SA or messages corresponding to the valid instruments from the RE submission. The SA generates a Status Advice message against the submitted message(s). Depending on the response, the CA either routes the Status Advice to the RE or completes the message reporting flow as all is correct. Where a single file is created, the per instrument record identifier is used to know which status relates to which venues' submission. This mapping is out of scope but is maintained by the CA.

## Supplied message definitions

- [auth.035.001.01 — FinancialInstrumentReportingTradingVolumeCapDataReportV01](../../../../messages/auth.035.001.01/index.md)
- [auth.031.001.01 — FinancialInstrumentReportingStatusAdviceV01](../../../../messages/auth.031.001.01/index.md)

Family mappings are grounded in Part1 tables T4–T9 and the matching supplied message catalog. The figure names remain literal; a family link does not turn an unversioned diagram into evidence for a particular schema version.

## Alternative and exceptional paths

The source conditions and narrative above define the applicable alternatives. Repeated arrows and all error branches are retained; no additional cancellation or reversal route is invented.

## Limitations

- The source loop/first alternative covers the Reporting Entity and Competent Authority lifelines while report arrows and the inner alternative cross that frame boundary to the Supervisory Authority. Mermaid expands these frames to the participating lifelines. Conditions, all arrows, order and the crossing-frame feature are retained in text; frame geometry is not identical.
- T6 uses FinancialInstrumentsTradingVolumeCapDataReport while the picture uses FinancialInstrumentReportingTradingVolumeCapDataReport. The contextual family link auth.035 comes from T6; the source picture label is retained literally.
- Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.
- The described flow is scoped to this publication; it is not advice on current regulation.
