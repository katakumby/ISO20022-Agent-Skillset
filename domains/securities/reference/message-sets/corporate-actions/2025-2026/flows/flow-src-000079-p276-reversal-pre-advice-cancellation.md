---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p276-reversal-pre-advice-cancellation"
title: "Reversal Pre-Advice Cancellation"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Confirmation and Reversal", "Reversal Pre-Advice Cancellation"], "locator": "/w:document/w:body/w:p[276]", "paragraph_id": "P276", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Confirmation and Reversal", "Reversal Pre-Advice Cancellation"], "locator": "/w:document/w:body/w:p[277]", "paragraph_id": "P277", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Confirmation and Reversal", "Reversal Pre-Advice Cancellation"], "locator": "/w:document/w:body/w:p[278]", "paragraph_id": "P278", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Confirmation and Reversal", "Reversal Pre-Advice Cancellation"], "locator": "/w:document/w:body/w:p[279]", "paragraph_id": "P279", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Confirmation and Reversal", "Reversal Pre-Advice Cancellation"], "locator": "/w:document/w:body/w:p[280]", "paragraph_id": "P280", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Confirmation and Reversal", "Reversal Pre-Advice Cancellation"], "locator": "/w:document/w:body/w:p[281]", "paragraph_id": "P281", "table_id": null}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner"]
message_mapping_evidence: [{"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Entitlements, Movement Preliminary Advice and Cancellation"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[2]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000080", "locator": "file page 360; 7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17"}, {"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Entitlements, Movement Preliminary Advice and Cancellation"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[3]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000080", "locator": "file page 813; 15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13"}]
message_ids: []
message_families: ["seev.035", "seev.044"]
search_terms: ["Reversal Pre-Advice Cancellation", "Account Servicer", "Account Owner", "seev.035", "seev.044"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Reversal Pre-Advice Cancellation

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P277** This scenario illustrates a classical sequence of corporate action messages for the confirmation and phase of a corporate action event when a cancellation of a reversal pre-advice occurs.

**P278** Once the announcement phase and the election phase (in the cases of elective corporate action events) are completed and the account servicer has confirmed to the account owner that the movements have been applied on its account, and for some reasons, the movements must be reversed, the account servicer may optionally send a reversal CorporateActionMovementPreliminaryAdvice to the account owner to pre-advise him that the securities and/or cash movements are going to be reversed. The account servicer may also indicate the reason for the reversal.

**P279** If it finally comes out after this that the movements will not be reversed, the account servicer must cancel the reversal pre-advice by sending a CorporateActionMovementPreliminaryAdviceCancellationAdvice to the account owner to confirm the cancellation of the announced reversal of the movements.

Source diagram evidence: [fig-0030](../documents/src-000079/diagrams/fig-0030.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `seev.035`, `seev.044`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Heading path: BusinessTransactions / Confirmation and Reversal / Reversal Pre-Advice Cancellation.
