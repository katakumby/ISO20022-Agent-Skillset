---
template: false
document_kind: "diagram"
review_status: "needs-review"
title: "Settlement reversal advice sequence"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
diagram_id: "fig-0005"
diagram_kind: "sequence"
content_origin: "source-reconstruction"
priority: "standard"
mermaid_renderer: "Mermaid browser API + Chromium 156.0.8078.81"
mermaid_version: "12.3.0"
render_status: "pass"
visual_review: "pass"
message_ids: ["sese.023.001.13"]
limitations: ["Source and reconstructed layouts differ; semantics and notation differences are documented below."]
source_locations: [{"source_id": "src-000196", "locator": "direct-body paragraph P626", "heading_path": ["BusinessTransactions", "Reversal Advice"], "xml_path": "/w:document/w:body/w:p[626]", "source_figure_id": "fig-0071"}]
original_asset: "domains/securities/assets/src-000196/originals/image71.png"
manual_curated: true
---

# Settlement reversal advice sequence

## Source and original artwork

[src-000196](<../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx>), §6.14 Reversal Advice, paragraph626. Paragraph IDs count direct-body paragraphs. Archive member `word/media/image71.png`.

[Unchanged original figure](<../../../../../../assets/src-000196/originals/image71.png>)

![Original figure](<../../../../../../assets/src-000196/originals/image71.png>)

## Mermaid reconstruction

```mermaid
sequenceDiagram
  participant I as Instructing Party
  participant E as Executing Servicing Party
  E->>I: SecuritiesSettlementTransactionConfirmation
  E->>I: SecuritiesSettlementTransactionReversalAdvice
```

## Entities and relationships

Both confirmation and reversal travel from executing/servicing to instructing party. Reversal reverses the prior confirmation; it is not an instructing-party cancellation request.

[Flow, participants, steps and alternatives](<../../flows/reversal-advice.md>)

## Review evidence

| Check | Result | Evidence |
| --- | --- | --- |
| Original figure inspection | performed | Source raster/EMF preview inspected on 2026-11-08 |
| Mermaid parse/render | pass | Mermaid 12.3.0; Chromium 156.0.8078.81; 2026-11-08 |
| Rendered reconstruction compared with original | pass | Compared two servicer-to-instructing-party arrows, confirmation then reversal, exact labels. |

[Pilot diagram index](<index.md>)

[Validated SVG](<../../../../../../assets/src-000196/reconstructed/05-reversal-sequence.svg>) · [Readable rendered PNG](<../../../../../../assets/src-000196/reconstructed/05-reversal-sequence.png>)

Visual review applies to this reconstructed view; it does not claim complete source-wide figure coverage or resolve source semantic defects.
