---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.72 InterestComputationMethodFormat4Choice", "35.1.16.72.2 Proprietary <Prtry>"]
file_pages: [1615]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.72.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1615 to 1615.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1615

```text
CodeName Name Definition
29th). It is the most commonly used
30/360 method for non-US straight and
convertible bonds issued before 1
January 1999.
A012 IC30E2360orEurobondbasismodel2 Method whereby interest is calculated
based on a 30-day month and a 360-day
year. Accrued interest to a value date on
the last day of a month shall be the
same as to the 30th calendar day of the
same month, except for the last day of
February whose day of the month value
shall be adapted to the value of the first
day of the interest period if the latter is
higher and if the period is one of a
regular schedule. This means that the
31st is assumed to be the 30th and 28
Feb of a non-leap year is assumed to be
equivalent to 29 Feb when the first day
of the interest period is the 29th, or to 30
Feb when the first day of the interest
period is the 30th or the 31st. The 29th
day of February in a leap year is
assumed to be equivalent to 30 Feb
when the first day of the interest period
is the 30th or the 31st. Similarly, if the
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
35.1.16.72.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the format of interest computation method.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1615 March 2026
```

