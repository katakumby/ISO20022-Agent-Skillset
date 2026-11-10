---
template: false
document_kind: "source-render-coverage"
review_status: "needs-review"
domain: "shared"
source_ids: ["src-000343"]
source_editions: ["march-2024"]
message_sets: ["t2s-administration"]
limitations: ["Word pagination is additional to stable original paragraph/XML/table locators.", "Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.", "Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.", "Floating/composite objects without unique binary asset hashes require direct page inspection.", "Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.", "No visual-review or reviewed status is conferred by this helper."]
---

# Word render and independent table-text reconciliation

[src-000343](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart1_Target2Securities_Administration_2023_2024_v2.docx`

[Complete derived Word PDF](../../../../../../../evidence/omitted/4d52f316c491dd80a51c400d.md) · [Detailed evidence, unmatched cells and figure-page candidates](../../../../../../../work/docx-render/src-000343/reconciliation.json)

Renderer: Microsoft Word 16.0 build 16.0.20527. File pages: 37. Original checksum unchanged at render. No visual review is implied.

| Table | Word file pages | Cell-text matches | Result |
| --- | --- | --- | --- |
| T1 | 5–5 | 12/12 | cell-text-reconciled |
| T2 | 5–6 | 36/36 | cell-text-reconciled |
| T3 | 6–7 | 15/15 | cell-text-reconciled |
| T4 | 7–7 | 8/8 | cell-text-reconciled |
| T5 | 11–11 | 6/6 | cell-text-reconciled |
| T6 | 11–12 | 21/22 | unmatched-cell-text-needs-inspection |
| T7 | 12–13 | 18/18 | cell-text-reconciled |
| T8 | 15–15 | 12/12 | cell-text-reconciled |
| T9 | 17–17 | 12/12 | cell-text-reconciled |
| T10 | 20–20 | 12/12 | cell-text-reconciled |
| T11 | 21–21 | 11/11 | cell-text-reconciled |
| T12 | 22–23 | 11/12 | unmatched-cell-text-needs-inspection |
| T13 | 24–25 | 11/12 | unmatched-cell-text-needs-inspection |
| T14 | 26–27 | 8/9 | unmatched-cell-text-needs-inspection |
| T15 | 28–28 | 9/9 | cell-text-reconciled |
| T16 | 37–37 | 15/15 | cell-text-reconciled |


## Limitations

- Word pagination is additional to stable original paragraph/XML/table locators.
- Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.
- Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.
- Floating/composite objects without unique binary asset hashes require direct page inspection.
- Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.
- No visual-review or reviewed status is conferred by this helper.

Derived header errors detected on file pages: 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37. Consult the original source; body/table evidence is evaluated separately.
