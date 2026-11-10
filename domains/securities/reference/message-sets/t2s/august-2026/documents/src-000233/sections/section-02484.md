---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.166 TaxLiability1Code"]
file_pages: [3306, 3307, 3308]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.166 TaxLiability1Code

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3306 to 3308.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3306

```text
82.2.2.166  TaxLiability1Code
Definition: Specifies the tax role capacity of the instructing party.
Type: CodeSet
CodeName Name Definition
PRIN TaxPrincipal Settlement party is acting as a principal
for tax liability.
AGEN TaxAgent Settlement party is acting as an agent for
tax liability.
82.2.2.167  TEFRARules1Code
Definition: Indicates the Tax Equity and Fiscal Responsibility Act (TEFRA) rule levied by the IRS under
which the security is issued.
Type: CodeSet
CodeName Name Definition
RULC C Indicates that the security is issued
under the TEFRA rule C.
RULD D Indicates that the security is issued
under the TEFRA rule D.
82.2.2.168  TimeUnit1Code
Definition: Unit of time associated with the contract.
Type: CodeSet
CodeName Name Definition
DAYC CalendarDay Time unit is calendar day.
HOUR Hour Time unit is hour.
MINU Minute Time unit is minute.
MNTH Month Time unit is month.
SECO Second Time unit is second.
WEEK Week Time unit is week.
YEAR Year Time unit is year.
82.2.2.169  TradeTransactionCondition1Code
Definition: Indicates the conditions under which the order/trade is to be/was executed.
Type: CodeSet
CodeName Name Definition
CBNS CumBonus Indicates whether the trade is executed
cum bonus.
XBNS ExBonus Indicates whether the trade is executed
ex bonus.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3306 August 2026
```

## File page 3307

```text
CodeName Name Definition
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
CLEN Clean Indicates that the trade is executed
clean, ie government tax must not be
paid on the accrued interest on the bond.
BLKO Block Indicates whether the trade is a block
trade or not, ie, whether allocation
instruction will follow or not.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3307 August 2026
```

## File page 3308

```text
CodeName Name Definition
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
BCRO ResultOption Result of option when set. (UK specific).
BCRP ResultRepo Result of repo when set (UK specific).
BCPD DeliverCountryIncorporation Place of delivery, in country of
incorporation when unset (UK specific).
BCFD DeliveryForm Form of delivery, not for foreign
registration when unset (UK specific).
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3308 August 2026
```

