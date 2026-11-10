---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.55 InterestComputationMethodFormat4Choice", "16.1.15.55.1 Code <Cd>"]
file_pages: [976, 977, 978]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.55.1 Code <Cd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 976 to 978.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 976

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 976
Or}   Proprietary <Prtry> [1..1] ± 979
16.1.15.55.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the method used to compute accruing interest of a financial
instrument.
Datatype: "InterestComputationMethod2Code" on page 1214
CodeName Name Definition
A001 IC30360ISDAor30360AmericanBasicRule Method whereby interest is calculated
based on a 30-day month and a 360-day
year. Accrued interest to a value date on
the last day of a month shall be the
same as to the 30th calendar day of the
same month, except for February, and
provided that the interest period started
on a 30th or a 31st. This means that a
31st is assumed to be a 30th if the
period started on a 30th or a 31st and
the 28 Feb (or 29 Feb for a leap year) is
assumed to be the 28th (or 29th). This is
the most commonly used 30/360 method
for US straight and convertible bonds.
A002 IC30365 Method whereby interest is calculated
based on a 30-day month in a way
similar to the 30/360 (basic rule) and a
365-day year. Accrued interest to a
value date on the last day of a month
shall be the same as to the 30th
calendar day of the same month, except
for February. This means that a 31st is
assumed to be the 30th and the 28 Feb
(or 29 Feb for a leap year) is assumed to
be the 28th (or 29th).
A003 IC30Actual Method whereby interest is calculated
based on a 30-day month in a way
similar to the 30/360 (basic rule) and the
assumed number of days in a year in a
way similar to the Actual/Actual (ICMA).
Accrued interest to a value date on the
last day of a month shall be the same as
to the 30th calendar day of the same
month, except for February. This means
that the 31st is assumed to be the 30th
and 28 Feb (or 29 Feb for a leap year) is
assumed to be the 28th (or 29th). The
assumed number of days in a year is
computed as the actual number of days
in the coupon period multiplied by the
number of interest payments in the year.
A004 Actual360 Method whereby interest is calculated
based on the actual number of accrued
days in the interest period and a 360-day
year.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 976 February 2026
```

## File page 977

```text
CodeName Name Definition
A005 Actual365Fixed Method whereby interest is calculated
based on the actual number of accrued
days in the interest period and a 365-day
year.
A006 ActualActualICMA Method whereby interest is calculated
based on the actual number of accrued
days and the assumed number of days
in a year, that is, the actual number of
days in the coupon period multiplied by
the number of interest payments in the
year. If the coupon period is irregular
(first or last coupon), it is extended or
split into quasi-interest periods that have
the length of a regular coupon period
and the computation is operated
separately on each quasi-interest period
and the intermediate results are summed
up.
A007 IC30E360orEuroBondBasismodel1 Method whereby interest is calculated
based on a 30-day month and a 360-day
year. Accrued interest to a value date on
the last day of a month shall be the
same as to the 30th calendar day of the
same month. This means that the 31st is
assumed to be the 30th and the 28 Feb
(or 29 Feb for a leap year) is assumed to
be equivalent to 30 Feb. However, if the
last day of the maturity coupon period is
the last day of February, it will not be
assumed to be the 30th. It is a variation
of the 30/360 (ICMA) method commonly
used for eurobonds. The usage of this
variation is only relevant when the
coupon periods are scheduled to end on
the last day of the month.
A008 ActualActualISDA Method whereby interest is calculated
based on the actual number of accrued
days of the interest period that fall
(falling on a normal year, year) divided
by 365, added to the actual number of
days of the interest period that fall
(falling on a leap year, year) divided by
366.
A009 Actual365LorActuActubasisRule Method whereby interest is calculated
based on the actual number of accrued
days and a 365-day year (if the coupon
payment date is NOT in a leap year) or a
366-day year (if the coupon payment
date is in a leap year).
A010 ActualActualAFB Method whereby interest is calculated
based on the actual number of accrued
days and a 366-day year (if 29 Feb falls
in the coupon period) or a 365-day year
(if 29 Feb does not fall in the coupon
period). If a coupon period is longer than
one year, it is split by repetitively
separating full year subperiods counting
backwards from the end of the coupon
period (a year backwards from 28 Feb
being 29 Feb, if it exists). The first of the
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 977 February 2026
```

## File page 978

```text
CodeName Name Definition
subperiods starts on the start date of the
accrued interest period and thus is
possibly shorter than a year. Then the
interest computation is operated
separately on each subperiod and the
intermediate results are summed up.
A011 IC30360ICMAor30360basicrule Method whereby interest is calculated
based on a 30-day month and a 360-day
year. Accrued interest to a value date on
the last day of a month shall be the
same as to the 30th calendar day of the
same month, except for February. This
means that the 31st is assumed to be
the 30th and 28 Feb (or 29 Feb for a
leap year) is assumed to be the 28th (or
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 978 February 2026
```

