---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
participant_id: "participant-src-000320-mtf"
title: "MTF"
source_labels: ["MTF"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[5]", "paragraph_id": null, "table_id": "T11"}]
flows: ["flow-src-000320-p127-reference-data", "flow-src-000320-p131-transparency-data", "flow-src-000320-p135-trading-volume-cap"]
process_sections: []
message_ids: []
message_families: []
search_terms: ["MTF"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: []
---

# MTF

Business context: Transactions and Financial Instruments Data Reporting. Source classification: business role.

## Definition

Multilateral Trading Facility is a multilateral system, operated by an investment firm or a market operator, which brings together multiple third-party buying and selling interests in financial instruments – in the system and in accordance with non-discretionary rules – in a way that results in a contract in accordance with Title II of Directive 2014/65/EU. 

Evidence: [T11](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0011.md), source row 5.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Reporting Entity](participant-src-000320-reporting-entity.md) | [T12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0012.md) row 3, column 2 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Reference Data](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p127-reference-data.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transparency Data](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p131-transparency-data.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Trading Volume Cap](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p135-trading-volume-cap.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `MTF`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000320](../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx).



<!-- FITRR-ACTIVITY-1 -->
[Business roles and functional participants — source notation](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0001.md)
<!-- /FITRR-ACTIVITY-1 -->
