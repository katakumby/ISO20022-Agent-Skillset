---
template: false
document_kind: "diagram-detail"
manual_curated: true
review_status: "reviewed"
domain: "securities"
diagram_id: "fig-0002-overview"
title: "Modes, actors and six query categories"
diagram_kind: "taxonomy"
content_origin: "source-reconstruction"
source_ids: ["src-000356"]
source_editions: ["march-2024"]
source_locations: [{"source_id": "src-000356", "locator": "BusinessProcess Description / BusinessProcess Diagram; direct-body paragraph P130; word/media/image2.png"}]
participants: ["participant-src-000356-central-system", "participant-src-000356-system-user", "participant-src-000356-central-securities-depositories-csd", "participant-src-000356-settlement-bank", "participant-src-000356-payment-bank", "participant-src-000356-national-central-bank-ncb"]
flow_ids: []
message_ids: []
message_sets: ["t2s-collateral-reporting"]
render_status: "pass"
visual_review: "pass"
issue_ids: []
limitations: ["Visible artwork reconstructed with native Mermaid notation; exact decorative symbols and source geometry retained in original. Native embedded Visio originals/static inspection are preserved separately; hidden content is not certified by preview review."]
parent_diagram: "fig-0002"
mermaid_version: "12.3.0"
review_date: "2026-11-09"
---



# Modes, actors and six query categories

Focused view of [the complete source query taxonomy](fig-0002.md). Source src-000356, direct-body P130, word/media/image2.png. This view partitions the artwork for readable retrieval; it adds no new query permissions or message bindings.

```mermaid
flowchart TB
 Q["Queries"] --> U["U2A"]
 Q --> A["A2A"]
 U --- Modes((" "))
 A --- Modes
 Modes --> C["CSDs"]
 Modes --> S["Settlement Banks"]
 Modes --> P["Payment Banks"]
 Modes --> N["NCBs"]
 C --- Actors((" "))
 S --- Actors
 P --- Actors
 N --- Actors
 Actors --> Ins["Instructions"]
 Actors --> Sec["Security account"]
 Actors --> Cash["Cash account"]
 Actors --> Day["Settlement day"]
 Actors --> Dyn["Dynamic data queries"]
 Actors --> Static["Static data"]
 style Modes fill:none,stroke:none
 style Actors fill:none,stroke:none```

[Complete unchanged source](../../../../../../assets/src-000356/originals/image2.png).

## Review evidence

Compared with original image2.png and Word page13: every included label and edge checked; all25 query leaves are preserved across the focused details. Mermaid12.3.0 / Chromium156.0.8078.81 render and visual comparison passed2026-11-09. [Compared focused reconstruction](../../../../../../assets/src-000356/reconstructed/fig-0002-overview.png).
