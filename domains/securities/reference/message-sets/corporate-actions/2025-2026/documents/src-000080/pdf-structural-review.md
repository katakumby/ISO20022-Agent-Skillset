---
template: false
document_kind: "extraction-audit"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
source_locations: [{"source_id": "src-000080", "file_pages": [1, 1252]}]
pdf_geometry_reconciliation: "pass-with-scoped-limitations"
pdf_table_text_reconciliation: "pass-with-recorded-character-mapping"
pdf_markdown_cell_preservation: "pass"
pdf_unclassified_painted_objects: 0
visual_review_pages: []
updated: "2026-11-09"
limitations: ["Geometric association with a table is not independent semantic review of its contents. All original lexical vector candidates remain available.", "PDFium omits unpainted clipping paths from its painted-object list; unsupported image/form/shading objects and non-axis paths remain unresolved.", "Cell text comparison normalizes only Unicode compatibility and whitespace, preserving case, digits and punctuation. Soft-hyphen control differences remain explicit exceptions.", "Span/null positions preserve missing separate extracted cells; their semantics require original page/table context.", "No claim that each page or each cell has been individually visually inspected. Text-only diagrams and source-level semantic ambiguities are outside this mechanical classification."]
---

# PDF table and painted-object reconciliation

Source: [src-000080](../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). All 1252 file pages were enumerated, with the registered source checksum verified unchanged. 2277 extracted table candidates contain 80810 physical cells. Their complete Markdown cell matrices match the maintained extraction. Independent PDFium bounded cell text matched 80798 cells after Unicode compatibility/whitespace normalization. 12 remaining comparisons differ only by PDFium U+0002 representing a source hyphen; every exact source/cell locator and both strings remain in the audit. No other cell-text difference or uncertain grid mapping was found.

[Per-page geometry and complete cell/exception index](../../../../../../../../work/documents/src-000080/structural-audit/summary.json) · [Method, limitations and corpus results](../../../../../../../../catalog/pdf-structural-review.md)

## Geometry disposition

| Painted geometry class | Objects |
| --- | --- |
| link-annotation-underline | 5577 |
| margin-rule-template-candidate | 5004 |
| table-associated-axis-line | 188710 |
| table-associated-filled-rectangle | 5788 |

Painted path association is a structural classification, not an individual visual review of every page. Original lexical vector-candidate inventories remain unchanged; unpainted clipping operators do not create visible diagram content.

No painted object remained outside the table-border/fill, link-underline and narrow page-rule templates. This does not assert absence of text-only diagrams or complete business-semantic review.

## Direct visual checks and limits

No page of this publication is claimed as individually visually inspected by this particular audit. The bounded painted geometry and independent cell-text checks cover all its pages, using the separately documented repeated-template rules. The manually inspected template examples include message lists, nested choice tables, code tables, warning panels, text constraints, publisher branding and legal links. Header/row shading and all table borders are retained in originals. This check does not validate business applicability, resolve conflicting definitions, or certify each table layout and every cell by individual visual reading.
