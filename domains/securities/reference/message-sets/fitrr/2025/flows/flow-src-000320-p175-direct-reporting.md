---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p175-direct-reporting"
title: "Reference data — direct reporting"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Reference Data Reporting BusinessTransaction", "Direct Reporting"], "locator": "/w:document/w:body/w:p[175]", "paragraph_id": "P175", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Reference Data Reporting BusinessTransaction", "Direct Reporting"], "locator": "/w:document/w:body/w:p[176]", "paragraph_id": "P176", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Reference Data Reporting BusinessTransaction", "Direct Reporting"], "locator": "/w:document/w:body/w:p[177]", "paragraph_id": "P177", "table_id": null}]
participants: ["participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: ["auth.017.001.02", "auth.031.001.01"]
message_families: ["auth.017", "auth.031"]
search_terms: ["Direct Reporting", "RE", "SA"]
limitations: ["Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.", "The described flow is scoped to this publication; it is not advice on current regulation."]
participant_ids: ["participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
manual_curated: true
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0017.md"]
---

# Reference data — direct reporting

[src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx); BusinessTransactions / Reference Data Reporting BusinessTransaction / Direct Reporting.

## Purpose, trigger, preconditions and outcomes

Source process definition [T13](../documents/src-000320/tables/tbl-0013.md) (the overall process conditions also apply to its reporting variant):

| Item | Description |
| --- | --- |
| Definition | A Reporting Entity (RM, MTF, OTF, SI) which has financial instruments that are admitted to trading that are still valid or for which a request for admission to trading has been made, must submit to its Competent Authority (CA), a list of all these instruments, which shall send it to ESMA. In case of delegation agreement, ESMA collect data directly from TV / SI. |
| Trigger | Data is submitted daily before the cut-off time stated in the Regulatory Technical Standard. |
| Pre-conditions | The reporting entity has financial instruments admitted to trading on a regulated market that are still valid or for a which a request for admission to trading has been made  |
| Post-conditions | The reporting entity has received a status advice message related to the data submitted and / or a reminder file (e.g. in case no file has been submitted by the reporting entity by the cut-off time). |
| Role | Reporting Entity |


## Participants and responsibilities

- [Reporting Entity](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md)
- [Supervisory Authority](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md)

The RE initiates its data submission; the CA or SA performs the checks assigned by the chosen reporting model. The ordered exchanges and source narrative below retain the actual responsible party.

## Ordered exchanges and decision points

| Order | Sender | Receiver | Literal source message / exchange | Source condition or fragment |
| --- | --- | --- | --- | --- |
| 1 | Reporting Entity | Supervisory Authority | FinancialInstrumentReportingReferenceDataReport | Outside conditional frame |
| 2 | Supervisory Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Outside conditional frame |


[Reconstructed sequence and retained original](../diagrams/fitrr-sequences/fig-0017.md)

## Source narrative and additional participants

**P176** This flow describes the Reference Data Reporting where an RE submits data directly to the SA. The SA is responsible for all data checking operations on the message and directly replies to the submitting RE.

## Supplied message definitions

- [auth.017.001.02 — FinancialInstrumentReportingReferenceDataReportV02](../../../../messages/auth.017.001.02/index.md)
- [auth.031.001.01 — FinancialInstrumentReportingStatusAdviceV01](../../../../messages/auth.031.001.01/index.md)

Family mappings are grounded in Part1 tables T4–T9 and the matching supplied message catalog. The figure names remain literal; a family link does not turn an unversioned diagram into evidence for a particular schema version.

## Alternative and exceptional paths

The source conditions and narrative above define the applicable alternatives. Repeated arrows and all error branches are retained; no additional cancellation or reversal route is invented.

## Limitations

- Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.
- The described flow is scoped to this publication; it is not advice on current regulation.
