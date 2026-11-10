---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.15 BlockTrade1Code"]
file_pages: [3216, 3217]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.15 BlockTrade1Code

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3216 to 3217.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3216

```text
CodeName Name Definition
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
82.2.2.15  BlockTrade1Code
Definition: Specifies whether the instruction is the parent or a children of a block trade.
Type: CodeSet
CodeName Name Definition
BLPA Parent Transaction is a block trade parent.
BLCH Child Transaction is a block trade child.
82.2.2.16  CalculationType1Code
Definition: Specifies the yield computation method.
Type: CodeSet
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3216 August 2026
```

## File page 3217

```text
CodeName Name Definition
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
YTMA YieldToMaturity Internal rate of return an investor would
achieve if he or she purchased that bond
at its current dirty price, and held it to
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3217 August 2026
```

