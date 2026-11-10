---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.32 EventFrequency4Code"]
file_pages: [625, 626]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.32 EventFrequency4Code

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 625 to 626.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 625

```text
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
MNTH Monthly Event takes place every month or once a
month.
QUTR Quarterly Event takes place every three months or
four times a year.
SEMI SemiAnnual Event takes place every six months or
two times a year.
WEEK Weekly Event takes place once a week.
7.2.2.32  EventFrequency4Code
Definition: Specifies the regularity of an event.
Type: CodeSet
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
ADHO Adhoc Event takes place as necessary.
MNTH Monthly Event takes place every month or once a
month.
DAIL Daily Event takes place every day.
INDA IntraDay Event takes place several times a day.
WEEK Weekly Event takes place once a week.
7.2.2.33  ExposureType3Code
Definition: Specifies the underlying business area/type of trade causing the collateral movement.
Type: CodeSet
CodeName Name Definition
CCIR CrossCurrencyIRS Cross currency agreement between two
parties (known as counterparties) where
one stream of future interest payments is
exchanged for another based on a
specified principal amount.
COMM Commodities Any good exchanged during commerce,
which includes goods traded on a
commodity exchange.
CRDS CreditDefaultSwap Swap designed to transfer the credit
exposure of fixed income products
between parties.
CRPR CrossProduct Combination of various types of trades.
CRSP CreditSupport Cash lending/borrowing; letter of credit;
signing of master agreement.
CRTL CreditLine Opening of a credit line before trading.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 625 February 2025
```

## File page 626

```text
CodeName Name Definition
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
TRCP TreasuryCrossProduct Combination of treasury related
exposure types.
BFWD BondForward Any securities traded out beyond 3 days
which include treasury notes, Japanese
Governement Bonds (JGBs) and Gilts.
RVPO ReverseRepurchaseAgreement In support of a reverse repurchase
agreement transaction.
TBAS ToBeAnnounced To be announced (TBA) related
collateral.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 626 February 2025
```

