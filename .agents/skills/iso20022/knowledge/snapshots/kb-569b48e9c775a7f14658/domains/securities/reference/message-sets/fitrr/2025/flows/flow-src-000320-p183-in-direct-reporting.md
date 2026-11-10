---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p183-in-direct-reporting"
title: "Reference data — indirect reporting"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Reference Data Reporting BusinessTransaction", "In-Direct Reporting"], "locator": "/w:document/w:body/w:p[183]", "paragraph_id": "P183", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Reference Data Reporting BusinessTransaction", "In-Direct Reporting"], "locator": "/w:document/w:body/w:p[184]", "paragraph_id": "P184", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Reference Data Reporting BusinessTransaction", "In-Direct Reporting"], "locator": "/w:document/w:body/w:p[185]", "paragraph_id": "P185", "table_id": null}]
participants: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: ["auth.017.001.02", "auth.031.001.01"]
message_families: ["auth.017", "auth.031"]
search_terms: ["In-Direct Reporting", "RE", "CA", "SA"]
limitations: ["The source loop/first alternative covers the Reporting Entity and Competent Authority lifelines while report arrows and the inner alternative cross that frame boundary to the Supervisory Authority. Mermaid expands these frames to the participating lifelines. Conditions, all arrows, order and the crossing-frame feature are retained in text; frame geometry is not identical.", "Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.", "The described flow is scoped to this publication; it is not advice on current regulation."]
participant_ids: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
manual_curated: true
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0019.md"]
---

# Reference data — indirect reporting

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); BusinessTransactions / Reference Data Reporting BusinessTransaction / In-Direct Reporting.

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
- [Competent Authority](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md)
- [Supervisory Authority](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md)

The RE initiates its data submission; the CA or SA performs the checks assigned by the chosen reporting model. The ordered exchanges and source narrative below retain the actual responsible party.

## Ordered exchanges and decision points

| Order | Sender | Receiver | Literal source message / exchange | Source condition or fragment |
| --- | --- | --- | --- | --- |
| 1 | Reporting Entity | Competent Authority | FinancialInstrumentReportingReferenceDataReport | Capture all Relevant Messages |
| 2 | Competent Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Capture all Relevant Messages / Message Received Correctly — All data is correct |
| 3 | Competent Authority | Supervisory Authority | FinancialInstrumentReportingReferenceDataReport | Capture all Relevant Messages / Message Received Correctly — All data is correct |
| 4 | Competent Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Capture all Relevant Messages / Some data errors |
| 5 | Competent Authority | Supervisory Authority | FinancialInstrumentReportingReferenceDataReport | Capture all Relevant Messages / Some data errors / Instruments with no Errors |
| 6 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingStatusAdvice | Message Received Correctly — All data is correct |
| 7 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingStatusAdvice | Some data errors |
| 8 | Competent Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Some data errors |


[Reconstructed sequence and retained original](../diagrams/fitrr-sequences/fig-0019.md)

## Source narrative and additional participants

**P184** This flow describes an RE submitting a Reference Data Report to the CA. The CA performs all message processing operations before submitting the same message or a new message of all valid instruments to the SA. For each message the CA checks, it generates a Status Advice message to the RE. As the RE can correct errors, the process loops until the RE has submitted all data that it wants to. In parallel to this, the CA submits either a single amalgamated message to the SA or messages corresponding to the valid instruments from the RE submission. The SA generates a Status Advice message against the submitted message(s). Depending on the response, the CA either routes the Status Advice to the RE or completes the message reporting flow as all is correct. Where a single file submission is used, the per instrument record identifier is used to know which status relates to which venues' submission. This mapping is out of scope but is maintained by the CA.

## Supplied message definitions

- [auth.017.001.02 — FinancialInstrumentReportingReferenceDataReportV02](../../../../messages/auth.017.001.02/index.md)
- [auth.031.001.01 — FinancialInstrumentReportingStatusAdviceV01](../../../../messages/auth.031.001.01/index.md)

Family mappings are grounded in Part1 tables T4–T9 and the matching supplied message catalog. The figure names remain literal; a family link does not turn an unversioned diagram into evidence for a particular schema version.

## Alternative and exceptional paths

The source conditions and narrative above define the applicable alternatives. Repeated arrows and all error branches are retained; no additional cancellation or reversal route is invented.

## Limitations

- The source loop/first alternative covers the Reporting Entity and Competent Authority lifelines while report arrows and the inner alternative cross that frame boundary to the Supervisory Authority. Mermaid expands these frames to the participating lifelines. Conditions, all arrows, order and the crossing-frame feature are retained in text; frame geometry is not identical.
- Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.
- The described flow is scoped to this publication; it is not advice on current regulation.
