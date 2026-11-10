---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.46 TradeType4Choice"]
file_pages: [355]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.46 TradeType4Choice

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 355 to 355.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 355

```text
Definition: Settlement capacity expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.46  TradeType4Choice
Definition: Choice of format for the trade type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 355
Or}   Proprietary <Prtry> [1..1] ± 356
7.1.19.46.1  Code <Cd>
Presence: [1..1]
Definition: Trade type information expressed as an ISO 20022 code.
Datatype: "TradeType3Code" on page 653
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
BRBR BrokerToBroker A trade from a broker to another broker.
RISK RiskTrade Trade involving risk.
VWAP VWAPGuarantee Trade whose price is guaranteed as the
weighted average of the trade prices on
a specific day.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 355 February 2025
```

