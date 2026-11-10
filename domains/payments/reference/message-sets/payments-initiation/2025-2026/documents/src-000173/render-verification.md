---
template: false
document_kind: "source-render-coverage"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
limitations: ["Word pagination is additional to stable original paragraph/XML/table locators.", "Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.", "Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.", "Floating/composite objects without unique binary asset hashes require direct page inspection.", "Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.", "No visual-review or reviewed status is conferred by this helper."]
---

# Word render and independent table-text reconciliation

[src-000173](../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx)

[Complete derived Word PDF](../../../../../../../../work/docx-render/src-000173/document.pdf) · [Detailed evidence, unmatched cells and figure-page candidates](../../../../../../../../work/docx-render/src-000173/reconciliation.json)

Renderer: Microsoft Word 16.0 build 16.0.20527. File pages: 69. Original checksum unchanged at render. No visual review is implied.

| Table | Word file pages | Cell-text matches | Result |
| --- | --- | --- | --- |
| T1 | 5–5 | 12/12 | cell-text-reconciled |
| T2 | 5–6 | 40/40 | cell-text-reconciled |
| T3 | 6–8 | 23/24 | unmatched-cell-text-needs-inspection |
| T4 | 8–8 | 6/6 | cell-text-reconciled |
| T5 | 8–8 | 6/6 | cell-text-reconciled |
| T6 | 9–10 | 28/28 | cell-text-reconciled |
| T7 | 10–10 | 8/8 | cell-text-reconciled |
| T8 | 10–11 | 38/38 | cell-text-reconciled |
| T9 | 12–12 | 12/12 | cell-text-reconciled |
| T10 | 12–12 | 12/12 | cell-text-reconciled |
| T11 | 12–13 | 12/12 | cell-text-reconciled |
| T12 | 13–13 | 11/11 | cell-text-reconciled |
| T13 | 13–13 | 12/12 | cell-text-reconciled |
| T14 | 13–13 | 12/12 | cell-text-reconciled |
| T15 | 13–14 | 12/12 | cell-text-reconciled |
| T16 | 14–14 | 12/12 | cell-text-reconciled |
| T17 | 14–15 | 12/12 | cell-text-reconciled |
| T18 | 15–15 | 11/12 | unmatched-cell-text-needs-inspection |
| T19 | 15–16 | 12/12 | cell-text-reconciled |
| T20 | 16–16 | 12/12 | cell-text-reconciled |
| T21 | 16–16 | 12/12 | cell-text-reconciled |
| T22 | 17–17 | 11/11 | cell-text-reconciled |
| T23 | 18–21 | 33/39 | unmatched-cell-text-needs-inspection |
| T24 | 41–45 | 360/360 | cell-text-reconciled |
| T25 | 51–51 | 60/60 | cell-text-reconciled |
| T26 | 52–54 | 142/142 | cell-text-reconciled |
| T27 | 56–58 | 172/172 | cell-text-reconciled |
| T28 | 61–63 | 266/266 | cell-text-reconciled |
| T29 | 69–69 | 15/15 | cell-text-reconciled |


## Limitations

- Word pagination is additional to stable original paragraph/XML/table locators.
- Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.
- Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.
- Floating/composite objects without unique binary asset hashes require direct page inspection.
- Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.
- No visual-review or reviewed status is conferred by this helper.

Derived header errors detected on file pages: 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69. Consult the original source; body/table evidence is evaluated separately.
