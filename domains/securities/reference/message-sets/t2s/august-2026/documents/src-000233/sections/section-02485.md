---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.170 TradeTransactionCondition2Code"]
file_pages: [3309]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.170 TradeTransactionCondition2Code

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3309 to 3309.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3309

```text
CodeName Name Definition
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
SPPR SpecialPrice Indicates whether the trade is executed
with a special price.
82.2.2.170  TradeTransactionCondition2Code
Definition: Specifies the conditions under which the order/trade is to be executed.
Type: CodeSet
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3309 August 2026
```

