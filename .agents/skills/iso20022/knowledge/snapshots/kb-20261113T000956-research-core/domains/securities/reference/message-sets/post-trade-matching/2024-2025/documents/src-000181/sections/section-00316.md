---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.55 PartialFill4", "7.1.19.55.3 TradeDate <TradDt>"]
file_pages: [380]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.55.3 TradeDate <TradDt>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 380 to 380.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 380

```text
7.1.19.55.3  TradeDate <TradDt>
Presence: [0..1]
Definition: Specifies the date/time on which the trade was executed.
TradeDate <TradDt> contains one of the following elements (see "TradeDate7Choice" on page 267 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 267
Or}   Value <Val> [1..1]  267
{Or     Code <Cd> [1..1] CodeSet 267
Or}     Proprietary <Prtry> [1..1] ± 268
7.1.19.55.4  PlaceOfTrade <PlcOfTrad>
Presence: [0..1]
Definition: Market in which a trade transaction is to be or has been executed.
Impacted by: C17 "IdentificationPresenceRule", C24 "MarketTypeAndIdentificationRule", C34
"PlaceOfTradeRule"
PlaceOfTrade <PlcOfTrad> contains the following elements (see "MarketIdentification97" on page 284
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 284
   Type <Tp> [0..1] ± 285
Constraints
• IdentificationPresenceRule
If Type/Code is not Various (VARI) OR Over The Counter (OTCO) then Identification must be
present.
• MarketTypeAndIdentificationRule
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
• PlaceOfTradeRule
If the trade was executed on multiple places of trade and the place of trade field is used, code VARI
must be used.
7.1.19.55.5  OriginalOrderedQuantity <OrgnlOrdrdQty>
Presence: [1..1]
Definition: Quantity of financial instrument ordered.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 380 February 2025
```

