---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
flow_id: "flow-src-000052-p161-buy-in-process"
title: "Buy-In process:"
source_locations: [{"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[161]", "paragraph_id": "P161", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[162]", "paragraph_id": "P162", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[163]", "paragraph_id": "P163", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[164]", "paragraph_id": "P164", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[165]", "paragraph_id": "P165", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[166]", "paragraph_id": "P166", "table_id": null}]
participants: ["participant-src-000052-ccp"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Buy-In process:", "CCP"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Buy-In process:

Source context: CCP Clearing. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| CCP | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P162** Definition: Process by which the CCP buy-in stocks to cover failed transactions.

**P163** Trigger: Non settlement of a trade after a certain number of days (depending on CCPs’).

**P164** Pre-conditions: The Clearing Member is not able to settle the trade(s).

**P165** Post-conditions: Settlement of the trade.

**P166** Role: CCP

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000052](../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart1_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v2.docx). Heading path: BusinessProcess Description / BusinessProcess Diagram.
