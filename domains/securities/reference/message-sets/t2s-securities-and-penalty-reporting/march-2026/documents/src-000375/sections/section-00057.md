---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "3.4 Message Building Blocks", "3.4.1 QueryDefinition <QryDef>", "3.4.1.2 SearchCriteria <SchCrit>", "3.4.1.2.23 TradeTransactionCondition <TradTxCond>"]
file_pages: [70, 71, 72]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 3.4.1.2.23 TradeTransactionCondition <TradTxCond>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 70 to 72.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 70

```text
Constraints
• Party2PresenceRule
If Party2 is present, then Party1 must be present.
On Condition
    /Party2 is present
Following Must be True
    /Party1 Must be present
• Party3PresenceRule
If Party3 is present, then Party2 must be present.
On Condition
    /Party3 is present
Following Must be True
    /Party2 Must be present
• Party4PresenceRule
If Party4 is present, then Party3 must be present.
On Condition
    /Party4 is present
Following Must be True
    /Party3 Must be present
• Party5PresenceRule
If Party5 is present, then Party4 must be present.
On Condition
    /Party5 is present
Following Must be True
    /Party4 Must be present
3.4.1.2.23  TradeTransactionCondition <TradTxCond>
Presence: [0..*]
Definition: Provides the conditions under which the order/trade is to be/was executed.
Datatype: "TradeTransactionCondition1Code" on page 541
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
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 70 March 2026
```

## File page 71

```text
CodeName Name Definition
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
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 71 March 2026
```

## File page 72

```text
CodeName Name Definition
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
BCBL BoardLot Board lots, not set for odd lots (UK
specific).
BCBN BadName Bad names, not set for good names (UK
specific).
BTEX BestExecution Trade to be executed done at best
execution.
CALL Call Trade to be executed following the
exercise of a call option on the security.
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 72 March 2026
```

