---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
flow_id: "flow-src-000368-p128-statement"
title: "Receive an unsolicited party activity statement"
source_locations: [{"source_id": "src-000368", "table_id": "T12", "xml_path": "/w:document/w:body/w:tbl[12]", "heading_path": ["BusinessProcess Description"]}, {"source_id": "src-000368", "table_id": "T18", "xml_path": "/w:document/w:body/w:tbl[18]", "heading_path": ["Description of BusinessActivities", "Party Reference Data", "Statement process"]}]
participants: ["participant-src-000368-instructing-party", "participant-src-000368-executing-servicing-party", "participant-src-000368-recipient-party"]
message_mapping_evidence: [{"source_id": "src-000368", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Party Reference Data"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[8]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.041.001.02"]
message_families: ["reda.041"]
search_terms: ["Statement", "Executing / Servicing Party", "reda.041"]
limitations: ["Part1 figures use message families; exact supplied definitions are independently confirmed in Part2 src-000369.", "Source conditions, queuing and rejection reasons remain scenario-specific."]
manual_curated: true
participant_ids: ["participant-src-000368-instructing-party", "participant-src-000368-executing-servicing-party", "participant-src-000368-recipient-party"]
issue_ids: []
---

# Receive an unsolicited party activity statement

[src-000368](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`; [T12](../documents/src-000368/tables/tbl-0012.md) and [T18](../documents/src-000368/tables/tbl-0018.md).

## Purpose, trigger, preconditions and outcomes

| Item | Description |
| --- | --- |
| Definition | The Recipient Party receives a Party Activity Advice statement which has been automatically produced by the Executing/Servicing Party. |
| Trigger | The process is triggered automatically. |
| Pre-conditions | A standing instruction is in place at the Executing/Servicing Party for sending of the statement. |
| Post-conditions | The acknowledgement of the sending of the statement. |
| Role | Executing/Servicing Party |


## Participants, activities and responsibilities

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000368-instructing-party.md)
- [Executing / Servicing Party](../../../../../../../shared/reference/participants/participant-src-000368-executing-servicing-party.md)
- [Recipient Party](../../../../../../../shared/reference/participants/participant-src-000368-recipient-party.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Instruction | Instructing Party might instruct Executing/Servicing Party to run a statement.<br>This is not covered by the current process as NO message will be created to cover this. | Instructing Party |
| Process Statement | Executing/Servicing Party processes the statement. | Executing/Servicing Party |
| Reporting | Executing/Servicing Party sends the statement to the Instructing Party. | Executing/Servicing Party |
| Monitor process | Instructing Party monitors the status of the instruction. | Instructing Party |


## Ordered scenarios, alternative and failure paths

**P292** Statement Process

**P295** Party Activity Advice 

**P296** The Executing/Servicing Party sends a statement to the Instructing Party containing information on changes occurred for Party reference data during the business day.

**P297** The statement is sent unilaterally in an unsolicited manner.

## Diagrams and exact supplied message definitions

- [Party activity statement activity](../diagrams/party-reference-data/fig-0011.md)
- [Unsolicited party activity advice sequence](../diagrams/party-reference-data/fig-0020.md)

- [reda.041.001.02](../../../../messages/reda.041.001.02/index.md)

## Scope qualifications

T18 draws/describes a possible statement instruction but explicitly says it is outside the process and no message is created for it. T12 requires a standing instruction; P297 says the statement is unsolicited. Recipient Party is retained from the narrative even though the picture labels the recipient Instructing Party.

P87 supplies the publication-specific BAH context. No cancellation or reversal of these reference-data requests is established by these source flows.
