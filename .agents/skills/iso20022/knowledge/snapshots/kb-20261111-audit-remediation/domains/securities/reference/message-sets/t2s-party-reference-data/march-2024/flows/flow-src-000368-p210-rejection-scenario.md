---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
flow_id: "flow-src-000368-p210-rejection-scenario"
title: "Rejection Scenario"
source_locations: [{"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[210]", "paragraph_id": "P210", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[211]", "paragraph_id": "P211", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[212]", "paragraph_id": "P212", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[213]", "paragraph_id": "P213", "table_id": null}]
participants: ["participant-src-000368-executing-servicing-party", "participant-src-000368-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000368", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Party Reference Data"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000368", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Party Reference Data"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["reda.016", "reda.022"]
search_terms: ["Rejection Scenario", "Executing / Servicing Party", "Instructing Party", "reda.016", "reda.022"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Rejection Scenario

Source context: T2S PartyReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000368-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000368-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P211** Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party

**P213** Party Modification Request (reda.022)Modification processParty Status Advice (reda.016): QUEUEDParty Status Advice (reda.016): REJECTED

Source diagram evidence: [fig-0015](../documents/src-000368/diagrams/fig-0015.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `reda.016`, `reda.022`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000368](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`. Heading path: BusinessTransactions / Modification Process / Rejection Scenario.
