---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.40 EventFrequency7Code"]
file_pages: [3238, 3239]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.40 EventFrequency7Code

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3238 to 3239.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3238

```text
CodeName Name Definition
SEMI SemiAnnual Event takes place every six months or
two times a year.
WEEK Weekly Event takes place once a week.
82.2.2.40  EventFrequency7Code
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
SEMI SemiAnnual Event takes place every six months or
two times a year.
QUTR Quarterly Event takes place every three months or
four times a year.
TOMN EveryTwoMonths Event takes place every two months.
TOWK EveryTwoWeeks Event takes place every two weeks.
TWMN TwiceAMonth Event takes place two times a month.
OVNG Overnight Event takes place overnight.
ONDE OnDemand Event takes place on demand.
82.2.2.41  ExposureType15Code
Definition: Specifies the underlying business area/type of trade causing the collateral movement.
Type: CodeSet
CodeName Name Definition
BFWD BondForward Any securities traded out beyond 3 days
which include treasury notes, Japanese
Governement Bonds (JGBs) and Gilts.
PAYM CashSettlement In support of any type of cash
settlement.
CCPC CCPCollateral Collateral covering the initial margin
requirements for OTC trades cleared
through a CCP.
COMM Commodities Any good exchanged during commerce,
which includes goods traded on a
commodity exchange.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3238 August 2026
```

## File page 3239

```text
CodeName Name Definition
CRDS CreditDefaultSwap Swap designed to transfer the credit
exposure of fixed income products
between parties.
CRTL CreditLine Opening of a credit line before trading.
CRSP CreditSupport Cash lending/borrowing; letter of credit;
signing of master agreement.
CCIR CrossCurrencyIRS Cross currency agreement between two
parties (known as counterparties) where
one stream of future interest payments is
exchanged for another based on a
specified principal amount.
CRPR CrossProduct Combination of various types of trades.
EQPT EquityOption Trading of equity option (also known as
stock options).
EXTD ExchangeTradedDerivatives Trading of exchanged traded derivatives
in general.
EQUS EquitySwap Equity swap trades where the return of
an equity is exchanged for either a fixed
or a floating rate of interest.
EXPT ExoticOption Trading of exotic option, for example, a
non standard option.
FIXI FixedIncome Trading of fixed income instruments.
FORX ForeignExchange FX trades in general.
FORW ForwardForeignExchange Forward FX trades.
FUTR Futures Agreement to buy or sell a specific
amount of a commodity or financial
instrument at a particular price on a
stipulated future date.
OPTN FXOption A contract that grants the holder the
right, but not the obligation, to buy or sell
currency at a specified exchange rate
during a specified period of time.
LIQU Liquidity In support of settlement via an RTGS or
other clearing system.
OTCD OTCDerivatives OTC derivatives trading.
REPO RepurchaseAgreement Relates to repurchase agreement
trading.
RVPO ReverseRepurchaseAgreement In support of a reverse repurchase
agreement transaction.
SLOA SecuredLoan Exposure is linked to a secured loan.
SBSC SecuritiesBuySellSellBuyBack Securities buy sell back.
SCRP SecuritiesCrossProducts Combination of securities related
exposure types.
SLEB SecuritiesLendingAndBorrowing Exposure is linked to a securities lending
or borrowing activity.
SHSL ShortSell Short sell exposure.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3239 August 2026
```

