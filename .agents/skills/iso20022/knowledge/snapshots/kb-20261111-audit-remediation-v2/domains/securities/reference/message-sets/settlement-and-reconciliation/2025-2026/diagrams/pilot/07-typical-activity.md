---
template: false
document_kind: "diagram"
review_status: "needs-review"
title: "Typical instruction and confirmation activity"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
diagram_id: "fig-0007"
diagram_kind: "flowchart"
content_origin: "source-reconstruction"
priority: "standard"
mermaid_renderer: "Mermaid browser API + Chromium 156.0.8078.81"
mermaid_version: "12.3.0"
render_status: "pass"
visual_review: "pass"
message_ids: ["sese.023.001.13"]
limitations: ["Source and reconstructed layouts differ; semantics and notation differences are documented below."]
source_locations: [{"source_id": "src-000196", "locator": "direct-body paragraph P198", "heading_path": ["Description of BusinessActivities", "Instruction and Confirmation - Typical Process"], "xml_path": "/w:document/w:body/w:p[198]", "source_figure_id": "fig-0010"}]
original_asset: "domains/securities/assets/src-000196/originals/image10.emf"
manual_curated: true
rendered_source_pages: [19]
rendered_source_pdf: "work/docx-render/src-000196/document.pdf"
source_page_mapping_method: "exact-asset-sha256 in Word shape OpenXML"
---

# Typical instruction and confirmation activity

## Source and original artwork

[src-000196](../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md), §5.1 Instruction and Confirmation – Typical Process, paragraph198; table28. Paragraph IDs count direct-body paragraphs. Archive member `word/media/image10.emf`.

[Unchanged original figure](../../../../../../../../evidence/omitted/8c936c386bc0ee805a65fe95.md)

Original is an EMF vector figure. A separate working PNG was rasterized through Windows System.Drawing for source inspection; original vector file is unchanged.

## Mermaid reconstruction

```mermaid
flowchart TB
  subgraph I["Instructing Party"]
    startI((Start)) --> instruct[Instruct]
    monitor["Monitor Matching and Settlement Process"] --> settledI{Settled?}
    settledI -->|No| updateI[Update Status]
    updateI --> monitor
    settledI -->|Yes| settleI[Settle instruction]
    settleI --> endI((End))
  end
  subgraph E["Executing/Servicing Party"]
    process[Process instruction] --> processed{Processed?}
    processed -->|No| invalid[Update Status]
    processed -->|Yes| matching["Matching and Settlement Process"]
    matching --> settledE{Settled?}
    settledE -->|No| pending[Update Status]
    pending --> matching
    settledE -->|Yes| settleE[Settle instruction]
    settleE --> endE((End))
  end
  instruct --> process
  invalid --> instruct
  pending --> monitor
  settleE --> monitor
```

## Entities and relationships

Swimlanes preserve responsibility. Not-processed status returns to instruction; pending settlement cycles back into matching and monitoring. Each party maintains a settlement decision and settle-instruction activity. Table28 permits a successful-validation status update intentionally absent from artwork.

[Flow, participants, steps and alternatives](../../flows/instruction-confirmation.md)

## Review evidence

| Check | Result | Evidence |
| --- | --- | --- |
| Original figure inspection | performed | Source raster/EMF preview inspected on 2026-11-08 |
| Mermaid parse/render | pass | Mermaid 12.3.0; Chromium 156.0.8078.81; 2026-11-08 |
| Rendered reconstruction compared with original | pass | Compared responsible-party boundaries, start/end points, both settlement decisions, successful/unsuccessful validation, pending loops and cross-party status paths to EMF preview; omitted successful-validation update remains explicitly stated in text. |

[Pilot diagram index](index.md)

[Validated SVG](../../../../../../../../evidence/omitted/c618eda0046fb8b1b25304f3.md) · [Readable rendered PNG](../../../../../../../../evidence/omitted/4a9060938b5b84d90f96a545.md)

Visual review applies to this reconstructed view; it does not claim complete source-wide figure coverage or resolve source semantic defects.

<!-- RENDERED-SOURCE-START -->
## Rendered source page context

[Read-only Word-rendered source PDF](../../../../../../../../evidence/omitted/aae5b215a8f3b7a6b1062885.md); file page(s) 19. The page association is established by exact original-asset SHA-256 in the Word shape inventory, not by shape ordinal. Full-page/composite visual comparison is pending unless a separate dated review is recorded.
<!-- RENDERED-SOURCE-END -->
