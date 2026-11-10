---
template: false
document_kind: "source-render-coverage"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000350"]
source_editions: ["august-2026"]
message_sets: ["t2s-cash-account-query-and-report"]
limitations: ["Word pagination is additional to stable original paragraph/XML/table locators.", "Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.", "Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.", "Floating/composite objects without unique binary asset hashes require direct page inspection.", "Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.", "No visual-review or reviewed status is conferred by this helper."]
---

# Word render and independent table-text reconciliation

[src-000350](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart1_Target2Securities_CashAccountQueryAndReport_v2.docx`

[Complete derived Word PDF](../../../../../../../../evidence/omitted/adaca86fb737213e59228349.md) · [Detailed evidence, unmatched cells and figure-page candidates](../../../../../../../../work/docx-render/src-000350/reconciliation.json)

Renderer: Microsoft Word 16.0 build 16.0.20527. File pages: 27. Original checksum unchanged at render. No visual review is implied.

| Table | Word file pages | Cell-text matches | Result |
| --- | --- | --- | --- |
| T1 | 4–4 | 0/12 | unmatched-cell-text-needs-inspection |
| T2 | 4–6 | 98/98 | cell-text-reconciled |
| T3 | 7–8 | 11/11 | cell-text-reconciled |
| T4 | 8–8 | 12/12 | cell-text-reconciled |
| T5 | 10–10 | 6/6 | cell-text-reconciled |
| T6 | 10–11 | 14/14 | cell-text-reconciled |
| T7 | 11–12 | 13/13 | cell-text-reconciled |
| T8 | 12–12 | 12/12 | cell-text-reconciled |
| T9 | 12–13 | 12/12 | cell-text-reconciled |
| T10 | 13–14 | 12/12 | cell-text-reconciled |
| T11 | 14–14 | 11/11 | cell-text-reconciled |
| T12 | 14–15 | 15/15 | cell-text-reconciled |
| T13 | 15–16 | 15/15 | cell-text-reconciled |
| T14 | 16–17 | 15/15 | cell-text-reconciled |
| T15 | 27–27 | 20/20 | cell-text-reconciled |


## Limitations

- Word pagination is additional to stable original paragraph/XML/table locators.
- Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.
- Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.
- Floating/composite objects without unique binary asset hashes require direct page inspection.
- Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.
- No visual-review or reviewed status is conferred by this helper.

Derived header errors detected on file pages: 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27. Consult the original source; body/table evidence is evaluated separately.
