---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.15 Market", "35.1.15.7 MarketType8Choice", "35.1.15.7.2 Proprietary <Prtry>"]
file_pages: [1529]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.15.7.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1529 to 1529.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1529

```text
CodeName Name Definition
PRIM PrimaryMarket The place is a primary market.
SECM SecondaryMarket The place is a secondary market.
OTCO OverTheCounter The place is over the counter.
VARI Various Various places.
EXCH StockExchange The place is a stock exchange.
35.1.15.7.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Market type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.15.8  MarketIdentification5Choice
Definition: Choice of market identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 1529
Or}   Description <Desc> [1..1] Text 1529
35.1.15.8.1  MarketIdentifierCode <MktIdrCd>
Presence: [1..1]
Definition: ISO 10383 Market Identification Code.
Datatype: "MICIdentifier" on page 2187
35.1.15.8.2  Description <Desc>
Presence: [1..1]
Definition: Description of the market when no Market Identifier Code is available.
Datatype: "Max140Text" on page 2191
35.1.16 Miscellaneous
35.1.16.1  ExposureType25Choice
Definition: Choice of format for the exposure information.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1529 March 2026
```

