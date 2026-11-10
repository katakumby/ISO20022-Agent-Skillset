---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000362"]
source_editions: ["february-2025"]
message_sets: ["t2s-limit-utilisation-journal"]
flow_id: "flow-src-000362-p152-limit-utilisation-journal-report"
title: "Limit Utilisation Journal Report"
source_locations: [{"source_id": "src-000362", "heading_path": ["BusinessTransactions", "Limit Utilisation Journal Report"], "locator": "/w:document/w:body/w:p[152]", "paragraph_id": "P152", "table_id": null}, {"source_id": "src-000362", "heading_path": ["BusinessTransactions", "Limit Utilisation Journal Report"], "locator": "/w:document/w:body/w:p[153]", "paragraph_id": "P153", "table_id": null}, {"source_id": "src-000362", "heading_path": ["BusinessTransactions", "Limit Utilisation Journal Report"], "locator": "/w:document/w:body/w:p[154]", "paragraph_id": "P154", "table_id": null}, {"source_id": "src-000362", "heading_path": ["BusinessTransactions", "Limit Utilisation Journal Report"], "locator": "/w:document/w:body/w:p[155]", "paragraph_id": "P155", "table_id": null}, {"source_id": "src-000362", "heading_path": ["BusinessTransactions", "Limit Utilisation Journal Report"], "locator": "/w:document/w:body/w:p[156]", "paragraph_id": "P156", "table_id": null}, {"source_id": "src-000362", "heading_path": ["BusinessTransactions", "Limit Utilisation Journal Report"], "locator": "/w:document/w:body/w:p[157]", "paragraph_id": "P157", "table_id": null}, {"source_id": "src-000362", "heading_path": ["BusinessTransactions", "Limit Utilisation Journal Report"], "locator": "/w:document/w:body/w:p[158]", "paragraph_id": "P158", "table_id": null}, {"source_id": "src-000362", "heading_path": ["BusinessTransactions", "Limit Utilisation Journal Report"], "locator": "/w:document/w:body/w:p[159]", "paragraph_id": "P159", "table_id": null}, {"source_id": "src-000362", "heading_path": ["BusinessTransactions", "Limit Utilisation Journal Report"], "locator": "/w:document/w:body/w:p[160]", "paragraph_id": "P160", "table_id": null}]
participants: ["participant-src-000362-central-counterparty", "participant-src-000362-payment-bank"]
message_mapping_evidence: [{"source_id": "src-000362", "heading_path": ["Scope and Functionality", "Scope", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["camt.064", "camt.065"]
search_terms: ["Limit Utilisation Journal Report", "Central Counterparty", "Payment Bank", "camt.064", "camt.065"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---



# Limit Utilisation Journal Report

Source context: T2S LimitUtilisationJournal. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Central Counterparty | [Participant](../../../../../../../shared/reference/participants/participant-src-000362-central-counterparty.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Payment Bank | [Participant](../../../../../../../shared/reference/participants/participant-src-000362-payment-bank.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P153** The LimitUtilisationJournalReport message (camt.065) is exchanged between the central system, (e.g. T2S in this case) and a CSD, NCB, payment bank or a directly connected system party (the central securities depository participant granted direct access, like a bank or central counterparty). It is used to return information about the limit amounts, utilisation and journal of transactions impacting the utilisation of limits. Its purpose is to report information regarding the limits as managed by the credit provider and corresponding to the criteria received within the incoming query message (camt.064).

## Messages and alternative paths

Source-supported message family mentions: `camt.064`, `camt.065`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000362](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart1_Target2Securities_LimitUtilisationJournal_v2.docx`. Heading path: BusinessTransactions / Limit Utilisation Journal Report.

Canonical reusable process modes: [pull mode](flow-src-000362-p137-pull-mode.md), [push mode](flow-src-000362-p143-push-mode.md).
