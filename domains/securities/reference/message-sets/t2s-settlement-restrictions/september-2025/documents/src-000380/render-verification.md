---
template: false
document_kind: "source-render-coverage"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_sets: ["t2s-settlement-restrictions"]
limitations: ["Word pagination is additional to stable original paragraph/XML/table locators.", "Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.", "Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.", "Floating/composite objects without unique binary asset hashes require direct page inspection.", "Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.", "No visual-review or reviewed status is conferred by this helper."]
---

# Word render and independent table-text reconciliation

[src-000380](../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`

[Complete derived Word PDF](../../../../../../../../work/docx-render/src-000380/document.pdf) · [Detailed evidence, unmatched cells and figure-page candidates](../../../../../../../../work/docx-render/src-000380/reconciliation.json)

Renderer: Microsoft Word 16.0 build 16.0.20527. File pages: 49. Original checksum unchanged at render. No visual review is implied.

| Table | Word file pages | Cell-text matches | Result |
| --- | --- | --- | --- |
| T1 | 4–4 | 12/12 | cell-text-reconciled |
| T2 | 4–5 | 34/34 | cell-text-reconciled |
| T3 | 5–6 | 11/11 | cell-text-reconciled |
| T4 | 8–8 | 16/16 | cell-text-reconciled |
| T5 | 14–14 | 6/6 | cell-text-reconciled |
| T6 | 14–14 | 12/12 | cell-text-reconciled |
| T7 | 15–16 | 13/13 | cell-text-reconciled |
| T8 | 16–16 | 12/12 | cell-text-reconciled |
| T9 | 17–17 | 11/11 | cell-text-reconciled |
| T10 | 18–18 | 24/24 | cell-text-reconciled |
| T11 | 19–20 | 21/21 | cell-text-reconciled |
| T12 | 21–21 | 24/24 | cell-text-reconciled |
| T13 | 22–23 | 21/21 | cell-text-reconciled |
| T14 | 49–49 | 25/25 | cell-text-reconciled |


## Limitations

- Word pagination is additional to stable original paragraph/XML/table locators.
- Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.
- Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.
- Floating/composite objects without unique binary asset hashes require direct page inspection.
- Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.
- No visual-review or reviewed status is conferred by this helper.
