---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "shared"
source_ids: ["src-000343"]
source_editions: ["march-2024"]
message_sets: ["t2s-administration"]
participant_id: "participant-src-000343-system-member"
title: "System Member"
source_labels: ["System Member"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000343", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000343", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[10]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000343", "heading_path": ["Description of BusinessActivities", "Report Query Request (admi.005)"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[2]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000343", "heading_path": ["Description of BusinessActivities", "Resend Request (admi.006)"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[2]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000343", "heading_path": ["Description of BusinessActivities", "Receipt Acknowledgement (admi.007)", "Scenario 1a"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[2]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000343", "heading_path": ["Description of BusinessActivities", "Receipt Acknowledgement (admi.007)", "Scenario 1b"], "locator": "/w:document/w:body/w:tbl[15]/w:tr[2]", "paragraph_id": null, "table_id": "T15"}]
flows: ["flow-src-000343-p126-report-query-process", "flow-src-000343-p136-resent-request-process", "flow-src-000343-p149-report-query-request-admi-005", "flow-src-000343-p154-resend-request-admi-006", "flow-src-000343-p162-scenario-1a", "flow-src-000343-p168-scenario-1b"]
process_sections: ["flow-src-000343-p160-receipt-acknowledgement-admi-007"]
message_ids: ["admi.005.001.02", "admi.006.001.01", "admi.007.001.01"]
message_families: ["admi.005", "admi.006", "admi.007"]
search_terms: ["System Member", "admi.005", "admi.006", "admi.007"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000343-p131-technical-processing", "flow-src-000343-p142-technical-processing", "flow-src-000343-p149-report-query-request-admi-005", "flow-src-000343-p154-resend-request-admi-006", "flow-src-000343-p162-scenario-1a", "flow-src-000343-p168-scenario-1b", "flow-src-000343-p175-report-query-request-business-transaction-admi-005", "flow-src-000343-p179-resend-request-business-transaction-admi-006", "flow-src-000343-p189-scenario-1-receipt-acknowledgement-sent-by-central-system-e-g-t2s-plat"]
---

# System Member

Business context: T2S Administration. Source classification: functional participant role.

## Definition

The party that is entitled to make full or partial use of the system transaction administrator, to make it perform business processes on its behalf. A member can submit transactions, and request and/or receive information. A member can be a direct or indirect member.

Evidence: [T5](../message-sets/t2s-administration/march-2024/documents/src-000343/tables/tbl-0005.md), source row 3.

The party that is entitled to make full or partial use of the system transaction administrator, to make it perform business processes on its behalf. A member can submit transactions, and request and/or receive information. A member can be a direct or indirect member.

Evidence: [T6](../message-sets/t2s-administration/march-2024/documents/src-000343/tables/tbl-0006.md), source row 10.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Report Query Request | Request to receive a specified report | Initiator | [T12](../message-sets/t2s-administration/march-2024/documents/src-000343/tables/tbl-0012.md) row 2 |
| Resend Request | Request to initiate the sending of a specified already sent message  | Initiator | [T13](../message-sets/t2s-administration/march-2024/documents/src-000343/tables/tbl-0013.md) row 2 |
| Scenario 1a<br> | Sending of an A2A-message (i.e. Query, Instruction etc.) | Initiator | [T14](../message-sets/t2s-administration/march-2024/documents/src-000343/tables/tbl-0014.md) row 2 |
| Scenario 1b<br> | Sending of an A2A-message (i.e. Query, Instruction etc.) | Initiator | [T15](../message-sets/t2s-administration/march-2024/documents/src-000343/tables/tbl-0015.md) row 2 |

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [T2S operator](participant-src-000343-t2s-operator.md) | [T7](../message-sets/t2s-administration/march-2024/documents/src-000343/tables/tbl-0007.md) row 2, column 2 |
| Business role listed for this functional participant | [National Central Bank](participant-src-000343-national-central-bank.md) | [T7](../message-sets/t2s-administration/march-2024/documents/src-000343/tables/tbl-0007.md) row 3, column 2 |
| Business role listed for this functional participant | [Payment Bank](participant-src-000343-payment-bank.md) | [T7](../message-sets/t2s-administration/march-2024/documents/src-000343/tables/tbl-0007.md) row 4, column 2 |
| Business role listed for this functional participant | [Settlement Infrastructure Direct Participant](participant-src-000343-settlement-infrastructure-direct-participant.md) | [T7](../message-sets/t2s-administration/march-2024/documents/src-000343/tables/tbl-0007.md) row 6, column 2 |
| Business role listed for this functional participant | [Instructing Party](participant-src-000343-instructing-party.md) | [T7](../message-sets/t2s-administration/march-2024/documents/src-000343/tables/tbl-0007.md) row 7, column 2 |
| Business role listed for this functional participant | [Executing/Servicing Party](participant-src-000343-executing-servicing-party.md) | [T7](../message-sets/t2s-administration/march-2024/documents/src-000343/tables/tbl-0007.md) row 8, column 2 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Report query process](../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p126-report-query-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Resent Request Process](../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p136-resent-request-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Report Query Request (admi.005)](../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p149-report-query-request-admi-005.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Resend Request (admi.006)](../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p154-resend-request-admi-006.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Receipt Acknowledgement (admi.007)](../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p160-receipt-acknowledgement-admi-007.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Scenario 1a](../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p162-scenario-1a.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Scenario 1b](../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p168-scenario-1b.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `admi.005`, `admi.006`, `admi.007`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `System Member`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000343](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart1_Target2Securities_Administration_2023_2024_v2.docx`.

<!-- ADMIN-FLOWS -->
## Curated administration responsibilities

- [Report query request activity](../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p149-report-query-request-admi-005.md)
- [Resend request activity](../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p154-resend-request-admi-006.md)
- [Receipt acknowledgement — receipt status](../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p162-scenario-1a.md)
- [Receipt acknowledgement — business-processing rejection](../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p168-scenario-1b.md)
- [Query the latest available report](../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p175-report-query-request-business-transaction-admi-005.md)
- [Resend an existing message or file](../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p179-resend-request-business-transaction-admi-006.md)
- [Central-system receipt acknowledgement](../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p189-scenario-1-receipt-acknowledgement-sent-by-central-system-e-g-t2s-plat.md)

<!-- ADMIN-MODULE-3 -->
[Resend request technical validation and routing](../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p131-technical-processing.md)

<!-- ADMIN-MODULE-6 -->
[A2A communication, inbound and outbound processing](../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p142-technical-processing.md)
