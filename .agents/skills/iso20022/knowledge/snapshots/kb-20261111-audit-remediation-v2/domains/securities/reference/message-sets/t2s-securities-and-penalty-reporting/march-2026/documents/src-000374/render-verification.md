---
template: false
document_kind: "source-render-coverage"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_sets: ["t2s-securities-and-penalty-reporting"]
limitations: ["Word pagination is additional to stable original paragraph/XML/table locators.", "Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.", "Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.", "Floating/composite objects without unique binary asset hashes require direct page inspection.", "Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.", "No visual-review or reviewed status is conferred by this helper."]
---

# Word render and independent table-text reconciliation

[src-000374](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`

[Complete derived Word PDF](../../../../../../../../evidence/omitted/8a45aa596f455c02770db95c.md) · [Detailed evidence, unmatched cells and figure-page candidates](../../../../../../../../work/docx-render/src-000374/reconciliation.json)

Renderer: Microsoft Word 16.0 build 16.0.20527. File pages: 71. Original checksum unchanged at render. No visual review is implied.

| Table | Word file pages | Cell-text matches | Result |
| --- | --- | --- | --- |
| T1 | 4–4 | 12/12 | cell-text-reconciled |
| T2 | 4–5 | 34/34 | cell-text-reconciled |
| T3 | 5–6 | 11/11 | cell-text-reconciled |
| T4 | 8–9 | 12/12 | cell-text-reconciled |
| T5 | 15–15 | 6/6 | cell-text-reconciled |
| T6 | 15–15 | 12/12 | cell-text-reconciled |
| T7 | 16–17 | 13/13 | cell-text-reconciled |
| T8 | 17–17 | 12/12 | cell-text-reconciled |
| T9 | 18–18 | 11/11 | cell-text-reconciled |
| T10 | 19–20 | 21/21 | cell-text-reconciled |
| T11 | 21–22 | 23/24 | unmatched-cell-text-needs-inspection |
| T12 | 23–23 | 15/15 | cell-text-reconciled |
| T13 | 71–71 | 20/20 | cell-text-reconciled |


## Limitations

- Word pagination is additional to stable original paragraph/XML/table locators.
- Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.
- Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.
- Floating/composite objects without unique binary asset hashes require direct page inspection.
- Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.
- No visual-review or reviewed status is conferred by this helper.
