---
template: false
document_kind: "source-render-coverage"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
limitations: ["Word pagination is additional to stable original paragraph/XML/table locators.", "Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.", "Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.", "Floating/composite objects without unique binary asset hashes require direct page inspection.", "Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.", "No visual-review or reviewed status is conferred by this helper."]
---

# Word render and independent table-text reconciliation

[src-000052](../../../../../../../../evidence/omitted/b45c53bac2be08dee677b607.md)

[Complete derived Word PDF](../../../../../../../../evidence/omitted/232fd202429b183fea1110fb.md) · [Detailed evidence, unmatched cells and figure-page candidates](../../../../../../../../evidence/archived/7db7c1ba9601b81c9bd98b6f.md)

Renderer: Microsoft Word 16.0 build 16.0.20527. File pages: 31. Original checksum unchanged at render. No visual review is implied.

| Table | Word file pages | Cell-text matches | Result |
| --- | --- | --- | --- |
| T1 | 5–5 | 12/12 | cell-text-reconciled |
| T2 | 5–6 | 34/34 | cell-text-reconciled |
| T3 | 6–7 | 13/13 | cell-text-reconciled |
| T4 | 8–8 | 8/8 | cell-text-reconciled |
| T5 | 8–8 | 4/4 | cell-text-reconciled |
| T6 | 8–8 | 4/4 | cell-text-reconciled |
| T7 | 8–9 | 4/4 | cell-text-reconciled |
| T8 | 9–9 | 8/8 | cell-text-reconciled |
| T9 | 9–9 | 4/4 | cell-text-reconciled |
| T10 | 10–10 | 17/17 | cell-text-reconciled |
| T11 | 10–12 | 12/12 | cell-text-reconciled |
| T12 | 16–17 | 6/7 | unmatched-cell-text-needs-inspection |
| T13 | 17–18 | 7/7 | cell-text-reconciled |
| T14 | 18–20 | 14/17 | unmatched-cell-text-needs-inspection |
| T15 | 20–22 | 7/8 | unmatched-cell-text-needs-inspection |
| T16 | 22–24 | 13/13 | cell-text-reconciled |
| T17 | 24–25 | 11/13 | unmatched-cell-text-needs-inspection |
| T18 | 31–31 | 14/14 | cell-text-reconciled |


## Limitations

- Word pagination is additional to stable original paragraph/XML/table locators.
- Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.
- Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.
- Floating/composite objects without unique binary asset hashes require direct page inspection.
- Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.
- No visual-review or reviewed status is conferred by this helper.

Derived header errors detected on file pages: 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31. Consult the original source; body/table evidence is evaluated separately.
