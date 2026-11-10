---
template: false
document_kind: "source-render-coverage"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_sets: ["bank-to-customer-cash-management"]
limitations: ["Word pagination is additional to stable original paragraph/XML/table locators.", "Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.", "Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.", "Floating/composite objects without unique binary asset hashes require direct page inspection.", "Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.", "No visual-review or reviewed status is conferred by this helper."]
---

# Word render and independent table-text reconciliation

[src-000004](../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart1_BankToCustomerCashManagement_2025_2026_v2.docx)

[Complete derived Word PDF](../../../../../../../../work/docx-render/src-000004/document.pdf) · [Detailed evidence, unmatched cells and figure-page candidates](../../../../../../../../work/docx-render/src-000004/reconciliation.json)

Renderer: Microsoft Word 16.0 build 16.0.20527. File pages: 41. Original checksum unchanged at render. No visual review is implied.

| Table | Word file pages | Cell-text matches | Result |
| --- | --- | --- | --- |
| T1 | 5–5 | 12/12 | cell-text-reconciled |
| T2 | 5–5 | 12/12 | cell-text-reconciled |
| T3 | 6–7 | 30/30 | cell-text-reconciled |
| T4 | 7–8 | 8/8 | cell-text-reconciled |
| T5 | 8–8 | 4/4 | cell-text-reconciled |
| T6 | 9–10 | 10/10 | cell-text-reconciled |
| T7 | 10–10 | 14/14 | cell-text-reconciled |
| T8 | 10–11 | 15/15 | cell-text-reconciled |
| T9 | 11–11 | 12/12 | cell-text-reconciled |
| T10 | 12–12 | 12/12 | cell-text-reconciled |
| T11 | 12–12 | 12/12 | cell-text-reconciled |
| T12 | 12–12 | 12/12 | cell-text-reconciled |
| T13 | 13–13 | 11/11 | cell-text-reconciled |
| T14 | 13–14 | 39/39 | cell-text-reconciled |
| T15 | 15–16 | 24/24 | cell-text-reconciled |
| T16 | 16–17 | 26/27 | unmatched-cell-text-needs-inspection |
| T17 | 17–18 | 27/27 | cell-text-reconciled |
| T18 | 23–25 | 172/172 | cell-text-reconciled |
| T19 | 28–30 | 268/268 | cell-text-reconciled |
| T20 | 35–36 | 106/106 | cell-text-reconciled |
| T21 | 38–39 | 49/49 | cell-text-reconciled |
| T22 | 41–41 | 15/15 | cell-text-reconciled |


## Limitations

- Word pagination is additional to stable original paragraph/XML/table locators.
- Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.
- Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.
- Floating/composite objects without unique binary asset hashes require direct page inspection.
- Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.
- No visual-review or reviewed status is conferred by this helper.

Derived header errors detected on file pages: 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41. Consult the original source; body/table evidence is evaluated separately.
