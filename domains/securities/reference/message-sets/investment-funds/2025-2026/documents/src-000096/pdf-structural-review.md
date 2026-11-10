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

Source: [src-000096](../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). All 5406 file pages were enumerated, with the registered source checksum verified unchanged. 8434 extracted table candidates contain 455224 physical cells. Their complete Markdown cell matrices match the maintained extraction. Independent PDFium bounded cell text matched 455059 cells after Unicode compatibility/whitespace normalization. 165 remaining comparisons differ only by PDFium U+0002 representing a source hyphen; every exact source/cell locator and both strings remain in the audit. No other cell-text difference or uncertain grid mapping was found.

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
| 4360 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../assets/src-000096/structural-audit/page-04360.png) |
| 4362 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../assets/src-000096/structural-audit/page-04362.png) |
| 4368 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../assets/src-000096/structural-audit/page-04368.png) |
| 4369 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../assets/src-000096/structural-audit/page-04369.png) |
| 4400 | 6 | substantive-warning-panels | [Inspected complete page](../../../../../../assets/src-000096/structural-audit/page-04400.png) |
| 4401 | 6 | substantive-warning-panels | [Inspected complete page](../../../../../../assets/src-000096/structural-audit/page-04401.png) |
| 4719 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../assets/src-000096/structural-audit/page-04719.png) |
| 4720 | 6 | substantive-warning-panels | [Inspected complete page](../../../../../../assets/src-000096/structural-audit/page-04720.png) |
| 4722 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../assets/src-000096/structural-audit/page-04722.png) |
| 4726 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../assets/src-000096/structural-audit/page-04726.png) |
| 4727 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../assets/src-000096/structural-audit/page-04727.png) |
| 5015 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../assets/src-000096/structural-audit/page-05015.png) |
| 5016 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../assets/src-000096/structural-audit/page-05016.png) |
| 5119 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../assets/src-000096/structural-audit/page-05119.png) |
| 5120 | 3 | substantive-warning-panels | [Inspected complete page](../../../../../../assets/src-000096/structural-audit/page-05120.png) |
| 5138 | 6 | substantive-warning-panels | [Inspected complete page](../../../../../../assets/src-000096/structural-audit/page-05138.png) |

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
