---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Market", "7.1.18.2 MarketIdentification93"]
file_pages: [282]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18.2 MarketIdentification93

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 282 to 282.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 282

```text
7.1.18.2  MarketIdentification93
Definition: Context, or geographic environment, in which trading parties may meet in order to negotiate
and execute trades among themselves.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 282
   Type <Tp> [0..1] ± 282
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
7.1.18.2.1  Identification <Id>
Presence: [0..1]
Definition: Code allocated to places of trade, ie, stock exchanges, regulated markets, eg, Electronic
Trading Platforms (ECN), and unregulated markets, eg, Automated Trading Systems (ATS), as sources
of prices and related information, in order to facilitate automated processing.
Identification <Id> contains one of the following elements (see "MarketIdentification3Choice" on
page 283 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 284
Or}   Description <Desc> [1..1] Text 284
7.1.18.2.2  Type <Tp>
Presence: [0..1]
Definition: Nature of a market in which transactions take place.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 282 February 2025
```

