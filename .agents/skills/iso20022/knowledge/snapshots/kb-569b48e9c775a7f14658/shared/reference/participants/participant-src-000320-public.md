---
template: false
document_kind: "participant"
review_status: "needs-review"
participant_id: "participant-src-000320-public"
title: "Public"
domain: "securities"
domains: ["securities"]
message_sets: ["fitrr"]
source_ids: ["src-000320"]
source_editions: ["July 2025"]
role_kind: "functional participant role"
source_labels: ["Public"]
aliases: []
source_locations: [{"source_id": "src-000320", "paragraph_id": "P199", "xml_path": "/w:document/w:body/w:p[199]", "heading_path": ["BusinessTransactions", "Data Distribution BusinessTransaction "]}, {"source_id": "src-000320", "paragraph_id": "P200", "xml_path": "/w:document/w:body/w:p[200]", "heading_path": ["BusinessTransactions", "Data Distribution BusinessTransaction "]}]
limitations: ["Definition is scoped to the distribution picture and narrative; no general institutional equivalence or identifier scheme is asserted."]
flow_ids: ["flow-src-000320-p198-data-distribution-business-transaction"]
message_ids: ["auth.017.001.02", "auth.036.001.03", "auth.039.001.01", "auth.042.001.02", "auth.043.001.01", "auth.047.001.01", "auth.048.001.01", "auth.049.001.02", "auth.050.001.01"]
---

# Public

Recipients of the published instrument reference data, including investment firms, reporting entities and academics in the distribution narrative. The diagram keeps this audience separate from its Reporting Entity lifeline.

## Responsibilities and relationships

Receives full and delta reference-data reports from the Supervisory Authority. No outgoing message is drawn.

## Provenance and navigation

[src-000320](../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); P199–P200, BusinessTransactions / Reference Data Distribution BusinessTransaction.

[Distribution diagram](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0023.md)

Identifier schemes are not specified for this role in the cited passage.


<!-- FITRR-SEQUENCES -->
## Source-reviewed sequence participation

- [Reference data distribution](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p198-data-distribution-business-transaction.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0023.md)
