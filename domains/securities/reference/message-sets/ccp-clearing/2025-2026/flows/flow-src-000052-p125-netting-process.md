---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
flow_id: "flow-src-000052-p125-netting-process"
title: "Netting process:"
source_locations: [{"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[125]", "paragraph_id": "P125", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[126]", "paragraph_id": "P126", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[127]", "paragraph_id": "P127", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[128]", "paragraph_id": "P128", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[129]", "paragraph_id": "P129", "table_id": null}, {"source_id": "src-000052", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[130]", "paragraph_id": "P130", "table_id": null}]
participants: ["participant-src-000052-ccp"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Netting process:", "CCP"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Netting process:

Source context: CCP Clearing. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| CCP | [Participant](../../../../../../../shared/reference/participants/participant-src-000052-ccp.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P126** Definition: Process by which a CCP takes all trades legs of a CM into account to calculate the net resulting position (client and house) which will be the basis for the margining process.

**P127** Trigger: End of day milestones from all markets.

**P128** Pre-conditions: None

**P129** Post-conditions: The CCP nets all the positions (per margin account– House and Client). The Clearing Member is informed of the netting results and it reconciles his netting calculation with the CCP results (based on the netting parameters).

**P130** Role: CCP

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000052](../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart1_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v2.docx). Heading path: BusinessProcess Description / BusinessProcess Diagram.
