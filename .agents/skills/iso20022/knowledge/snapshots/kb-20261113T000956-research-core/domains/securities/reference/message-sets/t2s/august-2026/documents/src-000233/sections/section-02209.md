---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.18 Market", "82.1.18.4 MarketIdentification3Choice"]
file_pages: [2972]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.18.4 MarketIdentification3Choice

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2972 to 2972.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2972

```text
Datatype: "Max35Text" on page 3328
82.1.18.4  MarketIdentification3Choice
Definition: Choice of market identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 2972
Or}   Description <Desc> [1..1] Text 2972
82.1.18.4.1  MarketIdentifierCode <MktIdrCd>
Presence: [1..1]
Definition: Market Identifier Code. Identification of a financial market, as stipulated in the norm ISO
10383 "Codes for exchanges and market identifications".
Datatype: "MICIdentifier" on page 3322
82.1.18.4.2  Description <Desc>
Presence: [1..1]
Definition: Description of the market when no Market Identifier Code is available.
Datatype: "Max35Text" on page 3328
82.1.18.5  PlaceOfTradeIdentification1
Definition: Identification of market in which a trade transaction has been executed.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MarketTypeAndIdentification <MktTpAndId> [0..1] ± C17 2972
   LEI <LEI> [0..1] IdentifierSet 2973
82.1.18.5.1  MarketTypeAndIdentification <MktTpAndId>
Presence: [0..1]
Definition: Identification and type of the place of trade.
Impacted by: C17 "MarketTypeAndIdentificationRule"
MarketTypeAndIdentification <MktTpAndId> contains the following elements (see
"MarketIdentification84" on page 2973 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 2973
   Type <Tp> [1..1] ± 2973
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2972 August 2026
```

