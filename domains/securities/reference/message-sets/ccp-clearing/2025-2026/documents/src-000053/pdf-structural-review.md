---
template: false
document_kind: "extraction-audit"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
source_locations: [{"source_id": "src-000053", "file_pages": [1, 495]}]
pdf_geometry_reconciliation: "pass-with-scoped-limitations"
pdf_table_text_reconciliation: "pass"
pdf_markdown_cell_preservation: "pass"
pdf_unclassified_painted_objects: 0
visual_review_pages: [1, 2, 6, 495]
updated: "2026-11-09"
limitations: ["Geometric association with a table is not independent semantic review of its contents. All original lexical vector candidates remain available.", "PDFium omits unpainted clipping paths from its painted-object list; unsupported image/form/shading objects and non-axis paths remain unresolved.", "Cell text comparison normalizes only Unicode compatibility and whitespace, preserving case, digits and punctuation. Soft-hyphen control differences remain explicit exceptions.", "Span/null positions preserve missing separate extracted cells; their semantics require original page/table context.", "No claim that each page or each cell has been individually visually inspected. Text-only diagrams and source-level semantic ambiguities are outside this mechanical classification."]
---

# PDF table and painted-object reconciliation

Source: [src-000053](../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). All 495 file pages were enumerated, with the registered source checksum verified unchanged. 773 extracted table candidates contain 31176 physical cells. Their complete Markdown cell matrices match the maintained extraction. Independent PDFium bounded cell text matched 31176 cells after Unicode compatibility/whitespace normalization. 0 remaining comparisons differ only by PDFium U+0002 representing a source hyphen; every exact source/cell locator and both strings remain in the audit. No other cell-text difference or uncertain grid mapping was found.

[Per-page geometry and complete cell/exception index](../../../../../../../../work/documents/src-000053/structural-audit/summary.json) · [Method, limitations and corpus results](../../../../../../../../catalog/pdf-structural-review.md)

## Geometry disposition

| Painted geometry class | Objects |
| --- | --- |
| link-annotation-underline | 2111 |
| margin-rule-template-candidate | 1976 |
| table-associated-axis-line | 72086 |
| table-associated-filled-rectangle | 2163 |
| unclassified-painted-path | 8 |

Painted path association is a structural classification, not an individual visual review of every page. Original lexical vector-candidate inventories remain unchanged; unpainted clipping operators do not create visible diagram content.

| File page | Objects | Disposition | Evidence |
| --- | --- | --- | --- |
| 1 | 7 | excluded-decorative | [Inspected complete page](../../../../../../assets/src-000053/structural-audit/page-00001.png) |
| 495 | 1 | text-link-underline | [Inspected complete page](../../../../../../assets/src-000053/structural-audit/page-00495.png) |

- Page1: Seven painted objects form the Swift publisher logo at upper left. Direct full-page inspection confirms branding, without a business entity/process/model.
- Page495: One horizontal line under www.swift.com in Legal Notices. It conveys no diagram relationship.

## Direct visual checks and limits

Complete rendered pages 1, 2, 6, 495 were directly inspected for candidate semantics and template layout. Their fingerprints are in [the visual evidence report](../../../../../../../../tracking/reviews/pdf-structural-visual.json). The manually inspected template examples include message lists, nested choice tables, code tables, warning panels, text constraints, publisher branding and legal links. Header/row shading and all table borders are retained in originals. This check does not validate business applicability, resolve conflicting definitions, or certify each table layout and every cell by individual visual reading.
