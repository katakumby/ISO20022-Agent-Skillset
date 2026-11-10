---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.2 Message Datatypes", "12.2.2 CodeSet", "12.2.2.18 MarketType2Code"]
file_pages: [479]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.2.2.18 MarketType2Code

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 479 to 479.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 479

```text
CodeName Name Definition
INDE InitialDeposit Margin required to enable a member to
start trading on a specific market where
high risks and amounts are involved.
NEMA NegociationMargin Margin calculated on the same basis as
for the variation margin but the margin is
kept by the central counterparty and not
"paid " to the other clearing member.
INMA InitialMargin Margin required for absorbing future
market price fluctuations (market risks)
occurring between the default of a
member and close-out of unsettled
securities positions by the central
counterparty.
VAMA VariationMargin Margin required to cover the risk linked
to the price fluctuations occurred on the
unsettled exposures towards central
counterparty.
INCA IncreaseCoverageAmount Additional margin required to cover a risk
increase (expressed in the reporting
currency). This results from a risk
management decision depending on
central counterparty specific criteria.
12.2.2.18  MarketType2Code
Definition: Specifies the type of market in which transactions take place, for example, primary.
Type: CodeSet
CodeName Name Definition
PRIM PrimaryMarket The place is a primary market.
SECM SecondaryMarket The place is a secondary market.
OTCO OverTheCounter The place is over the counter.
VARI Various Various places.
EXCH StockExchange The place is a stock exchange.
12.2.2.19  MarketType5Code
Definition: Specifies the type of place where a trade was executed, a price was sourced from, an
instrument is listed.
Type: CodeSet
CodeName Name Definition
OTCO OverTheCounter The place is over the counter.
EXCH StockExchange The place is a stock exchange.
12.2.2.20  NamePrefix1Code
Definition: Specifies the terms used to formally address a person.
Type: CodeSet
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 479
```

