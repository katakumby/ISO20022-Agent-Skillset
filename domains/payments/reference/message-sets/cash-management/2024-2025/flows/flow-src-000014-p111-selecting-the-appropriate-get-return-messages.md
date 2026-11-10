---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
flow_id: "flow-src-000014-p111-selecting-the-appropriate-get-return-messages"
title: "Selecting the appropriate Get/Return Messages"
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Selecting the appropriate Get/Return Messages"], "locator": "/w:document/w:body/w:p[111]", "paragraph_id": "P111", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Selecting the appropriate Get/Return Messages"], "locator": "/w:document/w:body/w:p[112]", "paragraph_id": "P112", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Selecting the appropriate Get/Return Messages"], "locator": "/w:document/w:body/w:p[113]", "paragraph_id": "P113", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Selecting the appropriate Get/Return Messages"], "locator": "/w:document/w:body/w:p[114]", "paragraph_id": "P114", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Selecting the appropriate Get/Return Messages"], "locator": "/w:document/w:body/w:p[115]", "paragraph_id": "P115", "table_id": null}]
participants: ["participant-src-000014-market-infrastructure"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Selecting the appropriate Get/Return Messages", "Market Infrastructure"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Selecting the appropriate Get/Return Messages

Source context: Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Market Infrastructure | [Participant](../../../../../../../shared/reference/participants/participant-src-000014-market-infrastructure.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P112** The Cash Management messages provide a high degree of flexibility. It is up to each particular system (be it a centralised system, a market infrastructure, or an account owner-account servicer relationship) to define its own solution by identifying:

**P113** which messages are allowed

**P114** the level of complexity allowed per message

**P115** This flexible approach results in a broad framework that can be considered as a toolbox. The framework needs to be constrained, taking into account factors such as the existing business needs and the current processes and capabilities of the systems. All these features will determine the particular combination of elements that define a particular implementation. At the same time, they also define the areas of potential evolution in the future.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000014](../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx). Heading path: BusinessTransactions / How to use the Cash Management Messages / Selecting the appropriate Get/Return Messages.
