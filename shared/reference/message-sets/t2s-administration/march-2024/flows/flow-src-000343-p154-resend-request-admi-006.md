---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "shared"
source_ids: ["src-000343"]
source_editions: ["march-2024"]
message_sets: ["t2s-administration"]
flow_id: "flow-src-000343-p154-resend-request-admi-006"
title: "Resend request activity"
source_locations: [{"source_id": "src-000343", "heading_path": ["Description of BusinessActivities", "Resend Request (admi.006)"], "locator": "/w:document/w:body/w:p[154]", "paragraph_id": "P154", "table_id": null}, {"source_id": "src-000343", "heading_path": ["Description of BusinessActivities", "Resend Request (admi.006)"], "locator": "/w:document/w:body/w:p[155]", "paragraph_id": "P155", "table_id": null}, {"source_id": "src-000343", "heading_path": ["Description of BusinessActivities", "Resend Request (admi.006)"], "locator": "/w:document/w:body/w:p[156]", "paragraph_id": "P156", "table_id": null}, {"source_id": "src-000343", "heading_path": ["Description of BusinessActivities", "Resend Request (admi.006)"], "locator": "/w:document/w:body/w:p[157]", "paragraph_id": "P157", "table_id": null}, {"source_id": "src-000343", "heading_path": ["Description of BusinessActivities", "Resend Request (admi.006)"], "locator": "/w:document/w:body/w:tbl[13]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000343", "heading_path": ["Description of BusinessActivities", "Resend Request (admi.006)"], "locator": "/w:document/w:body/w:p[158]", "paragraph_id": "P158", "table_id": null}, {"source_id": "src-000343", "heading_path": ["Description of BusinessActivities", "Resend Request (admi.006)"], "locator": "/w:document/w:body/w:p[159]", "paragraph_id": "P159", "table_id": null}]
participants: ["participant-src-000343-system-member", "participant-src-000343-system-transaction-administrator"]
message_mapping_evidence: [{"source_id": "src-000343", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Administration"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["admi.006.001.01", "admi.007.001.01"]
message_families: ["admi.006", "admi.007"]
search_terms: ["Resend Request (admi.006)", "System Transaction Administrator", "Settlement Infrastructure", "Instructing Party", "System Member", "Payment Bank", "admi.006"]
limitations: ["Source process and sequence labels are unversioned; exact supplied definitions are independently established by Part2 src-000344.", "Administrative acknowledgements, business outcomes and header usage remain separately scoped to the cited scenario."]
manual_curated: true
participant_ids: ["participant-src-000343-system-member", "participant-src-000343-system-transaction-administrator"]
---

# Resend request activity

[src-000343](../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart1_Target2Securities_Administration_2023_2024_v2.docx`; Description of BusinessActivities / Resend Request (admi.006).

## Purpose, trigger, preconditions and outcomes

[T9](../documents/src-000343/tables/tbl-0009.md)

| Item | Description |
| --- | --- |
| Definition | The Resend request enables directly connected CSDs, CBs or any parties authorized by them to request the resending of a message or a file (duplicate of the original message/file) supported by Central System. To instruct Central System for the resend of a message the technical address of the receiving party must be specified.   |
| Trigger | The process is triggered when a CB, CSD or any party authorised by them to use the Resend by defining specific criteria, e. g.  Business Date (optional field), Sequence number or Original Message Reference can be used to further specify the request: If no Business Date is specified the current Business Date is assumed  |
| Pre-conditions | The System User has the respective privilege to obtain the requested report. The corresponding business data (T2S outbound messages or files) are already produced and accessible  |
| Post-conditions | In response to the Resend Request message, Central System sends first a positive “Validation Result Resend” after the successful permission check. In parallel, the duplicate of the original message/file is sent. If an error occurs resulting from the processing of the Resend Request an error information is sent. |
| Role | System Member |


## Participants and responsibilities

[System Member](../../../../participants/participant-src-000343-system-member.md) initiates the query, resend request or original A2A message; [System Transaction Administrator](../../../../participants/participant-src-000343-system-transaction-administrator.md) performs the central-system checks, delivery and applicable response. P150/P155/P161 establish contextual institutional mappings; those mappings do not merge the role definitions.

| Step | Description | Initiator |
| --- | --- | --- |
| Resend Request | Request to initiate the sending of a specified already sent message  | System Member |
| Rejection message | Informs the instructing party (by error and description) in case if the instruction of Resend Message Request was not valid for processing.<br>There could be three different reasons for a rejection message:<br>plausibility check not successful<br>permission check not successful<br>no existing message which can be provided to system member. | System Transaction Administrator  |
| Response | Delivers the requested message (duplicate of the original) to the requesting system member  | System Transaction Administrator  |


## Source narrative

**P155** In the frame of Central flow, instructing party corresponds to the direct participant or payment bank, the servicing/executing party or the receiving party is the settlement infrastructure who achieves the ResendRequest.

## Ordered decisions and exchanges

- [Source figure 12 with all steps, directions and conditions](../diagrams/administration/fig-0012.md)

T9 requires the recipient technical address. Business Date is optional; when absent, the current Business Date is assumed. It also specifies a positive Validation Result Resend after successful permission checking, with the duplicate sent in parallel. Figures17/18 show the duplicate but omit that positive validation arrow; both scopes are retained. P182 specifies push-mode duplicate delivery and duplicate indication in the BAH.

## Header and file context

P86 uses BAH with ReportQueryRequest and ResendRequest. P87 says ReceiptAcknowledgement is generally sent without BAH, with BAH attached when it responds to ReportQueryRequest. P88 lists missing authentication, inbound processing rejection, oversize/timeout and query-queuing scenarios without BAH. P90 says Business File Header can bundle one or more business messages and acknowledges negative validation of a message or whole file. These are publication-specific usage statements, not a universal rule inferred from header schemas.

[BAH versus Business File Header](../../../../concepts/business-application-header-and-business-file-header.md)

## Supplied exact definitions

- [admi.006.001.01](../../../../messages/admi.006.001.01/index.md)
- [admi.007.001.01](../../../../messages/admi.007.001.01/index.md)
