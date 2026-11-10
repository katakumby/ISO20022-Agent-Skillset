---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
flow_id: "flow-src-000371-p156-query"
title: "Query securities account data or audit trail"
source_locations: [{"source_id": "src-000371", "table_id": "T11", "xml_path": "/w:document/w:body/w:tbl[11]"}, {"source_id": "src-000371", "table_id": "T17", "xml_path": "/w:document/w:body/w:tbl[17]"}]
participants: ["participant-src-000371-executing-servicing-party", "participant-src-000371-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000371", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[6]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000371", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[7]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.019.001.01", "reda.021.001.01", "reda.036.001.01", "reda.037.001.01"]
message_families: ["reda.019", "reda.021", "reda.036", "reda.037"]
search_terms: ["Query", "Executing/Servicing Party", "Instructing Party", "reda.019", "reda.021"]
limitations: ["Exact definitions independently confirmed in supplied Part2 src-000372; family labels in Part1 retained."]
manual_curated: true
participant_ids: ["participant-src-000371-account-owner", "participant-src-000371-account-owner-parent", "participant-src-000371-account-servicer", "participant-src-000371-audit-approving-user", "participant-src-000371-audit-initiating-user", "participant-src-000371-executing-servicing-party", "participant-src-000371-instructing-party"]
issue_ids: []
---

# Query securities account data or audit trail

[src-000371](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`; [T11](../documents/src-000371/tables/tbl-0011.md) and [T17](../documents/src-000371/tables/tbl-0017.md).

## Purpose, trigger, preconditions and outcome

| Item | Description |
| --- | --- |
| Definition | The Instructing Party asks the Executing/Servicing Party a response to a query. |
| Trigger | The process is triggered when the Instructing Party sends a Securities Account Query message. |
| Pre-conditions | The query type must be known by the Instructing party and the Executing/Servicing Party. |
| Post-conditions | The Securities Account Report message including all of the retrieved securities account records |
| Role | Instructing Party |


## Participants and ordered activities

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000371-instructing-party.md)
- [Executing/Servicing Party](../../../../../../../shared/reference/participants/participant-src-000371-executing-servicing-party.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Instruction | Instructing Party instructs Executing/Servicing Party to run a query or Audit Trail Query. | Instructing Party |
| Process Query | Executing/Servicing Party processes the request.<br>In case the processing of the query takes too much time or cannot give any positive response, the Executing/Servicing Party sends an error message back to the Instructing Party with the error code and the related explanation. | Executing/Servicing Party |
| Response | Executing/Services Party sends the response to the Instructing Party according to query results. | Executing/Servicing Party |
| Monitor Process | Instructing Party monitors the status of the instruction. | Instructing Party |


## Scenarios, alternatives and failures

**P300** Query/Response Process

**P301** Securities Account Query/Securities Account Report Scenario

**P305** Securities Account Query

**P306** The Instructing Party sends an instruction to the Executing/Servicing Party to run a query according to specified criteria.

**P307** Securities Account Report 

**P308** Depending on the query criteria, it is possible that the processing will take more than a certain timeor that the result of the query will be empty due to wrong combination of criteria or no result set. In this case, an error message within a query response message is sent to the Instructing Party.

**P309** Securities Account Report 

**P310** The Executing/Servicing Party sends a query response that meets the specified criteria to the Instructing Party.

**P311** Securities Account Audit Trail Query/Securities Account Audit Trail Report Scenario

**P314** Securities Account Audit Trail Query

**P315** The Instructing Party sends an instruction to the Executing/Servicing Party to run a query according to specified criteria’s to retrieve the complete audit trail on a specific securities account.

**P316** Securities Account Audit Trail Report

**P317** Depending on the query criteria, it is possible that the processing will take more than a certain timeor that the result of the query will be empty due to wrong combination of criteria or no result set. In this case, an error message within a query response message is sent to the Instructing Party.

**P318** Securities Account Audit Trail Report

**P319** The Executing/Servicing Party sends a query response that meets the specified criteria to the Instructing Party.

## Diagrams and messages

- [Query and response activity](../diagrams/securities-account-reference-data/fig-0010.md)
- [Securities account query and report](../diagrams/securities-account-reference-data/fig-0018.md)
- [Securities account audit trail query and report](../diagrams/securities-account-reference-data/fig-0019.md)

- [reda.019.001.01](../../../../messages/reda.019.001.01/index.md)
- [reda.021.001.01](../../../../messages/reda.021.001.01/index.md)
- [reda.036.001.01](../../../../messages/reda.036.001.01/index.md)
- [reda.037.001.01](../../../../messages/reda.037.001.01/index.md)

## Scope

P85/P89 establishes BAH usage. The source does not define a cancellation or reversal request for these flows. Conditional queuing is not made mandatory. T18 explicitly excludes the optional statement instruction from message scope; T12 requires a standing instruction and P326 makes delivery unsolicited.

<!-- DATA-ROLE-account-owner -->
[Account owner](../../../../../../../shared/reference/participants/participant-src-000371-account-owner.md) appears in the narrative/reference data; no extra actor lane or message direction is inferred.

<!-- DATA-ROLE-account-servicer -->
[Account servicer](../../../../../../../shared/reference/participants/participant-src-000371-account-servicer.md) appears in the narrative/reference data; no extra actor lane or message direction is inferred.

<!-- DATA-ROLE-account-owner-parent -->
[Account owner Parent](../../../../../../../shared/reference/participants/participant-src-000371-account-owner-parent.md) appears in the narrative/reference data; no extra actor lane or message direction is inferred.

<!-- DATA-ROLE-audit-initiating-user -->
[Audit initiating user](../../../../../../../shared/reference/participants/participant-src-000371-audit-initiating-user.md) appears in the narrative/reference data; no extra actor lane or message direction is inferred.

<!-- DATA-ROLE-audit-approving-user -->
[Audit approving user](../../../../../../../shared/reference/participants/participant-src-000371-audit-approving-user.md) appears in the narrative/reference data; no extra actor lane or message direction is inferred.
