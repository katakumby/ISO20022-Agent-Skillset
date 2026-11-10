---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p191-proxy-reporting"
title: "Non-working days — proxy reporting"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Non Working Day BusinessTransaction ", "Proxy Reporting"], "locator": "/w:document/w:body/w:p[191]", "paragraph_id": "P191", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Non Working Day BusinessTransaction ", "Proxy Reporting"], "locator": "/w:document/w:body/w:p[192]", "paragraph_id": "P192", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Non Working Day BusinessTransaction ", "Proxy Reporting"], "locator": "/w:document/w:body/w:p[193]", "paragraph_id": "P193", "table_id": null}]
participants: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: ["auth.039.001.01", "auth.031.001.01"]
message_families: ["auth.039", "auth.031"]
search_terms: ["Proxy Reporting", "RE", "CA", "SA"]
limitations: ["Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.", "The described flow is scoped to this publication; it is not advice on current regulation."]
participant_ids: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
manual_curated: true
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0021.md"]
---

# Non-working days — proxy reporting

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); BusinessTransactions / Non Working Day BusinessTransaction  / Proxy Reporting.

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

- [Reporting Entity](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md)
- [Competent Authority](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md)
- [Supervisory Authority](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md)

The RE initiates its data submission; the CA or SA performs the checks assigned by the chosen reporting model. The ordered exchanges and source narrative below retain the actual responsible party.

## Ordered exchanges and decision points

| Order | Sender | Receiver | Literal source message / exchange | Source condition or fragment |
| --- | --- | --- | --- | --- |
| 1 | Reporting Entity | Competent Authority | FinancialInstrumentReportingNonWorkingDayReport | Outside conditional frame |
| 2 | Competent Authority | Supervisory Authority | FinancialInstrumentReportingNonWorkingDayReport | Competent Authority Validation Checks (Schema; Filename; Reporting Entity) — Validation Successful |
| 3 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingStatusAdvice | Competent Authority Validation Checks (Schema; Filename; Reporting Entity) — Validation Successful |
| 4 | Competent Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Competent Authority Validation Checks (Schema; Filename; Reporting Entity) — Validation Successful |
| 5 | Competent Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Validation Failures |


[Reconstructed sequence and retained original](../diagrams/fitrr-sequences/fig-0021.md)

## Source narrative and additional participants

**P192** This flow describes the Non-Working day reporting where an RE submits to the SA via a CA. In this flow, the CA performs high level checks ranging from naming convention checks through to schema validations. The CA is expected to either find the message conforms or it does not, it is not expected to perform detailed operations and message parsing. Once a message conforms, it is submitted to the SA resulting in a one-to-one mapping of conforming files to submitted files. Where a submission has been made to the SA, the CA shall expect a Status Advice detailing the results from the in-depth operations that are performed on the message. Where a message does not conform, the CA is to create the Status Advice to the submitting RE.

## Supplied message definitions

- [auth.039.001.01 — FinancialInstrumentReportingNonWorkingDayReportV01](../../../../messages/auth.039.001.01/index.md)
- [auth.031.001.01 — FinancialInstrumentReportingStatusAdviceV01](../../../../messages/auth.031.001.01/index.md)

Family mappings are grounded in Part1 tables T4–T9 and the matching supplied message catalog. The figure names remain literal; a family link does not turn an unversioned diagram into evidence for a particular schema version.

## Alternative and exceptional paths

The CA returns a failure status instead of forwarding a failed message. Successful validation forwards the report to the SA and returns the SA status through the CA.

## Limitations

- Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.
- The described flow is scoped to this publication; it is not advice on current regulation.
