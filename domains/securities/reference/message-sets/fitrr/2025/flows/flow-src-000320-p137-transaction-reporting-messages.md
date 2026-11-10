---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p137-transaction-reporting-messages"
title: "Transaction Reporting Messages"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[137]", "paragraph_id": "P137", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[138]", "paragraph_id": "P138", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[20]", "paragraph_id": null, "table_id": "T20"}, {"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[139]", "paragraph_id": "P139", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[21]", "paragraph_id": null, "table_id": "T21"}, {"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[140]", "paragraph_id": "P140", "table_id": null}]
participants: ["participant-src-000320-reporting-entity", "participant-src-000320-arm", "participant-src-000320-if", "participant-src-000320-competent-authority"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Transaction Reporting Messages", "Reporting Entity", "ARM", "IF", "CA"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Transaction Reporting Messages

Source context: Transactions and Financial Instruments Data Reporting. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Any entity (IF, ARM) that has to report transanction data to CA. Reported data is related to the transactions in the instruments that are admitted to trading or their derivatives.

Evidence: [T20](../documents/src-000320/tables/tbl-0020.md), source row 2.

CA that has to exchange relevant transanction data to another CA. Relevant data must fulfill exchange conditions agreed between CAs.

Evidence: [T21](../documents/src-000320/tables/tbl-0021.md), source row 2.

### Trigger

Data is submitted daily and no later than the close of the following working day transaction was executed.

Evidence: [T20](../documents/src-000320/tables/tbl-0020.md), source row 3.

CA received transaction data which fulfills exchange conditions agreed between CAs.

Evidence: [T21](../documents/src-000320/tables/tbl-0021.md), source row 3.

### Pre-conditions

Transaction in the financial instrument or its derivate is executed.

Evidence: [T20](../documents/src-000320/tables/tbl-0020.md), source row 4.

Transaction in the financial instrument or its derivate is executed and reported to one of CAs.

Evidence: [T21](../documents/src-000320/tables/tbl-0021.md), source row 4.

### Post-conditions

The reporting entity has received a  status advice related to the submitted transactions report message.

Evidence: [T20](../documents/src-000320/tables/tbl-0020.md), source row 5.

Sending CA has received a status advice related to the exchanged data.

Evidence: [T21](../documents/src-000320/tables/tbl-0021.md), source row 5.

### Role

Reporting entity

Evidence: [T20](../documents/src-000320/tables/tbl-0020.md), source row 6.

Sending CA

Evidence: [T21](../documents/src-000320/tables/tbl-0021.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Reporting Entity | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| ARM | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-arm.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| IF | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-if.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| CA | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P138** Transaction data submission

Source table [T20](../documents/src-000320/tables/tbl-0020.md).

**P139** Transaction data exchange

Source table [T21](../documents/src-000320/tables/tbl-0021.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx). Heading path: BusinessProcess Description.
