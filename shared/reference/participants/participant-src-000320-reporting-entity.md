---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
participant_id: "participant-src-000320-reporting-entity"
title: "Reporting Entity"
source_labels: ["RE", "Reporting Entity"]
role_type: "functional participant role"
aliases: ["RE"]
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[2]", "paragraph_id": null, "table_id": "T10"}]
flows: ["flow-src-000320-p127-reference-data", "flow-src-000320-p131-transparency-data", "flow-src-000320-p135-trading-volume-cap", "flow-src-000320-p137-transaction-reporting-messages", "flow-src-000320-p153-mi-fir-specific-additional-reference-data", "flow-src-000320-p155-transparency-trading-activity", "flow-src-000320-p159-trading-volume-cap", "flow-src-000320-p162-financial-instrument-transaction-report"]
process_sections: ["flow-src-000320-p169-overview-of-reporting-classifications", "flow-src-000320-p201-incomplete-data-business-transaction", "flow-src-000320-p209-transparency-data-report-business-transaction", "flow-src-000320-p221-trading-activity-report-business-transaction"]
message_ids: ["auth.016.001.03", "auth.017.001.02", "auth.031.001.01", "auth.032.001.01", "auth.033.001.03", "auth.035.001.01", "auth.036.001.03", "auth.039.001.01", "auth.040.001.01", "auth.041.001.01", "auth.042.001.02", "auth.043.001.01", "auth.047.001.01", "auth.048.001.01", "auth.049.001.02", "auth.050.001.01"]
message_families: ["auth.016"]
search_terms: ["Reporting Entity", "auth.016"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000320-p144-reference-data-submission", "flow-src-000320-p146-reference-data-distribution", "flow-src-000320-p148-non-working-days", "flow-src-000320-p150-missing-incomplete-data-submission", "flow-src-000320-p153-mi-fir-specific-additional-reference-data", "flow-src-000320-p155-transparency-trading-activity", "flow-src-000320-p157-transparency-result-data", "flow-src-000320-p159-trading-volume-cap", "flow-src-000320-p162-financial-instrument-transaction-report", "flow-src-000320-p175-direct-reporting", "flow-src-000320-p178-proxy-reporting", "flow-src-000320-p183-in-direct-reporting", "flow-src-000320-p188-direct-reporting", "flow-src-000320-p191-proxy-reporting", "flow-src-000320-p194-in-direct-reporting", "flow-src-000320-p198-data-distribution-business-transaction", "flow-src-000320-p203-direct-reporting", "flow-src-000320-p206-proxy-and-in-direct-reporting", "flow-src-000320-p211-direct-reporting", "flow-src-000320-p214-proxy-reporting", "flow-src-000320-p217-in-direct-reporting", "flow-src-000320-p223-direct-reporting", "flow-src-000320-p226-proxy-reporting", "flow-src-000320-p229-in-direct-reporting", "flow-src-000320-p238-direct-reporting", "flow-src-000320-p241-proxy-reporting", "flow-src-000320-p244-in-direct-reporting", "flow-src-000320-p248-financial-instrument-transaction-report"]
alias_evidence: [{"source_id": "src-000320", "table_id": "T2", "row": 26, "source_label": "RE", "expanded_label": "Reporting Entity"}]
---

# Reporting Entity

Business context: Transactions and Financial Instruments Data Reporting. Source classification: functional participant role.

## Definition

Any entity that has to report under the scope of MiFIR / MiFID II Article 22, 26, or 27. This data is either reported directly to ESMA or to ESMA through the venues CA depending on the delegation agreement that exists.

Evidence: [T10](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0010.md), source row 2.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [RM](participant-src-000320-rm.md) | [T12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0012.md) row 2, column 2 |
| Business role listed for this functional participant | [MTF](participant-src-000320-mtf.md) | [T12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0012.md) row 3, column 2 |
| Business role listed for this functional participant | [SI](participant-src-000320-si.md) | [T12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0012.md) row 4, column 2 |
| Business role listed for this functional participant | [OTF](participant-src-000320-otf.md) | [T12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0012.md) row 5, column 2 |
| Business role listed for this functional participant | [CTP](participant-src-000320-ctp.md) | [T12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0012.md) row 6, column 2 |
| Business role listed for this functional participant | [APA](participant-src-000320-apa.md) | [T12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0012.md) row 7, column 2 |
| Business role listed for this functional participant | [IF](participant-src-000320-if.md) | [T12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0012.md) row 8, column 2 |
| Business role listed for this functional participant | [ARM](participant-src-000320-arm.md) | [T12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0012.md) row 9, column 2 |
| Business role listed for this functional participant | [NCA](participant-src-000320-nca.md) | [T12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0012.md) row 10, column 2 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Reference Data](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p127-reference-data.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transparency Data](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p131-transparency-data.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Trading Volume Cap](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p135-trading-volume-cap.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transaction Reporting Messages](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p137-transaction-reporting-messages.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [MiFIR specific additional Reference Data](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p153-mi-fir-specific-additional-reference-data.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transparency Trading Activity](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p155-transparency-trading-activity.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Trading Volume Cap](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p159-trading-volume-cap.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Financial Instrument Transaction Report](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p162-financial-instrument-transaction-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Overview of Reporting Classifications](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p169-overview-of-reporting-classifications.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Incomplete Data BusinessTransaction](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p201-incomplete-data-business-transaction.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transparency Data Report BusinessTransaction](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p209-transparency-data-report-business-transaction.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Trading Activity Report BusinessTransaction](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p221-trading-activity-report-business-transaction.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `auth.016`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Reporting Entity`. No external identifier scheme or alias equivalence has been inferred.

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
- [Trading volume cap — direct reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p238-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0033.md)
- [Trading volume cap — proxy reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p241-proxy-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0034.md)
- [Trading volume cap — indirect reporting](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p244-in-direct-reporting.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0035.md)
- [Transaction reporting and authority exchange](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p248-financial-instrument-transaction-report.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0036.md)























<!-- FITRR-ALIAS -->
## Source-supported abbreviation

**RE** is explicitly defined as **Reporting Entity** in [T2](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0002.md), row 26. This alias is scoped to this publication; it does not merge the functional participant with an institution or business role.
<!-- /FITRR-ALIAS -->

<!-- FITRR-RESPONSIBILITIES -->
## Source-assigned activities

| Activity | Source responsibility | Precise evidence |
| --- | --- | --- |
| Capture and Submit Reference Data | Extract local data, create the message and submit it to the appropriate authority based on the agreements that exist between the CA and SA | [T23 row 2](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0023.md) |
| Receive and Process Response | RE checks for and receives feedback on the message data they submitted. They download and process the status advice message to identify if any further actions need to be taken complete the data submission process | [T23 row 11](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0023.md) |
| Corrective Action | RE must fix any issues that have been identified and if applicable, resubmit the message | [T23 row 12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0023.md) |
| Capture and submit Non-Working Days | Before the end of the year or where new non-working days have been identified, extract all non-working days for a given period including weekends e.g. until the end of a calendar year, generate and submit the non-working day message to the SA | [T25 row 2](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0025.md) |
| Receive and Process Response | RE processes the status advice message they have received to know if further actions need to be taken or not | [T25 row 11](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0025.md) |
| Corrective Action (a) | RE must fix any issues that have been identified and if applicable, resubmit the message | [T25 row 12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0025.md) |
| Receive and Process Message | RE which have not reported a full data set as expected at the SA will receive a status advice message capturing which instruments and data has not been submitted. RE shall process the message and perform all necessary corrective action to ensure future submissions are full and complete | [T26 row 7](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0026.md) |
| Capture and Submit Transparency Data Report Message | Extract local data, create the message and submit it to the appropriate authority based on the agreements that exist between the CA and SA | [T27 row 2](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0027.md) |
| Receive and Process Response | RE checks for and receives status advice messages which provide details on the records they submitted. They download and process the status advice message to identify if any further actions need to be taken complete the data submission process | [T27 row 11](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0027.md) |
| Corrective Action | Where an issue has been identified in a submitted record, the record must be fixed and the updated records re-submitted | [T27 row 12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0027.md) |
| Capture and Submit Trading Activity Message | Extract local data, create the message and submit it to the appropriate authority based on the agreements that exist between the CA and supervisory authority | [T28 row 2](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0028.md) |
| Receive and Process Response | RE checks for and receives status advice messages which provide details on the records they submitted. They download and process the status advice message to identify if any further actions need to be taken complete the data submission process | [T28 row 11](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0028.md) |
| Corrective Action | Where an issue has been identified in a submitted record, the record must be fixed and the updated records re-submitted | [T28 row 12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0028.md) |
| Capture and Submit Trading Volume Cap Message | Extract equity / equity like trading data, create the message and submit it to the appropriate authority based on the agreements that exist between the CA and SA | [T30 row 2](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0030.md) |
| Receive and Process Response | RE checks for and receives status advice messages which provide details on the records they submitted. They download and process the status advice message to identify if any further actions need to be taken complete the data submission process | [T30 row 11](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0030.md) |
| Corrective Action | Where an issue has been identified in a submitted record, the record must be fixed and the updated records re-submitted | [T30 row 12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0030.md) |
| Generate and Submit Transaction Report Message | Reporting entity generates report related to executed transactions and submits it to the CA | [T31 row 2](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0031.md) |
| Receive and Process Response | RE checks for and receives status advice messages which provides details on the records they submitted. They download and process the status advice message to identify if any further actions need to be taken complete the data submission process | [T31 row 5](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0031.md) |
| Corrective Action | Where an issue has been identified in a submitted record, the record must be fixed and the updated records re-submitted | [T31 row 6](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0031.md) |


The source Initiator cells govern this table. T26 assigns Receive Message to SA while its description and diagram identify CA; [issue-000036](../../../tracking/issues.md#issue-000036) preserves the conflict. T18 has a separate calculation-result role conflict, [issue-000032](../../../tracking/issues.md#issue-000032).

Identifier context: P207 says a reminder should be at the Reporting Entity identifier level, for example Segment MIC. This is a reminder-routing example, not a universal identifier requirement for every participant or flow.
<!-- /FITRR-RESPONSIBILITIES -->

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
