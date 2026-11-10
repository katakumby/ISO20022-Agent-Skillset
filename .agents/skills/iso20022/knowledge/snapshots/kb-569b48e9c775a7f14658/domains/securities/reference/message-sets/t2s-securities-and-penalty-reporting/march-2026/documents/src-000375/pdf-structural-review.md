---
template: false
document_kind: "extraction-audit"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
source_locations: [{"source_id": "src-000375", "file_pages": [1, 558]}]
pdf_geometry_reconciliation: "pass-with-scoped-limitations"
pdf_table_text_reconciliation: "pass-with-recorded-character-mapping"
pdf_markdown_cell_preservation: "pass"
pdf_unclassified_painted_objects: 0
visual_review_pages: [489]
updated: "2026-11-09"
limitations: ["Geometric association with a table is not independent semantic review of its contents. All original lexical vector candidates remain available.", "PDFium omits unpainted clipping paths from its painted-object list; unsupported image/form/shading objects and non-axis paths remain unresolved.", "Cell text comparison normalizes only Unicode compatibility and whitespace, preserving case, digits and punctuation. Soft-hyphen control differences remain explicit exceptions.", "Span/null positions preserve missing separate extracted cells; their semantics require original page/table context.", "No claim that each page or each cell has been individually visually inspected. Text-only diagrams and source-level semantic ambiguities are outside this mechanical classification."]
---

# PDF table and painted-object reconciliation

Source: [src-000375](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. All 558 file pages were enumerated, with the registered source checksum verified unchanged. 1067 extracted table candidates contain 38243 physical cells. Their complete Markdown cell matrices match the maintained extraction. Independent PDFium bounded cell text matched 38237 cells after Unicode compatibility/whitespace normalization. 6 remaining comparisons differ only by PDFium U+0002 representing a source hyphen; every exact source/cell locator and both strings remain in the audit. No other cell-text difference or uncertain grid mapping was found.

[Per-page geometry and complete cell/exception index](../../../../../../../../work/documents/src-000375/structural-audit/summary.json) · [Method, limitations and corpus results](../../../../../../../../catalog/pdf-structural-review.md)

## Geometry disposition

| Painted geometry class | Objects |
| --- | --- |
| link-annotation-underline | 2257 |
| margin-rule-template-candidate | 2228 |
| table-associated-axis-line | 89475 |
| table-associated-filled-rectangle | 2713 |
| unclassified-painted-path | 5 |

Painted path association is a structural classification, not an individual visual review of every page. Original lexical vector-candidate inventories remain unchanged; unpainted clipping operators do not create visible diagram content.

| File page | Objects | Disposition | Evidence |
| --- | --- | --- | --- |
| 489 | 5 | table-border-outside-estimated-bbox | [Inspected complete page](../../../../../../../../evidence/omitted/6e86ddd1ddb7be55a0e27377.md) |

- Page489: Five painted lines are the right-hand Datatype column edges in the existing Currency/Ccy XML-attribute table. Source drawing extends about 1.72 points beyond the estimated table rectangle; all cell text is already preserved and independently matched.

## Direct visual checks and limits

Complete rendered pages 489 were directly inspected for candidate semantics and template layout. Their fingerprints are in [the visual evidence report](../../../../../../../../tracking/reviews/pdf-structural-visual.json). The manually inspected template examples include message lists, nested choice tables, code tables, warning panels, text constraints, publisher branding and legal links. Header/row shading and all table borders are retained in originals. This check does not validate business applicability, resolve conflicting definitions, or certify each table layout and every cell by individual visual reading.
