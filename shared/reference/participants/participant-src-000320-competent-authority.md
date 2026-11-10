---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
participant_id: "participant-src-000320-competent-authority"
title: "Competent Authority"
source_labels: ["CA", "Competent Authority"]
role_type: "functional participant role"
aliases: ["CA"]
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[3]", "paragraph_id": null, "table_id": "T10"}]
flows: ["flow-src-000320-p127-reference-data"]
process_sections: []
message_ids: ["auth.016.001.03", "auth.017.001.02", "auth.031.001.01", "auth.032.001.01", "auth.033.001.03", "auth.035.001.01", "auth.036.001.03", "auth.039.001.01", "auth.040.001.01", "auth.041.001.01", "auth.042.001.02", "auth.043.001.01", "auth.044.001.03", "auth.045.001.03", "auth.047.001.01", "auth.048.001.01", "auth.049.001.02", "auth.050.001.01"]
message_families: []
search_terms: ["Competent Authority"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000320-p144-reference-data-submission", "flow-src-000320-p146-reference-data-distribution", "flow-src-000320-p148-non-working-days", "flow-src-000320-p150-missing-incomplete-data-submission", "flow-src-000320-p153-mi-fir-specific-additional-reference-data", "flow-src-000320-p155-transparency-trading-activity", "flow-src-000320-p157-transparency-result-data", "flow-src-000320-p159-trading-volume-cap", "flow-src-000320-p162-financial-instrument-transaction-report", "flow-src-000320-p178-proxy-reporting", "flow-src-000320-p183-in-direct-reporting", "flow-src-000320-p188-direct-reporting", "flow-src-000320-p191-proxy-reporting", "flow-src-000320-p194-in-direct-reporting", "flow-src-000320-p198-data-distribution-business-transaction", "flow-src-000320-p206-proxy-and-in-direct-reporting", "flow-src-000320-p214-proxy-reporting", "flow-src-000320-p217-in-direct-reporting", "flow-src-000320-p226-proxy-reporting", "flow-src-000320-p229-in-direct-reporting", "flow-src-000320-p234-in-direct-reporting", "flow-src-000320-p241-proxy-reporting", "flow-src-000320-p244-in-direct-reporting", "flow-src-000320-p248-financial-instrument-transaction-report"]
alias_evidence: [{"source_id": "src-000320", "table_id": "T2", "row": 6, "source_label": "CA", "expanded_label": "Competent Authority"}]
---

# Competent Authority

Business context: Transactions and Financial Instruments Data Reporting. Source classification: functional participant role.

## Definition

Entity which regulates reporting entities and either collects and transmits data to ESMA or has delegated the collection of data to ESMA through an appropriate delegation agreement.

Evidence: [T10](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0010.md), source row 3.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [NCA](participant-src-000320-nca.md) | [T12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0012.md) row 10, column 3 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Reference Data](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p127-reference-data.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Competent Authority`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000320](../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx).




<!-- FITRR-SEQUENCES -->
## Source-reviewed sequence participation

- [Reference data — proxy reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p178-proxy-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0018.md)
- [Reference data — indirect reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p183-in-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0019.md)
- [Non-working days — direct reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p188-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0020.md)
- [Non-working days — proxy reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p191-proxy-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0021.md)
- [Non-working days — indirect reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p194-in-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0022.md)
- [Reference data distribution](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p198-data-distribution-business-transaction.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0023.md)
- [Incomplete reference data — indirect reminder](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p206-proxy-and-in-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0025.md)
- [Transparency data — proxy reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p214-proxy-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0027.md)
- [Transparency data — indirect reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p217-in-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0028.md)
- [Trading activity — proxy reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p226-proxy-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0030.md)
- [Trading activity — indirect reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p229-in-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0031.md)
- [Trading activity results — authority reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p234-in-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0032.md)
- [Trading volume cap — proxy reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p241-proxy-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0034.md)
- [Trading volume cap — indirect reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p244-in-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0035.md)
- [Transaction reporting and authority exchange](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p248-financial-instrument-transaction-report.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0036.md)

























<!-- FITRR-ALIAS -->
## Source-supported abbreviation

**CA** is explicitly defined as **Competent Authority** in [T2](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0002.md), row 6. This alias is scoped to this publication; it does not merge the functional participant with an institution or business role.
<!-- /FITRR-ALIAS -->

<!-- FITRR-RESPONSIBILITIES -->
## Source-assigned activities

| Activity | Source responsibility | Precise evidence |
| --- | --- | --- |
| Receive Message (a) | CA not delegating data collection receives the message. Based on the agreement, they either submit the message directly or they perform additional operations on the message | [T23 row 3](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0023.md) |
| Submit Message | CA not delegating data collection, submits the message using the same channel as REs | [T23 row 4](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0023.md) |
| Process Message | CA not delegating operations to the SA, must check and validate all data that is received<br>CA generates and distributes a status advice message detailing all information that has been identified during the message processing | [T23 row 6](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0023.md) |
| Receive Response | CA checks periodically for the status of the message that they have submitted and downloads the response | [T23 row 8](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0023.md) |
| Process Response | CA not delegating operations to the SA, must check that the data they submit has been accepted. Where it has been accepted, all processing of that submission is complete. Where an issue is identified, they must inform the RE of this.  | [T23 row 9](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0023.md) |
| Route Response | CA delegating data calculation operations, must route the response information to the original RE<br>CA not delegating operations may still need to route the response from the SA to the RE in the case where an issue was identified by the SA | [T23 row 10](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0023.md) |
| Receive and Process Message Bundle | Connect to the SA download channel and download the messages that are being distributed. Process the files contained in the bundle and update all necessary systems of the CA accordingly | [T24 row 5](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0024.md) |
| Receive Message (a) | CA not delegating data collection receives the message | [T25 row 3](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0025.md) |
| Process Message | CA not delegating operations to the SA, must check and validate all data that is received<br>CA generates and distributes a status advice message detailing all information that has been identified during the message processing | [T25 row 4](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0025.md) |
| Non-Working Day of the Year | CA captures their non-working days for submission to the SA | [T25 row 5](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0025.md) |
| Submit Message | CA not delegating data collection, submits the message using the same channel as reporting entities | [T25 row 6](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0025.md) |
| Receive Response | CA checks periodically for the status of the message that they have submitted and downloads the response. As a CA can have made a submission on their Non-Working days, they are checking for messages meant for them as well as messages meant for REs that either need to be processed or routed | [T25 row 9](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0025.md) |
| Route Response | CA delegating data calculation operations, must route the response information to the original RE | [T25 row 10](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0025.md) |
| Process Response | Based on the response of the message submitted, CAs perform any necessary additional data operations that are appropriate | [T25 row 13](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0025.md) |
| Corrective Action (b) | CA fixes any issues that have been found with the message they have submitted | [T25 row 14](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0025.md) |
| Route Message | CA delegating data calculation operations, must route the response information to the original RE | [T26 row 5](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0026.md) |
| Process and Generate Message | CA not delegating calculations, receives one or more files which must be processed and the appropriate data extracted which is to be communicated to REs | [T26 row 6](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0026.md) |
| Receive Message (a) | CA not delegating data collection receives the message. Based on the agreement, they either submit the message directly to the SA or they perform additional operations | [T27 row 3](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0027.md) |
| Submit Message | CA not delegating data collection, submits the message to the SA using the same channel as REs | [T27 row 4](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0027.md) |
| Process Message | CA not delegating calculation processing to the SA, must check and validate all data that is received e.g. data checks, data aggregation, error record removal. Depending on the data checks, they submit an appropriate message to the supervisory authority<br>They must generate and distribute a status advice message to the reporting entity | [T27 row 5](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0027.md) |
| Receive Response | CA checks periodically for the status of the message that they have submitted and downloads the response once available | [T27 row 8](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0027.md) |
| Process Response | CA not delegating calculations, must check the response from the SA to identify should the response be routed to the RE or not. If no issues were found, there is no need to inform the RE as they already have received the appropriate status advice. If an issue exists, this must be routed to the RE so that they can take appropriate actions | [T27 row 9](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0027.md) |
| Route Response | CA delegating data calculation operations, must route the response information to the original RE<br>CA not delegating operations may still need to route the response from the SA to the RE in the case where an issue was identified by the SA | [T27 row 10](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0027.md) |
| Receive Message (a) | CA not delegating data collection receives the message. Based on the agreement, they either submit the message directly to the SA or they perform additional operations | [T28 row 3](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0028.md) |
| Submit Message | CA not delegating data collection, submits the message to the SA using the same channel as REs | [T28 row 4](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0028.md) |
| Process Message | CA not delegating calculation processing to the SA, must check and validate all data that is received e.g. data checks, data aggregation, error record removal. Depending on the data checks, they submit an appropriate message to the SA<br>They must generate and distribute a status advice message to the RE | [T28 row 5](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0028.md) |
| Receive Response | CA checks periodically for the status of the message that they have submitted and download the response once available | [T28 row 8](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0028.md) |
| Process Response | CA not delegating calculations, must check the response from the SA to identify should the response be routed to the RE or not. If no issues were found, there is no need to inform the RE as they already have received the appropriate status advice. If an issue exists, this must be routed to the reporting entity so that they can take appropriate actions | [T28 row 9](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0028.md) |
| Route Response | CA delegating data calculation operations, must route the response information to the original RE<br>CA not delegating operations may still need to route the response from the SA to the RE in the case where an issue was identified by the SA | [T28 row 10](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0028.md) |
| Calculate and Submit Trading Activity Result | CA not delegating Transparency Calculations must perform the transparency calculation on the data for which they are the CA. Results, once known are submitted to the SA | [T29 row 2](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0029.md) |
| Receive and Process Response | Check periodically for the status of the message that has been submitted. Where a response exists, download and process the message contents | [T29 row 5](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0029.md) |
| Corrective Action | Where an issue has been identified in a submitted record, the record must be fixed and the updated records re-submitted | [T29 row 6](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0029.md) |
| Receive Message (a) | CA not delegating data collection receives the message. Based on the agreement, they either submit the message directly to the SA or they perform additional operations | [T30 row 3](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0030.md) |
| Submit Message | CA not delegating data collection, submits the message to the SA using the same channel as REs | [T30 row 4](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0030.md) |
| Process Message | CA not delegating calculation processing to the SA, must check and validate all data that is received e.g. data checks, data aggregation, error record removal. Depending on the data checks, they submit an appropriate message to the SA<br>They must generate and distribute a status advice message to the RE | [T30 row 5](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0030.md) |
| Receive Response | CAs check periodically for the status of the message that they have submitted and download the response once available | [T30 row 8](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0030.md) |
| Process Response | CA not delegating calculations, must check the response from the SA to identify should the response be routed to the RE or not. If no issues were found, there is no need to inform the reporting entity as they already have received the appropriate status advice. If an issue exists, this must be routed to the RE so that they can take appropriate actions | [T30 row 9](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0030.md) |
| Route Response | CA delegating data calculation operations, must route the response information to the original RE<br>CA not delegating operations may still need to route the response from the SA to the RE in the case where an issue was identified by the SA | [T30 row 10](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0030.md) |
| Receive Messages | CA receives the messages and performs additional operations on them | [T31 row 3](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0031.md) |
| Process Message and Generate Status Advice | Each received message is checked for <br>Completeness and correctness of message <br>Transaction to be exchanged with relevant CA<br>Once complete, generate the status advice file for distribution | [T31 row 4](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0031.md) |


The source Initiator cells govern this table. T26 assigns Receive Message to SA while its description and diagram identify CA; [issue-000036](../../../tracking/issues.md#issue-000036) preserves the conflict. T18 has a separate calculation-result role conflict, [issue-000032](../../../tracking/issues.md#issue-000032).
<!-- /FITRR-RESPONSIBILITIES -->

<!-- FITRR-ACTIVITY-1 -->
[Business roles and functional participants — source notation](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0001.md)
<!-- /FITRR-ACTIVITY-1 -->

<!-- FITRR-ACTIVITY-2 -->
[Financial instrument reporting use cases](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0002.md)
<!-- /FITRR-ACTIVITY-2 -->

<!-- FITRR-ACTIVITY-3 -->
[Transaction data submission and exchange use cases](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0003.md)
<!-- /FITRR-ACTIVITY-3 -->

<!-- FITRR-ACTIVITY-8 -->
[Reference data submission](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0008.md) · [Activities and responsibilities](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p144-reference-data-submission.md)
<!-- /FITRR-ACTIVITY-8 -->

<!-- FITRR-ACTIVITY-9 -->
[Reference data distribution](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0009.md) · [Activities and responsibilities](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p146-reference-data-distribution.md)
<!-- /FITRR-ACTIVITY-9 -->

<!-- FITRR-ACTIVITY-10 -->
[Non-working days](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0010.md) · [Activities and responsibilities](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p148-non-working-days.md)
<!-- /FITRR-ACTIVITY-10 -->

<!-- FITRR-ACTIVITY-11 -->
[Missing or incomplete data](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0011.md) · [Activities and responsibilities](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p150-missing-incomplete-data-submission.md)
<!-- /FITRR-ACTIVITY-11 -->

<!-- FITRR-ACTIVITY-12 -->
[MiFIR additional reference / transparency data](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0012.md) · [Activities and responsibilities](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p153-mi-fir-specific-additional-reference-data.md)
<!-- /FITRR-ACTIVITY-12 -->

<!-- FITRR-ACTIVITY-13 -->
[Trading activity](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0013.md) · [Activities and responsibilities](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p155-transparency-trading-activity.md)
<!-- /FITRR-ACTIVITY-13 -->

<!-- FITRR-ACTIVITY-14 -->
[Trading activity results](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0014.md) · [Activities and responsibilities](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p157-transparency-result-data.md)
<!-- /FITRR-ACTIVITY-14 -->

<!-- FITRR-ACTIVITY-15 -->
[Trading volume cap](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0015.md) · [Activities and responsibilities](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p159-trading-volume-cap.md)
<!-- /FITRR-ACTIVITY-15 -->

<!-- FITRR-ACTIVITY-16 -->
[Transaction reporting and authority exchange](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0016.md) · [Activities and responsibilities](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p162-financial-instrument-transaction-report.md)
<!-- /FITRR-ACTIVITY-16 -->
