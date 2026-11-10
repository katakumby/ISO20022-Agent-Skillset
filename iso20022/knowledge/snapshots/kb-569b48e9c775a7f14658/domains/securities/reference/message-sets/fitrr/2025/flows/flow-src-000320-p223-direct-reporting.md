---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p223-direct-reporting"
title: "Trading activity — direct reporting"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Trading Activity Report BusinessTransaction", "Direct Reporting"], "locator": "/w:document/w:body/w:p[223]", "paragraph_id": "P223", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Trading Activity Report BusinessTransaction", "Direct Reporting"], "locator": "/w:document/w:body/w:p[224]", "paragraph_id": "P224", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Trading Activity Report BusinessTransaction", "Direct Reporting"], "locator": "/w:document/w:body/w:p[225]", "paragraph_id": "P225", "table_id": null}]
participants: ["participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: ["auth.040.001.01", "auth.041.001.01", "auth.031.001.01"]
message_families: ["auth.040", "auth.041", "auth.031"]
search_terms: ["Direct Reporting", "RE", "SA"]
limitations: ["Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.", "The described flow is scoped to this publication; it is not advice on current regulation."]
participant_ids: ["participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
manual_curated: true
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0029.md"]
---

# Trading activity — direct reporting

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); BusinessTransactions / Trading Activity Report BusinessTransaction / Direct Reporting.

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
- [Supervisory Authority](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md)

The RE initiates its data submission; the CA or SA performs the checks assigned by the chosen reporting model. The ordered exchanges and source narrative below retain the actual responsible party.

## Ordered exchanges and decision points

| Order | Sender | Receiver | Literal source message / exchange | Source condition or fragment |
| --- | --- | --- | --- | --- |
| 1 | Reporting Entity | Supervisory Authority | FinancialInstrumentReportingEquityTradingActivityReport OR FinancialInstrumentReportingNonEquityTradingActivityReport | Outside conditional frame |
| 2 | Supervisory Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Outside conditional frame |


[Reconstructed sequence and retained original](../diagrams/fitrr-sequences/fig-0029.md)

## Source narrative and additional participants

**P222** For Transparency Trading Activity Report, two types of similar data will be submitted by the venues - Equity specific information and Non-Equity specific information. The information captured in these messages is quantitative in nature reflecting that it relates to the specific trading activity on instruments reported as part of Reference Data and Transparency Data Reporting. Within the submitted messages, a single Reporting Entity is not expected to submit both messages as they may not operate instruments in scope of a specific message e.g. they may trade only Equity or Non-Equity but not both.

**P224** This flow describes an RE submitting either an Equity or Non-Equity Transparency Trading Activity report message directly to the SA. For each message submitted to the SA, a Status Advice message is generated.

## Supplied message definitions

- [auth.040.001.01 — FinancialInstrumentReportingEquityTradingActivityReportV01](../../../../messages/auth.040.001.01/index.md)
- [auth.041.001.01 — FinancialInstrumentReportingNonEquityTradingActivityReportV01](../../../../messages/auth.041.001.01/index.md)
- [auth.031.001.01 — FinancialInstrumentReportingStatusAdviceV01](../../../../messages/auth.031.001.01/index.md)

Family mappings are grounded in Part1 tables T4–T9 and the matching supplied message catalog. The figure names remain literal; a family link does not turn an unversioned diagram into evidence for a particular schema version.

## Alternative and exceptional paths

The source conditions and narrative above define the applicable alternatives. Repeated arrows and all error branches are retained; no additional cancellation or reversal route is invented.

## Limitations

- Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.
- The described flow is scoped to this publication; it is not advice on current regulation.
