---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p221-stock-transfers-single-leg-transfer"
title: "Stock Transfers (Single Leg Transfer)"
source_locations: [{"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Stock Transfers (Single Leg Transfer)"], "locator": "/w:document/w:body/w:p[221]", "paragraph_id": "P221", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Stock Transfers (Single Leg Transfer)"], "locator": "/w:document/w:body/w:p[222]", "paragraph_id": "P222", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Stock Transfers (Single Leg Transfer)"], "locator": "/w:document/w:body/w:p[223]", "paragraph_id": "P223", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Stock Transfers (Single Leg Transfer)"], "locator": "/w:document/w:body/w:p[224]", "paragraph_id": "P224", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Stock Transfers (Single Leg Transfer)"], "locator": "/w:document/w:body/w:p[225]", "paragraph_id": "P225", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Stock Transfers (Single Leg Transfer)"], "locator": "/w:document/w:body/w:tbl[43]", "paragraph_id": null, "table_id": "T43"}]
participants: ["participant-src-000095-transferee-s-bank-instructing-party", "participant-src-000095-transferor-s-bank-executing-party", "participant-src-000095-transferor-s-bank-instructing-party", "participant-src-000095-transferee-s-bank-executing-party", "participant-src-000095-transfer-agent", "participant-src-000095-end-client"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[2]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 433; 24 sese.001.001.10 TransferOutInstructionV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[6]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 608; 28 sese.005.001.10 TransferInInstructionV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[8]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 695; 30 sese.007.001.10 TransferInConfirmationV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[4]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000096", "locator": "file page 816; 34 sese.011.001.10 TransferInstructionStatusReportV10"}]
message_ids: []
message_families: ["sese.001", "sese.005", "sese.007", "sese.011"]
search_terms: ["Stock Transfers (Single Leg Transfer)", "Transferee's Bank (Instructing Party)", "Transferor's Bank (Instructing Party)", "Transferor's Bank (Executing Party)", "Transferee's Bank (Executing Party)", "Instructing Party", "Executing Party", "Transfer Agent", "Intermediary", "Transferor", "Transferee", "Custodian", "sese.001", "sese.005", "sese.007", "sese.011"]
limitations: ["All process connectors except the initial start arrow are plain lines in this artwork. Direction of named message exchanges is established separately by T43. End Client is mentioned in action labels and T43 but has no separate lane. T43 leaves the fourth activity Initiator blank.", "Unlabelled plain source connectors are retained as undirected lines; business direction established by the activity table is described separately. Blank start/end and control symbols remain blank. Mermaid swimlanes preserve responsibility labels but not the exact source geometry."]
manual_curated: true
participant_ids: ["participant-src-000095-transferee-s-bank-instructing-party", "participant-src-000095-transferor-s-bank-executing-party", "participant-src-000095-transferor-s-bank-instructing-party", "participant-src-000095-transferee-s-bank-executing-party", "participant-src-000095-transfer-agent", "participant-src-000095-end-client"]
related_diagrams: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0015.md"]
updated: "2026-11-09"
diagram_review: {"status": "pass", "date": "2026-11-09", "reviewer": "shared-evidence agent", "scope": "Original extracted picture and complete Word-rendered source page compared with rendered Mermaid PNG; checked actor occurrences, source labels, endpoints, arrowheads/plain lines, lane/control boundaries and alternatives. Complete-page composition checked in contact sheets; original pictures inspected at readable size.", "source_page": 34, "result_notes": ["All source edges and labels compared; plain-line connectors not promoted to inferred direction."]}
issue_ids: []
---



# Transfer Flow — Single Leg (from transfer agent perspective)

[src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx); Description of BusinessActivities / Stock Transfers (Single Leg Transfer); direct-body paragraph P225; T43.

## Purpose, trigger and conditions

The activity source does not provide a separate trigger/precondition/postcondition table for this view. Conditions and outcomes are those explicitly stated in the activity rows and narrative below.

This scenario is based on the Securities Market Practice Group (SMPG) Investment Funds working group market practice. (P222)

The instructing party may be a transferor's bank or transferee's bank. The executing party may be the transfer agent. (P223)

There may be one an intermediary/transferee's custodian between the transferee's bank and the transfer agent. There may be one an intermediary/transferor's custodian between the transferor's bank and the transfer agent. (P224)

## Participants and responsibilities

- [transferee s bank instructing party](../../../../../../../shared/reference/participants/participant-src-000095-transferee-s-bank-instructing-party.md)
- [transferor s bank executing party](../../../../../../../shared/reference/participants/participant-src-000095-transferor-s-bank-executing-party.md)
- [transferor s bank instructing party](../../../../../../../shared/reference/participants/participant-src-000095-transferor-s-bank-instructing-party.md)
- [transferee s bank executing party](../../../../../../../shared/reference/participants/participant-src-000095-transferee-s-bank-executing-party.md)
- [transfer agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)
- [end client](../../../../../../../shared/reference/participants/participant-src-000095-end-client.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Instruct Transfer | A transfer in instruction is sent by the transferee’s bank to the transferor's bank. The transferee's bank must have enough information to instruct the transfer | Transferee's Bank (Instructing Party) |
| Validate Instruction + provide Status | The transfer in instruction is validated, a transfer instruction status report is sent. | Transferor's Bank (Executing Party) |
| Instruct Transfer | A transfer out instruction is sent by the transferor’s bank to the transfer agent.  | Transferor's Bank (Instructing Party) |
| Validate Instruction + provide Status | The transfer out instruction is validated, a transfer instruction status report is sent. |  |
| Confirm Transfer | The transfer out and transfer in confirmations are simultaneously sent by the transfer agent to the transferor’s bank and the transferee’s bank. | Transfer Agent |
| Inform End Client | The transferee's bank informs the end-client of the transfer. | Transferee's Bank (Executing Party) |
| Inform End Client | The transferor's bank informs the end-client of the transfer. | Transferor's Bank (Executing Party) |


## Ordered paths, messages and alternatives

[Complete source reconstruction, connector list and decision paths](../diagrams/funds-processes/fig-0015.md)

Follow the source graph for connected activities; the source table lists responsibilities rather than a universal execution order. Source-labelled exchange types are retained; this high-level activity view does not establish exact message versions.

## Source qualifications and omissions

- All process connectors except the initial start arrow are plain lines in this artwork. Direction of named message exchanges is established separately by T43. End Client is mentioned in action labels and T43 but has no separate lane. T43 leaves the fourth activity Initiator blank.
- Unlabelled plain source connectors are retained as undirected lines; business direction established by the activity table is described separately. Blank start/end and control symbols remain blank. Mermaid swimlanes preserve responsibility labels but not the exact source geometry.
