---
template: false
document_kind: "source-render-coverage"
review_status: "needs-review"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_sets: ["external-code-sets"]
limitations: ["Word pagination is additional to stable original paragraph/XML/table locators.", "Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.", "Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.", "Floating/composite objects without unique binary asset hashes require direct page inspection.", "Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.", "No visual-review or reviewed status is conferred by this helper."]
---

# Word render and independent table-text reconciliation

[src-000003](../../../../../../../evidence/omitted/1dcbe16191b6c8898a146b17.md)

[Complete derived Word PDF](../../../../../../../evidence/omitted/44b6a63e1a64d2360dfb99ba.md) · [Detailed evidence, unmatched cells and figure-page candidates](../../../../../../../evidence/archived/ba0ff81ebc4f2144797970cb.md)

Renderer: Microsoft Word 16.0 build 16.0.20527. File pages: 91. Original checksum unchanged at render. No visual review is implied.

| Table | Word file pages | Cell-text matches | Result |
| --- | --- | --- | --- |
| T1 | 6–6 | 7/8 | unmatched-cell-text-needs-inspection |
| T2 | 7–7 | 56/56 | cell-text-reconciled |
| T3 | 11–12 | 25/25 | cell-text-reconciled |
| T4 | 13–13 | 11/11 | cell-text-reconciled |
| T5 | 14–15 | 41/41 | cell-text-reconciled |
| T6 | 15–16 | 13/13 | cell-text-reconciled |
| T7 | 16–17 | 25/25 | cell-text-reconciled |
| T8 | 17–18 | 23/23 | cell-text-reconciled |
| T9 | 18–19 | 19/19 | cell-text-reconciled |
| T10 | 19–19 | 17/17 | cell-text-reconciled |
| T11 | 19–20 | 17/17 | cell-text-reconciled |
| T12 | 20–21 | 19/19 | cell-text-reconciled |
| T13 | 21–21 | 29/29 | cell-text-reconciled |
| T14 | 22–22 | 15/15 | cell-text-reconciled |
| T15 | 22–22 | 3/3 | cell-text-reconciled |
| T16 | 23–23 | 27/27 | cell-text-reconciled |
| T17 | 25–26 | 55/55 | cell-text-reconciled |
| T18 | 27–27 | 17/17 | cell-text-reconciled |
| T19 | 27–28 | 27/27 | cell-text-reconciled |
| T20 | 29–30 | 41/41 | cell-text-reconciled |
| T21 | 30–31 | 19/19 | cell-text-reconciled |
| T22 | 31–31 | 13/13 | cell-text-reconciled |
| T23 | 31–32 | 27/27 | cell-text-reconciled |
| T24 | 32–32 | 11/11 | cell-text-reconciled |
| T25 | 33–33 | 15/15 | cell-text-reconciled |
| T26 | 34–34 | 7/7 | cell-text-reconciled |
| T27 | 34–36 | 55/55 | cell-text-reconciled |
| T28 | 37–37 | 7/7 | cell-text-reconciled |
| T29 | 38–38 | 17/17 | cell-text-reconciled |
| T30 | 39–40 | 7/7 | cell-text-reconciled |
| T31 | 40–40 | 15/15 | cell-text-reconciled |
| T32 | 41–42 | 11/11 | cell-text-reconciled |
| T33 | 42–42 | 9/9 | cell-text-reconciled |
| T34 | 43–44 | 15/15 | cell-text-reconciled |
| T35 | 44–44 | 9/9 | cell-text-reconciled |
| T36 | 44–44 | 7/7 | cell-text-reconciled |
| T37 | 46–48 | 79/79 | cell-text-reconciled |
| T38 | 49–49 | 17/17 | cell-text-reconciled |
| T39 | 49–50 | 44/44 | cell-text-reconciled |
| T40 | 51–53 | 67/67 | cell-text-reconciled |
| T41 | 54–55 | 51/51 | cell-text-reconciled |
| T42 | 56–56 | 11/11 | cell-text-reconciled |
| T43 | 57–57 | 19/19 | cell-text-reconciled |
| T44 | 62–62 | 49/49 | cell-text-reconciled |
| T45 | 62–66 | 433/433 | cell-text-reconciled |
| T46 | 67–68 | 118/118 | cell-text-reconciled |
| T47 | 68–68 | 59/59 | cell-text-reconciled |
| T48 | 69–78 | 1045/1045 | cell-text-reconciled |
| T49 | 79–79 | 60/60 | cell-text-reconciled |
| T50 | 80–80 | 51/52 | unmatched-cell-text-needs-inspection |
| T51 | 81–81 | 52/52 | cell-text-reconciled |
| T52 | 82–82 | 77/77 | cell-text-reconciled |
| T53 | 83–88 | 608/608 | cell-text-reconciled |
| T54 | 89–89 | 68/68 | cell-text-reconciled |
| T55 | 90–91 | 79/80 | unmatched-cell-text-needs-inspection |


## Limitations

- Word pagination is additional to stable original paragraph/XML/table locators.
- Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.
- Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.
- Floating/composite objects without unique binary asset hashes require direct page inspection.
- Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.
- No visual-review or reviewed status is conferred by this helper.
