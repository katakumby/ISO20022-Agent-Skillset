---
template: false
document_kind: "extraction-audit"
review_status: "needs-review"
source_ids: ["src-000005", "src-000015", "src-000053", "src-000080", "src-000096", "src-000163", "src-000174", "src-000181", "src-000197", "src-000233", "src-000321", "src-000344", "src-000346", "src-000351", "src-000354", "src-000357", "src-000360", "src-000363", "src-000366", "src-000369", "src-000372", "src-000375", "src-000378", "src-000381"]
updated: "2026-11-09"
---

# Part2 PDF structural reconciliation

All 24 Part2 publications, 20,396 pages and 32,667 grid-table candidates were checked. All 1,574,592 physical cell texts have independent bounded extraction checks: 1,574,312 exact normalized matches and 280 explicit PDFium discretionary-hyphen encoding differences, with no other differences. All maintained Markdown cell matrices match. The 88 residual painted objects on 22 pages were directly inspected; 20 additional substantive Warning panels were preserved as focused table pages. No residual painted diagram candidate remains unclassified.

[Actual visual evidence and object dispositions](../evidence/archived/83d378ffe49d6ff696b2a7e3.md) · [Machine-readable result](../evidence/archived/a1542bba09de01477c1b842a.md) · [Mechanical source summaries](../evidence/archived/0981dc9ec6d5312c4747edc0.md)

## Method and limits

PDFium enumerates actual painted paths, text, images and forms, distinguishing visible content from lexical clipping operators. Narrow page rules, axis-aligned table borders/fills and actual link-annotation underlines are classified against exact page geometry. Every remaining object is retained with its ordinal, bounding box, path segments and source checksum; manual dispositions never erase that record. Table-cell coordinates provide independent bounded PDFium text comparison against the first extractor. Only whitespace and Unicode compatibility are normalized; case, punctuation and digits remain significant. The 280 U+0002/hyphen exceptions retain both strings and exact cells. The full src-000381 file page 4 directly confirms the printed hyphen convention.

Direct visual inspection covers 29 named full pages, including every residual object and repeated-table examples. This does not claim that all 20,396 pages or all cells were individually visually reread. Geometric association with a table does not settle semantic correctness, source contradictions or exact-version applicability. Text-only diagram completeness is outside this painted-geometry check. Original lexical vector inventories remain unchanged and traceable. The 3 header PDFs have separate curated review evidence and are outside this 24-publication audit.

| Source | Pages | Grid tables | Physical cells | Hyphen differences | Evidence |
| --- | --- | --- | --- | --- | --- |
| src-000005 | 919 | 1255 | 90931 | 0 | [Source audit](../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000005/pdf-structural-review.md) |
| src-000015 | 891 | 1238 | 69145 | 19 | [Source audit](../domains/payments/reference/message-sets/cash-management/2024-2025/documents/src-000015/pdf-structural-review.md) |
| src-000053 | 495 | 773 | 31176 | 0 | [Source audit](../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000053/pdf-structural-review.md) |
| src-000080 | 1252 | 2277 | 80810 | 12 | [Source audit](../domains/securities/reference/message-sets/corporate-actions/2025-2026/documents/src-000080/pdf-structural-review.md) |
| src-000096 | 5406 | 8434 | 455224 | 165 | [Source audit](../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000096/pdf-structural-review.md) |
| src-000163 | 1247 | 1485 | 109720 | 0 | [Source audit](../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/pdf-structural-review.md) |
| src-000174 | 610 | 742 | 55216 | 0 | [Source audit](../domains/payments/reference/message-sets/payments-initiation/2025-2026/documents/src-000174/pdf-structural-review.md) |
| src-000181 | 670 | 1244 | 46263 | 4 | [Source audit](../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000181/pdf-structural-review.md) |
| src-000197 | 2193 | 3837 | 131404 | 14 | [Source audit](../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/pdf-structural-review.md) |
| src-000233 | 3330 | 5539 | 276182 | 31 | [Source audit](../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/pdf-structural-review.md) |
| src-000321 | 457 | 858 | 27648 | 8 | [Source audit](../domains/securities/reference/message-sets/fitrr/2025/documents/src-000321/pdf-structural-review.md) |
| src-000344 | 69 | 89 | 3989 | 0 | [Source audit](../shared/reference/message-sets/t2s-administration/march-2024/documents/src-000344/pdf-structural-review.md) |
| src-000346 | 154 | 191 | 11538 | 0 | [Source audit](../domains/securities/reference/message-sets/t2s-billing/december-2025/documents/src-000346/pdf-structural-review.md) |
| src-000351 | 185 | 232 | 13173 | 0 | [Source audit](../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/pdf-structural-review.md) |
| src-000354 | 84 | 123 | 3607 | 0 | [Source audit](../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000354/pdf-structural-review.md) |
| src-000357 | 84 | 115 | 4692 | 0 | [Source audit](../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/documents/src-000357/pdf-structural-review.md) |
| src-000360 | 498 | 946 | 36052 | 8 | [Source audit](../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/pdf-structural-review.md) |
| src-000363 | 46 | 73 | 2454 | 0 | [Source audit](../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/pdf-structural-review.md) |
| src-000366 | 79 | 127 | 3644 | 0 | [Source audit](../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/documents/src-000366/pdf-structural-review.md) |
| src-000369 | 189 | 283 | 14901 | 0 | [Source audit](../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/documents/src-000369/pdf-structural-review.md) |
| src-000372 | 100 | 146 | 5601 | 0 | [Source audit](../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/pdf-structural-review.md) |
| src-000375 | 558 | 1067 | 38243 | 6 | [Source audit](../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000375/pdf-structural-review.md) |
| src-000378 | 535 | 905 | 39627 | 4 | [Source audit](../domains/securities/reference/message-sets/t2s-securities-reference-data/march-2024/documents/src-000378/pdf-structural-review.md) |
| src-000381 | 345 | 688 | 23352 | 9 | [Source audit](../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/pdf-structural-review.md) |

## Resume locally

`python tools/audit_pdf_structures.py --root PATH --source src-000096` resumes unchanged page shards; `--start-page N --end-page N` bounds a run. `--render-pages N N --dpi 120` creates source-page images without claiming review. `--refresh-markdown` rechecks cell matrices after markup-only repairs. `python tools/publish_pdf_audit.py --root PATH` republishes the recorded manual evidence and requires all residual candidates to match the explicit reviewed source/page list. New or changed objects fail instead of inheriting approval.
