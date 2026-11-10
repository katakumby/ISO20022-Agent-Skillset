---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p140-complex-scenario"
title: "Complex scenario:"
source_locations: [{"source_id": "src-000173", "locator": "/w:document/w:body/w:p[140]", "paragraph_id": "P140", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[141]", "paragraph_id": "P141", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"]}]
participants: ["participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-forwarding-agent", "participant-src-000173-initiating-party", "participant-src-000173-ultimate-creditor", "participant-src-000173-ultimate-debtor"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Complex scenario:", "Initiating Party/ Debtor Agent / Forwarding Agent", "Forwarding Agent / Debtor Agent", "Debtor Agent / Forwarding Agent", "Debtor Agent / Creditor Agent", "Initiating Party/Debtor", "Forwarding Agent", "Initiating Party", "Creditor Agent", "Debtor Agent", "Creditor", "Debtor", "Party"]
limitations: ["Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.", "Lane containers denote source responsibility columns, not new business institutions. Source rounded action boxes are rendered as rectangles; source final bullseye is a concentric Mermaid node with the central fill documented here. Colour and exact line routing remain in original.", "Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling.", "Source has no lane boundaries. One rendering container groups the chain for layout only. Solid and dashed arrows retain their source appearance; no undocumented condition is assigned to dashed arrows."]
manual_curated: true
participant_ids: ["participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-forwarding-agent", "participant-src-000173-initiating-party", "participant-src-000173-ultimate-creditor", "participant-src-000173-ultimate-debtor"]
related_diagrams: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/diagrams/initiation/fig-0008.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and rendered page context compared; tables retain independent review status."}
message_reference_scope: "Family/name-level Part1 flows; supplied exact definitions linked separately."
---



# Complex scenario:

[src-000173](../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx)

## Purpose and trigger

Complex customer-to-bank chain separating initiating and ultimate parties.

Source shows optional chain variants with dashed connectors, but supplies no separate condition on each dashed edge.

## Participants and responsibilities

| Scoped participant | Participation evidence |
| --- | --- |
| [creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [creditor agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debtor](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debtor agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [forwarding agent](../../../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [initiating party](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | Source figure occurrence; exact action/message direction is shown below. |
| [ultimate creditor](../../../../../../../shared/reference/participants/participant-src-000173-ultimate-creditor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [ultimate debtor](../../../../../../../shared/reference/participants/participant-src-000173-ultimate-debtor.md) | Source figure occurrence; exact action/message direction is shown below. |


## Source-defined conditions and activities

**P140** Complex scenario:

### fig-0008

[Source reconstruction and review](../diagrams/initiation/fig-0008.md); direct-body paragraph P141; Word file page17.

| Step | From/action | To/action | Source connection |
| --- | --- | --- | --- |
| 1 | Ultimate Debtor | Debtor | dashed directed |
| 2 | Debtor | Initiating Party | dashed directed |
| 3 | Initiating Party | Debtor Agent | directed |
| 4 | Initiating Party | Forwarding Agent | dashed directed |
| 5 | Forwarding Agent | Debtor Agent | dashed directed |
| 6 | Debtor Agent | Creditor Agent | directed |
| 7 | Creditor Agent | Creditor | directed |
| 8 | Creditor | Ultimate Creditor | directed |



## Outcomes, alternatives and related processes

Multiple functional roles can be performed by the same or different actors; no cross-role institutional identity follows.

- Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.
- Lane containers denote source responsibility columns, not new business institutions. Source rounded action boxes are rendered as rectangles; source final bullseye is a concentric Mermaid node with the central fill documented here. Colour and exact line routing remain in original.
- Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling.
- Source has no lane boundaries. One rendering container groups the chain for layout only. Solid and dashed arrows retain their source appearance; no undocumented condition is assigned to dashed arrows.

## Supplied message definitions

| Family | Exact supplied reference | Scope |
| --- | --- | --- |



## Review

Compared source narrative, picture labels/directions and complete figure page context on 2026-11-09. This bounded flow evidence has been reviewed; participant classification/schema/table references keep their own review status.
