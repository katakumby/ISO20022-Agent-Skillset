---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
flow_id: "flow-src-000371-p259-confirmation-scenario"
title: "Confirmation Scenario"
source_locations: [{"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[259]", "paragraph_id": "P259", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[260]", "paragraph_id": "P260", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[261]", "paragraph_id": "P261", "table_id": null}, {"source_id": "src-000371", "heading_path": ["BusinessTransactions", "Deletion Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[262]", "paragraph_id": "P262", "table_id": null}]
participants: ["participant-src-000371-executing-servicing-party", "participant-src-000371-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000371", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000371", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["reda.020", "reda.032"]
search_terms: ["Confirmation Scenario", "Executing/Servicing Party", "Instructing Party", "reda.020", "reda.032"]
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

**P260** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing party

**P262** Securities Account Deletion Request (reda.032)Deletion processSecurities Account Status Advice (reda.020): QUEUEDSecurities Account Status Advice (reda.020):  COMPLETED

Source diagram evidence: [fig-0016](../documents/src-000371/diagrams/fig-0016.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `reda.020`, `reda.032`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000371](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Heading path: BusinessTransactions / Deletion Process / Confirmation Scenario.
