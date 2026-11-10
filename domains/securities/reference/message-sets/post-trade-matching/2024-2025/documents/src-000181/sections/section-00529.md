---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.30 Yield Calculation"]
file_pages: [607, 608]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.30 Yield Calculation

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 607 to 608.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 607

```text
7.1.30 Yield Calculation
7.1.30.1  YieldCalculation7
Definition: Return provided by a financial instrument.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] Rate 607
   CalculationType <ClctnTp> [1..1] CodeSet 607
   RedemptionPrice <RedPric> [0..1] ± 609
   ValueDate <ValDt> [0..1] Date 610
   ValuePeriod <ValPrd> [0..1]  610
{Or     FromDateTime <FrDtTm> [1..1] DateTime 610
Or     ToDateTime <ToDtTm> [1..1] DateTime 610
Or}     DateTimeRange <DtTmRg> [1..1] ± 610
   CalculationDate <ClctnDt> [0..1] Date 611
7.1.30.1.1  Value <Val>
Presence: [1..1]
Definition: Result of the yield calculation.
Datatype: "PercentageRate" on page 667
7.1.30.1.2  CalculationType <ClctnTp>
Presence: [1..1]
Definition: Specifies the type of calculation.
Datatype: "CalculationType1Code" on page 617
CodeName Name Definition
AFTX AfterTax The yield on the bond net of any tax
consequences from holding the bond.
The discount on municipal securities can
be subject to both capital gains taxes
and ordinary income taxes. Calculated
from dollar price.
ANNU Annual The annual interest or dividend income
an investment earns, expressed as a
percentage of the investment's total
value.
ISSU AtIssue The yield of the bond offered on the
issue date.
AVMA ToAverageMaturity The yield achieved by substituting a
bond's average maturity for the issue's
final maturity date.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 607 February 2025
```

## File page 608

```text
CodeName Name Definition
BOOK Book The yield of a security calculated by
using its book value instead of the
current market price. This term is
typically used in the US domestic
market.
YTNC YieldToNextCall Yield of a bond to the next possible call
date.
CHCL ChangeSinceClose The change in the yield since the
previous day's closing yield.
CLOS Closing The yield of a bond based on the closing
price.
CMPD Compound The yield of certain Japanese bonds
based on its price. Certain Japanese
bonds have irregular first or last
coupons, and the yield is calculated
compound for these irregular periods.
CUYI CurrentYield The ratio of the interest payment amount
to the clean price.
TRGR TrueGross Yield calculated using the price including
accrued interest, where coupon dates
are moved from holidays and weekends
to the next trading day.
GVEQ GovernmentEquivalent Ask yield based on semi-annual coupons
compounding in all periods and actual/
actual calendar.
FLAS InflationAssumption Based on price, the return an investor
would require on a normal bond that
would make the real return equal to that
of the inflation-indexed bond, assuming
a constant inflation rate.
NVFL InverseFloater Inverse Floater Bond Yield - Inverse
floater semi-annual bond equivalent rate.
LSCL LastClose Most Recent Closing Yield - The last
available yield stored in history,
computed using price.
LSMT LastMonth Closing Yield Most Recent Month - The
yield of a bond based on the closing
price as of the most recent month's end.
LSQR LastQuarter Closing Yield Most Recent Quarter - The
yield of a bond based on the closing
price as of the most recent quarter's end.
LSYR LastYear Closing Yield Most Recent Year - The
yield of a bond based on the closing
price as of the most recent year's end.
LGAL LongestAverageLife The yield assuming only mandatory
sinks are taken. This results in a lower
paydown of debt; the yield is then
calculated to the final payment date.
MARK MarkToMarket An adjustment in the valuation of a
securities portfolio to reflect the current
market values of the respective
securities in the portfolio.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 608 February 2025
```

