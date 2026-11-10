---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
flow_id: "flow-src-000052-p167-reporting-process-out-of-scope"
title: "Reporting process (Out of scope):"
source_locations: [{"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[167]", "paragraph_id": "P167", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[168]", "paragraph_id": "P168", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[169]", "paragraph_id": "P169", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[170]", "paragraph_id": "P170", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[171]", "paragraph_id": "P171", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[172]", "paragraph_id": "P172", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[173]", "paragraph_id": "P173", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[174]", "paragraph_id": "P174", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[175]", "paragraph_id": "P175", "table_id": null}]
participants: ["participant-src-000052-ccp"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Reporting process (Out of scope):", "CCP"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Reporting process (Out of scope):

Source context: CCP Clearing. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| CCP | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P168** Definition: Process by which CCPs provide reports on cash settlement information, on trade(s) that did not settle correctly at the settlement date, or on the valuation of the collateral posted by the clearing members.

**P169** Trigger: End of day milestones from all markets.

**P170** Pre-conditions: The CCP has received the report with all failed trades from the Central Securities Depository or the end of day process has generated reports that are sent out to the clearing members.

**P171** Post-conditions: None

**P172** Role: CCP

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000052](../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart1_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v2.docx). Heading path: BusinessProcess Description / BusinessProcess Diagram.
