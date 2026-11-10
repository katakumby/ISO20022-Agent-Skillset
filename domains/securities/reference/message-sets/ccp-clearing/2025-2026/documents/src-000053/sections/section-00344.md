---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.12 Market", "12.1.12.4 MarketIdentification84", "12.1.12.4.2 Type <Tp>"]
file_pages: [437]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.12.4.2 Type <Tp>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 437 to 437.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 437

```text
Identification <Id> contains one of the following elements (see MarketIdentification1Choice on
page 435 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 435
Or}   Description <Desc> [1..1] Text 435
12.1.12.4.2  Type <Tp>
Presence: [1..1]
Definition: Nature of a market in which transactions take place.
Type <Tp> contains one of the following elements (see MarketType8Choice on page 434 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 434
Or}   Proprietary <Prtry> [1..1] ± 434
12.1.12.5  MarketType9Choice
Definition: Choice of format for the market type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 437
Or}   Proprietary <Prtry> [1..1] ± 437
12.1.12.5.1  Code <Cd>
Presence: [1..1]
Definition: Market type expressed as an ISO 20022 code.
Datatype: MarketType5Code on page 479
CodeName Name Definition
OTCO OverTheCounter The place is over the counter.
EXCH StockExchange The place is a stock exchange.
12.1.12.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Market type expressed as a proprietary code.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 437
```

