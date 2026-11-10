---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "shared"
source_ids: ["src-000343"]
source_editions: ["march-2024"]
message_sets: ["t2s-administration"]
flow_id: "flow-src-000343-p160-receipt-acknowledgement-admi-007"
title: "Receipt Acknowledgement (admi.007)"
source_locations: [{"source_id": "src-000343", "heading_path": ["Description of BusinessActivities", "Receipt Acknowledgement (admi.007)"], "locator": "/w:document/w:body/w:p[160]", "paragraph_id": "P160", "table_id": null}, {"source_id": "src-000343", "heading_path": ["Description of BusinessActivities", "Receipt Acknowledgement (admi.007)"], "locator": "/w:document/w:body/w:p[161]", "paragraph_id": "P161", "table_id": null}]
participants: ["participant-src-000343-system-transaction-administrator", "participant-src-000343-settlement-infrastructure", "participant-src-000343-system-member"]
message_mapping_evidence: [{"source_id": "src-000343", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Administration"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["admi.007"]
search_terms: ["Receipt Acknowledgement (admi.007)", "System Transaction Administrator", "Settlement Infrastructure", "System Member", "admi.007"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Receipt Acknowledgement (admi.007)

Source context: T2S Administration. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| System Transaction Administrator | [Participant](../../../../participants/participant-src-000343-system-transaction-administrator.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Settlement Infrastructure | [Participant](../../../../participants/participant-src-000343-settlement-infrastructure.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| System Member | [Participant](../../../../participants/participant-src-000343-system-member.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P161** Note: In the frame of the Central System workflows, System Transaction Administrator corresponds to the settlement infrastructure, the System Member to the Central System-Participant.

## Messages and alternative paths

Source-supported message family mentions: `admi.007`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000343](../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart1_Target2Securities_Administration_2023_2024_v2.docx`. Heading path: Description of BusinessActivities / Receipt Acknowledgement (admi.007).
