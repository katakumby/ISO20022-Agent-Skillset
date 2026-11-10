---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
flow_id: "flow-src-000371-p157-generate-statement"
title: "Receive unsolicited securities account activity"
source_locations: [{"source_id": "src-000371", "table_id": "T12", "xml_path": "/w:document/w:body/w:tbl[12]"}, {"source_id": "src-000371", "table_id": "T18", "xml_path": "/w:document/w:body/w:tbl[18]"}]
participants: ["participant-src-000371-executing-servicing-party"]
message_mapping_evidence: [{"source_id": "src-000371", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[8]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.035.001.01"]
message_families: ["reda.035"]
search_terms: ["Generate Statement", "Executing/Servicing Party", "reda.035"]
limitations: ["Exact definitions independently confirmed in supplied Part2 src-000372; family labels in Part1 retained."]
manual_curated: true
participant_ids: ["participant-src-000371-instructing-party", "participant-src-000371-executing-servicing-party", "participant-src-000371-recipient-party"]
issue_ids: []
---

# Receive unsolicited securities account activity

[src-000371](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`; [T12](../documents/src-000371/tables/tbl-0012.md) and [T18](../documents/src-000371/tables/tbl-0018.md).

## Purpose, trigger, preconditions and outcome

| Item | Description |
| --- | --- |
| Definition | The Recipient Party receives a Securities Account Activity Advice statement which has been automatically produced by the Executing/Servicing Party. |
| Trigger | The process is triggered automatically. |
| Pre-conditions | A standing instruction is in place at the Executing/Servicing Party for sending of the statement. |
| Post-conditions | The acknowledgement of the sending of the statement. |
| Role | Executing/Servicing Party |


## Participants and ordered activities

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000371-instructing-party.md)
- [Executing/Servicing Party](../../../../../../../shared/reference/participants/participant-src-000371-executing-servicing-party.md)
- [Recipient Party](../../../../../../../shared/reference/participants/participant-src-000371-recipient-party.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Instruction | Instructing Party might instruct Executing/Servicing Party to run a statement.<br>This is not covered by the current process as NO message will be created to cover this. | Instructing Party |
| Process Statement | Executing/Servicing Party processes the statement. | Executing/Servicing Party |
| Reporting | Executing/Servicing Party sends the statement to the Instructing Party. | Executing/Servicing Party |
| Monitor Process | Instructing Party monitors the status of the instruction. | Instructing Party |


## Scenarios, alternatives and failures

**P320** Statement Process

**P324** Securities Account Activity Advice 

**P325** The Executing/Servicing Party sends a statement to the Instructing Party containing information on changes occurred for securities account reference data during the business day

**P326** The statement is sent unilaterally in an unsolicited manner.

## Diagrams and messages

- [Statement activity](../diagrams/securities-account-reference-data/fig-0011.md)
- [Unsolicited securities account activity advice](../diagrams/securities-account-reference-data/fig-0020.md)

- [reda.035.001.01](../../../../messages/reda.035.001.01/index.md)

## Scope

P85/P89 establishes BAH usage. The source does not define a cancellation or reversal request for these flows. Conditional queuing is not made mandatory. T18 explicitly excludes the optional statement instruction from message scope; T12 requires a standing instruction and P326 makes delivery unsolicited.
