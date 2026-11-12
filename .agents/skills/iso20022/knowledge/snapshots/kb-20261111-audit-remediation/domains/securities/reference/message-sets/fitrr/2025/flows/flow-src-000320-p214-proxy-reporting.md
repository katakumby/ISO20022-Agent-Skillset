---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p214-proxy-reporting"
title: "Transparency data — proxy reporting"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Transparency Data Report BusinessTransaction ", "Proxy Reporting"], "locator": "/w:document/w:body/w:p[214]", "paragraph_id": "P214", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Transparency Data Report BusinessTransaction ", "Proxy Reporting"], "locator": "/w:document/w:body/w:p[215]", "paragraph_id": "P215", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Transparency Data Report BusinessTransaction ", "Proxy Reporting"], "locator": "/w:document/w:body/w:p[216]", "paragraph_id": "P216", "table_id": null}]
participants: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: ["auth.032.001.01", "auth.033.001.03", "auth.031.001.01"]
message_families: ["auth.032", "auth.033", "auth.031"]
search_terms: ["Proxy Reporting", "RE", "CA", "SA"]
limitations: ["Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.", "The described flow is scoped to this publication; it is not advice on current regulation."]
participant_ids: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
manual_curated: true
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0027.md"]
---

# Transparency data — proxy reporting

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); BusinessTransactions / Transparency Data Report BusinessTransaction  / Proxy Reporting.

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
| 1 | Reporting Entity | Competent Authority | FinancialInstrumentReportingEquityTransparencyDataReport OR FinancialInstrumentReportingNonEquityTransparencyDataReport | Outside conditional frame |
| 2 | Competent Authority | Supervisory Authority | FinancialInstrumentReportingEquityTransparencyDataReport OR FinancialInstrumentReportingNonEquityTransparencyDataReport | Competent Authority Validation Checks (Schema; Filename; Reporting Entity) — Validation Successful |
| 3 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingStatusAdvice | Competent Authority Validation Checks (Schema; Filename; Reporting Entity) — Validation Successful |
| 4 | Competent Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Competent Authority Validation Checks (Schema; Filename; Reporting Entity) — Validation Successful |
| 5 | Competent Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Validation Failure |


[Reconstructed sequence and retained original](../diagrams/fitrr-sequences/fig-0027.md)

## Source narrative and additional participants

**P210** For Transparency Data Report, two types of similar data will be submitted by the venues - Equity specific information and Non-Equity specific information. The overall flow is the same regardless of the type of instrument transparency reference data that is being submitted. Distinct messages were used as differences exist in the level of information captured per message. Within the submitted messages, a single Reporting Entity is not expected to submit both messages as they may not operate instruments in scope of a specific message e.g. they may trade only Equity or Non-Equity but not both.

**P215** This flow describes an RE submitting either an Equity or Non-Equity Transparency Data Reporting message directly to the CA. In this case, the CA performs high level checks ranging from naming convention checks through to schema validations. The CA is expected to either find the message conforms or it does not, it is not expected to perform detailed operations and message parsing. Once a message conforms, it is submitted to the SA resulting in a one-to-one mapping of conforming files to submitted files. Where a submission has been made to the SA, the CA shall expect a Status Advice detailing the results from the in-depth operations that are performed on the message. Where a message does not conform, the CA is to create the Status Advice to the submitting RE.

## Supplied message definitions

- [auth.032.001.01 — FinancialInstrumentReportingEquityTransparencyDataReportV01](../../../../messages/auth.032.001.01/index.md)
- [auth.033.001.03 — FinancialInstrumentReportingNonEquityTransparencyDataReportV03](../../../../messages/auth.033.001.03/index.md)
- [auth.031.001.01 — FinancialInstrumentReportingStatusAdviceV01](../../../../messages/auth.031.001.01/index.md)

Family mappings are grounded in Part1 tables T4–T9 and the matching supplied message catalog. The figure names remain literal; a family link does not turn an unversioned diagram into evidence for a particular schema version.

## Alternative and exceptional paths

The CA returns a failure status instead of forwarding a failed message. Successful validation forwards the report to the SA and returns the SA status through the CA.

## Limitations

- Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.
- The described flow is scoped to this publication; it is not advice on current regulation.
