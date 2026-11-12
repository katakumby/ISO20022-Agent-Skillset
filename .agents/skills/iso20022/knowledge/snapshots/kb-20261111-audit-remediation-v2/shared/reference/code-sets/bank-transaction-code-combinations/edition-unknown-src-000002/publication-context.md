---
template: false
review_status: "needs-review"
document_kind: "code-set-publication-context"
domain: "shared"
source_ids: ["src-000002", "src-000003"]
source_locations: ["BTC_Codification!A1:H3", "History Log!A1:D15", "DOCX title paragraphs 7,10,11"]
source_edition: null
issues: ["issue-000002"]
source_editions: ["November 2025 Version 8.0"]
---

# Bank Transaction Code publication identity

The workbook title is “Bank Transaction Code - all permitted combinations of the BTC code sets” (src-000002, BTC_Codification!A1:H1). Its filename includes 30Nov2025. The latest populated History Log row is A15:D15: 31-May-25, “Addition of 2 codes”, CR1471, v8.1. These facts are preserved separately; the filename date is not promoted to a confirmed internal publication edition.

The associated description document is a distinct source, src-000003. Its title-page paragraphs 7,10,11 state “Bank Transaction Codes – External Code Sets”, November2025 and “Version 8.0 – Approved Version”. The workbook history and DOCX cover need not share a version numbering scheme. Their equivalence is not inferred and the three source publications are not silently combined with the JSON filename label 2Q2026 v3.

## Workbook coverage and interpretation

The code-combination table has 1,567 data rows at BTC_Codification!A4:H1570. The source titles are merged A1:H1 and A2:H2. Row3 provides Domain, Family, SubFamily, exact domain/family/subfamily code identifiers, Status and Status Date. The Introduction note says light-grey codes are generic and available across domains and families; original font/style definitions and per-cell style IDs are retained in extraction metadata, and their visual color semantics remain needs-review. History Log!A1:D15 contains one header and 14 populated history records; source formatting extends farther and is retained as metadata.

No formulas, comments, chart objects or picture anchors occur in this workbook according to OOXML inspection. The two worksheets are visible. All 12,606 nonempty cell coordinates and values were independently compared against openpyxl with zero differences. This check does not replace visual formatting review.

[Complete workbook tables](index.md), [History Log](sheets/02-history-log/index.md), [issue-000002](../../../../../tracking/issues.md#issue-000002).
