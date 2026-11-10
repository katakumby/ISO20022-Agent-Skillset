---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p203-direct-reporting"
title: "Incomplete reference data — direct reminder"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Incomplete Data BusinessTransaction", "Direct Reporting"], "locator": "/w:document/w:body/w:p[203]", "paragraph_id": "P203", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Incomplete Data BusinessTransaction", "Direct Reporting"], "locator": "/w:document/w:body/w:p[204]", "paragraph_id": "P204", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Incomplete Data BusinessTransaction", "Direct Reporting"], "locator": "/w:document/w:body/w:p[205]", "paragraph_id": "P205", "table_id": null}]
participants: ["participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: ["auth.031.001.01"]
message_families: ["auth.031"]
search_terms: ["Direct Reporting", "SA"]
limitations: ["Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.", "The described flow is scoped to this publication; it is not advice on current regulation."]
participant_ids: ["participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
manual_curated: true
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0024.md"]
---

# Incomplete reference data — direct reminder

[src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx); BusinessTransactions / Incomplete Data BusinessTransaction / Direct Reporting.

## Purpose, trigger, preconditions and outcomes

Source process definition [T13](../documents/src-000320/tables/tbl-0013.md) (the overall process conditions also apply to its reporting variant):

| Item | Description |
| --- | --- |
| Definition | A Reporting Entity (RM, MTF, OTF, SI) which has financial instruments that are admitted to trading that are still valid or for which a request for admission to trading has been made, must submit to its Competent Authority (CA), a list of all these instruments, which shall send it to ESMA. In case of delegation agreement, ESMA collect data directly from TV / SI. |
| Trigger | Data is submitted daily before the cut-off time stated in the Regulatory Technical Standard. |
| Pre-conditions | The reporting entity has financial instruments admitted to trading on a regulated market that are still valid or for a which a request for admission to trading has been made  |
| Post-conditions | The reporting entity has received a status advice message related to the data submitted and / or a reminder file (e.g. in case no file has been submitted by the reporting entity by the cut-off time). |
| Role | Reporting Entity |


Reminder-specific trigger: the SA checks venue submissions and expected records and identifies incomplete or missing reference data (P202). The recipient must correct the situation in the next reporting window; the general process conditions above do not replace that reminder trigger.

## Participants and responsibilities

- [Reporting Entity](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md)
- [Supervisory Authority](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md)

Initiation and responsibility follow the explicit message directions and narrative below; a participant appearing on a lifeline is not automatically a sender.

## Ordered exchanges and decision points

| Order | Sender | Receiver | Literal source message / exchange | Source condition or fragment |
| --- | --- | --- | --- | --- |
| 1 | Supervisory Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Outside conditional frame |


[Reconstructed sequence and retained original](../diagrams/fitrr-sequences/fig-0024.md)

## Source narrative and additional participants

**P202** Based on the number of venues that will submit data, the chance that not all data for a given day is submitted is high. As part of data quality, checks will be performed to see if all reporting entities for a specific dataset submitted all their data. Where not all data has been reported, a reminder will be sent to these venues informing them either that they made no data submission or of all instruments they failed to submit based on the data the supervisory authority is aware of. Where a reporting entity receives a reminder file, it is incumbent on them to fix the issue and submit complete data in the next submission window.

**P204** This flow describes an end of day / end of reporting period operation where the SA upon checking all its' data per venue identifies issues (e.g. missed submissions, missed records) and distributes a Status Advice message, with status Reminder, directly to those venues which report directly to it.

## Supplied message definitions

- [auth.031.001.01 — FinancialInstrumentReportingStatusAdviceV01](../../../../messages/auth.031.001.01/index.md)

Family mappings are grounded in Part1 tables T4–T9 and the matching supplied message catalog. The figure names remain literal; a family link does not turn an unversioned diagram into evidence for a particular schema version.

## Alternative and exceptional paths

The source conditions and narrative above define the applicable alternatives. Repeated arrows and all error branches are retained; no additional cancellation or reversal route is invented.

## Limitations

- Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.
- The described flow is scoped to this publication; it is not advice on current regulation.
