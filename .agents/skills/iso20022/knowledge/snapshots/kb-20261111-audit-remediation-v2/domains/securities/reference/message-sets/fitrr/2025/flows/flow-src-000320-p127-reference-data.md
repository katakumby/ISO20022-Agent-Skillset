---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p127-reference-data"
title: "Reference Data"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[127]", "paragraph_id": "P127", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[128]", "paragraph_id": "P128", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[13]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[129]", "paragraph_id": "P129", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[14]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[130]", "paragraph_id": "P130", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[15]", "paragraph_id": null, "table_id": "T15"}]
participants: ["participant-src-000320-supervisory-authority", "participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-esma", "participant-src-000320-mtf", "participant-src-000320-otf", "participant-src-000320-rm", "participant-src-000320-si", "participant-src-000320-competent-authority"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Reference Data", "Supervisory Authority", "Competent Authority", "Reporting Entity", "ESMA", "MTF", "OTF", "RM", "SI", "CA"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Reference Data

Source context: Transactions and Financial Instruments Data Reporting. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

A Reporting Entity (RM, MTF, OTF, SI) which has financial instruments that are admitted to trading that are still valid or for which a request for admission to trading has been made, must submit to its Competent Authority (CA), a list of all these instruments, which shall send it to ESMA. In case of delegation agreement, ESMA collect data directly from TV / SI.

Evidence: [T13](../documents/src-000320/tables/tbl-0013.md), source row 2.

A Supervisory Authority receives instruments reference data and shares it with other Business Participants.

Evidence: [T14](../documents/src-000320/tables/tbl-0014.md), source row 2.

A reporting entity is required to submit data to the supervisory authority details on a daily basis except for days when the venue is not open for trading - holidays / weekends. To support knowing which venues are open and which are closed on specific days, all reporting entities must submit details, per venue they operate, on when they will be closed for trading.

Evidence: [T15](../documents/src-000320/tables/tbl-0015.md), source row 2.

### Trigger

Data is submitted daily before the cut-off time stated in the Regulatory Technical Standard.

Evidence: [T13](../documents/src-000320/tables/tbl-0013.md), source row 3.

Daily upon reception of data from Entities reporting instruments reference data.

Evidence: [T14](../documents/src-000320/tables/tbl-0014.md), source row 3.

Ad hoc.

Evidence: [T15](../documents/src-000320/tables/tbl-0015.md), source row 3.

### Pre-conditions

The reporting entity has financial instruments admitted to trading on a regulated market that are still valid or for a which a request for admission to trading has been made 

Evidence: [T13](../documents/src-000320/tables/tbl-0013.md), source row 4.

ESMA has received and generated a complete list of all instruments admitted to trading that are still valid or where a request for admission to trading has been made in the EEA. ESMA has generated all appropriate additional files.

Evidence: [T14](../documents/src-000320/tables/tbl-0014.md), source row 4.

An entity knows what non-working days (including weekends) it plans through the year and submits this to the supervisory authority.

Evidence: [T15](../documents/src-000320/tables/tbl-0015.md), source row 4.

### Post-conditions

The reporting entity has received a status advice message related to the data submitted and / or a reminder file (e.g. in case no file has been submitted by the reporting entity by the cut-off time).

Evidence: [T13](../documents/src-000320/tables/tbl-0013.md), source row 5.

All data has been distributed to CAs for them to integrate within their systems as required.

Evidence: [T14](../documents/src-000320/tables/tbl-0014.md), source row 5.

The supervisory authority knows the dates when a specific venue will not be required to submit relevant data.

Evidence: [T15](../documents/src-000320/tables/tbl-0015.md), source row 5.

### Role

Reporting Entity

Evidence: [T13](../documents/src-000320/tables/tbl-0013.md), source row 6.

Supervisory Authority

Evidence: [T14](../documents/src-000320/tables/tbl-0014.md), source row 6.

Reporting entity

Evidence: [T15](../documents/src-000320/tables/tbl-0015.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Supervisory Authority | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Competent Authority | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Reporting Entity | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| ESMA | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-esma.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| MTF | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-mtf.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| OTF | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-otf.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| RM | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-rm.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| SI | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-si.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| CA | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P128** Reference data submission

Source table [T13](../documents/src-000320/tables/tbl-0013.md).

**P129** Reference data processing and distribution

Source table [T14](../documents/src-000320/tables/tbl-0014.md).

**P130** Non-Working Days Submission

Source table [T15](../documents/src-000320/tables/tbl-0015.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md). Heading path: BusinessProcess Description.
