---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.50 InterestComputationMethodFormat4Choice", "7.1.19.50.2 Proprietary <Prtry>"]
file_pages: [374, 375]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.50.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 374 to 375.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 374

```text
CodeName Name Definition
assumed to be the 30th, even if it is the
last day of the maturity coupon period.
A014 Actual365NL Method whereby interest is calculated
based on the actual number of accrued
days in the interest period, excluding any
leap day from the count, and a 365-day
year.
NARR Narrative Other method than A001-A020. See
Narrative.
7.1.19.50.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the format of interest computation method.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.51  ExposureType18Choice
Definition: Choice of format for the exposure information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 374
Or}   Proprietary <Prtry> [1..1] ± 376
7.1.19.51.1  Code <Cd>
Presence: [1..1]
Definition: Collateral movement exposure type expressed as an ISO 20022 code.
Datatype: "ExposureType3Code" on page 625
CodeName Name Definition
CCIR CrossCurrencyIRS Cross currency agreement between two
parties (known as counterparties) where
one stream of future interest payments is
exchanged for another based on a
specified principal amount.
COMM Commodities Any good exchanged during commerce,
which includes goods traded on a
commodity exchange.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 374 February 2025
```

## File page 375

```text
CodeName Name Definition
CRDS CreditDefaultSwap Swap designed to transfer the credit
exposure of fixed income products
between parties.
CRPR CrossProduct Combination of various types of trades.
CRSP CreditSupport Cash lending/borrowing; letter of credit;
signing of master agreement.
CRTL CreditLine Opening of a credit line before trading.
EQPT EquityOption Trading of equity option (also known as
stock options).
EQUS EquitySwap Equity swap trades where the return of
an equity is exchanged for either a fixed
or a floating rate of interest.
EXPT ExoticOption Trading of exotic option, for example, a
non standard option.
EXTD ExchangeTradedDerivatives Trading of exchanged traded derivatives
in general.
FIXI FixedIncome Trading of fixed income instruments.
FORW ForwardForeignExchange Forward FX trades.
FORX ForeignExchange FX trades in general.
FUTR Futures Agreement to buy or sell a specific
amount of a commodity or financial
instrument at a particular price on a
stipulated future date.
LIQU Liquidity In support of settlement via an RTGS or
other clearing system.
OPTN FXOption A contract that grants the holder the
right, but not the obligation, to buy or sell
currency at a specified exchange rate
during a specified period of time.
OTCD OTCDerivatives OTC derivatives trading.
PAYM CashSettlement In support of any type of cash
settlement.
REPO Repo Relates to repurchase agreement
trading.
SBSC SecuritiesBuySellSellBuyBack Securities buy sell back.
SCIE SingleCurrencyIRSExotic Exotic single currency interest rate swap.
SCIR SingleCurrencyIRS Single currency interest rate swap.
SCRP SecuritiesCrossProducts Combination of securities related
exposure types.
SLEB SecuritiesLendingAndBorrowing Exposure is linked to a securities lending
or borrowing activity.
SLOA SecuredLoan Exposure is linked to a secured loan.
SWPT Swaption Option on interest rate swap.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 375 February 2025
```

