---
template: false
document_kind: "source-render-coverage"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_sets: ["t2s-link-reference-data"]
limitations: ["Word pagination is additional to stable original paragraph/XML/table locators.", "Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.", "Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.", "Floating/composite objects without unique binary asset hashes require direct page inspection.", "Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.", "No visual-review or reviewed status is conferred by this helper."]
---

# Word render and independent table-text reconciliation

[src-000365](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`

[Complete derived Word PDF](../../../../../../../../evidence/omitted/79242b7eb76617e8393527d0.md) · [Detailed evidence, unmatched cells and figure-page candidates](../../../../../../../../evidence/archived/9b40569224f492706bab639e.md)

Renderer: Microsoft Word 16.0 build 16.0.20527. File pages: 34. Original checksum unchanged at render. No visual review is implied.

| Table | Word file pages | Cell-text matches | Result |
| --- | --- | --- | --- |
| T1 | 5–5 | 12/12 | cell-text-reconciled |
| T2 | 5–6 | 34/34 | cell-text-reconciled |
| T3 | 6–7 | 11/11 | cell-text-reconciled |
| T4 | 7–7 | 14/14 | cell-text-reconciled |
| T5 | 10–10 | 6/6 | cell-text-reconciled |
| T6 | 10–11 | 14/14 | cell-text-reconciled |
| T7 | 11–12 | 17/17 | cell-text-reconciled |
| T8 | 12–12 | 12/12 | cell-text-reconciled |
| T9 | 13–13 | 12/12 | cell-text-reconciled |
| T10 | 14–14 | 11/11 | cell-text-reconciled |
| T11 | 15–15 | 18/18 | cell-text-reconciled |
| T12 | 16–17 | 18/18 | cell-text-reconciled |
| T13 | 33–33 | 40/40 | cell-text-reconciled |


## Limitations

- Word pagination is additional to stable original paragraph/XML/table locators.
- Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.
- Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.
- Floating/composite objects without unique binary asset hashes require direct page inspection.
- Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.
- No visual-review or reviewed status is conferred by this helper.

Derived header errors detected on file pages: 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34. Consult the original source; body/table evidence is evaluated separately.
