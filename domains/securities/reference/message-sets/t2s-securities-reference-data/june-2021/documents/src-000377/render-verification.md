---
template: false
document_kind: "source-render-coverage"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_sets: ["t2s-securities-reference-data"]
limitations: ["Word pagination is additional to stable original paragraph/XML/table locators.", "Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.", "Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.", "Floating/composite objects without unique binary asset hashes require direct page inspection.", "Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.", "No visual-review or reviewed status is conferred by this helper."]
---

# Word render and independent table-text reconciliation

[src-000377](../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`

[Complete derived Word PDF](../../../../../../../../work/docx-render/src-000377/document.pdf) · [Detailed evidence, unmatched cells and figure-page candidates](../../../../../../../../work/docx-render/src-000377/reconciliation.json)

Renderer: Microsoft Word 16.0 build 16.0.20527. File pages: 48. Original checksum unchanged at render. No visual review is implied.

| Table | Word file pages | Cell-text matches | Result |
| --- | --- | --- | --- |
| T1 | 5–5 | 12/12 | cell-text-reconciled |
| T2 | 5–6 | 36/36 | cell-text-reconciled |
| T3 | 6–8 | 11/12 | unmatched-cell-text-needs-inspection |
| T4 | 8–8 | 24/24 | cell-text-reconciled |
| T5 | 11–11 | 6/6 | cell-text-reconciled |
| T6 | 11–12 | 9/10 | unmatched-cell-text-needs-inspection |
| T7 | 12–13 | 11/11 | cell-text-reconciled |
| T8 | 13–13 | 12/12 | cell-text-reconciled |
| T9 | 13–14 | 11/12 | unmatched-cell-text-needs-inspection |
| T10 | 14–14 | 12/12 | cell-text-reconciled |
| T11 | 14–14 | 12/12 | cell-text-reconciled |
| T12 | 14–15 | 12/12 | cell-text-reconciled |
| T13 | 15–15 | 11/11 | cell-text-reconciled |
| T14 | 16–17 | 18/18 | cell-text-reconciled |
| T15 | 17–18 | 17/18 | unmatched-cell-text-needs-inspection |
| T16 | 18–19 | 17/18 | unmatched-cell-text-needs-inspection |
| T17 | 20–20 | 15/15 | cell-text-reconciled |
| T18 | 20–21 | 15/15 | cell-text-reconciled |
| T19 | 48–48 | 15/15 | cell-text-reconciled |


## Limitations

- Word pagination is additional to stable original paragraph/XML/table locators.
- Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.
- Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.
- Floating/composite objects without unique binary asset hashes require direct page inspection.
- Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.
- No visual-review or reviewed status is conferred by this helper.

Derived header errors detected on file pages: 48. Consult the original source; body/table evidence is evaluated separately.
