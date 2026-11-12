---
template: false
document_kind: "source-render-coverage"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
limitations: ["Word pagination is additional to stable original paragraph/XML/table locators.", "Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.", "Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.", "Floating/composite objects without unique binary asset hashes require direct page inspection.", "Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.", "No visual-review or reviewed status is conferred by this helper."]
---

# Word render and independent table-text reconciliation

[src-000371](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`

[Complete derived Word PDF](../../../../../../../../evidence/omitted/fb60d3f89e1ecdb542b60017.md) · [Detailed evidence, unmatched cells and figure-page candidates](../../../../../../../../work/docx-render/src-000371/reconciliation.json)

Renderer: Microsoft Word 16.0 build 16.0.20527. File pages: 42. Original checksum unchanged at render. No visual review is implied.

| Table | Word file pages | Cell-text matches | Result |
| --- | --- | --- | --- |
| T1 | 4–4 | 0/12 | unmatched-cell-text-needs-inspection |
| T2 | 4–7 | 71/71 | cell-text-reconciled |
| T3 | 7–8 | 11/11 | cell-text-reconciled |
| T4 | 8–8 | 18/18 | cell-text-reconciled |
| T5 | 11–11 | 6/6 | cell-text-reconciled |
| T6 | 11–12 | 10/12 | unmatched-cell-text-needs-inspection |
| T7 | 12–13 | 15/15 | cell-text-reconciled |
| T8 | 13–13 | 12/12 | cell-text-reconciled |
| T9 | 14–14 | 12/12 | cell-text-reconciled |
| T10 | 14–14 | 12/12 | cell-text-reconciled |
| T11 | 14–15 | 12/12 | cell-text-reconciled |
| T12 | 15–16 | 12/12 | cell-text-reconciled |
| T13 | 16–16 | 11/11 | cell-text-reconciled |
| T14 | 17–18 | 18/18 | cell-text-reconciled |
| T15 | 18–19 | 17/18 | unmatched-cell-text-needs-inspection |
| T16 | 19–20 | 17/18 | unmatched-cell-text-needs-inspection |
| T17 | 20–21 | 15/15 | cell-text-reconciled |
| T18 | 21–22 | 15/15 | cell-text-reconciled |
| T19 | 42–42 | 15/15 | cell-text-reconciled |


## Limitations

- Word pagination is additional to stable original paragraph/XML/table locators.
- Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.
- Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.
- Floating/composite objects without unique binary asset hashes require direct page inspection.
- Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.
- No visual-review or reviewed status is conferred by this helper.

Derived header errors detected on file pages: 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42. Consult the original source; body/table evidence is evaluated separately.
