---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
participant_id: "participant-src-000320-if"
title: "IF"
source_labels: ["IF"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[10]", "paragraph_id": null, "table_id": "T11"}]
flows: ["flow-src-000320-p137-transaction-reporting-messages", "flow-src-000320-p144-reference-data-submission", "flow-src-000320-p148-non-working-days", "flow-src-000320-p150-missing-incomplete-data-submission", "flow-src-000320-p153-mi-fir-specific-additional-reference-data", "flow-src-000320-p155-transparency-trading-activity", "flow-src-000320-p159-trading-volume-cap", "flow-src-000320-p162-financial-instrument-transaction-report"]
process_sections: ["flow-src-000320-p201-incomplete-data-business-transaction"]
message_ids: []
message_families: ["auth.016"]
search_terms: ["IF", "auth.016"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: []
---

# IF

Business context: Transactions and Financial Instruments Data Reporting. Source classification: business role.

## Definition

Investment Firm is any legal person whose regular occupation or business is the provision of one or more investment services to third parties and/or the performance of one or more investment activities on a professional basis.

Evidence: [T11](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0011.md), source row 10.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Reporting Entity](participant-src-000320-reporting-entity.md) | [T12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0012.md) row 8, column 2 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Transaction Reporting Messages](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p137-transaction-reporting-messages.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Reference Data Submission](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p144-reference-data-submission.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Non-Working Days](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p148-non-working-days.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Missing / Incomplete Data Submission](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p150-missing-incomplete-data-submission.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [MiFIR specific additional Reference Data](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p153-mi-fir-specific-additional-reference-data.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transparency Trading Activity](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p155-transparency-trading-activity.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Trading Volume Cap](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p159-trading-volume-cap.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Financial Instrument Transaction Report](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p162-financial-instrument-transaction-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Incomplete Data BusinessTransaction](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p201-incomplete-data-business-transaction.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `auth.016`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `IF`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000320](../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx).



<!-- FITRR-ACTIVITY-1 -->
[Business roles and functional participants — source notation](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0001.md)
<!-- /FITRR-ACTIVITY-1 -->
