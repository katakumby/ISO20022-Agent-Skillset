---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.33 MarketType2Code"]
file_pages: [515]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.33 MarketType2Code

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 515 to 515.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 515

```text
CodeName Name Definition
CLNT ClientSide Instruction is for a client side transaction.
MAKT MarketSide Instruction is for a market side
transaction.
7.2.2.33  MarketType2Code
Definition: Specifies the type of market in which transactions take place, for example, primary.
Type: CodeSet
CodeName Name Definition
PRIM PrimaryMarket The place is a primary market.
SECM SecondaryMarket The place is a secondary market.
OTCO OverTheCounter The place is over the counter.
VARI Various Various places.
EXCH StockExchange The place is a stock exchange.
7.2.2.34  MarketType4Code
Definition: Specifies the type of place where a trade was executed, a price was sourced from, an
instrument is listed.
Type: CodeSet
CodeName Name Definition
FUND Fund The place is a fund (transfer agent, fund
itself, etc.).
LMAR LocalMarket The place is a local market.
THEO Theoretical The place is theoretical.
VEND Vendor The place is a vendor.
7.2.2.35  MatchingStatus1Code
Definition: Provides the matching status of the instruction at the time the settlement instruction was
sent.
Type: CodeSet
CodeName Name Definition
MACH Matched Instruction has been matched.
NMAT Unmatched Instruction has not been matched.
7.2.2.36  NamePrefix2Code
Definition: Specifies the terms used to formally address a person.
Type: CodeSet
CodeName Name Definition
DOCT Doctor Title of the person is Doctor or Dr.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 515 March 2026
```

