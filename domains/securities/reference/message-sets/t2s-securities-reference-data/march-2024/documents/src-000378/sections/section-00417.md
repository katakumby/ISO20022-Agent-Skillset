---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.2 Message Datatypes", "13.2.2 CodeSet", "13.2.2.8 CalculationType1Code"]
file_pages: [510, 511, 512]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.2.2.8 CalculationType1Code

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 510 to 512.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 510

```text
CodeName Name Definition
LIBI LIBID Rate at which major international banks
are willing to take deposits from one
another, is normally 1/8 percent below
LIBOR.
London InterBank Bid Rate, the rate bid
by banks on Eurocurrency deposits; the
international rate that banks lend to other
banks.
LIBO LIBOR London Interbank Offered Rate, the
interest rate that major international
banks in London charge each other for
borrowing.
SWAP SWAP In curve construction, Swap is the long
portion of the curve constituting about 3
years to 30 years term.
The exchange of one security, currency
or interest rate for another to change the
maturity (bonds), or quality of issues
(stocks or bonds), or because
investment objectives have changed.
TREA Treasury Treasury benchmark that comes in three
types: the yield curve, the par curve, and
the spot curve. All curves also have a
constituent time series.
EURI Euribor Euro Interbank Offer Rate is the rate at
which Euro inter-bank term deposits
within the Euro zone are offered by one
prime bank to another prime bank.
PFAN Pfandbriefe Pfandbriefe security is a collateralised
bullet bond backed by either mortgage
loans or loans to the public sector.
Pfandbriefe differ from traditional asset-
backed securities in significant ways.
The most important difference is that
Pfandbriefe carry no pre-payment risk
since they remain on the balance sheet
of the issuing institution. Therefore, their
spreads over sovereign bonds are
attributable to liquidity and credit quality
alone. New indices have been created
and existing indices have been modified
in response to the growing importance of
the Pfandbriefe market. The Deutsche
Borse has three synthetic indices called
REX, JEX, and PEX. The Pfandbriefe
curve is used as a reference for credit as
well as mortgage market.
13.2.2.8  CalculationType1Code
Definition: Specifies the yield computation method.
Type: CodeSet
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 510 March 2024
```

## File page 511

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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 511 March 2024
```

## File page 512

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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 512 March 2024
```

