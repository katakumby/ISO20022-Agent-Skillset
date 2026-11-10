---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.12 Market"]
file_pages: [434]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.12 Market

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 434 to 434.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 434

```text
– Error Text: Invalid currency code
• CurrencyAmount
(Rule)
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Error handling:
– Error severity: Fatal
– Error Code: D00007
– Error Text: Invalid currency code or too many decimal digits.
12.1.12 Market
12.1.12.1  MarketType8Choice
Definition: Choice of format for the market type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 434
Or}   Proprietary <Prtry> [1..1] ± 434
12.1.12.1.1  Code <Cd>
Presence: [1..1]
Definition: Market type expressed as an ISO 20022 code.
Datatype: MarketType2Code on page 479
CodeName Name Definition
PRIM PrimaryMarket The place is a primary market.
SECM SecondaryMarket The place is a secondary market.
OTCO OverTheCounter The place is over the counter.
VARI Various Various places.
EXCH StockExchange The place is a stock exchange.
12.1.12.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Market type expressed as a proprietary code.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 434
```

