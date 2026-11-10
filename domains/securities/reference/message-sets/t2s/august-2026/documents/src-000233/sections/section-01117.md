---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.2 Replace <Rplc>", "28.4.2.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.2.1.3 Debt <Debt>", "28.4.2.2.1.3.52 YieldCalculation <YldClctn>", "28.4.2.2.1.3.52.1 Value <Val>"]
file_pages: [1612, 1613, 1614]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.2.1.3.52.1 Value <Val>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1612 to 1614.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1612

```text
YieldCalculation <YldClctn> contains the following YieldCalculation6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] Rate 1612
   CalculationType <ClctnTp> [0..1]  1612
{Or     Code <Cd> [1..1] CodeSet 1612
Or}     Proprietary <Prtry> [1..1] ± 1615
   RedemptionPrice <RedPric> [0..1]  1615
     ValueType <ValTp> [0..1] CodeSet 1615
     Value <Val> [1..1] ± 1616
     PriceType <PricTp> [0..1] CodeSet 1616
   ValueDate <ValDt> [1..1] Date 1617
   ValuePeriod <ValPrd> [1..1]  1617
{Or     FromDateTime <FrDtTm> [1..1] DateTime 1617
Or     ToDateTime <ToDtTm> [1..1] DateTime 1618
Or}     DateTimeRange <DtTmRg> [1..1] ± 1618
   CalculationDate <ClctnDt> [1..1] DateTime 1618
28.4.2.2.1.3.52.1  Value <Val>
Presence: [1..1]
Definition: Result of the yield calculation.
Datatype: "PercentageRate" on page 3325
28.4.2.2.1.3.52.2  CalculationType <ClctnTp>
Presence: [0..1]
Definition: Specifies the type of calculation.
CalculationType <ClctnTp> contains one of the following CalculationType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1612
Or}   Proprietary <Prtry> [1..1] ± 1615
28.4.2.2.1.3.52.2.1  Code <Cd>
Presence: [1..1]
Definition: Calculation type expressed as an ISO 20022 code.
Datatype: "CalculationType1Code" on page 3216
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1612 August 2026
```

## File page 1613

```text
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1613 August 2026
```

## File page 1614

```text
CodeName Name Definition
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
YTMA YieldToMaturity Internal rate of return an investor would
achieve if he or she purchased that bond
at its current dirty price, and held it to
maturity, assuming all coupon and
principal payments are received as
scheduled.
NXRF ToNextRefund Yield To Next Refund (Sinking Fund
Bonds) - Yield assuming all bonds are
redeemed at the next refund date at the
redemption price.
PNAV OpenAverage The average yield of the respective
securities in the portfolio.
NXPT ToNextPut The yield to the date at which the bond
holder can next put the bond to the
issuer.
PRCL PreviousClose The yield of a bond based on the closing
price 1 day ago.
PRYL Proceeds The CD equivalent yield when the
remaining time to maturity is less than
two years.
SEMI SemiAnnual The yield of a bond whose coupon
payments are reinvested semi-annually.
SHLF ShortestAverageLife The yield assuming that all sinks
(mandatory and voluntary) are taken at
par. This results in a faster paydown of
debt; the yield is then calculated to the
shortest average life date.
SPLL Simple The yield of a bond assuming no
reinvestment of coupon payments.
(Act/360 day count).
TXQV TaxEquivalent The after tax yield grossed up by the
maximum federal tax rate of 39.6%. For
comparison to taxable yields.
TTDT ToTenderDate The yield on a Municipal bond to its
mandatory tender date.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1614 August 2026
```

