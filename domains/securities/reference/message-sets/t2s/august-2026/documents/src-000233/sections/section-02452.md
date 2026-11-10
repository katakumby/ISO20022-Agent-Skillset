---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.87 MarketType2Code"]
file_pages: [3263]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.87 MarketType2Code

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3263 to 3263.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3263

```text
82.2.2.87  MarketType2Code
Definition: Specifies the type of market in which transactions take place, for example, primary.
Type: CodeSet
CodeName Name Definition
PRIM PrimaryMarket The place is a primary market.
SECM SecondaryMarket The place is a secondary market.
OTCO OverTheCounter The place is over the counter.
VARI Various Various places.
EXCH StockExchange The place is a stock exchange.
82.2.2.88  MarketType4Code
Definition: Specifies the type of place where a trade was executed, a price was sourced from, an
instrument is listed.
Type: CodeSet
CodeName Name Definition
FUND Fund The place is a fund (transfer agent, fund
itself, etc.).
LMAR LocalMarket The place is a local market.
THEO Theoretical The place is theoretical.
VEND Vendor The place is a vendor.
82.2.2.89  MatchingProcess1Code
Definition: Specifies the action to be performed on the matching process.
Type: CodeSet
CodeName Name Definition
UNMT Unmatch The referenced transaction is requested
to be unmatched.
MTRE ResumeMatching Matching process is to be resumed for
the referenced transaction.
82.2.2.90  MatchingStatus1Code
Definition: Provides the matching status of the instruction at the time the settlement instruction was
sent.
Type: CodeSet
CodeName Name Definition
MACH Matched Instruction has been matched.
NMAT Unmatched Instruction has not been matched.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3263 August 2026
```

