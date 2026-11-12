---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p315-cancellation-of-a-preliminary-movement-advice"
title: "Cancellation of a Preliminary Movement Advice"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Usage Rules", "Cancellation of a Preliminary Movement Advice"], "locator": "/w:document/w:body/w:p[315]", "paragraph_id": "P315", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Usage Rules", "Cancellation of a Preliminary Movement Advice"], "locator": "/w:document/w:body/w:p[316]", "paragraph_id": "P316", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Usage Rules", "Cancellation of a Preliminary Movement Advice"], "locator": "/w:document/w:body/w:p[317]", "paragraph_id": "P317", "table_id": null}]
participants: ["participant-src-000079-account-servicer"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Cancellation of a Preliminary Movement Advice", "Account Servicer"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Cancellation of a Preliminary Movement Advice

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P316** When an election instruction is cancelled - At this point the resulting entitlement has been recalculated to zero and the service provider may send a cancellation of the Movement Preliminary Advice to convey that the movements have been taken down.

**P317** A Movement Preliminary Advice can be sent to pre-advise of a reversal of corporate action cash or securities postings. If the CA Confirmation Reversal does not finally take place, this pre-advice of movement reversal may be cancelled by the account servicer.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Heading path: BusinessTransactions / Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios  / Usage Rules / Cancellation of a Preliminary Movement Advice.
