---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p226-portfolio-and-stock-transfers-single-leg"
title: "Portfolio and Stock Transfers (Single Leg)"
source_locations: [{"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", " Portfolio and Stock Transfers (Single Leg)"], "locator": "/w:document/w:body/w:p[226]", "paragraph_id": "P226", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", " Portfolio and Stock Transfers (Single Leg)"], "locator": "/w:document/w:body/w:p[227]", "paragraph_id": "P227", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", " Portfolio and Stock Transfers (Single Leg)"], "locator": "/w:document/w:body/w:p[228]", "paragraph_id": "P228", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", " Portfolio and Stock Transfers (Single Leg)"], "locator": "/w:document/w:body/w:p[229]", "paragraph_id": "P229", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", " Portfolio and Stock Transfers (Single Leg)"], "locator": "/w:document/w:body/w:tbl[44]", "paragraph_id": null, "table_id": "T44"}]
participants: ["participant-src-000095-transferor", "participant-src-000095-transferee", "participant-src-000095-intermediary", "participant-src-000095-transfer-agent"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[2]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000096", "locator": "file page 1308; 38 sese.018.001.10 AccountHoldingInformationV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[3]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000096", "locator": "file page 1442; 39 sese.019.001.09 AccountHoldingInformationRequestV09"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[2]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000096", "locator": "file page 943; 35 sese.012.001.12 PortfolioTransferInstructionV12"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[2]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 433; 24 sese.001.001.10 TransferOutInstructionV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[4]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 519; 26 sese.003.001.10 TransferOutConfirmationV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[8]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 695; 30 sese.007.001.10 TransferInConfirmationV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[4]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000096", "locator": "file page 816; 34 sese.011.001.10 TransferInstructionStatusReportV10"}]
message_ids: []
message_families: ["sese.001", "sese.003", "sese.007", "sese.011", "sese.012", "sese.018", "sese.019"]
search_terms: ["Portfolio and Stock Transfers (Single Leg)", "Instructing Party", "Executing Party", "Transfer Agent", "Intermediary", "Transferor", "Transferee", "Custodian", "sese.001", "sese.003", "sese.007", "sese.011", "sese.012", "sese.018", "sese.019"]
limitations: ["The source has two horizontal phases: Exchange of Information through Validate Information; Portfolio & Asset Transfer from Instruct Portfolio Transfer onward. This phase split is preserved in text to avoid confusing the two distinct Intermediary lanes. Status is not required if transfer is registered immediately. Plain source lines do not become inferred arrowheads.", "Unlabelled plain source connectors are retained as undirected lines; business direction established by the activity table is described separately. Blank start/end and control symbols remain blank. Mermaid swimlanes preserve responsibility labels but not the exact source geometry."]
manual_curated: true
participant_ids: ["participant-src-000095-transferor", "participant-src-000095-transferee", "participant-src-000095-intermediary", "participant-src-000095-transfer-agent"]
related_diagrams: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0016.md"]
updated: "2026-11-09"
diagram_review: {"status": "pass", "date": "2026-11-09", "reviewer": "shared-evidence agent", "scope": "Original extracted picture and complete Word-rendered source page compared with rendered Mermaid PNG; checked actor occurrences, source labels, endpoints, arrowheads/plain lines, lane/control boundaries and alternatives. Complete-page composition checked in contact sheets; original pictures inspected at readable size.", "source_page": 36, "result_notes": ["All source edges and labels compared; plain-line connectors not promoted to inferred direction."]}
issue_ids: []
---



# Transfer — Single Leg (Transferor instructing)

[src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md); Description of BusinessActivities /  Portfolio and Stock Transfers (Single Leg); direct-body paragraph P229; T44.

## Purpose, trigger and conditions

The activity source does not provide a separate trigger/precondition/postcondition table for this view. Conditions and outcomes are those explicitly stated in the activity rows and narrative below.

The instructing party may be a transferor's bank, transferor's intermediary/custodian, transferee's bank or transferee's intermediary/custodian. (P227)

The executing party may be the transferor's intermediary/custodian, transferee's intermediary/custodian or transfer agent. (P228)

## Participants and responsibilities

- [transferor](../../../../../../../shared/reference/participants/participant-src-000095-transferor.md)
- [transferee](../../../../../../../shared/reference/participants/participant-src-000095-transferee.md)
- [intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md)
- [transfer agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Request Delivery Chain Information | The account holding information request is sent by the transferor. | Transferor |
| Provide Delivery Chain Information | The request is validated by the transferor’s Intermediary, who subsequently sends the delivery chain account holding information to the transferor.  | Intermediary |
| Advise Transfer Intention | The transferor advises the transferee of its intention to transfer an investor’s portfolio, the delivery chain account information is provided. | Transferor |
| Record Asserts to be Received | The assets to be received are recorded by the transferee. The transferee requests its intermediary for the receiving chain account holding information. | Transferee |
| Record Asserts to be Received | The assets to be received are recorded by the transferee’s intermediary, who subsequently notifies the transferee of the receiving chain account holding information. | Intermediary |
| Advice Receiving Account Information | The transferee notifies the transferor of the receiving chain account holding information. | Transferee |
| Instruct Portfolio Transfer | The portfolio transfer instruction is sent by the transferor to its intermediary. | Transferor |
| Instruct Asset transfer | A transfer out instruction is sent by the transferor’s Intermediary to the transfer agent. | Intermediary |
| Provide Status | The transfer out instruction is validated by the transfer agent, who optionally sends a transfer instruction status report; if the transfer could not be registered immediately. | Transfer Agent |
| Confirm Transfer | The transfer out and transfer in confirmations are simultaneously sent by the transfer agent to the transferor’s intermediary and the transferee’s intermediary. | Transfer Agent |
| Confirm transfer | The transfer out confirmation is sent by the transferor’s intermediary to the transferor, while the transfer in confirmation is sent to the transferee’s intermediary to complete the stock transfer. | Intermediary |


## Ordered paths, messages and alternatives

[Complete source reconstruction, connector list and decision paths](../diagrams/funds-processes/fig-0016.md)

Follow the source graph for connected activities; the source table lists responsibilities rather than a universal execution order. Source-labelled exchange types are retained; this high-level activity view does not establish exact message versions.

## Source qualifications and omissions

- The source has two horizontal phases: Exchange of Information through Validate Information; Portfolio & Asset Transfer from Instruct Portfolio Transfer onward. This phase split is preserved in text to avoid confusing the two distinct Intermediary lanes. Status is not required if transfer is registered immediately. Plain source lines do not become inferred arrowheads.
- Unlabelled plain source connectors are retained as undirected lines; business direction established by the activity table is described separately. Blank start/end and control symbols remain blank. Mermaid swimlanes preserve responsibility labels but not the exact source geometry.
