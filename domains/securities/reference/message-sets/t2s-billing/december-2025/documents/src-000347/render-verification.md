---
template: false
document_kind: "source-render-coverage"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
message_sets: ["t2s-billing"]
limitations: ["Word pagination is additional to stable original paragraph/XML/table locators.", "Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.", "Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.", "Floating/composite objects without unique binary asset hashes require direct page inspection.", "Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.", "No visual-review or reviewed status is conferred by this helper."]
---

# Word render and independent table-text reconciliation

[src-000347](../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`

[Complete derived Word PDF](../../../../../../../../work/docx-render/src-000347/document.pdf) · [Detailed evidence, unmatched cells and figure-page candidates](../../../../../../../../work/docx-render/src-000347/reconciliation.json)

Renderer: Microsoft Word 16.0 build 16.0.20527. File pages: 21. Original checksum unchanged at render. No visual review is implied.

| Table | Word file pages | Cell-text matches | Result |
| --- | --- | --- | --- |
| T1 | 3–3 | 12/12 | cell-text-reconciled |
| T2 | 3–4 | 40/40 | cell-text-reconciled |
| T3 | 4–5 | 11/11 | cell-text-reconciled |
| T4 | 5–5 | 6/6 | cell-text-reconciled |
| T5 | 7–7 | 6/6 | cell-text-reconciled |
| T6 | 7–8 | 14/14 | cell-text-reconciled |
| T7 | 8–9 | 13/13 | cell-text-reconciled |
| T8 | 9–9 | 12/12 | cell-text-reconciled |
| T9 | 10–10 | 11/11 | cell-text-reconciled |
| T10 | 11–12 | 18/18 | cell-text-reconciled |
| T11 | 13–13 | 12/12 | cell-text-reconciled |
| T12 | 21–21 | 30/30 | cell-text-reconciled |


## Limitations

- Word pagination is additional to stable original paragraph/XML/table locators.
- Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.
- Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.
- Floating/composite objects without unique binary asset hashes require direct page inspection.
- Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.
- No visual-review or reviewed status is conferred by this helper.

Derived header errors detected on file pages: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21. Consult the original source; body/table evidence is evaluated separately.
