---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p135-trading-volume-cap"
title: "Trading Volume Cap"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[135]", "paragraph_id": "P135", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[136]", "paragraph_id": "P136", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[19]", "paragraph_id": null, "table_id": "T19"}]
participants: ["participant-src-000320-reporting-entity", "participant-src-000320-mtf", "participant-src-000320-ctp", "participant-src-000320-rm"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Trading Volume Cap", "Reporting Entity", "MTF", "CTP", "RM"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Trading Volume Cap

Source context: Transactions and Financial Instruments Data Reporting. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

For all Equity / Equity-like instruments that are traded in the EEA, Reporting Entities (RM, MTF, CTP) are to report volumes of trade per currency that they have undertaken on each instrument over the preceding period (01-15 or 16-31 of each month). The report captures total volume of trades as well as volumes of trades that have been undertaken under Negotiated Transactions and Reference Price waivers.

Evidence: [T19](../documents/src-000320/tables/tbl-0019.md), source row 2.

### Trigger

The Reporting Entity submits data twice per month, typically on the 1st and 16th of each month.

Evidence: [T19](../documents/src-000320/tables/tbl-0019.md), source row 3.

### Pre-conditions

The Equity / Equity like financial instruments have been previously submitted through the reference data and transparency additional reference data messages.

Evidence: [T19](../documents/src-000320/tables/tbl-0019.md), source row 4.

### Post-conditions

The double volume cap calculations are performed taking into account a years' worth of data to establish the percentage of trades that are being performed under either Reference Price or Negotiated Transactions waiver.

Evidence: [T19](../documents/src-000320/tables/tbl-0019.md), source row 5.

### Role

Reporting entity

Evidence: [T19](../documents/src-000320/tables/tbl-0019.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Reporting Entity | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| MTF | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-mtf.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| CTP | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-ctp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| RM | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-rm.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P136** Trading Volume Cap data submission

Source table [T19](../documents/src-000320/tables/tbl-0019.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx). Heading path: BusinessProcess Description.
