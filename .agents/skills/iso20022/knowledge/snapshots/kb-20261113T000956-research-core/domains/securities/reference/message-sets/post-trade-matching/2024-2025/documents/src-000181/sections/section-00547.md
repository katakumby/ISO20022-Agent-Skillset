---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.38 FutureAndOptionContractType1Code"]
file_pages: [628, 629, 630]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.38 FutureAndOptionContractType1Code

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 628 to 630.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 628

```text
CodeName Name Definition
MNTH Monthly Event takes place every month or once a
month.
QURT Quarterly Event takes place every three months or
four times a year.
MIAN SemiAnnual Event takes place every six months or
two times a year.
WEEK Weekly Event takes place once a week.
DAIL Daily Event takes place every day.
ADHO Adhoc Event takes place on request or as
necessary.
INDA IntraDay Event takes place several times a day.
7.2.2.38  FutureAndOptionContractType1Code
Definition: Future And Option Contract Type.
Type: CodeSet
CodeName Name Definition
ORDY Ordinary Ordinary future and option contract.
INDX Index Future and option contract on an index
as opposed to an underlying equity.
EXFU ExercisedFuture Receipt of future contract when an
option on a future is exercised.
7.2.2.39  InterestComputationMethod1Code
Definition: Specifies the method used to compute accruing interest of a financial instrument.
Type: CodeSet
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
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 628 February 2025
```

## File page 629

```text
CodeName Name Definition
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
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 629 February 2025
```

## File page 630

```text
CodeName Name Definition
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
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 630 February 2025
```

