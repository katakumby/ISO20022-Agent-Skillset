---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.2 CodeSet", "16.2.2.70 FractionDispositionType10Code"]
file_pages: [1211]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.2.70 FractionDispositionType10Code

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1211 to 1211.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1211

```text
16.2.2.70  FractionDispositionType10Code
Definition: Indicates that fractional value should be retained; no rounding.
Type: CodeSet
CodeName Name Definition
BUYU BuyUp Buy securities up to next whole number.
CINL CashInLieuOfFraction Fractional part of cash. Take cash in lieu
of fractions.
EXPI Expire Let fractions expire worthless.
DIST IssueFraction Take distribution of fractions in the form
of securities.
16.2.2.71  FractionDispositionType11Code
Definition: Indicates that fractional value should be retained; no rounding.
Type: CodeSet
CodeName Name Definition
BUYU BuyUp Buy securities up to next whole number.
CINL CashInLieuOfFraction Fractional part of cash. Take cash in lieu
of fractions.
DIST IssueFraction Take distribution of fractions in the form
of securities.
RDDN RoundDown Round the entitlement down to the last
full unit/minimum nominal quantity,
fractions are discarded.
STAN RoundToNearest If the fraction is greater than or equal to
0.5 of the resulting security then round
up, else round down as specified in the
respective RDUP and RDDN codes.
RDUP RoundUp Round up to the next full unit/minimum
nominal quantity at no cost.
16.2.2.72  FractionDispositionType8Code
Definition: Indicates that fractional value should be retained; no rounding.
Type: CodeSet
CodeName Name Definition
BUYU BuyUp Buy securities up to next whole number.
CINL CashInLieuOfFraction Fractional part of cash. Take cash in lieu
of fractions.
DIST IssueFraction Take distribution of fractions in the form
of securities.
RDDN RoundDown Round the entitlement down to the last
full unit/minimum nominal quantity,
fractions are discarded.
STAN RoundToNearest If the fraction is greater than or equal to
0.5 of the resulting security then round
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1211 February 2026
```

