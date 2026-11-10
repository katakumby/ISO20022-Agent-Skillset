---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p195-corporate-action-event-withdrawal-process"
title: "Corporate Action Event Withdrawal Process"
source_locations: [{"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities ", "Corporate Action Event Withdrawal Process"], "locator": "/w:document/w:body/w:p[195]", "paragraph_id": "P195", "table_id": null}, {"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities ", "Corporate Action Event Withdrawal Process"], "locator": "/w:document/w:body/w:p[196]", "paragraph_id": "P196", "table_id": null}, {"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities ", "Corporate Action Event Withdrawal Process"], "locator": "/w:document/w:body/w:tbl[28]", "paragraph_id": null, "table_id": "T28"}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner", "participant-src-000079-issuer"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Corporate Action Event Withdrawal Process", "Account Servicer", "Account Owner", "Issuer"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Corporate Action Event Withdrawal Process

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Issuer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-issuer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0019](../documents/src-000079/diagrams/fig-0019.md). Mermaid reconstruction and visual review are pending.

Source table [T28](../documents/src-000079/tables/tbl-0028.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Corporate Action withdrawal process | Advise the account owner that a previously announced corporate action has been withdrawn by the issuer. | Account Servicer |
| Process Corporate Action withdrawal | Process corporate action withdrawal: the account owner processes the corporate action withdrawal. | Account Owner |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Heading path: Description of BusinessActivities / BusinessActivities  / Corporate Action Event Withdrawal Process.
