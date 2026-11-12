---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
flow_id: "flow-src-000368-p295-party-activity-advice"
title: "Party Activity Advice"
source_locations: [{"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Statement Process"], "locator": "/w:document/w:body/w:p[295]", "paragraph_id": "P295", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Statement Process"], "locator": "/w:document/w:body/w:p[296]", "paragraph_id": "P296", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Statement Process"], "locator": "/w:document/w:body/w:p[297]", "paragraph_id": "P297", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Statement Process"], "locator": "/w:document/w:body/w:p[298]", "paragraph_id": "P298", "table_id": null}]
participants: ["participant-src-000368-executing-servicing-party", "participant-src-000368-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000368", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Party Reference Data"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[8]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["reda.041"]
search_terms: ["Party Activity Advice", "Executing / Servicing Party", "Instructing Party", "reda.041"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Party Activity Advice

Source context: T2S PartyReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000368-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000368-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P296** The Executing/Servicing Party sends a statement to the Instructing Party containing information on changes occurred for Party reference data during the business day.

**P297** The statement is sent unilaterally in an unsolicited manner.

## Messages and alternative paths

Source-supported message family mentions: `reda.041`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000368](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`. Heading path: BusinessTransactions / Statement Process.
