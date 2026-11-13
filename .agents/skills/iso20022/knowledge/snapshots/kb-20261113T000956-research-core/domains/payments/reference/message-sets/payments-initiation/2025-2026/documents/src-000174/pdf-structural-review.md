---
template: false
document_kind: "extraction-audit"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
source_locations: [{"source_id": "src-000174", "file_pages": [1, 610]}]
pdf_geometry_reconciliation: "pass-with-scoped-limitations"
pdf_table_text_reconciliation: "pass"
pdf_markdown_cell_preservation: "pass"
pdf_unclassified_painted_objects: 0
visual_review_pages: []
updated: "2026-11-09"
limitations: ["Geometric association with a table is not independent semantic review of its contents. All original lexical vector candidates remain available.", "PDFium omits unpainted clipping paths from its painted-object list; unsupported image/form/shading objects and non-axis paths remain unresolved.", "Cell text comparison normalizes only Unicode compatibility and whitespace, preserving case, digits and punctuation. Soft-hyphen control differences remain explicit exceptions.", "Span/null positions preserve missing separate extracted cells; their semantics require original page/table context.", "No claim that each page or each cell has been individually visually inspected. Text-only diagrams and source-level semantic ambiguities are outside this mechanical classification."]
---

# PDF table and painted-object reconciliation

Source: [src-000174](../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). All 610 file pages were enumerated, with the registered source checksum verified unchanged. 742 extracted table candidates contain 55216 physical cells. Their complete Markdown cell matrices match the maintained extraction. Independent PDFium bounded cell text matched 55216 cells after Unicode compatibility/whitespace normalization. 0 remaining comparisons differ only by PDFium U+0002 representing a source hyphen; every exact source/cell locator and both strings remain in the audit. No other cell-text difference or uncertain grid mapping was found.

[Per-page geometry and complete cell/exception index](../../../../../../../../evidence/archived/5a7118d25feb185e21a925b6.md) · [Method, limitations and corpus results](../../../../../../../../catalog/pdf-structural-review.md)

## Geometry disposition

| Painted geometry class | Objects |
| --- | --- |
| link-annotation-underline | 2150 |
| margin-rule-template-candidate | 2436 |
| table-associated-axis-line | 124102 |
| table-associated-filled-rectangle | 3347 |

Painted path association is a structural classification, not an individual visual review of every page. Original lexical vector-candidate inventories remain unchanged; unpainted clipping operators do not create visible diagram content.

No painted object remained outside the table-border/fill, link-underline and narrow page-rule templates. This does not assert absence of text-only diagrams or complete business-semantic review.

## Direct visual checks and limits

No page of this publication is claimed as individually visually inspected by this particular audit. The bounded painted geometry and independent cell-text checks cover all its pages, using the separately documented repeated-template rules. The manually inspected template examples include message lists, nested choice tables, code tables, warning panels, text constraints, publisher branding and legal links. Header/row shading and all table borders are retained in originals. This check does not validate business applicability, resolve conflicting definitions, or certify each table layout and every cell by individual visual reading.
