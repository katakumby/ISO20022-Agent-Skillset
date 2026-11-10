---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.78 TradeType3Code"]
file_pages: [653]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.78 TradeType3Code

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 653 to 653.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 653

```text
CodeName Name Definition
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
SPCU SpecialCumDividend Indicates whether the trade is executed
with a special cum
dividend, that is, buying after the ex date
and getting the dividend.
SPEX SpecialExDividend Indicates whether the trade is executed
with a special ex
dividend, that is, selling before the ex
date without the coupon.
GTDL GuaranteedDelivery Indicates whether the delivery of the
financial instrument on settlement date
is guaranteed.
7.2.2.78  TradeType3Code
Definition: Specifies the type of executed order.
Type: CodeSet
CodeName Name Definition
BSKT Basket A basket trade, i.e. a unit of 15 or more
financial instruments used in program
trading.
INDX Index A trade of a predetermined set of
financial instruments.
IPOO IPO Transaction is an Initial Public Offer
(IPO) order.
LIST List A trade of a predetermined set of
financial instruments.
PRAL PreAllocation A pre-allocated trade.
PROG Program A program trade, i.e. a computer-driven
trade of buying and selling of baskets of
15 or more financial instruments by
index arbitrage specialists or institutional
traders.
TRAD Trade An executed order.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 653 February 2025
```

