---
template: false
document_kind: "extraction-audit"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
source_locations: [{"source_id": "src-000096", "file_pages": [1, 5406]}]
pdf_geometry_reconciliation: "pass-with-scoped-limitations"
pdf_table_text_reconciliation: "pass-with-recorded-character-mapping"
pdf_markdown_cell_preservation: "pass"
pdf_unclassified_painted_objects: 0
visual_review_pages: [4360, 4362, 4368, 4369, 4400, 4401, 4719, 4720, 4722, 4726, 4727, 5015, 5016, 5119, 5120, 5138]
updated: "2026-11-09"
limitations: ["Geometric association with a table is not independent semantic review of its contents. All original lexical vector candidates remain available.", "PDFium omits unpainted clipping paths from its painted-object list; unsupported image/form/shading objects and non-axis paths remain unresolved.", "Cell text comparison normalizes only Unicode compatibility and whitespace, preserving case, digits and punctuation. Soft-hyphen control differences remain explicit exceptions.", "Span/null positions preserve missing separate extracted cells; their semantics require original page/table context.", "No claim that each page or each cell has been individually visually inspected. Text-only diagrams and source-level semantic ambiguities are outside this mechanical classification."]
---

# PDF table and painted-object reconciliation

Source: [src-000096](../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). All 5406 file pages were enumerated, with the registered source checksum verified unchanged. 8434 extracted table candidates contain 455224 physical cells. Their complete Markdown cell matrices match the maintained extraction. Independent PDFium bounded cell text matched 455059 cells after Unicode compatibility/whitespace normalization. 165 remaining comparisons differ only by PDFium U+0002 representing a source hyphen; every exact source/cell locator and both strings remain in the audit. No other cell-text difference or uncertain grid mapping was found.

[Per-page geometry and complete cell/exception index](../../../../../../../../work/documents/src-000096/structural-audit/summary.json) · [Method, limitations and corpus results](../../../../../../../../catalog/pdf-structural-review.md)

## Geometry disposition

| Painted geometry class | Objects |
| --- | --- |
| link-annotation-underline | 22460 |
| margin-rule-template-candidate | 21620 |
| table-associated-axis-line | 1036830 |
| table-associated-filled-rectangle | 26879 |
| unclassified-painted-path | 60 |

Painted path association is a structural classification, not an individual visual review of every page. Original lexical vector-candidate inventories remain unchanged; unpainted clipping operators do not create visible diagram content.

| File page | Objects | Disposition | Evidence |
| --- | --- | --- | --- |
| 4360 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../../../evidence/omitted/71f75e91e04473fe43b2e038.md) |
| 4362 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../../../evidence/omitted/5dcd6191a0a72386f476dec7.md) |
| 4368 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../../../evidence/omitted/861c413c7ee9c25e173c9226.md) |
| 4369 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../../../evidence/omitted/ce615ea5632cdd6a589c035b.md) |
| 4400 | 6 | substantive-warning-panels | [Inspected complete page](../../../../../../../../evidence/omitted/c3c3cac07b5847e3e1ef3694.md) |
| 4401 | 6 | substantive-warning-panels | [Inspected complete page](../../../../../../../../evidence/omitted/61f339026332734c4b6bdbc1.md) |
| 4719 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../../../evidence/omitted/5a4ac113b2639458dfd5d3d6.md) |
| 4720 | 6 | substantive-warning-panels | [Inspected complete page](../../../../../../../../evidence/omitted/1362b00f7a6dd38914de507e.md) |
| 4722 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../../../evidence/omitted/5719cda97351c374eae2daf0.md) |
| 4726 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../../../evidence/omitted/7c0a0b9ba146df87cac2d7e8.md) |
| 4727 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../../../evidence/omitted/99460f28ead3483950452675.md) |
| 5015 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../../../evidence/omitted/8ffe1c60dc41da6256d6fb26.md) |
| 5016 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../../../evidence/omitted/2997695cd2faac764795976e.md) |
| 5119 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../../../evidence/omitted/73d6eeb43d5e04f52c113e92.md) |
| 5120 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../../../evidence/omitted/c4c4fa4ccf63e161626b71a3.md) |
| 5138 | 6 | substantive-warning-panels | [Inspected complete page](../../../../../../../../evidence/omitted/70b57945e1a9c7daf292f183.md) |

- Page4360: Shaded single-row Warning panels express source choice conditions. All 20 panels across 16 pages now have supplemental table records; not diagrams.
- Page4362: Shaded single-row Warning panels express source choice conditions. All 20 panels across 16 pages now have supplemental table records; not diagrams.
- Page4368: Shaded single-row Warning panels express source choice conditions. All 20 panels across 16 pages now have supplemental table records; not diagrams.
- Page4369: Shaded single-row Warning panels express source choice conditions. All 20 panels across 16 pages now have supplemental table records; not diagrams.
- Page4400: Shaded single-row Warning panels express source choice conditions. All 20 panels across 16 pages now have supplemental table records; not diagrams.
- Page4401: Shaded single-row Warning panels express source choice conditions. All 20 panels across 16 pages now have supplemental table records; not diagrams.
- Page4719: Shaded single-row Warning panels express source choice conditions. All 20 panels across 16 pages now have supplemental table records; not diagrams.
- Page4720: Shaded single-row Warning panels express source choice conditions. All 20 panels across 16 pages now have supplemental table records; not diagrams.
- Page4722: Shaded single-row Warning panels express source choice conditions. All 20 panels across 16 pages now have supplemental table records; not diagrams.
- Page4726: Shaded single-row Warning panels express source choice conditions. All 20 panels across 16 pages now have supplemental table records; not diagrams.
- Page4727: Shaded single-row Warning panels express source choice conditions. All 20 panels across 16 pages now have supplemental table records; not diagrams.
- Page5015: Shaded single-row Warning panels express source choice conditions. All 20 panels across 16 pages now have supplemental table records; not diagrams.
- Page5016: Shaded single-row Warning panels express source choice conditions. All 20 panels across 16 pages now have supplemental table records; not diagrams.
- Page5119: Shaded single-row Warning panels express source choice conditions. All 20 panels across 16 pages now have supplemental table records; not diagrams.
- Page5120: Shaded single-row Warning panels express source choice conditions. All 20 panels across 16 pages now have supplemental table records; not diagrams.
- Page5138: Shaded single-row Warning panels express source choice conditions. All 20 panels across 16 pages now have supplemental table records; not diagrams.

[All 20 additional Warning panels](tables/supplemental/index.md)

## Direct visual checks and limits

Complete rendered pages 4360, 4362, 4368, 4369, 4400, 4401, 4719, 4720, 4722, 4726, 4727, 5015, 5016, 5119, 5120, 5138 were directly inspected for candidate semantics and template layout. Their fingerprints are in [the visual evidence report](../../../../../../../../tracking/reviews/pdf-structural-visual.json). The manually inspected template examples include message lists, nested choice tables, code tables, warning panels, text constraints, publisher branding and legal links. Header/row shading and all table borders are retained in originals. This check does not validate business applicability, resolve conflicting definitions, or certify each table layout and every cell by individual visual reading.
