---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
participant_id: "participant-src-000320-supervisory-authority"
title: "Supervisory Authority"
source_labels: ["SA", "Supervisory Authority"]
role_type: "functional participant role"
aliases: ["SA"]
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[4]", "paragraph_id": null, "table_id": "T10"}]
flows: ["flow-src-000320-p127-reference-data", "flow-src-000320-p131-transparency-data", "flow-src-000320-p153-mi-fir-specific-additional-reference-data", "flow-src-000320-p155-transparency-trading-activity"]
process_sections: ["flow-src-000320-p186-non-working-day-business-transaction", "flow-src-000320-p198-data-distribution-business-transaction", "flow-src-000320-p201-incomplete-data-business-transaction"]
message_ids: ["auth.017.001.02", "auth.031.001.01", "auth.032.001.01", "auth.033.001.03", "auth.035.001.01", "auth.036.001.03", "auth.039.001.01", "auth.040.001.01", "auth.041.001.01", "auth.042.001.02", "auth.043.001.01", "auth.044.001.03", "auth.045.001.03", "auth.047.001.01", "auth.048.001.01", "auth.049.001.02", "auth.050.001.01"]
message_families: []
search_terms: ["Supervisory Authority"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000320-p144-reference-data-submission", "flow-src-000320-p146-reference-data-distribution", "flow-src-000320-p148-non-working-days", "flow-src-000320-p150-missing-incomplete-data-submission", "flow-src-000320-p153-mi-fir-specific-additional-reference-data", "flow-src-000320-p155-transparency-trading-activity", "flow-src-000320-p157-transparency-result-data", "flow-src-000320-p159-trading-volume-cap", "flow-src-000320-p175-direct-reporting", "flow-src-000320-p178-proxy-reporting", "flow-src-000320-p183-in-direct-reporting", "flow-src-000320-p188-direct-reporting", "flow-src-000320-p191-proxy-reporting", "flow-src-000320-p194-in-direct-reporting", "flow-src-000320-p198-data-distribution-business-transaction", "flow-src-000320-p203-direct-reporting", "flow-src-000320-p206-proxy-and-in-direct-reporting", "flow-src-000320-p211-direct-reporting", "flow-src-000320-p214-proxy-reporting", "flow-src-000320-p217-in-direct-reporting", "flow-src-000320-p223-direct-reporting", "flow-src-000320-p226-proxy-reporting", "flow-src-000320-p229-in-direct-reporting", "flow-src-000320-p234-in-direct-reporting", "flow-src-000320-p238-direct-reporting", "flow-src-000320-p241-proxy-reporting", "flow-src-000320-p244-in-direct-reporting"]
alias_evidence: [{"source_id": "src-000320", "table_id": "T2", "row": 29, "source_label": "SA", "expanded_label": "Supervisory Authority"}]
---

# Supervisory Authority

Business context: Transactions and Financial Instruments Data Reporting. Source classification: functional participant role.

## Definition

Entity which collects, validates and performs all relevant message related operations including tracking on time / late submissions. Example of operations include collating reference data, performing transparency calculations, performing double volume cap calculations.

Evidence: [T10](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0010.md), source row 4.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [NCA](participant-src-000320-nca.md) | [T12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0012.md) row 10, column 4 |
| Business role listed for this functional participant | [ESMA](participant-src-000320-esma.md) | [T12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0012.md) row 11, column 4 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Reference Data](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p127-reference-data.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transparency Data](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p131-transparency-data.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [MiFIR specific additional Reference Data](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p153-mi-fir-specific-additional-reference-data.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transparency Trading Activity](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p155-transparency-trading-activity.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Non Working Day BusinessTransaction](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p186-non-working-day-business-transaction.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Data Distribution BusinessTransaction](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p198-data-distribution-business-transaction.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Incomplete Data BusinessTransaction](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p201-incomplete-data-business-transaction.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Supervisory Authority`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000320](../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx).




<!-- FITRR-SEQUENCES -->
## Source-reviewed sequence participation

- [Reference data — direct reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p175-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0017.md)
- [Reference data — proxy reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p178-proxy-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0018.md)
- [Reference data — indirect reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p183-in-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0019.md)
- [Non-working days — direct reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p188-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0020.md)
- [Non-working days — proxy reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p191-proxy-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0021.md)
- [Non-working days — indirect reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p194-in-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0022.md)
- [Reference data distribution](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p198-data-distribution-business-transaction.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0023.md)
- [Incomplete reference data — direct reminder](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p203-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0024.md)
- [Incomplete reference data — indirect reminder](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p206-proxy-and-in-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0025.md)
- [Transparency data — direct reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p211-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0026.md)
- [Transparency data — proxy reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p214-proxy-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0027.md)
- [Transparency data — indirect reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p217-in-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0028.md)
- [Trading activity — direct reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p223-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0029.md)
- [Trading activity — proxy reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p226-proxy-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0030.md)
- [Trading activity — indirect reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p229-in-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0031.md)
- [Trading activity results — authority reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p234-in-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0032.md)
- [Trading volume cap — direct reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p238-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0033.md)
- [Trading volume cap — proxy reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p241-proxy-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0034.md)
- [Trading volume cap — indirect reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p244-in-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0035.md)





















<!-- FITRR-ALIAS -->
## Source-supported abbreviation

**SA** is explicitly defined as **Supervisory Authority** in [T2](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0002.md), row 29. This alias is scoped to this publication; it does not merge the functional participant with an institution or business role.
<!-- /FITRR-ALIAS -->

<!-- FITRR-RESPONSIBILITIES -->
## Source-assigned activities

| Activity | Source responsibility | Precise evidence |
| --- | --- | --- |
| Receive Message (b) | SA retrieves the submitted messages from the submission channel | [T23 row 5](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0023.md) |
| Process Message and Generate Status Advice | Each received message is checked for <br>Completeness of message<br>Validity against previously submitted data<br>Once complete, generate the status advice file for distribution | [T23 row 7](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0023.md) |
| Download 3rd Party Data | Additional quality control data is downloaded from 3rd party reference systems - country code, currency list, Legal Entity Identifier (LEI) code lists | [T24 row 2](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0024.md) |
| Format for Distribution | Using both internal data and 3rd party data, create ISO 20022 messages for the following for distribution: <br>Reference Data (Full, Delta, Invalid, Index Expression of Interest)<br>Country and Currency Data<br>MIC list <br>CFI Data<br>Non-Working Day Data<br>LEI data is also distributed but it is not changed from that downloaded from Global Legal Entity Identifier Foundation (GLEIF) source | [T24 row 3](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0024.md) |
| Distribute | Upload to a known location by a set time e.g. 0800 Central European Time (CET), the distribution bundle that will be downloadable by CAs | [T24 row 4](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0024.md) |
| Receive Message (b) | SA retrieves the submitted messages from the submission channel | [T25 row 7](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0025.md) |
| Process Message and Generate Status Advice | Process all received non-working days files verifying various information in the file including. Once complete, generate the status advice file for distribution | [T25 row 8](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0025.md) |
| Check Data Completeness | SA checks all data that it has received to identify if all venues have submitted all the data they are meant to. Issues that can be identified and which result in incomplete data include:<br>No message has been submitted by a specific venue<br>Not all data that should have been submitted has been submitted | [T26 row 2](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0026.md) |
| Create Message | For each venue which meets the criteria of incomplete data, SA creates a status advice message and distribute it to the venue informing them that they have reported incomplete data for the given day and submitted dataset | [T26 row 3](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0026.md) |
| Receive Message | CA not delegating data collection, must accept the status advice message and perform necessary operations based on the delegation agreement that is to be used | [T26 row 4](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0026.md) |
| Receive Message (b) | SA retrieves the submitted messages from the submission channel | [T27 row 6](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0027.md) |
| Process Message and Generate Status Advice | Each received message is checked for <br>Completeness of message<br>Validity against previously submitted data<br>Once complete, generate the status advice file for distribution | [T27 row 7](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0027.md) |
| Receive Message (b) | SA retrieves the submitted messages from the submission channel | [T28 row 6](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0028.md) |
| Process Message and Generate Status Advice | Each received message is checked for <br>Completeness of message<br>Validity against previously submitted data<br>Once complete, generate the status advice file for distribution | [T28 row 7](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0028.md) |
| Receive Message | SA retrieves the submitted messages from the submission channel | [T29 row 3](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0029.md) |
| Process Message and Generate Status Advice | Process all result data that has been received, including verifying the data is accurate against known bounds. Based on the message process, create and distribute the status advice message to the submitting entity | [T29 row 4](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0029.md) |
| Receive Message (b) | SA retrieves the submitted messages from the submission channel | [T30 row 6](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0030.md) |
| Process Message and Generate Status Advice | Each received message is checked for <br>Completeness of message<br>Validity against previously submitted data<br>Once complete, generate the status advice file for distribution | [T30 row 7](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0030.md) |


The source Initiator cells govern this table. T26 assigns Receive Message to SA while its description and diagram identify CA; [issue-000036](../../../tracking/issues.md#issue-000036) preserves the conflict. T18 has a separate calculation-result role conflict, [issue-000032](../../../tracking/issues.md#issue-000032).
<!-- /FITRR-RESPONSIBILITIES -->

<!-- FITRR-ACTIVITY-1 -->
[Business roles and functional participants — source notation](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0001.md)
<!-- /FITRR-ACTIVITY-1 -->

<!-- FITRR-ACTIVITY-2 -->
[Financial instrument reporting use cases](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0002.md)
<!-- /FITRR-ACTIVITY-2 -->

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
