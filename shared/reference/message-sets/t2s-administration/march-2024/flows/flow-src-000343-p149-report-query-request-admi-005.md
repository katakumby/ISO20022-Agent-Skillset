---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "shared"
source_ids: ["src-000343"]
source_editions: ["march-2024"]
message_sets: ["t2s-administration"]
flow_id: "flow-src-000343-p149-report-query-request-admi-005"
title: "Report query request activity"
source_locations: [{"source_id": "src-000343", "heading_path": ["Description of BusinessActivities", "Report Query Request (admi.005)"], "locator": "/w:document/w:body/w:p[149]", "paragraph_id": "P149", "table_id": null}, {"source_id": "src-000343", "heading_path": ["Description of BusinessActivities", "Report Query Request (admi.005)"], "locator": "/w:document/w:body/w:p[150]", "paragraph_id": "P150", "table_id": null}, {"source_id": "src-000343", "heading_path": ["Description of BusinessActivities", "Report Query Request (admi.005)"], "locator": "/w:document/w:body/w:p[151]", "paragraph_id": "P151", "table_id": null}, {"source_id": "src-000343", "heading_path": ["Description of BusinessActivities", "Report Query Request (admi.005)"], "locator": "/w:document/w:body/w:tbl[12]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000343", "heading_path": ["Description of BusinessActivities", "Report Query Request (admi.005)"], "locator": "/w:document/w:body/w:p[152]", "paragraph_id": "P152", "table_id": null}, {"source_id": "src-000343", "heading_path": ["Description of BusinessActivities", "Report Query Request (admi.005)"], "locator": "/w:document/w:body/w:p[153]", "paragraph_id": "P153", "table_id": null}]
participants: ["participant-src-000343-system-member", "participant-src-000343-system-transaction-administrator"]
message_mapping_evidence: [{"source_id": "src-000343", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Administration"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["admi.005.001.02", "admi.007.001.01"]
message_families: ["admi.005", "admi.007"]
search_terms: ["Report Query Request (admi.005)", "System Transaction Administrator", "Settlement Infrastructure", "Instructing Party", "System Member", "Payment Bank", "admi.005"]
limitations: ["Source process and sequence labels are unversioned; exact supplied definitions are independently established by Part2 src-000344.", "Administrative acknowledgements, business outcomes and header usage remain separately scoped to the cited scenario."]
manual_curated: true
participant_ids: ["participant-src-000343-system-member", "participant-src-000343-system-transaction-administrator"]
---

# Report query request activity

[src-000343](../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart1_Target2Securities_Administration_2023_2024_v2.docx`; Description of BusinessActivities / Report Query Request (admi.005).

## Purpose, trigger, preconditions and outcomes

[T8](../documents/src-000343/tables/tbl-0008.md)

| Item | Description |
| --- | --- |
| Definition | The Report Query Request is sent by a CB, CSD or any party authorised by them to use the report query. It aims at querying the latest available report data of a specific report type. This message enables the sender to request a report (available and/or already sent) according to his access rights. The sender instructs Central System to send the latest available Report and uses the possible selection parameters to specify the report further.  |
| Trigger | The process is triggered when a CB, CSD or any party authorised by them to use the report query, defines specific search criteria. If none or not all of these selection parameters are specified, Central System returns all reports available consistent with the access rights. |
| Pre-conditions | The  System User has the respective privilege to obtain the requested report. The corresponding business data should be available and accessible. |
| Post-conditions | A Query Response Message for Business Data including requested business data is sent back to the requesting System Actor, i.e. either the retrieved data sets or a notification that the extraction returned a zero result. In case no business data is found a query response message for operational error is sent back to the requesting System Actor indicating the error(s) which occurred. |
| Role | System Member  |


## Participants and responsibilities

[System Member](../../../../participants/participant-src-000343-system-member.md) initiates the query, resend request or original A2A message; [System Transaction Administrator](../../../../participants/participant-src-000343-system-transaction-administrator.md) performs the central-system checks, delivery and applicable response. P150/P155/P161 establish contextual institutional mappings; those mappings do not merge the role definitions.

| Step | Description | Initiator |
| --- | --- | --- |
| Report Query Request | Request to receive a specified report | System Member |
| Rejection message | Informs the instruction party (by error and description) in case if the instruction of Report Query was not valid for processing.<br>There could be three different reasons for a rejection message:<br>plausibility check not successful<br>permission check not successful<br>no existing report which can be provided to system member. | System Transaction Administrator  |
| Response | Delivers the requested report (e. g. Statement of Holdings, Statement of Transactions etc.) to the requesting system member | System Transaction Administrator  |


## Source narrative

**P150** In the frame of Central System flow, instructing party corresponds to the direct participant, payment bank or CSD, the servicing/executing party or the receiving party is the settlement infrastructure who achieves the report query request. 

## Ordered decisions and exchanges

- [Source figure 11 with all steps, directions and conditions](../diagrams/administration/fig-0011.md)

This query requests the latest available report data according to access rights. T8 says omitted selection criteria return all available reports consistent with those rights. It is distinct from resending an already produced original message or file. Three source rejection checks are plausibility, permission and report availability (T12/figure11).

## Header and file context

P86 uses BAH with ReportQueryRequest and ResendRequest. P87 says ReceiptAcknowledgement is generally sent without BAH, with BAH attached when it responds to ReportQueryRequest. P88 lists missing authentication, inbound processing rejection, oversize/timeout and query-queuing scenarios without BAH. P90 says Business File Header can bundle one or more business messages and acknowledges negative validation of a message or whole file. These are publication-specific usage statements, not a universal rule inferred from header schemas.

[BAH versus Business File Header](../../../../concepts/business-application-header-and-business-file-header.md)

## Supplied exact definitions

- [admi.005.001.02](../../../../messages/admi.005.001.02/index.md)
- [admi.007.001.01](../../../../messages/admi.007.001.01/index.md)
