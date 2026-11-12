---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.2 Message Datatypes", "9.2.2 CodeSet", "9.2.2.23 LinkageType1Code"]
file_pages: [330]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.2.2.23 LinkageType1Code

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 330 to 330.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 330

```text
CodeName Name Definition
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
9.2.2.23  LinkageType1Code
Definition: Type of linkage requested.
Type: CodeSet
CodeName Name Definition
LINK Link Request is to link the referenced
transactions.
UNLK Unlink Request is to unlink the referenced
transactions.
SOFT Soft Request is to soft link the referenced
transactions.
9.2.2.24  MatchingProcess1Code
Definition: Specifies the action to be performed on the matching process.
Type: CodeSet
CodeName Name Definition
UNMT Unmatch The referenced transaction is requested
to be unmatched.
MTRE ResumeMatching Matching process is to be resumed for
the referenced transaction.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 330 September 2025
```

