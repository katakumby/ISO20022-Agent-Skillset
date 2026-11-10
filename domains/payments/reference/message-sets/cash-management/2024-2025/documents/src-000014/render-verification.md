---
template: false
document_kind: "source-render-coverage"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
limitations: ["Word pagination is additional to stable original paragraph/XML/table locators.", "Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.", "Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.", "Floating/composite objects without unique binary asset hashes require direct page inspection.", "Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.", "No visual-review or reviewed status is conferred by this helper."]
---

# Word render and independent table-text reconciliation

[src-000014](../../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx)

[Complete derived Word PDF](../../../../../../../../work/docx-render/src-000014/document.pdf) · [Detailed evidence, unmatched cells and figure-page candidates](../../../../../../../../work/docx-render/src-000014/reconciliation.json)

Renderer: Microsoft Word 16.0 build 16.0.20527. File pages: 38. Original checksum unchanged at render. No visual review is implied.

| Table | Word file pages | Cell-text matches | Result |
| --- | --- | --- | --- |
| T1 | 5–5 | 12/12 | cell-text-reconciled |
| T2 | 5–5 | 4/4 | cell-text-reconciled |
| T3 | 6–7 | 28/28 | cell-text-reconciled |
| T4 | 8–8 | 6/6 | cell-text-reconciled |
| T5 | 8–8 | 10/10 | cell-text-reconciled |
| T6 | 8–8 | 12/12 | cell-text-reconciled |
| T7 | 8–9 | 10/10 | cell-text-reconciled |
| T8 | 9–9 | 16/16 | cell-text-reconciled |
| T9 | 9–9 | 12/12 | cell-text-reconciled |
| T10 | 9–9 | 8/8 | cell-text-reconciled |
| T11 | 9–9 | 12/12 | cell-text-reconciled |
| T12 | 10–10 | 6/6 | cell-text-reconciled |
| T13 | 10–11 | 16/16 | cell-text-reconciled |
| T14 | 11–12 | 19/19 | cell-text-reconciled |
| T15 | 16–17 | 62/62 | cell-text-reconciled |
| T16 | 38–38 | 15/15 | cell-text-reconciled |


## Limitations

- Word pagination is additional to stable original paragraph/XML/table locators.
- Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.
- Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.
- Floating/composite objects without unique binary asset hashes require direct page inspection.
- Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.
- No visual-review or reviewed status is conferred by this helper.

Derived header errors detected on file pages: 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38. Consult the original source; body/table evidence is evaluated separately.
