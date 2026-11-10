---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.41 InterestType2Code"]
file_pages: [634]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.41 InterestType2Code

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 634 to 634.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 634

```text
CodeName Name Definition
coupon period starts on the last day of
February, it is assumed to produce only
one day of interest in February as if it
was starting on 30 Feb when the end of
the period is the 30th or the 31st, or two
days of interest in February when the
end of the period is the 29th, or three
days of interest in February when it is 28
Feb of a non-leap year and the end of
the period is before the 29th.
A013 IC30E3360orEurobondbasismodel3 Method whereby interest is calculated
based on a 30-day month and a 360-day
year. Accrued interest to a value date on
the last day of a month shall be the
same as to the 30th calendar day of the
same month. This means that the 31st is
assumed to be the 30th and 28 Feb (or
29 Feb for a leap year) is assumed to be
equivalent to 30 Feb. It is a variation of
the 30E/360 (or Eurobond basis) method
where the last day of February is always
assumed to be the 30th, even if it is the
last day of the maturity coupon period.
A014 Actual365NL Method whereby interest is calculated
based on the actual number of accrued
days in the interest period, excluding any
leap day from the count, and a 365-day
year.
NARR Narrative Other method than A001-A020. See
Narrative.
7.2.2.41  InterestType2Code
Definition: Indicates if the deal price is excluding or including the accrued interest.
Type: CodeSet
CodeName Name Definition
CINT CumInterest Indicates deal price including accrued
interest.
XINT ExInterest Indicates deal price excluding accrued
interest.
7.2.2.42  LegalFramework1Code
Definition: Identifies the legal framework of the transaction.
Type: CodeSet
CodeName Name Definition
FRAN PensionLivree Relates to the French legal framework
for repos, that is, relates to a "Pension
Livrée".
7.2.2.43  LendingTransactionMethod1Code
Definition: Lending method applied to the securities financing contract.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 634 February 2025
```

