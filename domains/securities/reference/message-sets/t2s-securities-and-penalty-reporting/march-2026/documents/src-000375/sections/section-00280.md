---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.17 Market", "7.1.17.4 MarketIdentification3Choice"]
file_pages: [357]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.17.4 MarketIdentification3Choice

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 357 to 357.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 357

```text
Datatype: "Max35Text" on page 557
7.1.17.4  MarketIdentification3Choice
Definition: Choice of market identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 357
Or}   Description <Desc> [1..1] Text 357
7.1.17.4.1  MarketIdentifierCode <MktIdrCd>
Presence: [1..1]
Definition: Market Identifier Code. Identification of a financial market, as stipulated in the norm ISO
10383 "Codes for exchanges and market identifications".
Datatype: "MICIdentifier" on page 553
7.1.17.4.2  Description <Desc>
Presence: [1..1]
Definition: Description of the market when no Market Identifier Code is available.
Datatype: "Max35Text" on page 557
7.1.17.5  PlaceOfTradeIdentification1
Definition: Identification of market in which a trade transaction has been executed.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MarketTypeAndIdentification <MktTpAndId> [0..1] ± C17 357
   LEI <LEI> [0..1] IdentifierSet 358
7.1.17.5.1  MarketTypeAndIdentification <MktTpAndId>
Presence: [0..1]
Definition: Identification and type of the place of trade.
Impacted by: C17 "MarketTypeAndIdentificationRule"
MarketTypeAndIdentification <MktTpAndId> contains the following elements (see
"MarketIdentification84" on page 358 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 358
   Type <Tp> [1..1] ± 358
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 357 March 2026
```

