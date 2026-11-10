---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p217-in-direct-reporting"
title: "Transparency data — indirect reporting"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Transparency Data Report BusinessTransaction ", "In-Direct Reporting"], "locator": "/w:document/w:body/w:p[217]", "paragraph_id": "P217", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Transparency Data Report BusinessTransaction ", "In-Direct Reporting"], "locator": "/w:document/w:body/w:p[218]", "paragraph_id": "P218", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Transparency Data Report BusinessTransaction ", "In-Direct Reporting"], "locator": "/w:document/w:body/w:p[219]", "paragraph_id": "P219", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Transparency Data Report BusinessTransaction ", "In-Direct Reporting"], "locator": "/w:document/w:body/w:p[220]", "paragraph_id": "P220", "table_id": null}]
participants: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: ["auth.032.001.01", "auth.033.001.03", "auth.031.001.01"]
message_families: ["auth.032", "auth.033", "auth.031"]
search_terms: ["In-Direct Reporting", "RE", "CA", "SA"]
limitations: ["The source loop/first alternative covers the Reporting Entity and Competent Authority lifelines while report arrows and the inner alternative cross that frame boundary to the Supervisory Authority. Mermaid expands these frames to the participating lifelines. Conditions, all arrows, order and the crossing-frame feature are retained in text; frame geometry is not identical.", "Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.", "The described flow is scoped to this publication; it is not advice on current regulation."]
participant_ids: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
manual_curated: true
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0028.md"]
---

# Transparency data — indirect reporting

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); BusinessTransactions / Transparency Data Report BusinessTransaction  / In-Direct Reporting.

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
- [Competent Authority](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md)
- [Supervisory Authority](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md)

The RE initiates its data submission; the CA or SA performs the checks assigned by the chosen reporting model. The ordered exchanges and source narrative below retain the actual responsible party.

## Ordered exchanges and decision points

| Order | Sender | Receiver | Literal source message / exchange | Source condition or fragment |
| --- | --- | --- | --- | --- |
| 1 | Reporting Entity | Competent Authority | FinancialInstrumentReportingEquityTransparencyDataReport OR FinancialInstrumentReportingNonEquityTransparencyDataReport | Capture all Relevant Messages |
| 2 | Competent Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Capture all Relevant Messages / Message Received Correctly — All data is correct |
| 3 | Competent Authority | Supervisory Authority | FinancialInstrumentReportingEquityTransparencyDataReport OR FinancialInstrumentReportingNonEquityTransparencyDataReport | Capture all Relevant Messages / Message Received Correctly — All data is correct |
| 4 | Competent Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Capture all Relevant Messages / Some data errors |
| 5 | Competent Authority | Supervisory Authority | FinancialInstrumentReportingEquityTransparencyDataReport OR FinancialInstrumentReportingNonEquityTransparencyDataReport | Capture all Relevant Messages / Some data errors / Instruments with no Errors |
| 6 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingStatusAdvice | Message Received Correctly — All data is correct |
| 7 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingStatusAdvice | Some data errors |
| 8 | Competent Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Some data errors |


[Reconstructed sequence and retained original](../diagrams/fitrr-sequences/fig-0028.md)

## Source narrative and additional participants

**P210** For Transparency Data Report, two types of similar data will be submitted by the venues - Equity specific information and Non-Equity specific information. The overall flow is the same regardless of the type of instrument transparency reference data that is being submitted. Distinct messages were used as differences exist in the level of information captured per message. Within the submitted messages, a single Reporting Entity is not expected to submit both messages as they may not operate instruments in scope of a specific message e.g. they may trade only Equity or Non-Equity but not both.

**P218** This flow describes an RE submitting either an Equity or Non-Equity Transparency Data Reporting to the CA. The CA performs all message processing operations before submitting the same message or a new message of all valid instruments to the SA. For each message the CA checks, it generates a Status Advice message to the RE. As the RE can correct errors, the process loops until the RE has submitted all data that it wants to. In parallel to this, the CA submits either a single amalgamated message to the SA or messages corresponding to the valid instruments from the RE submission. The SA generates a Status Advice message against the submitted message(s). Depending on the response, the CA either routes the Status Advice to the RE or completes the message reporting flow as all is correct. Where a single file is created, the per instrument record identifier is used to know which status relates to which venues' submission. This mapping is out of scope but is maintained by the CA.

## Supplied message definitions

- [auth.032.001.01 — FinancialInstrumentReportingEquityTransparencyDataReportV01](../../../../messages/auth.032.001.01/index.md)
- [auth.033.001.03 — FinancialInstrumentReportingNonEquityTransparencyDataReportV03](../../../../messages/auth.033.001.03/index.md)
- [auth.031.001.01 — FinancialInstrumentReportingStatusAdviceV01](../../../../messages/auth.031.001.01/index.md)

Family mappings are grounded in Part1 tables T4–T9 and the matching supplied message catalog. The figure names remain literal; a family link does not turn an unversioned diagram into evidence for a particular schema version.

## Alternative and exceptional paths

The source conditions and narrative above define the applicable alternatives. Repeated arrows and all error branches are retained; no additional cancellation or reversal route is invented.

## Limitations

- The source loop/first alternative covers the Reporting Entity and Competent Authority lifelines while report arrows and the inner alternative cross that frame boundary to the Supervisory Authority. Mermaid expands these frames to the participating lifelines. Conditions, all arrows, order and the crossing-frame feature are retained in text; frame geometry is not identical.
- Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.
- The described flow is scoped to this publication; it is not advice on current regulation.
