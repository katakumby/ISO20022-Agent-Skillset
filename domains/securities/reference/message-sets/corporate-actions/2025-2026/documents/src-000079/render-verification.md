---
template: false
document_kind: "source-render-coverage"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
limitations: ["Word pagination is additional to stable original paragraph/XML/table locators.", "Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.", "Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.", "Floating/composite objects without unique binary asset hashes require direct page inspection.", "Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.", "No visual-review or reviewed status is conferred by this helper."]
---

# Word render and independent table-text reconciliation

[src-000079](../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx)

[Complete derived Word PDF](../../../../../../../../work/docx-render/src-000079/document.pdf) · [Detailed evidence, unmatched cells and figure-page candidates](../../../../../../../../work/docx-render/src-000079/reconciliation.json)

Renderer: Microsoft Word 16.0 build 16.0.20527. File pages: 115. Original checksum unchanged at render. No visual review is implied.

| Table | Word file pages | Cell-text matches | Result |
| --- | --- | --- | --- |
| T1 | 5–5 | 12/12 | cell-text-reconciled |
| T2 | 5–5 | 10/10 | cell-text-reconciled |
| T3 | 6–6 | 14/14 | cell-text-reconciled |
| T4 | 9–9 | 12/12 | cell-text-reconciled |
| T5 | 9–9 | 18/18 | cell-text-reconciled |
| T6 | 9–9 | 9/9 | cell-text-reconciled |
| T7 | 9–9 | 12/12 | cell-text-reconciled |
| T8 | 10–11 | 6/6 | cell-text-reconciled |
| T9 | 11–11 | 24/24 | cell-text-reconciled |
| T10 | 11–12 | 30/30 | cell-text-reconciled |
| T11 | 13–14 | 11/12 | unmatched-cell-text-needs-inspection |
| T12 | 14–14 | 10/12 | unmatched-cell-text-needs-inspection |
| T13 | 14–14 | 12/12 | cell-text-reconciled |
| T14 | 14–15 | 11/12 | unmatched-cell-text-needs-inspection |
| T15 | 15–15 | 12/12 | cell-text-reconciled |
| T16 | 15–15 | 12/12 | cell-text-reconciled |
| T17 | 15–16 | 10/12 | unmatched-cell-text-needs-inspection |
| T18 | 16–16 | 12/12 | cell-text-reconciled |
| T19 | 16–16 | 11/12 | unmatched-cell-text-needs-inspection |
| T20 | 17–17 | 11/11 | cell-text-reconciled |
| T21 | 22–23 | 30/30 | cell-text-reconciled |
| T22 | 23–24 | 26/27 | unmatched-cell-text-needs-inspection |
| T23 | 24–25 | 14/15 | unmatched-cell-text-needs-inspection |
| T24 | 25–25 | 9/9 | cell-text-reconciled |
| T25 | 26–26 | 9/9 | cell-text-reconciled |
| T26 | 26–27 | 9/9 | cell-text-reconciled |
| T27 | 27–27 | 9/9 | cell-text-reconciled |
| T28 | 28–28 | 9/9 | cell-text-reconciled |
| T29 | 43–44 | 48/48 | cell-text-reconciled |
| T30 | 115–115 | 15/15 | cell-text-reconciled |


## Limitations

- Word pagination is additional to stable original paragraph/XML/table locators.
- Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.
- Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.
- Floating/composite objects without unique binary asset hashes require direct page inspection.
- Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.
- No visual-review or reviewed status is conferred by this helper.

Derived header errors detected on file pages: 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114. Consult the original source; body/table evidence is evaluated separately.
