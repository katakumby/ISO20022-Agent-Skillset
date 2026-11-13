---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
flow_id: "flow-src-000368-p126-query"
title: "Query party reference data or audit trail"
source_locations: [{"source_id": "src-000368", "table_id": "T11", "xml_path": "/w:document/w:body/w:tbl[11]", "heading_path": ["BusinessProcess Description"]}, {"source_id": "src-000368", "table_id": "T17", "xml_path": "/w:document/w:body/w:tbl[17]", "heading_path": ["Description of BusinessActivities", "Party Reference Data", "Query/Query Response process"]}]
participants: ["participant-src-000368-instructing-party", "participant-src-000368-executing-servicing-party"]
message_mapping_evidence: [{"source_id": "src-000368", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Party Reference Data"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[6]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000368", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Party Reference Data"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[7]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.015.001.01", "reda.017.001.02", "reda.042.001.01", "reda.043.001.02"]
message_families: ["reda.015", "reda.017", "reda.042", "reda.043"]
search_terms: ["Query", "Executing / Servicing Party", "Instructing Party", "reda.015", "reda.017"]
limitations: ["Part1 figures use message families; exact supplied definitions are independently confirmed in Part2 src-000369.", "Source conditions, queuing and rejection reasons remain scenario-specific."]
manual_curated: true
participant_ids: ["participant-src-000368-instructing-party", "participant-src-000368-executing-servicing-party"]
issue_ids: ["issue-000046"]
---

# Query party reference data or audit trail

[src-000368](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`; [T11](../documents/src-000368/tables/tbl-0011.md) and [T17](../documents/src-000368/tables/tbl-0017.md).

## Purpose, trigger, preconditions and outcomes

| Item | Description |
| --- | --- |
| Definition | The Instructing Party asks the Executing/Servicing Party a response to a query. |
| Trigger | The process is triggered when the Instructing Party sends a Party Query message. |
| Pre-conditions | The query type must be known by the Instructing party and the Executing/Servicing Party. |
| Post-conditions | The Party Report message including all of the retrieved Party Records |
| Role | Instructing Party |


## Participants, activities and responsibilities

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000368-instructing-party.md)
- [Executing / Servicing Party](../../../../../../../shared/reference/participants/participant-src-000368-executing-servicing-party.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Instruction | Instructing Party instructs Executing/Servicing Party to run a query or Audit Trail Query. | Instructing Party |
| Process Query | Executing/Servicing Party processes the request.<br>In case the processing of the query takes too much time or cannot give any positive response, the Executing/Servicing Party sends an error message back to the Instructing Party with the error code and the related explanation. | Executing/Servicing Party |
| Response | Executing/Services Party sends the response to the Instructing Party according to query results. | Executing/Servicing Party |
| Monitor process | Instructing Party monitors the status of the instruction. | Instructing Party |


## Ordered scenarios, alternative and failure paths

**P270** Query/Response Process

**P271** Party Query/ Party Report Scenario

**P275** Party query

**P276** The Instructing Party sends an instruction to the Executing/Servicing Party to run a query according to specified criteria.

**P277** Party Report 

**P278** Depending on the query criteria, it is possible that the processing will take more than a certain timeor that the result of the query will be empty due to wrong combination of criteria or no result set. In this case, an error message within a query response message is sent to the Instructing Party.

**P279** Party Report 

**P280** The Executing/Servicing Party sends a query response that meets the specified criteria to the Instructing Party.

**P282** Party Audit Trail Query/ Party Audit Trail Report Scenario

**P285** Party Audit Trail Query

**P286** The Instructing Party sends an instruction to the Executing/Servicing Party to run a query according to specified criteria’s to retrieve the complete audit trail on a specific party.

**P287** Party Audit Trail Report

**P288** Depending on the query criteria, it is possible that the processing will take more than a certain timeor that the result of the query will be empty due to wrong combination of criteria or no result set. In this case, an error message within a query response message is sent to the Instructing Party.

**P289** Party Audit Trail Report

**P290** The Executing/Servicing Party sends a query response that meets the specified criteria to the Instructing Party.

## Diagrams and exact supplied message definitions

- [Party query and response activity](../diagrams/party-reference-data/fig-0010.md)
- [Party query and report sequence](../diagrams/party-reference-data/fig-0018.md)
- [Party audit trail query and report sequence](../diagrams/party-reference-data/fig-0019.md)

- [reda.015.001.01](../../../../messages/reda.015.001.01/index.md)
- [reda.017.001.02](../../../../messages/reda.017.001.02/index.md)
- [reda.042.001.01](../../../../messages/reda.042.001.01/index.md)
- [reda.043.001.02](../../../../messages/reda.043.001.02/index.md)

## Scope qualifications

P99–P103 distinguishes party/list/restricted-party search and audit-trail search. P102 calls an audit-query error Party Report, while P103 and the audit sequence name Party Audit Trail Report; issue-000046 preserves both.

P87 supplies the publication-specific BAH context. No cancellation or reversal of these reference-data requests is established by these source flows.
