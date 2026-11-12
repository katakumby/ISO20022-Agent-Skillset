---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "shared"
source_ids: ["src-000343"]
source_editions: ["march-2024"]
message_sets: ["t2s-administration"]
flow_id: "flow-src-000343-p126-report-query-process"
title: "Report query process"
source_locations: [{"source_id": "src-000343", "heading_path": ["BusinessProcess Description", "Report Query Request"], "locator": "/w:document/w:body/w:p[126]", "paragraph_id": "P126", "table_id": null}, {"source_id": "src-000343", "heading_path": ["BusinessProcess Description", "Report Query Request"], "locator": "/w:document/w:body/w:tbl[8]", "paragraph_id": null, "table_id": "T8"}, {"source_id": "src-000343", "heading_path": ["BusinessProcess Description", "Report Query Request"], "locator": "/w:document/w:body/w:p[127]", "paragraph_id": "P127", "table_id": null}, {"source_id": "src-000343", "heading_path": ["BusinessProcess Description", "Report Query Request"], "locator": "/w:document/w:body/w:p[128]", "paragraph_id": "P128", "table_id": null}]
participants: ["participant-src-000343-system-member"]
message_mapping_evidence: [{"source_id": "src-000343", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Administration"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["admi.005"]
search_terms: ["Report query process", "System Member", "admi.005"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Report query process

Source context: T2S Administration. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The Report Query Request is sent by a CB, CSD or any party authorised by them to use the report query. It aims at querying the latest available report data of a specific report type. This message enables the sender to request a report (available and/or already sent) according to his access rights. The sender instructs Central System to send the latest available Report and uses the possible selection parameters to specify the report further. 

Evidence: [T8](../documents/src-000343/tables/tbl-0008.md), source row 2.

### Trigger

The process is triggered when a CB, CSD or any party authorised by them to use the report query, defines specific search criteria. If none or not all of these selection parameters are specified, Central System returns all reports available consistent with the access rights.

Evidence: [T8](../documents/src-000343/tables/tbl-0008.md), source row 3.

### Pre-conditions

The  System User has the respective privilege to obtain the requested report. The corresponding business data should be available and accessible.

Evidence: [T8](../documents/src-000343/tables/tbl-0008.md), source row 4.

### Post-conditions

A Query Response Message for Business Data including requested business data is sent back to the requesting System Actor, i.e. either the retrieved data sets or a notification that the extraction returned a zero result. In case no business data is found a query response message for operational error is sent back to the requesting System Actor indicating the error(s) which occurred.

Evidence: [T8](../documents/src-000343/tables/tbl-0008.md), source row 5.

### Role

System Member 

Evidence: [T8](../documents/src-000343/tables/tbl-0008.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| System Member | [Participant](../../../../participants/participant-src-000343-system-member.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T8](../documents/src-000343/tables/tbl-0008.md).

## Messages and alternative paths

Source-supported message family mentions: `admi.005`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000343](../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart1_Target2Securities_Administration_2023_2024_v2.docx`. Heading path: BusinessProcess Description / Report Query Request.
