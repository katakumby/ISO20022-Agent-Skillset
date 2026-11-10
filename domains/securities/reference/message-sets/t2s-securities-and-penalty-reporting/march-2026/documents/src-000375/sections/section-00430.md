---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.74 ShortLong1Code"]
file_pages: [541, 542, 543, 544]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.74 ShortLong1Code

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 541 to 544.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 541

```text
Type: CodeSet
CodeName Name Definition
SAGE SettlingAgent Settlement party is trading and settling
transactions in financial instruments on
behalf of its client(s).
CUST SettlingCustodian Settlement party is a custodian. It
receives/delivers the securities and
carries out custodial duties.
SPRI SettlingPrincipal Settlement party is settling its own
trades.
RISP SettlingRisklessPrincipal Party settles trades that were
simultaneously offset.
7.2.2.74  ShortLong1Code
Definition: Specifies whether the securities position is short or long, that is, whether the balance is a
negative or positive balance.
Type: CodeSet
CodeName Name Definition
SHOR Short Position is short, that is, the balance is
negative.
LONG Long Position is long, that is, the balance is
positive.
7.2.2.75  StatementUpdateType1Code
Definition: Specifies the nature of a statement update, for example, it is a complete statement.
Type: CodeSet
CodeName Name Definition
COMP Complete Statement is complete.
DELT Delta Statement contains changes only.
7.2.2.76  TaxLiability1Code
Definition: Specifies the tax role capacity of the instructing party.
Type: CodeSet
CodeName Name Definition
PRIN TaxPrincipal Settlement party is acting as a principal
for tax liability.
AGEN TaxAgent Settlement party is acting as an agent for
tax liability.
7.2.2.77  TradeTransactionCondition1Code
Definition: Indicates the conditions under which the order/trade is to be/was executed.
Type: CodeSet
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 541 March 2026
```

## File page 542

```text
CodeName Name Definition
CBNS CumBonus Indicates whether the trade is executed
cum bonus.
XBNS ExBonus Indicates whether the trade is executed
ex bonus.
CCPN CumCoupon Indicates whether the trade is executed
cum coupon.
XCPN ExCoupon Indicates whether the trade is executed
ex coupon.
CDIV CumDividend Indicates whether the trade is executed
cum dividend.
XDIV ExDividend Indicates whether the trade is executed
ex dividend.
CRTS CumRights Indicates whether the trade is executed
cum rights.
XRTS ExRights Indicates whether the trade is executed
ex rights.
CWAR CumWarrant Indicates whether the trade is executed
cum warrant.
XWAR ExWarrant Indicates whether the trade is executed
ex warrant.
SPCU SpecialCumDividend Indicates whether the trade is executed
with a special cum
dividend, that is, buying after the ex date
and getting the dividend.
SPEX SpecialExDividend Indicates whether the trade is executed
with a special ex
dividend, that is, selling before the ex
date without the coupon.
DUEB BrokerDueBill Indicates that the trade is executed cum-
dividend or cum-coupon and a due bill is
required.
A due bill is a contractual agreement to
pay the dividend along with the delivery
of
the financial instrument.
SSTI SoldShort Indicates whether the trade is sold short.
When the seller does not have the
financial instrument, the delivery is
effected by borrowing the financial
instrument by or
for the account of the seller.
DIRT Dirty Indicates that the trade is executed dirty,
ie government tax must be paid on the
accrued interest on the bond.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 542 March 2026
```

## File page 543

```text
CodeName Name Definition
CLEN Clean Indicates that the trade is executed
clean, ie government tax must not be
paid on the accrued interest on the bond.
BLKO Block Indicates whether the trade is a block
trade or not, ie, whether allocation
instruction will follow or not.
GTDL GuaranteedDelivery Indicates whether the delivery of the
financial instrument on settlement date
is guaranteed.
FRAC Fractions Indicates whether fractional parts are
allowed.
CRST CrossTrade Indicates that cross trades are allowed
whereby buy and sell orders are offset
without recording the trade on the
exchange.
NCRS NoCrossTrade Indicates that cross trades, whereby buy
and sell orders are offset without
recording the trade on the exchange, are
not allowed.
DORD DirectOrder Indicates that the order is to be executed
by a trading party other than the trading
party to which the
order is sent. In this case, the instructing
party has traded with another broker
which will
subsequently send an advice of
execution to the executing party who
received the order
and which is acting as clearing broker.
DIOR DirectedOrder Indicates that the order must be
executed with a specific trading party.
WARE WarehouseTrade Warehouse Trade.
DNIN NotIncrease A limit order to buy or a stop order to sell
or a stop limit order which is not to be
increased in shares on the ex-dividend
date as a result of a stock dividend or
distribution.
DNRE NotReduce A limit order to buy or a stop order to
sell, or a stop-limit order to sell which is
not to be reduced in price by the amount
of an ordinary cash dividend. Only
applies to ordinary stock dividends; it
should be reduced for other distributions.
e.g. when a stock goes 'ex' stock
dividend or rights.
FORW ForwardPriceTrade Indicates that the order is based on a
forward price.
HIST HistoricPriceTrade Indicates that the order is based on a
historic price.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 543 March 2026
```

## File page 544

```text
CodeName Name Definition
BCRO ResultOption Result of option when set. (UK specific).
BCRP ResultRepo Result of repo when set (UK specific).
BCPD DeliverCountryIncorporation Place of delivery, in country of
incorporation when unset (UK specific).
BCFD DeliveryForm Form of delivery, not for foreign
registration when unset (UK specific).
BCBL BoardLot Board lots, not set for odd lots (UK
specific).
BCBN BadName Bad names, not set for good names (UK
specific).
BTEX BestExecution Trade to be executed done at best
execution.
CALL Call Trade to be executed following the
exercise of a call option on the security.
CLBR ClosureBeforeRollOver Trade to be executed for closure of a
previous position before the rollover of a
position (Deferred Settlement Service).
MONT Monthly Trade to be executed for month-end
settlement (Deferred Settlement
Service).
NBFR NewTradeFollowingRollover Trade to be executed for a new trade
position on the next month following the
roll-over of a position (Deferred
Settlement Service).
TRFR TradeFollowingRollover Trade to be executed on the next month
following the roll-over of positions.
PUTT Putt Trade to be executed following the
exercise of a put option on the security.
SPCC SpecialCumCoupon Indicates whether the trade is executed
with a special cum coupon.
SECN SpecialExCoupon Indicates whether the trade is executed
with a special ex coupon.
SEBN SpecialExBonus Indicates whether the trade is executed
special ex bonus.
SCBN SpecialCumBonus Indicates whether the trade is executed
special cum bonus.
SCRT SpecialCumRights Indicates whether the trade is executed
special cum rights.
SERT SpecialExRights Indicates whether the trade is executed
special ex rights.
SCCR SpecialCumCapitalRepayments Indicates whether the trade is executed
special cum capital repayments.
SECR SpecialExCapitalRepayments Indicates whether the trade is executed
special ex capital repayments.
CAST CashSettlement Indicates whether the trade is executed
with a cash settlement.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 544 March 2026
```

