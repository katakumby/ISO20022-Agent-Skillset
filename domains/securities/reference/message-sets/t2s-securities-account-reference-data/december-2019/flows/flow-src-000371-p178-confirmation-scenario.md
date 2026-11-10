---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
flow_id: "flow-src-000371-p178-confirmation-scenario"
title: "Confirmation Scenario"
source_locations: [{"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[178]", "paragraph_id": "P178", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[179]", "paragraph_id": "P179", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[180]", "paragraph_id": "P180", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Creation Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[181]", "paragraph_id": "P181", "table_id": null}]
participants: ["participant-src-000371-executing-servicing-party", "participant-src-000371-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000371", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000371", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["reda.018", "reda.020"]
search_terms: ["Confirmation Scenario", "Executing/Servicing Party", "Instructing Party", "reda.018", "reda.020"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Confirmation Scenario

Source context: T2S SecuritiesAccountReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing/Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000371-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000371-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P179** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing Party.

**P181** Creation ProcessSecurities Account Status Advice (reda.020): QUEUEDSecurities Account Status Advice (reda.020): COMPLETEDCOMPLETEDSecurities Account Creation Request (reda.018)

Source diagram evidence: [fig-0012](../documents/src-000371/diagrams/fig-0012.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `reda.018`, `reda.020`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000371](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Heading path: BusinessTransactions / Creation Process / Confirmation Scenario.
