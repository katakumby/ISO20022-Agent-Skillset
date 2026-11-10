---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.14 Market", "16.1.14.4 MarketIdentification84", "16.1.14.4.2 Type <Tp>"]
file_pages: [885]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.14.4.2 Type <Tp>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 885 to 885.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 885

```text
Identification <Id> contains one of the following elements (see "MarketIdentification1Choice" on
page 883 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 883
Or}   Description <Desc> [1..1] Text 883
16.1.14.4.2  Type <Tp>
Presence: [1..1]
Definition: Nature of a market in which transactions take place.
Type <Tp> contains one of the following elements (see "MarketType8Choice" on page 885 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 885
Or}   Proprietary <Prtry> [1..1] ± 885
16.1.14.5  MarketType8Choice
Definition: Choice of format for the market type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 885
Or}   Proprietary <Prtry> [1..1] ± 885
16.1.14.5.1  Code <Cd>
Presence: [1..1]
Definition: Market type expressed as an ISO 20022 code.
Datatype: "MarketType2Code" on page 1219
CodeName Name Definition
PRIM PrimaryMarket The place is a primary market.
SECM SecondaryMarket The place is a secondary market.
OTCO OverTheCounter The place is over the counter.
VARI Various Various places.
EXCH StockExchange The place is a stock exchange.
16.1.14.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Market type expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 885 February 2026
```

