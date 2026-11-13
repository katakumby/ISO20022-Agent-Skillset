---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
flow_id: "flow-src-000052-p113-trade-management-process"
title: "Trade Management process:"
source_locations: [{"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[113]", "paragraph_id": "P113", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[114]", "paragraph_id": "P114", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[115]", "paragraph_id": "P115", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[116]", "paragraph_id": "P116", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[117]", "paragraph_id": "P117", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[118]", "paragraph_id": "P118", "table_id": null}]
participants: ["participant-src-000052-ccp"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Trade Management process:", "CCP"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Trade Management process:

Source context: CCP Clearing. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| CCP | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P114** Definition: Process by which the CCP creates two trades (after Novation) from the one received from the exchange and reports them to the Clearing Members (CMs). The Novation is the legal concept that enables a CCP to become the counterparty. Through novation the original contract between the buyer and seller is extinguished and replaced by two new contracts, one between the CCP and the buyer and the one between the CCP and the seller.

**P115** Trigger: The process is triggered when the trading venue (either an exchange of a multilateral trading facility) notifies a trade to the CCP.

**P116** Pre-conditions: CCP accepts the trade.

**P117** Post-conditions: The Clearing member is notified of the trade.

**P118** Role: CCP

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000052](../../../../../../../evidence/omitted/b45c53bac2be08dee677b607.md). Heading path: BusinessProcess Description / BusinessProcess Diagram.
