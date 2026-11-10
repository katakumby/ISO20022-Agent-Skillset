---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p230-portfolio-and-stock-transfers-double-matched-leg"
title: "Portfolio and Stock Transfers (Double/Matched Leg)"
source_locations: [{"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Portfolio and Stock Transfers (Double/Matched Leg)"], "locator": "/w:document/w:body/w:p[230]", "paragraph_id": "P230", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Portfolio and Stock Transfers (Double/Matched Leg)"], "locator": "/w:document/w:body/w:p[231]", "paragraph_id": "P231", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Portfolio and Stock Transfers (Double/Matched Leg)"], "locator": "/w:document/w:body/w:p[232]", "paragraph_id": "P232", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Portfolio and Stock Transfers (Double/Matched Leg)"], "locator": "/w:document/w:body/w:p[233]", "paragraph_id": "P233", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Portfolio and Stock Transfers (Double/Matched Leg)"], "locator": "/w:document/w:body/w:tbl[45]", "paragraph_id": null, "table_id": "T45"}]
participants: ["participant-src-000095-transferor", "participant-src-000095-transferee", "participant-src-000095-transfer-agent"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[2]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 433; 24 sese.001.001.10 TransferOutInstructionV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[6]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 608; 28 sese.005.001.10 TransferInInstructionV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[8]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 695; 30 sese.007.001.10 TransferInConfirmationV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[4]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000096", "locator": "file page 816; 34 sese.011.001.10 TransferInstructionStatusReportV10"}]
message_ids: []
message_families: ["sese.001", "sese.005", "sese.007", "sese.011"]
search_terms: ["Portfolio and Stock Transfers (Double/Matched Leg)", "Instructing Party", "Executing Party", "Transfer Agent", "Intermediary", "Transferor", "Transferee", "Custodian", "sese.001", "sese.005", "sese.007", "sese.011"]
limitations: ["The two Agree Transfer actions and their bidirectional Conversation are explicitly Out of Scope. Received status is not required if transfer is registered immediately. Only transferor and transfer-agent final symbols are drawn; no transferee final node is invented. Plain connectors are retained without inferred arrowheads.", "Unlabelled plain source connectors are retained as undirected lines; business direction established by the activity table is described separately. Blank start/end and control symbols remain blank. Mermaid swimlanes preserve responsibility labels but not the exact source geometry."]
manual_curated: true
participant_ids: ["participant-src-000095-transferor", "participant-src-000095-transferee", "participant-src-000095-transfer-agent"]
related_diagrams: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0017.md"]
updated: "2026-11-09"
diagram_review: {"status": "pass", "date": "2026-11-09", "reviewer": "shared-evidence agent", "scope": "Original extracted picture and complete Word-rendered source page compared with rendered Mermaid PNG; checked actor occurrences, source labels, endpoints, arrowheads/plain lines, lane/control boundaries and alternatives. Complete-page composition checked in contact sheets; original pictures inspected at readable size.", "source_page": 38, "result_notes": ["All source edges and labels compared; plain-line connectors not promoted to inferred direction."]}
issue_ids: []
---



# Transfer Flow — Double Leg (institution to institution)

[src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx); Description of BusinessActivities / Portfolio and Stock Transfers (Double/Matched Leg); direct-body paragraph P233; T45.

## Purpose, trigger and conditions

The activity source does not provide a separate trigger/precondition/postcondition table for this view. Conditions and outcomes are those explicitly stated in the activity rows and narrative below.

The instructing party may be a transferor's bank, transferor's intermediary/custodian, transferee's bank or transferee's intermediary/custodian. (P231)

The executing party may be the transferor's intermediary/custodian, transferee's intermediary/custodian or transfer agent. (P232)

## Participants and responsibilities

- [transferor](../../../../../../../shared/reference/participants/participant-src-000095-transferor.md)
- [transferee](../../../../../../../shared/reference/participants/participant-src-000095-transferee.md)
- [transfer agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Instruct Transfer | The transfer out instruction is sent by the transferor to the transferee’s transfer agent. | Transferor |
| Instruct Transfer | The transfer in instruction is sent by the transferee to its transfer agent. | Transferee |
| Provide Status | The transfer out and transfer in instructions are validated by the transfer agent, who sends first a transfer instruction status report with the status received to the transferor and transferee as soon as their instructions have been received and optionally a second transfer instruction status report with the status matched is sent to the transferor and transferee, if the transfer could not be registered immediately. | Transfer Agent |
| Confirmed | The transfer out and transfer in confirmations are simultaneously sent by the transfer agent to the transferor and the transferee to complete the transfer. | Transfer Agent |


## Ordered paths, messages and alternatives

[Complete source reconstruction, connector list and decision paths](../diagrams/funds-processes/fig-0017.md)

Follow the source graph for connected activities; the source table lists responsibilities rather than a universal execution order. Source-labelled exchange types are retained; this high-level activity view does not establish exact message versions.

## Source qualifications and omissions

- The two Agree Transfer actions and their bidirectional Conversation are explicitly Out of Scope. Received status is not required if transfer is registered immediately. Only transferor and transfer-agent final symbols are drawn; no transferee final node is invented. Plain connectors are retained without inferred arrowheads.
- Unlabelled plain source connectors are retained as undirected lines; business direction established by the activity table is described separately. Blank start/end and control symbols remain blank. Mermaid swimlanes preserve responsibility labels but not the exact source geometry.
