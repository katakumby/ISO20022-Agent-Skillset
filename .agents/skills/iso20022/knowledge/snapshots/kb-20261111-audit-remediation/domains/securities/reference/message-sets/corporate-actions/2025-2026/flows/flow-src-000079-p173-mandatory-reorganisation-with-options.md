---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p173-mandatory-reorganisation-with-options"
title: "Mandatory Reorganisation with Options"
source_locations: [{"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities Timeline", "Elective Corporate Action Events Sequence", "Mandatory Reorganisation with Options"], "locator": "/w:document/w:body/w:p[173]", "paragraph_id": "P173", "table_id": null}, {"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities Timeline", "Elective Corporate Action Events Sequence", "Mandatory Reorganisation with Options"], "locator": "/w:document/w:body/w:p[174]", "paragraph_id": "P174", "table_id": null}, {"source_id": "src-000079", "heading_path": ["Description of BusinessActivities", "BusinessActivities Timeline", "Elective Corporate Action Events Sequence", "Mandatory Reorganisation with Options"], "locator": "/w:document/w:body/w:p[175]", "paragraph_id": "P175", "table_id": null}]
participants: ["participant-src-000079-account-owner", "participant-src-000079-account-servicer", "participant-src-000079-issuer"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Mandatory Reorganisation with Options"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "The source dashed connector between the pre-confirmation region and final post-reversal merge has no clearly readable arrowhead in the supplied PNG. It is reconstructed as an undirected dashed connection; no reverse loop or extra execution order is inferred."]
manual_curated: true
issue_ids: ["issue-000024"]
---







# Mandatory Reorganisation with Options

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P174** This covers mandatory reorganisation with options (REOR/CHOS) and mandatory distribution with options (DISN/CHOS) and voluntary reorganisation (REOR/VOLU).

Source diagram evidence: [fig-0011](../documents/src-000079/diagrams/fig-0011.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Heading path: Description of BusinessActivities / BusinessActivities Timeline / Elective Corporate Action Events Sequence / Mandatory Reorganisation with Options.

## Source activity reconstruction

This high-level process view is scoped by P171/P174 to REOR/CHOS, DISN/CHOS and REOR/VOLU. It contains event announcement/amendment, issuer withdrawal, account-servicer cancellation, eligibility/entitlement, optional preliminary advice, confirmation and reversal paths. The options flow additionally contains preliminary and final eligibility phases, instruction processing and transaction cancellation. Every unlabeled source diamond remains an unlabeled diamond; no unstated guard is supplied. The small blank junction circle is a derived routing aid for the source line junction, not a new business activity. The general source note says event sequences can vary and this is only a possible sequence. The source does not draw participant lanes here; responsible roles must be retrieved from the named process references, not inferred from box position.

[Corporate action processes with options](../diagrams/detailed-activities/fig-0011.md). The source dashed connector between the pre-confirmation region and final post-reversal merge has no clearly readable arrowhead in the supplied PNG. It is reconstructed as an undirected dashed connection; no reverse loop or extra execution order is inferred.

## Responsible roles from process definitions

Source T11-T19 provides the functional responsibilities independently of drawing layout: Account Servicer for notification, entitlement, reminder, preliminary advice, confirmation, reversal and status; Account Owner for election; cancellation can involve either role according to its target. [Election process (T14)](../documents/src-000079/tables/tbl-0014.md); [Cancellation process (T18)](../documents/src-000079/tables/tbl-0018.md). These source roles do not turn a process arrow into an exact message exchange.
