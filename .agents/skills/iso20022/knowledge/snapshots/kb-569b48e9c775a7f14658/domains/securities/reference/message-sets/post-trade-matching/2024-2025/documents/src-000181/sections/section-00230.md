---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Market", "7.1.18.4 MarketIdentification3Choice", "7.1.18.4.1 MarketIdentifierCode <MktIdrCd>"]
file_pages: [284]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18.4.1 MarketIdentifierCode <MktIdrCd>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 284 to 284.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 284

```text
7.1.18.4.1  MarketIdentifierCode <MktIdrCd>
Presence: [1..1]
Definition: Market Identifier Code. Identification of a financial market, as stipulated in the norm ISO
10383 "Codes for exchanges and market identifications".
Datatype: "MICIdentifier" on page 664
7.1.18.4.2  Description <Desc>
Presence: [1..1]
Definition: Description of the market when no Market Identifier Code is available.
Datatype: "Max35Text" on page 669
7.1.18.5  MarketIdentification97
Definition: Context, or geographic environment, in which trading parties may meet in order to negotiate
and execute trades among themselves.
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
7.1.18.5.1  Identification <Id>
Presence: [0..1]
Definition: Code allocated to places of trade, ie, stock exchanges, regulated markets, eg, Electronic
Trading Platforms (ECN), and unregulated markets, eg, Automated Trading Systems (ATS), as sources
of prices and related information, in order to facilitate automated processing.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 284 February 2025
```

