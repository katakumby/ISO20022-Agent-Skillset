---
template: false
document_kind: "participant"
review_status: "needs-review"
participant_id: "participant-src-000320-third-party-systems"
title: "3rd Party Systems"
domain: "securities"
domains: ["securities"]
message_sets: ["fitrr"]
source_ids: ["src-000320"]
source_editions: ["July 2025"]
role_kind: "functional participant role"
source_labels: ["3rd Party Systems"]
aliases: []
source_locations: [{"source_id": "src-000320", "paragraph_id": "P199", "xml_path": "/w:document/w:body/w:p[199]", "heading_path": ["BusinessTransactions", "Data Distribution BusinessTransaction "]}, {"source_id": "src-000320", "paragraph_id": "P200", "xml_path": "/w:document/w:body/w:p[200]", "heading_path": ["BusinessTransactions", "Data Distribution BusinessTransaction "]}]
limitations: ["Definition is scoped to the distribution picture and narrative; no general institutional equivalence or identifier scheme is asserted."]
flow_ids: ["flow-src-000320-p198-data-distribution-business-transaction"]
message_ids: ["auth.017.001.02", "auth.036.001.03", "auth.039.001.01", "auth.042.001.02", "auth.043.001.01", "auth.047.001.01", "auth.048.001.01", "auth.049.001.02", "auth.050.001.01"]
---

# 3rd Party Systems

External systems from which the Supervisory Authority requests and downloads additional data in the distribution picture. Both exchanges are explicitly outside this message-set scope.

## Responsibilities and relationships

Receives an out-of-scope data request from the Supervisory Authority and returns an out-of-scope download.

## Provenance and navigation

[src-000320](../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx); P199–P200, BusinessTransactions / Reference Data Distribution BusinessTransaction.

[Distribution diagram](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0023.md)

Identifier schemes are not specified for this role in the cited passage.


<!-- FITRR-SEQUENCES -->
## Source-reviewed sequence participation

- [Reference data distribution](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p198-data-distribution-business-transaction.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0023.md)
