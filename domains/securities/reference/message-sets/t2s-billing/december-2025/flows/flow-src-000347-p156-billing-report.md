---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
message_sets: ["t2s-billing"]
flow_id: "flow-src-000347-p156-billing-report"
title: "Billing Report"
source_locations: [{"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Billing Report"], "locator": "/w:document/w:body/w:p[156]", "paragraph_id": "P156", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Billing Report"], "locator": "/w:document/w:body/w:p[157]", "paragraph_id": "P157", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Billing Report"], "locator": "/w:document/w:body/w:p[158]", "paragraph_id": "P158", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Billing Report"], "locator": "/w:document/w:body/w:p[159]", "paragraph_id": "P159", "table_id": null}]
participants: ["participant-src-000347-executing-servicing-party", "participant-src-000347-instructing-party", "participant-src-000347-national-central-bank", "participant-src-000347-operator", "participant-src-000347-settlement-infrastructure", "participant-src-000347-system-member"]
message_mapping_evidence: [{"source_id": "src-000347", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Billing"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["camt.077.001.01"]
message_families: ["camt.077"]
search_terms: ["Billing Report", "Executing / Servicing Party", "camt.077"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Flow interpretation checked against its linked source diagram; table review is recorded separately."]
manual_curated: true
---



# Billing Report

Source context: T2S Billing. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000347-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P157** Applies when the report is sent by the Executing/Servicing Party.

**P158** Report ProcessInvoice / Consumption Data / Cancellation Report (camt.077)Report ProcessInvoice / Consumption Data / Cancellation Report (camt.077)

Source diagram evidence: [fig-0011](../documents/src-000347/diagrams/fig-0011.md). Dedicated source reconstruction and actual review evidence are linked below.

## Messages and alternative paths

Source-supported message family mentions: `camt.077`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000347](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`. Heading path: BusinessTransactions / Billing Report.

## Curated source process

Executing/Servicing Party sends one depicted billing report to Instructing Party. Official invoice and consumption data (for NCBs only) are communicated when the specific business-day event is reached. Invoice cancellation status is communicated after processing a cancellation request previously submitted by the operator. The operator and its preceding request are narrative context, intentionally absent from this one-arrow report illustration; no cancellation-request message identifier is invented.

[Complete source diagram reconstruction](../diagrams/curated/fig-0011.md).

### Complete adjacent scenario narrative

**P157** Applies when the report is sent by the Executing/Servicing Party.

**P160** Billing Report

**P161** The Executing/Servicing Party sends the report to the Instructing Party to communicate:

**P162** An official invoice

**P163** Consumption data (for NCBs only)

**P164** whenever a specific event is reached in the business day.

**P166** The Executing/Servicing Party sends the report to the Instructing Party to communicate:

**P167** the cancellation status of an invoice

**P168** At the end of the processing of a previously sent cancellation request submitted by the operator.

| Participant | Source-specific responsibility |
| --- | --- |
| [instructing party](../../../../../../../shared/reference/participants/participant-src-000347-instructing-party.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |
| [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000347-executing-servicing-party.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |
| [system member](../../../../../../../shared/reference/participants/participant-src-000347-system-member.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |
| [settlement infrastructure](../../../../../../../shared/reference/participants/participant-src-000347-settlement-infrastructure.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |
| [operator](../../../../../../../shared/reference/participants/participant-src-000347-operator.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |
| [national central bank](../../../../../../../shared/reference/participants/participant-src-000347-national-central-bank.md) | Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable. |


