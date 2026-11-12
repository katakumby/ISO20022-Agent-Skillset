---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p178-proxy-reporting"
title: "Reference data — proxy reporting"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Reference Data Reporting BusinessTransaction", "Proxy Reporting"], "locator": "/w:document/w:body/w:p[178]", "paragraph_id": "P178", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Reference Data Reporting BusinessTransaction", "Proxy Reporting"], "locator": "/w:document/w:body/w:p[179]", "paragraph_id": "P179", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Reference Data Reporting BusinessTransaction", "Proxy Reporting"], "locator": "/w:document/w:body/w:p[180]", "paragraph_id": "P180", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Reference Data Reporting BusinessTransaction", "Proxy Reporting"], "locator": "/w:document/w:body/w:p[181]", "paragraph_id": "P181", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Reference Data Reporting BusinessTransaction", "Proxy Reporting"], "locator": "/w:document/w:body/w:p[182]", "paragraph_id": "P182", "table_id": null}]
participants: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: ["auth.017.001.02", "auth.031.001.01"]
message_families: ["auth.017", "auth.031"]
search_terms: ["Proxy Reporting", "RE", "CA", "SA"]
limitations: ["Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.", "The described flow is scoped to this publication; it is not advice on current regulation."]
participant_ids: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
manual_curated: true
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0018.md"]
---

# Reference data — proxy reporting

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); BusinessTransactions / Reference Data Reporting BusinessTransaction / Proxy Reporting.

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
| 1 | Reporting Entity | Competent Authority | FinancialInstrumentReportingReferenceDataReport | Outside conditional frame |
| 2 | Competent Authority | Supervisory Authority | FinancialInstrumentReportingReferenceDataReport | Competent Authority Validation Checks (Schema; Filename; Reporting Entity) — Validation Success |
| 3 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingStatusAdvice | Competent Authority Validation Checks (Schema; Filename; Reporting Entity) — Validation Success |
| 4 | Competent Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Competent Authority Validation Checks (Schema; Filename; Reporting Entity) — Validation Success |
| 5 | Competent Authority | Reporting Entity | FinancialInstrumentReportingStatusAdvice | Validation Failure |


[Reconstructed sequence and retained original](../diagrams/fitrr-sequences/fig-0018.md)

## Source narrative and additional participants

**P179** This flow describes an RE submitting the Reference Data Reporting to the SA via a CA. In this case, the CA performs high level checks ranging from naming convention checks through to schema validations. The CA is expected to either find the message conforms or it does not, it is not expected to perform detailed operations and message parsing. Once a message conforms, it is submitted to the SA resulting in a one-to-one mapping of conforming files to submitted files. Where a submission has been made to the SA, the CA shall expect a Status Advice detailing the results from the in-depth operations that are performed on the message. Where a message does not conform, the CA is to create the Status Advice to the submitting RE.

## Supplied message definitions

- [auth.017.001.02 — FinancialInstrumentReportingReferenceDataReportV02](../../../../messages/auth.017.001.02/index.md)
- [auth.031.001.01 — FinancialInstrumentReportingStatusAdviceV01](../../../../messages/auth.031.001.01/index.md)

Family mappings are grounded in Part1 tables T4–T9 and the matching supplied message catalog. The figure names remain literal; a family link does not turn an unversioned diagram into evidence for a particular schema version.

## Alternative and exceptional paths

The CA returns a failure status instead of forwarding a failed message. Successful validation forwards the report to the SA and returns the SA status through the CA.

## Limitations

- Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.
- The described flow is scoped to this publication; it is not advice on current regulation.
