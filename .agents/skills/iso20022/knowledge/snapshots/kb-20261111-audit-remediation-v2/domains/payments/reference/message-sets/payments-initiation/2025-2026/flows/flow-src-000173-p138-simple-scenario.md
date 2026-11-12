---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p138-simple-scenario"
title: "Simple scenario:"
source_locations: [{"source_id": "src-000173", "locator": "/w:document/w:body/w:p[138]", "paragraph_id": "P138", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"]}, {"source_id": "src-000173", "locator": "/w:document/w:body/w:p[139]", "paragraph_id": "P139", "heading_path": ["Description of BusinessActivities", "Customer to Bank Payment Order"]}]
participants: ["participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Simple scenario:"]
limitations: ["Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.", "Lane containers denote source responsibility columns, not new business institutions. Source rounded action boxes are rendered as rectangles; source final bullseye is a concentric Mermaid node with the central fill documented here. Colour and exact line routing remain in original.", "Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling.", "Source has no lane boundaries. One rendering container groups the chain for layout only. Solid and dashed arrows retain their source appearance; no undocumented condition is assigned to dashed arrows."]
manual_curated: true
participant_ids: ["participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-debtor-agent"]
related_diagrams: ["domains/payments/reference/message-sets/payments-initiation/2025-2026/diagrams/initiation/fig-0007.md"]
issue_ids: []
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative, original diagrams and rendered page context compared; tables retain independent review status."}
message_reference_scope: "Family/name-level Part1 flows; supplied exact definitions linked separately."
---



# Simple scenario:

[src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Purpose and trigger

Simple four-party credit-transfer chain.

Source defines participant-chain scope, without additional formal preconditions in this figure.

## Participants and responsibilities

| Scoped participant | Participation evidence |
| --- | --- |
| [creditor](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [creditor agent](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debtor](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md) | Source figure occurrence; exact action/message direction is shown below. |
| [debtor agent](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Source figure occurrence; exact action/message direction is shown below. |


## Source-defined conditions and activities

**P138** Simple scenario:

### fig-0007

[Source reconstruction and review](../diagrams/initiation/fig-0007.md); direct-body paragraph P139; Word file page17.

| Step | From/action | To/action | Source connection |
| --- | --- | --- | --- |
| 1 | Debtor | Debtor Agent | directed |
| 2 | Debtor Agent | Creditor Agent | directed |
| 3 | Creditor Agent | Creditor | directed |



## Outcomes, alternatives and related processes

Debtor → debtor agent → creditor agent → creditor; the figure is a chain view, not a complete settlement protocol.

- Actor pictograms identify roles in this context, not a fixed institutional identity. Source narrative may describe participants/steps omitted from this bounded figure.
- Lane containers denote source responsibility columns, not new business institutions. Source rounded action boxes are rendered as rectangles; source final bullseye is a concentric Mermaid node with the central fill documented here. Colour and exact line routing remain in original.
- Part1 message labels alone do not establish exact supplied schema versions. Original figures and their complete rendered page remain the evidence for geometry and line styling.
- Source has no lane boundaries. One rendering container groups the chain for layout only. Solid and dashed arrows retain their source appearance; no undocumented condition is assigned to dashed arrows.

## Supplied message definitions

| Family | Exact supplied reference | Scope |
| --- | --- | --- |



## Review

Compared source narrative, picture labels/directions and complete figure page context on 2026-11-09. This bounded flow evidence has been reviewed; participant classification/schema/table references keep their own review status.
