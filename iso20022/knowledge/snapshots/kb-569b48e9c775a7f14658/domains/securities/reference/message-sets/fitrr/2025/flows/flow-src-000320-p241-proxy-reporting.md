---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p241-proxy-reporting"
title: "Trading volume cap — proxy reporting"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Trading Volume Cap BusinessTransaction ", "Proxy Reporting"], "locator": "/w:document/w:body/w:p[241]", "paragraph_id": "P241", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Trading Volume Cap BusinessTransaction ", "Proxy Reporting"], "locator": "/w:document/w:body/w:p[242]", "paragraph_id": "P242", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Trading Volume Cap BusinessTransaction ", "Proxy Reporting"], "locator": "/w:document/w:body/w:p[243]", "paragraph_id": "P243", "table_id": null}]
participants: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: ["auth.035.001.01", "auth.031.001.01"]
message_families: ["auth.035", "auth.031"]
search_terms: ["Proxy Reporting", "RE", "CA", "SA"]
limitations: ["The first source arrow has an open head, unlike the filled heads on later arrows. Its distinct glyph is retained; no transport or timing semantics is inferred.", "T6 uses FinancialInstrumentsTradingVolumeCapDataReport while the picture uses FinancialInstrumentReportingTradingVolumeCapDataReport. The contextual family link auth.035 comes from T6; the source picture label is retained literally.", "Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.", "The described flow is scoped to this publication; it is not advice on current regulation."]
participant_ids: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
manual_curated: true
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0034.md"]
---

# Trading volume cap — proxy reporting

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); BusinessTransactions / Trading Volume Cap BusinessTransaction  / Proxy Reporting.

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
| 1 | Reporting Entity | Competent Authority | FinancialInstrumentReportingTradingVolumeCapDataReport | Outside conditional frame |
| 2 | Competent Authority | Supervisory Authority | FinancialInstrumentReportingTradingVolumeCapDataReport | Competent Authority Validation Checks (Schema; Filename; Reporting Entity) — Validation Successful |
| 3 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingStatusAdvice | Competent Authority Validation Checks (Schema; Filename; Reporting Entity) — Validation Successful |
| 4 | Competent Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Competent Authority Validation Checks (Schema; Filename; Reporting Entity) — Validation Successful |
| 5 | Competent Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Validation Failure |


[Reconstructed sequence and retained original](../diagrams/fitrr-sequences/fig-0034.md)

## Source narrative and additional participants

**P242** This flow describes an RE submitting a Trading Volume Cap Data report message directly to the CA. In this case, the CA performs high level checks ranging from naming convention checks through to schema validations. The CA is expected to either find the message conforms or it does not, it is not expected to perform detailed operations and message parsing. Once a message conforms, it is submitted to the SA resulting in a one-to-one mapping of conforming files to submitted files. Where a submission has been made to the SA, the CA shall expect a Status Advice detailing the results from the in-depth operations that are performed on the message. Where a message does not conform, the CA is to create the Status Advice to the submitting RE.

## Supplied message definitions

- [auth.035.001.01 — FinancialInstrumentReportingTradingVolumeCapDataReportV01](../../../../messages/auth.035.001.01/index.md)
- [auth.031.001.01 — FinancialInstrumentReportingStatusAdviceV01](../../../../messages/auth.031.001.01/index.md)

Family mappings are grounded in Part1 tables T4–T9 and the matching supplied message catalog. The figure names remain literal; a family link does not turn an unversioned diagram into evidence for a particular schema version.

## Alternative and exceptional paths

The CA returns a failure status instead of forwarding a failed message. Successful validation forwards the report to the SA and returns the SA status through the CA.

## Limitations

- The first source arrow has an open head, unlike the filled heads on later arrows. Its distinct glyph is retained; no transport or timing semantics is inferred.
- T6 uses FinancialInstrumentsTradingVolumeCapDataReport while the picture uses FinancialInstrumentReportingTradingVolumeCapDataReport. The contextual family link auth.035 comes from T6; the source picture label is retained literally.
- Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.
- The described flow is scoped to this publication; it is not advice on current regulation.
