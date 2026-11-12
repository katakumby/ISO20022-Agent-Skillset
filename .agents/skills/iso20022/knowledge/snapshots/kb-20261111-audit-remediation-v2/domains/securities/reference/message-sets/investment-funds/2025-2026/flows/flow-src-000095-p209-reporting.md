---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p209-reporting"
title: "Reporting"
source_locations: [{"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reporting"], "locator": "/w:document/w:body/w:p[209]", "paragraph_id": "P209", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reporting"], "locator": "/w:document/w:body/w:p[210]", "paragraph_id": "P210", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reporting"], "locator": "/w:document/w:body/w:p[211]", "paragraph_id": "P211", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reporting"], "locator": "/w:document/w:body/w:tbl[39]", "paragraph_id": null, "table_id": "T39"}]
participants: ["participant-src-000095-reporting-party", "participant-src-000095-requesting-party"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Price Report "], "locator": "/w:document/w:body/w:tbl[14]/w:tr[2]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000096", "locator": "file page 159; 13 reda.001.001.05 PriceReportV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Price Report "], "locator": "/w:document/w:body/w:tbl[14]/w:tr[3]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000096", "locator": "file page 222; 14 reda.002.001.05 PriceReportCancellationV05"}]
message_ids: []
message_families: ["reda.001", "reda.002"]
search_terms: ["Reporting", "Requesting Party", "Reporting Party", "reda.001", "reda.002"]
limitations: ["Statement is the literal source edge label although the nodes and T39 concern a price report. The error path is dashed; Correction Required has only a Yes branch. T39 supplies the reason requirement and replacement rule.", "Unlabelled plain source connectors are retained as undirected lines; business direction established by the activity table is described separately. Blank start/end and control symbols remain blank. Mermaid swimlanes preserve responsibility labels but not the exact source geometry."]
manual_curated: true
participant_ids: ["participant-src-000095-reporting-party", "participant-src-000095-requesting-party"]
related_diagrams: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0011.md"]
updated: "2026-11-09"
diagram_review: {"status": "pass", "date": "2026-11-09", "reviewer": "shared-evidence agent", "scope": "Original extracted picture and complete Word-rendered source page compared with rendered Mermaid PNG; checked actor occurrences, source labels, endpoints, arrowheads/plain lines, lane/control boundaries and alternatives. Complete-page composition checked in contact sheets; original pictures inspected at readable size.", "source_page": 28, "result_notes": ["All source edges and labels compared; plain-line connectors not promoted to inferred direction."]}
issue_ids: []
---



# Reporting Flow

[src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md); Description of BusinessActivities / Reporting; direct-body paragraph P211; T39.

## Purpose, trigger and conditions

The activity source does not provide a separate trigger/precondition/postcondition table for this view. Conditions and outcomes are those explicitly stated in the activity rows and narrative below.

This example shows the reporting of prices. (P210)

## Participants and responsibilities

- [reporting party](../../../../../../../shared/reference/participants/participant-src-000095-reporting-party.md)
- [requesting party](../../../../../../../shared/reference/participants/participant-src-000095-requesting-party.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Send Price Report | The reporting party sends a price report to the receiving party at the agreed frequency or in response to a request. | Reporting Party |
| Send Cancellation | If a price report is found to have been issued in error or contains incorrect information, a price report cancellation message is sent by the reporting party to the requesting party specifying the reason for cancellation. | Reporting Party |
| Send New Price Report | If the cancellation is because the price report contained incorrect information, the reporting party sends a new price report to the receiving party. | Reporting Party |


## Ordered paths, messages and alternatives

[Complete source reconstruction, connector list and decision paths](../diagrams/funds-processes/fig-0011.md)

Follow the source graph for connected activities; the source table lists responsibilities rather than a universal execution order. Source-labelled exchange types are retained; this high-level activity view does not establish exact message versions.

## Source qualifications and omissions

- Statement is the literal source edge label although the nodes and T39 concern a price report. The error path is dashed; Correction Required has only a Yes branch. T39 supplies the reason requirement and replacement rule.
- Unlabelled plain source connectors are retained as undirected lines; business direction established by the activity table is described separately. Blank start/end and control symbols remain blank. Mermaid swimlanes preserve responsibility labels but not the exact source geometry.
