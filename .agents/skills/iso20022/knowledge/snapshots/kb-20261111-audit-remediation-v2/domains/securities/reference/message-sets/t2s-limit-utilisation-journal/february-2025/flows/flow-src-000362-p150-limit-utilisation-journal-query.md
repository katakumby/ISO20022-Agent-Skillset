---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000362"]
source_editions: ["february-2025"]
message_sets: ["t2s-limit-utilisation-journal"]
flow_id: "flow-src-000362-p150-limit-utilisation-journal-query"
title: "Limit Utilisation Journal Query"
source_locations: [{"source_id": "src-000362", "heading_path": ["BusinessTransactions", "Limit Utilisation Journal Query"], "locator": "/w:document/w:body/w:p[150]", "paragraph_id": "P150", "table_id": null}, {"source_id": "src-000362", "heading_path": ["BusinessTransactions", "Limit Utilisation Journal Query"], "locator": "/w:document/w:body/w:p[151]", "paragraph_id": "P151", "table_id": null}]
participants: ["participant-src-000362-central-counterparty", "participant-src-000362-payment-bank"]
message_mapping_evidence: [{"source_id": "src-000362", "heading_path": ["Scope and Functionality", "Scope", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["camt.064"]
search_terms: ["Limit Utilisation Journal Query", "Central Counterparty", "Payment Bank", "camt.064"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---



# Limit Utilisation Journal Query

Source context: T2S LimitUtilisationJournal. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Central Counterparty | [Participant](../../../../../../../shared/reference/participants/participant-src-000362-central-counterparty.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Payment Bank | [Participant](../../../../../../../shared/reference/participants/participant-src-000362-payment-bank.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P151** A CSD, NCB, payment bank or a directly connected system participant (the central securities depository participant granted direct access, like a bank or a central counterparty) sends a Limit Utilisation Journal Query via camt.064 to the central system (e.g. T2S in this case). Its purpose is to query information regarding the journal of transaction impacting the utilisation of limits that have been defined by the system participant.

## Messages and alternative paths

Source-supported message family mentions: `camt.064`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000362](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart1_Target2Securities_LimitUtilisationJournal_v2.docx`. Heading path: BusinessTransactions / Limit Utilisation Journal Query.

Canonical reusable process modes: [pull mode](flow-src-000362-p137-pull-mode.md), [push mode](flow-src-000362-p143-push-mode.md).
