---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p131-transparency-data"
title: "Transparency Data"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[131]", "paragraph_id": "P131", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[132]", "paragraph_id": "P132", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[16]", "paragraph_id": null, "table_id": "T16"}, {"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[133]", "paragraph_id": "P133", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[17]", "paragraph_id": null, "table_id": "T17"}, {"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[134]", "paragraph_id": "P134", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[18]", "paragraph_id": null, "table_id": "T18"}]
participants: ["participant-src-000320-supervisory-authority", "participant-src-000320-reporting-entity", "participant-src-000320-esma", "participant-src-000320-mtf", "participant-src-000320-otf", "participant-src-000320-ctp", "participant-src-000320-apa", "participant-src-000320-rm", "participant-src-000320-competent-authority"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Transparency Data", "Supervisory Authority", "Reporting Entity", "ESMA", "MTF", "OTF", "CTP", "APA", "RM", "CA"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Transparency Data

Source context: Transactions and Financial Instruments Data Reporting. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

To support correct implementation of the transparency regime, specific transparency reference data must be submitted by a Reporting Entity (RM, MTF, OTF, APA, CTP) to ESMA.

Evidence: [T16](../documents/src-000320/tables/tbl-0016.md), source row 2.

A Reporting Entity (RM, MTF, OTF, APA, CTP) must submit aggregated quantitative data in relation to the trading activity on the venue for each instrument admitted to trading and each trading day.

Evidence: [T17](../documents/src-000320/tables/tbl-0017.md), source row 2.

CAs that have not delegated calculation operations to ESMA must perform and distribute the results of the transparency calculations they perform to ESMA for publication.

Evidence: [T18](../documents/src-000320/tables/tbl-0018.md), source row 2.

### Trigger

Data is submitted when the financial instrument is first traded or requested to trade has occurred
or
On a change to the data reported as part of the Transparency Reference Data

Evidence: [T16](../documents/src-000320/tables/tbl-0016.md), source row 3.

Data is submitted daily.

Evidence: [T17](../documents/src-000320/tables/tbl-0017.md), source row 3.

Transparency calculations must be performed by specific cut-off times, defined by MiFIR regulations. At the cut-off, the venue (CA) performs the specified calculations.

Evidence: [T18](../documents/src-000320/tables/tbl-0018.md), source row 3.

### Pre-conditions

The financial instrument is registered on the reporting entities system.

Evidence: [T16](../documents/src-000320/tables/tbl-0016.md), source row 4.

Data is submitted with a 7 day lag (calendar days) to ensure cancelations and other operations have been processed as best as possible.

Evidence: [T17](../documents/src-000320/tables/tbl-0017.md), source row 4.

The CA has captured all data it requires to perform the transparency calculation.

Evidence: [T18](../documents/src-000320/tables/tbl-0018.md), source row 4.

### Post-conditions

The reporting entity has submitted appropriate MiFIR specific additional reference data to ESMA.

Evidence: [T16](../documents/src-000320/tables/tbl-0016.md), source row 5.

Data related to all financial instruments traded on the venue pertaining to Transparency have been submitted to the CA / ESMA.

Evidence: [T17](../documents/src-000320/tables/tbl-0017.md), source row 5.

The transparency calculation has been performed by the CA with the result data submitted to ESMA for publication along with all other Transparency results.

Evidence: [T18](../documents/src-000320/tables/tbl-0018.md), source row 5.

### Role

Reporting Entity

Evidence: [T16](../documents/src-000320/tables/tbl-0016.md), source row 6.

Reporting Entity

Evidence: [T17](../documents/src-000320/tables/tbl-0017.md), source row 6.

Supervisory Authority

Evidence: [T18](../documents/src-000320/tables/tbl-0018.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Supervisory Authority | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Reporting Entity | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| ESMA | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-esma.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| MTF | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-mtf.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| OTF | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-otf.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| CTP | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-ctp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| APA | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-apa.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| RM | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-rm.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| CA | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P132** Transparency Data Report Submission

Source table [T16](../documents/src-000320/tables/tbl-0016.md).

**P133** Trading Activity Report Submission

Source table [T17](../documents/src-000320/tables/tbl-0017.md).

**P134** Trading Activity Result Submission

Source table [T18](../documents/src-000320/tables/tbl-0018.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md). Heading path: BusinessProcess Description.
