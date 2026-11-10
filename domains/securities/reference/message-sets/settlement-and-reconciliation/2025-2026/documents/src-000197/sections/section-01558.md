---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.42 ExposureType15Code"]
file_pages: [2063, 2064]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.42 ExposureType15Code

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 2063 to 2064.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2063

```text
CodeName Name Definition
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
35.2.2.42  ExposureType15Code
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2063 March 2026
```

## File page 2064

```text
CodeName Name Definition
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
SCIR SingleCurrencyIRS Single currency interest rate swap.
SCIE SingleCurrencyIRSExotic Exotic single currency interest rate swap.
SWPT Swaption Option on interest rate swap.
TBAS ToBeAnnounced To be announced (TBA) related
collateral.
UDMS UnclearedDerivativeMarginSegregation Relates to uncleared derivative margin
segregation. This could be for variation
or initial margin.
TRCP TreasuryCrossProduct Combination of treasury related
exposure types.
CBCO CentralBankCreditOperations Exposures related to activity with central
banks.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2064 March 2026
```

