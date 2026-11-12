---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Miscellaneous", "7.1.18.34 Number22Choice", "7.1.18.34.1 Short <Shrt>"]
file_pages: [391, 392, 393]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18.34.1 Short <Shrt>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 391 to 393.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 391

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Short <Shrt> [1..1] Text 391
Or}   Long <Lng> [1..1] ± 391
7.1.18.34.1  Short <Shrt>
Presence: [1..1]
Definition: Number of maximum 3 numeric text.
Datatype: "Exact3NumericText" on page 555
7.1.18.34.2  Long <Lng>
Presence: [1..1]
Definition: Number of maximum 35 text, with the possibility to provide an issuer for the number
identification.
Long <Lng> contains the following elements (see "GenericIdentification1" on page 352 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 352
   Issuer <Issr> [0..1] Text 352
7.1.18.35  InterestComputationMethodFormat4Choice
Definition: Choice between a standard code or proprietary code to specify the type of interest
computation method.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 391
Or}   Proprietary <Prtry> [1..1] ± 394
7.1.18.35.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the method used to compute accruing interest of a financial
instrument.
Datatype: "InterestComputationMethod2Code" on page 511
CodeName Name Definition
A001 IC30360ISDAor30360AmericanBasicRule Method whereby interest is calculated
based on a 30-day month and a 360-day
year. Accrued interest to a value date on
the last day of a month shall be the
same as to the 30th calendar day of the
same month, except for February, and
provided that the interest period started
on a 30th or a 31st. This means that a
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 391 March 2026
```

## File page 392

```text
CodeName Name Definition
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
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 392 March 2026
```

## File page 393

```text
CodeName Name Definition
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
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 393 March 2026
```

