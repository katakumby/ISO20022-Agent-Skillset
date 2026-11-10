---
template: false
document_kind: "source-render-coverage"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000356"]
source_editions: ["march-2024"]
message_sets: ["t2s-collateral-reporting"]
limitations: ["Word pagination is additional to stable original paragraph/XML/table locators.", "Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.", "Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.", "Floating/composite objects without unique binary asset hashes require direct page inspection.", "Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.", "No visual-review or reviewed status is conferred by this helper."]
---

# Word render and independent table-text reconciliation

[src-000356](../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralReporting_2023_2024_v2.docx`

[Complete derived Word PDF](../../../../../../../../work/docx-render/src-000356/document.pdf) · [Detailed evidence, unmatched cells and figure-page candidates](../../../../../../../../work/docx-render/src-000356/reconciliation.json)

Renderer: Microsoft Word 16.0 build 16.0.20527. File pages: 19. Original checksum unchanged at render. No visual review is implied.

| Table | Word file pages | Cell-text matches | Result |
| --- | --- | --- | --- |
| T1 | 5–5 | 12/12 | cell-text-reconciled |
| T2 | 5–6 | 36/36 | cell-text-reconciled |
| T3 | 6–7 | 15/15 | cell-text-reconciled |
| T4 | 7–7 | 6/6 | cell-text-reconciled |
| T5 | 10–10 | 6/6 | cell-text-reconciled |
| T6 | 10–11 | 22/22 | cell-text-reconciled |
| T7 | 11–12 | 18/18 | cell-text-reconciled |
| T8 | 15–15 | 11/11 | cell-text-reconciled |
| T9 | 16–16 | 11/12 | unmatched-cell-text-needs-inspection |
| T10 | 19–19 | 15/15 | cell-text-reconciled |


## Limitations

- Word pagination is additional to stable original paragraph/XML/table locators.
- Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.
- Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.
- Floating/composite objects without unique binary asset hashes require direct page inspection.
- Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.
- No visual-review or reviewed status is conferred by this helper.

Derived header errors detected on file pages: 10, 11, 12, 13, 14, 15, 16, 17, 18, 19. Consult the original source; body/table evidence is evaluated separately.
