---
template: false
document_kind: "diagram"
review_status: "needs-review"
title: "Cancellation request sequence"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
diagram_id: "fig-0003"
diagram_kind: "sequence"
content_origin: "source-reconstruction"
priority: "standard"
mermaid_renderer: "Mermaid browser API + Chromium 156.0.8078.81"
mermaid_version: "12.3.0"
render_status: "pass"
visual_review: "pass"
message_ids: ["sese.023.001.13"]
limitations: ["Source and reconstructed layouts differ; semantics and notation differences are documented below."]
source_locations: [{"source_id": "src-000196", "locator": "direct-body paragraph P613", "heading_path": ["BusinessTransactions", "Cancellation Request"], "xml_path": "/w:document/w:body/w:p[613]", "source_figure_id": "fig-0069"}]
original_asset: "domains/securities/assets/src-000196/originals/image69.png"
manual_curated: true
rendered_source_pages: [91]
rendered_source_pdf: "work/docx-render/src-000196/document.pdf"
source_page_mapping_method: "exact-asset-sha256 in Word shape OpenXML"
---

# Cancellation request sequence

## Source and original artwork

[src-000196](../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md), §6.12 Cancellation Request, paragraph613. Paragraph IDs count direct-body paragraphs. Archive member `word/media/image69.png`.

[Unchanged original figure](../../../../../../../../evidence/omitted/de8b88df356b66e8b9b52cfc.md)

[Original figure](../../../../../../../../evidence/omitted/de8b88df356b66e8b9b52cfc.md)

## Mermaid reconstruction

```mermaid
sequenceDiagram
  participant I as Instructing Party
  participant E as Executing Servicing Party
  I->>E: Any instruction
  I->>E: SecuritiesTransactionCancellationRequest
  opt Optional
    E->>I: SecuritiesTransactionCancellationRequestStatusAdvice
  end
  E->>I: SecuritiesTransactionCancellationRequestStatusAdvice
```

## Entities and relationships

Original instruction and cancellation request go to executing/servicing party. Optional intermediate and final request statuses return. Completed status is stated in paragraph612, not written on the source arrow.

[Flow, participants, steps and alternatives](../../flows/cancellation-request.md)

## Review evidence

| Check | Result | Evidence |
| --- | --- | --- |
| Original figure inspection | performed | Source raster/EMF preview inspected on 2026-11-08 |
| Mermaid parse/render | pass | Mermaid 12.3.0; Chromium 156.0.8078.81; 2026-11-08 |
| Rendered reconstruction compared with original | pass | Compared original instruction and cancellation request directions, optional intermediate status, final status and all labels. |

[Pilot diagram index](index.md)

[Validated SVG](../../../../../../../../evidence/omitted/09dbfa46b4311a2b8ec2bdf1.md) · [Readable rendered PNG](../../../../../../../../evidence/omitted/1486906d393e3c66a930995d.md)

Visual review applies to this reconstructed view; it does not claim complete source-wide figure coverage or resolve source semantic defects.

<!-- RENDERED-SOURCE-START -->
## Rendered source page context

[Read-only Word-rendered source PDF](../../../../../../../../evidence/omitted/aae5b215a8f3b7a6b1062885.md); file page(s) 91. The page association is established by exact original-asset SHA-256 in the Word shape inventory, not by shape ordinal. Full-page/composite visual comparison is pending unless a separate dated review is recorded.
<!-- RENDERED-SOURCE-END -->
