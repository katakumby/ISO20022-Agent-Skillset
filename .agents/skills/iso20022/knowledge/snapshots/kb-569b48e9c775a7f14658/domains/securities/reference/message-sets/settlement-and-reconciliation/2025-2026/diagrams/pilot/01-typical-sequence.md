---
template: false
document_kind: "diagram"
review_status: "needs-review"
title: "Instruction and confirmation sequence"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
diagram_id: "fig-0001"
diagram_kind: "sequence"
content_origin: "source-reconstruction"
priority: "standard"
mermaid_renderer: "Mermaid browser API + Chromium 156.0.8078.81"
mermaid_version: "12.3.0"
render_status: "pass"
visual_review: "pass"
message_ids: ["sese.023.001.13"]
limitations: ["Source and reconstructed layouts differ; semantics and notation differences are documented below."]
source_locations: [{"source_id": "src-000196", "locator": "direct-body paragraph P328", "heading_path": ["BusinessTransactions", "Instruction and Confirmation"], "xml_path": "/w:document/w:body/w:p[328]", "source_figure_id": "fig-0037"}]
original_asset: "domains/securities/assets/src-000196/originals/image37.png"
manual_curated: true
rendered_source_pages: [56]
rendered_source_pdf: "work/docx-render/src-000196/document.pdf"
source_page_mapping_method: "exact-asset-sha256 in Word shape OpenXML"
---

# Instruction and confirmation sequence

## Source and original artwork

[src-000196](../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md), §6.1 Instruction and Confirmation, paragraph328. Paragraph IDs count direct-body paragraphs. Archive member `word/media/image37.png`.

[Unchanged original figure](../../../../../../../../evidence/omitted/fcf08935f892a13538a03b64.md)

[Original figure](../../../../../../../../evidence/omitted/fcf08935f892a13538a03b64.md)

## Mermaid reconstruction

```mermaid
sequenceDiagram
  participant I as Instructing Party
  participant E as Executing Servicing Party
  I->>E: SecuritiesSettlementTransactionInstruction
  opt Optional processing status
    E->>I: SecuritiesSettlementTransactionStatusAdvice
  end
  opt Optional settlement status
    E->>I: SecuritiesSettlementTransactionStatusAdvice
  end
  E->>I: SecuritiesSettlementTransactionConfirmation
```

## Entities and relationships

Two optional status messages are separately shown. Both go from executing/servicing to instructing party; confirmation is last. Source building icons are decorative actor symbols, not institutional restrictions.

[Flow, participants, steps and alternatives](../../flows/instruction-confirmation.md)

## Review evidence

| Check | Result | Evidence |
| --- | --- | --- |
| Original figure inspection | performed | Source raster/EMF preview inspected on 2026-11-08 |
| Mermaid parse/render | pass | Mermaid 12.3.0; Chromium 156.0.8078.81; 2026-11-08 |
| Rendered reconstruction compared with original | pass | Compared both actors, instruction direction, two separate optional status boxes, confirmation and message labels. |

[Pilot diagram index](index.md)

[Validated SVG](../../../../../../../../evidence/omitted/4fbcd4a73425e7f2d4ab05d6.md) · [Readable rendered PNG](../../../../../../../../evidence/omitted/e9cad73e96662308e2cab555.md)

Visual review applies to this reconstructed view; it does not claim complete source-wide figure coverage or resolve source semantic defects.

<!-- RENDERED-SOURCE-START -->
## Rendered source page context

[Read-only Word-rendered source PDF](../../../../../../../../evidence/omitted/aae5b215a8f3b7a6b1062885.md); file page(s) 56. The page association is established by exact original-asset SHA-256 in the Word shape inventory, not by shape ordinal. Full-page/composite visual comparison is pending unless a separate dated review is recorded.
<!-- RENDERED-SOURCE-END -->
