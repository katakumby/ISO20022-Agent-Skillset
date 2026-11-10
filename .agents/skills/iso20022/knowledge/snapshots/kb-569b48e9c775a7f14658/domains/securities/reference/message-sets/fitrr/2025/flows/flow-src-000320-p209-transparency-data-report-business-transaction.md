---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p209-transparency-data-report-business-transaction"
title: "Transparency Data Report BusinessTransaction"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Transparency Data Report BusinessTransaction "], "locator": "/w:document/w:body/w:p[209]", "paragraph_id": "P209", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Transparency Data Report BusinessTransaction "], "locator": "/w:document/w:body/w:p[210]", "paragraph_id": "P210", "table_id": null}]
participants: ["participant-src-000320-reporting-entity"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Transparency Data Report BusinessTransaction", "Reporting Entity"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Transparency Data Report BusinessTransaction

Source context: Transactions and Financial Instruments Data Reporting. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Reporting Entity | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P210** For Transparency Data Report, two types of similar data will be submitted by the venues - Equity specific information and Non-Equity specific information. The overall flow is the same regardless of the type of instrument transparency reference data that is being submitted. Distinct messages were used as differences exist in the level of information captured per message. Within the submitted messages, a single Reporting Entity is not expected to submit both messages as they may not operate instruments in scope of a specific message e.g. they may trade only Equity or Non-Equity but not both.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md). Heading path: BusinessTransactions / Transparency Data Report BusinessTransaction .
