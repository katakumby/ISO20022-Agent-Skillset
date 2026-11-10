---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000350"]
source_editions: ["august-2026"]
message_sets: ["t2s-cash-account-query-and-report"]
flow_id: "flow-src-000350-p161-cash-account-activity-advice-process"
title: "Cash Account Activity Advice Process"
source_locations: [{"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Cash Account Activity Advice Process"], "locator": "/w:document/w:body/w:p[161]", "paragraph_id": "P161", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Cash Account Activity Advice Process"], "locator": "/w:document/w:body/w:p[162]", "paragraph_id": "P162", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Cash Account Activity Advice Process"], "locator": "/w:document/w:body/w:p[163]", "paragraph_id": "P163", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Cash Account Activity Advice Process"], "locator": "/w:document/w:body/w:p[164]", "paragraph_id": "P164", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Cash Account Activity Advice Process"], "locator": "/w:document/w:body/w:p[165]", "paragraph_id": "P165", "table_id": null}]
participants: ["participant-src-000350-executing-servicing-party", "participant-src-000350-instructing-party", "participant-src-000350-recipient-party"]
message_mapping_evidence: [{"source_id": "src-000350", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Cash Account Query and report"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.038.001.01"]
message_families: ["reda.038"]
search_terms: ["Cash Account Activity Advice Process", "Executing / Servicing Party", "Instructing Party", "reda.038"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
---



# Cash Account Activity Advice Process

Source context: T2S CashAccountQueryAndReport. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000350-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000350-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0011](../documents/src-000350/diagrams/fig-0011.md). A canonical source reconstruction and actual review evidence are linked below.

**P163** Cash Account Activity Advice

**P164** The Executing/Servicing Party sends a statement to the Instructing Party containing information on changes occurred for Cash Account reference data during the business day.
The statement is  sent unilaterally in an unsolicited manner.

## Messages and alternative paths

Source-supported message family mentions: `reda.038`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000350](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart1_Target2Securities_CashAccountQueryAndReport_v2.docx`. Heading path: BusinessTransactions / Query/Response Process / Cash Account Activity Advice Process.

## Curated source flow

Executing/Servicing Party unilaterally sends CashAccountActivityAdvice to Instructing Party. P164 specifies changes to cash-account reference data during the business day. P91-P95 includes creation, modification and deletion, with advice elements varying by requestor scope and delivery to subscribers. Recipient Party in T10 is also linked as a contextual narrative role; no extra sender or request exchange is added.

[Complete source diagram](../diagrams/curated/fig-0011.md).

### Adjacent source narrative

**P163** Cash Account Activity Advice

**P164** The Executing/Servicing Party sends a statement to the Instructing Party containing information on changes occurred for Cash Account reference data during the business day.
The statement is  sent unilaterally in an unsolicited manner.

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000350-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000350-executing-servicing-party.md), [recipient party](../../../../../../../shared/reference/participants/participant-src-000350-recipient-party.md).
