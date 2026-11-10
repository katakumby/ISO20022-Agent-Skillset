---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p186-non-working-day-business-transaction"
title: "Non Working Day BusinessTransaction"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Non Working Day BusinessTransaction "], "locator": "/w:document/w:body/w:p[186]", "paragraph_id": "P186", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Non Working Day BusinessTransaction "], "locator": "/w:document/w:body/w:p[187]", "paragraph_id": "P187", "table_id": null}]
participants: ["participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Non Working Day BusinessTransaction", "Supervisory Authority"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Non Working Day BusinessTransaction

Source context: Transactions and Financial Instruments Data Reporting. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Supervisory Authority | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P187** To perform all operations correctly, the Supervisory Authority and CAs need to know the non-working days of all venues. To support this, all venues, Reporting Entities and CAs must report their non-working days. For this reason, both directly report this information to the Supervisory Authority

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md). Heading path: BusinessTransactions / Non Working Day BusinessTransaction .
