---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.44 MarketClientSide1Code"]
file_pages: [635]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.44 MarketClientSide1Code

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 635 to 635.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 635

```text
Type: CodeSet
CodeName Name Definition
ODTR OnDemandTrade Contract applies to a specific security
only.
EXTR ExclusiveTrade Contract applies to a number of different
securities within the same pool/fund.
7.2.2.44  MarketClientSide1Code
Definition: Specifies if an instruction is for a market or client side transaction.
Type: CodeSet
CodeName Name Definition
CLNT ClientSide Instruction is for a client side transaction.
MAKT MarketSide Instruction is for a market side
transaction.
7.2.2.45  MarketType2Code
Definition: Specifies the type of market in which transactions take place, for example, primary.
Type: CodeSet
CodeName Name Definition
PRIM PrimaryMarket The place is a primary market.
SECM SecondaryMarket The place is a secondary market.
OTCO OverTheCounter The place is over the counter.
VARI Various Various places.
EXCH StockExchange The place is a stock exchange.
7.2.2.46  MarketType6Code
Definition: Specifies the type of place where a trade was executed, a price was sourced from, an
instrument is listed.
Type: CodeSet
CodeName Name Definition
OTCO OverTheCounter The place is over the counter.
VARI Various Various places.
EXCH StockExchange The place is a stock exchange.
7.2.2.47  MatchingStatus1Code
Definition: Provides the matching status of the instruction at the time the settlement instruction was
sent.
Type: CodeSet
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 635 February 2025
```

