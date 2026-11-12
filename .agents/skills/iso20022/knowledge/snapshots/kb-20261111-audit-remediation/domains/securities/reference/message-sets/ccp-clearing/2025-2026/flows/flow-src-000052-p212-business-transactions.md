---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
flow_id: "flow-src-000052-p212-business-transactions"
title: "BusinessTransactions"
source_locations: [{"source_id": "src-000052", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[212]", "paragraph_id": "P212", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[213]", "paragraph_id": "P213", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[214]", "paragraph_id": "P214", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[215]", "paragraph_id": "P215", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessTransactions"], "locator": "/w:document/w:body/w:p[216]", "paragraph_id": "P216", "table_id": null}]
participants: ["participant-src-000052-central-counterparty-ccp"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["BusinessTransactions", "Central Counterparty (CCP)"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# BusinessTransactions

Source context: CCP Clearing. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Central Counterparty (CCP) | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-central-counterparty-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P213** This section describes the message flows based on the activity diagrams documented above. It shows the typical exchanges of information in the context of a BusinessTransaction. 

**P214** Solid lines indicate mandatory messages.

**P215** Dotted lines indicate optional/potential messages.

**P216** The sequence diagrams describe the message flows between the central counterparty (CCP) and the clearing member. 

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000052](../../../../../../../evidence/omitted/b45c53bac2be08dee677b607.md). Heading path: BusinessTransactions.
