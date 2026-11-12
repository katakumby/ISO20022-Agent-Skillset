---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p291-business-need"
title: "Business Need"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Need"], "locator": "/w:document/w:body/w:p[291]", "paragraph_id": "P291", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Need"], "locator": "/w:document/w:body/w:p[292]", "paragraph_id": "P292", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Need"], "locator": "/w:document/w:body/w:p[293]", "paragraph_id": "P293", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Need"], "locator": "/w:document/w:body/w:p[294]", "paragraph_id": "P294", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Need"], "locator": "/w:document/w:body/w:p[295]", "paragraph_id": "P295", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Need"], "locator": "/w:document/w:body/w:p[296]", "paragraph_id": "P296", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Need"], "locator": "/w:document/w:body/w:p[297]", "paragraph_id": "P297", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Need"], "locator": "/w:document/w:body/w:p[298]", "paragraph_id": "P298", "table_id": null}]
participants: []
message_mapping_evidence: [{"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Entitlements, Movement Preliminary Advice and Cancellation"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[2]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000080", "locator": "file page 360; 7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17"}]
message_ids: []
message_families: ["seev.035"]
search_terms: ["Business Need", "seev.035"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Business Need

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P292** Corporate Action Movement Preliminary Advice messaging addresses three key business needs:

**P293** Facilitate automated payment processing and payment management

**P294** The CA Movement Preliminary Advice is the building block for payment automation, it will allow for the message to interface automatically into payment processing systems and identify pre-matching of payments which will result in increased payment STP. 

**P295** Increase efficiency 

**P296** Custodians and clients could benefit from a CA Movement Preliminary Advice message that confirms payment details. The CA Movement Preliminary Advice message will report all critical details of corporate action payments at the account level within structured tags incorporating tax treatment information, rates, commissions, and fees. The CA Movement Preliminary Advice message can be linked to the CA Movement Confirmation message and achieve reconciliation at the account, tax profile, and specific transaction level. 

**P297** Reduce operational risk

**P298** In ISO 15022, the practice of using MT 564 for announcement of updated event details commingled with Movement Preliminary Advice of payment details is problematic. From an Event Management perspective, critical updates of event details could be missed if the MT 564 is perceived to be sent for final entitlement and/or cash reconciliation purposes. Similarly, the client could potentially miss Movement Preliminary Advice details needed to facilitate cash projections if the MT 564 is perceived to be for event or entitlement update details.

## Messages and alternative paths

Source-supported message family mentions: `seev.035`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Heading path: BusinessTransactions / Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios  / Business Need.
