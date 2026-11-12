---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.172 PortfolioWithdrawalReason1Code"]
file_pages: [5343]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.172 PortfolioWithdrawalReason1Code

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5343 to 5343.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5343

```text
66.2.2.172  PortfolioWithdrawalReason1Code
Definition: Specifies a reason for a withdrawal from the investment product.
Type: CodeSet
CodeName Name Definition
FTRS FirstTimeResidentialProperty Withdrawal is for a first time residential
property.
66.2.2.173  PositionEffect3Code
Definition: Specifies the order in which events are processed.
Type: CodeSet
CodeName Name Definition
FIFO Fifo First in, first out. Results in a position
obtained after having sold in priority the
securities bought chronologically.
LIFO Lifo Last in, last out. Results in a position
obtained after having sold in priority the
securities bought chronologically.
66.2.2.174  PriceMethod1Code
Definition: Specifies the type of pricing calculation method.
Type: CodeSet
CodeName Name Definition
FORW ForwardPrice Price will be calculated after the close of
the dealing period. An investor,
therefore, does not know the exact buy
or sell price.
HIST HistoricalPrice Price is calculated at an earlier valuation
point preceding the dealing period. An
investor, therefore, knows the exact buy
or sell price.
66.2.2.175  PriceReportFunction1Code
Definition: Specifies the function of the price report.
Type: CodeSet
CodeName Name Definition
REPL CompleteReplacementPriceReport The price report conveys the correction
of the complete set of prices previously
sent for the same price report
identification.
NEWP NewPriceReport The price report is 'new', that is the
report is not being used as a correction
of previously sent prices.
PART PartialCorrectionPriceReport The price report conveys the correction
of some of the prices previously sent for
the same price report identification.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5343 May 2026
```

