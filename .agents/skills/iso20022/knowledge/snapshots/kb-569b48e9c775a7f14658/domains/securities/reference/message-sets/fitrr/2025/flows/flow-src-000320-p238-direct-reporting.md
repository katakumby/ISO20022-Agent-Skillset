---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p238-direct-reporting"
title: "Trading volume cap — direct reporting"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Trading Volume Cap BusinessTransaction ", "Direct Reporting"], "locator": "/w:document/w:body/w:p[238]", "paragraph_id": "P238", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Trading Volume Cap BusinessTransaction ", "Direct Reporting"], "locator": "/w:document/w:body/w:p[239]", "paragraph_id": "P239", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Trading Volume Cap BusinessTransaction ", "Direct Reporting"], "locator": "/w:document/w:body/w:p[240]", "paragraph_id": "P240", "table_id": null}]
participants: ["participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: ["auth.035.001.01", "auth.031.001.01"]
message_families: ["auth.035", "auth.031"]
search_terms: ["Direct Reporting", "RE", "SA"]
limitations: ["T6 uses FinancialInstrumentsTradingVolumeCapDataReport while the picture uses FinancialInstrumentReportingTradingVolumeCapDataReport. The contextual family link auth.035 comes from T6; the source picture label is retained literally.", "Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.", "The described flow is scoped to this publication; it is not advice on current regulation."]
participant_ids: ["participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
manual_curated: true
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0033.md"]
---

# Trading volume cap — direct reporting

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); BusinessTransactions / Trading Volume Cap BusinessTransaction  / Direct Reporting.

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
- [Supervisory Authority](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md)

The RE initiates its data submission; the CA or SA performs the checks assigned by the chosen reporting model. The ordered exchanges and source narrative below retain the actual responsible party.

## Ordered exchanges and decision points

| Order | Sender | Receiver | Literal source message / exchange | Source condition or fragment |
| --- | --- | --- | --- | --- |
| 1 | Reporting Entity | Supervisory Authority | FinancialInstrumentReportingTradingVolumeCapDataReport | Outside conditional frame |
| 2 | Supervisory Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Outside conditional frame |


[Reconstructed sequence and retained original](../diagrams/fitrr-sequences/fig-0033.md)

## Source narrative and additional participants

**P239** This flow describes an RE submitting a Trading Volume Cap Data report message directly to the SA. For each message submitted to the SA, a Status Advice message is generated.

## Supplied message definitions

- [auth.035.001.01 — FinancialInstrumentReportingTradingVolumeCapDataReportV01](../../../../messages/auth.035.001.01/index.md)
- [auth.031.001.01 — FinancialInstrumentReportingStatusAdviceV01](../../../../messages/auth.031.001.01/index.md)

Family mappings are grounded in Part1 tables T4–T9 and the matching supplied message catalog. The figure names remain literal; a family link does not turn an unversioned diagram into evidence for a particular schema version.

## Alternative and exceptional paths

The source conditions and narrative above define the applicable alternatives. Repeated arrows and all error branches are retained; no additional cancellation or reversal route is invented.

## Limitations

- T6 uses FinancialInstrumentsTradingVolumeCapDataReport while the picture uses FinancialInstrumentReportingTradingVolumeCapDataReport. The contextual family link auth.035 comes from T6; the source picture label is retained literally.
- Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.
- The described flow is scoped to this publication; it is not advice on current regulation.
