---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p152-movement-confirmation"
title: "Movement Confirmation"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[152]", "paragraph_id": "P152", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[16]", "paragraph_id": null, "table_id": "T16"}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Movement Confirmation", "Account Servicer", "Account Owner"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Movement Confirmation

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The process of confirming that a corporate action event has been completed and that the appropriate postings to the account owner’s safekeeping account(s) have been effected.

Evidence: [T16](../documents/src-000079/tables/tbl-0016.md), source row 2.

### Trigger

Securities or cash have been credited or debited to/from an account as the result of a corporate action event.

Evidence: [T16](../documents/src-000079/tables/tbl-0016.md), source row 3.

### Pre-conditions

Postings of cash / securities are done to the account owner’s account(s)

Evidence: [T16](../documents/src-000079/tables/tbl-0016.md), source row 4.

### Post-conditions

None

Evidence: [T16](../documents/src-000079/tables/tbl-0016.md), source row 5.

### Role

Account servicer

Evidence: [T16](../documents/src-000079/tables/tbl-0016.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T16](../documents/src-000079/tables/tbl-0016.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Heading path: BusinessProcess Description.
