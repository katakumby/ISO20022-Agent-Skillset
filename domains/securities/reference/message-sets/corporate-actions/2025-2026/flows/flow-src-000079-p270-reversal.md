---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p270-reversal"
title: "Reversal"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Confirmation and Reversal", "Reversal"], "locator": "/w:document/w:body/w:p[270]", "paragraph_id": "P270", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Confirmation and Reversal", "Reversal"], "locator": "/w:document/w:body/w:p[271]", "paragraph_id": "P271", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Confirmation and Reversal", "Reversal"], "locator": "/w:document/w:body/w:p[272]", "paragraph_id": "P272", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Confirmation and Reversal", "Reversal"], "locator": "/w:document/w:body/w:p[273]", "paragraph_id": "P273", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Confirmation and Reversal", "Reversal"], "locator": "/w:document/w:body/w:p[274]", "paragraph_id": "P274", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Confirmation and Reversal", "Reversal"], "locator": "/w:document/w:body/w:p[275]", "paragraph_id": "P275", "table_id": null}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner"]
message_mapping_evidence: [{"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Entitlements, Movement Preliminary Advice and Cancellation"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[2]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000080", "locator": "file page 360; 7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17"}, {"source_id": "src-000080", "locator": "file page 665; 9 seev.037.001.17 CorporateActionMovementReversalAdviceV17"}]
message_ids: []
message_families: ["seev.035", "seev.037"]
search_terms: ["Reversal", "Account Servicer", "Account Owner", "seev.035", "seev.037"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---





# Reversal

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P271** This scenario illustrates a classical sequence of corporate action messages for the confirmation and phase of a corporate action event when a reversal occurs.

**P272** Once the announcement phase and the election phase (in the cases of elective corporate action events) are completed and the account servicer has confirmed to the account owner that the movements have been applied on its account, and for some reasons, the movements must be reversed, the account servicer may optionally send a reversal CorporateActionMovementPreliminaryAdvice to the account owner to pre-advise him that the securities and/or cash movements are going to be reversed. The account servicer may also indicate the reason for the reversal.

**P273** The account servicer must also send a CorporateActionMovementReversalAdvice to the account owner to confirm the reversal of the movements have been carried out. The account servicer may also indicate the reason for the reversal into the CorporateActionMovementReversalAdvice.

Source diagram evidence: [fig-0029](../documents/src-000079/diagrams/fig-0029.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `seev.035`, `seev.037`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Heading path: BusinessTransactions / Confirmation and Reversal / Reversal.

## Direction of reported movements in reversal advice

Source src-000079, Business Scenarios / Scenario 5: Mandatory Event with Reversal of Payment, P344-P346, distinguishes the direction of reported movements from the direction of the message exchange. The preliminary advice of a reversal reports movements opposite to those in the referred movement confirmation: credits become debits and debits become credits (P344). The actual movement reversal reports movements identical to those in the referred confirmation (P345). Where the final entitlements are re-booked after a reversal, the source recommends treating that re-booking as a new payment, subject to the agreed preliminary-advice criteria (P346). Both preliminary advice and reversal messages in image37 flow from the account servicer to the account owner.

[Scenario 5 source reconstruction](../diagrams/routing-scenarios/fig-0037.md).
