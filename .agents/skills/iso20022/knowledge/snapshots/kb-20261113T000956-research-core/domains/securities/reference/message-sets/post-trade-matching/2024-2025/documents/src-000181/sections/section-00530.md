---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.30 Yield Calculation", "7.1.30.1 YieldCalculation7", "7.1.30.1.3 RedemptionPrice <RedPric>"]
file_pages: [609]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.30.1.3 RedemptionPrice <RedPric>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 609 to 609.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 609

```text
CodeName Name Definition
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
TRYL True The yield calculated with coupon dates
moved from a weekend or holiday to the
next valid settlement date.
WRST ToWorstConvention The lowest yield to all possible
redemption date scenarios.
7.1.30.1.3  RedemptionPrice <RedPric>
Presence: [0..1]
Definition: Price to which the yield has been calculated.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 609 February 2025
```

