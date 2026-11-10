---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p188-direct-reporting"
title: "Non-working days — direct reporting"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Non Working Day BusinessTransaction ", "Direct Reporting"], "locator": "/w:document/w:body/w:p[188]", "paragraph_id": "P188", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Non Working Day BusinessTransaction ", "Direct Reporting"], "locator": "/w:document/w:body/w:p[189]", "paragraph_id": "P189", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Non Working Day BusinessTransaction ", "Direct Reporting"], "locator": "/w:document/w:body/w:p[190]", "paragraph_id": "P190", "table_id": null}]
participants: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: ["auth.039.001.01", "auth.031.001.01"]
message_families: ["auth.039", "auth.031"]
search_terms: ["Direct Reporting", "RE", "CA", "SA"]
limitations: ["Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.", "The described flow is scoped to this publication; it is not advice on current regulation."]
participant_ids: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
manual_curated: true
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0020.md"]
---

# Non-working days — direct reporting

[src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx); BusinessTransactions / Non Working Day BusinessTransaction  / Direct Reporting.

## Purpose, trigger, preconditions and outcomes

Source process definition [T15](../documents/src-000320/tables/tbl-0015.md) (the overall process conditions also apply to its reporting variant):

| Item | Description |
| --- | --- |
| Definition | A reporting entity is required to submit data to the supervisory authority details on a daily basis except for days when the venue is not open for trading - holidays / weekends. To support knowing which venues are open and which are closed on specific days, all reporting entities must submit details, per venue they operate, on when they will be closed for trading. |
| Trigger | Ad hoc. |
| Pre-conditions | An entity knows what non-working days (including weekends) it plans through the year and submits this to the supervisory authority. |
| Post-conditions | The supervisory authority knows the dates when a specific venue will not be required to submit relevant data. |
| Role | Reporting entity |


## Participants and responsibilities

- [Reporting Entity](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md) / [Competent Authority](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md)
- [Supervisory Authority](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md)

The RE initiates its data submission; the CA or SA performs the checks assigned by the chosen reporting model. The ordered exchanges and source narrative below retain the actual responsible party.

## Ordered exchanges and decision points

| Order | Sender | Receiver | Literal source message / exchange | Source condition or fragment |
| --- | --- | --- | --- | --- |
| 1 | Reporting Entity / Competent Authority | Supervisory Authority | FinancialInstrumentReportingNonWorkingDayReport | Outside conditional frame |
| 2 | Supervisory Authority | Reporting Entity / Competent Authority | FinancialInstrumentReportingStatusAdvice | Outside conditional frame |


[Reconstructed sequence and retained original](../diagrams/fitrr-sequences/fig-0020.md)

## Source narrative and additional participants

**P187** To perform all operations correctly, the Supervisory Authority and CAs need to know the non-working days of all venues. To support this, all venues, Reporting Entities and CAs must report their non-working days. For this reason, both directly report this information to the Supervisory Authority

**P189** This flow describes the Non-Working day reporting where an RE or CA submits data directly to the SA reporting their non-working days. The SA is responsible for all data checking operations on the message and generates a Status Advice message for each submitted message to the submitting entity.

## Supplied message definitions

- [auth.039.001.01 — FinancialInstrumentReportingNonWorkingDayReportV01](../../../../messages/auth.039.001.01/index.md)
- [auth.031.001.01 — FinancialInstrumentReportingStatusAdviceV01](../../../../messages/auth.031.001.01/index.md)

Family mappings are grounded in Part1 tables T4–T9 and the matching supplied message catalog. The figure names remain literal; a family link does not turn an unversioned diagram into evidence for a particular schema version.

## Alternative and exceptional paths

The source conditions and narrative above define the applicable alternatives. Repeated arrows and all error branches are retained; no additional cancellation or reversal route is invented.

## Limitations

- Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.
- The described flow is scoped to this publication; it is not advice on current regulation.
