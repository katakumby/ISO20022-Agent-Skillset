---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.67 SettlementInstructionGeneration1Code"]
file_pages: [646]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.67 SettlementInstructionGeneration1Code

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 646 to 646.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 646

```text
Type: CodeSet
CodeName Name Definition
REGU Regular Settlement takes place under the
standard rules applicable to the market
and instrument.
CASH Cash Settlement takes place on the trade
date.
NXTD NextDay Settlement takes place on the day after
trade date.
TONE TPlusOne Settlement takes place on the trade date
plus one business day.
TTWO TPlusTwo Settlement takes place on the trade date
plus two business days.
TTRE TPlusThree Settlement takes place on the trade date
plus three business days.
TFOR TPlusFour Settlement takes place on the trade date
plus four business days.
TFIV TPlusFive Settlement takes place on the trade date
plus five business days.
SELL SellersOption Settlement takes place at the choice/
option of the seller.
WDIS WhenDistributed Settlement takes place when the
financial instrument is distributed.
WHID WhenIssuedOrDistributed Settlement takes place when the
financial instrument is issued or
distributed.
TBAT ToBeAnnouncedTrade Settlement takes place as a result of a
"to be announced" trade.
WISS WhenIssued Settlement is to be done when the
security is issued.
7.2.2.67  SettlementInstructionGeneration1Code
Definition: Settlement Instruction Generation Code.
Type: CodeSet
CodeName Name Definition
GENS InstructionGenerationByETCProvider Specifies if the ETC service provider is
to generate a settlement instruction.
NOGE NotInstructionGenerationByETCProvider Specifies if the ETC service provider is
not to generate a settlement instruction
where a previous agreement to do so
exists.
7.2.2.68  SettlementStandingInstructionDatabase1Code
Definition: Indicates what settlement standing instruction database is to be used to derive the settlement
parties involved in the transaction.
Type: CodeSet
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 646 February 2025
```

