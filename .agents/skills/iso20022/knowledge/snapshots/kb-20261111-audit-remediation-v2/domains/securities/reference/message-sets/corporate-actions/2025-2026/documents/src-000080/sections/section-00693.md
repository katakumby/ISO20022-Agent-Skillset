---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.14 Market", "16.1.14.3 MarketIdentification3Choice", "16.1.14.3.1 MarketIdentifierCode <MktIdrCd>"]
file_pages: [884]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.14.3.1 MarketIdentifierCode <MktIdrCd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 884 to 884.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 884

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 884
Or}   Description <Desc> [1..1] Text 884
16.1.14.3.1  MarketIdentifierCode <MktIdrCd>
Presence: [1..1]
Definition: Market Identifier Code. Identification of a financial market, as stipulated in the norm ISO
10383 "Codes for exchanges and market identifications".
Datatype: "MICIdentifier" on page 1246
16.1.14.3.2  Description <Desc>
Presence: [1..1]
Definition: Description of the market when no Market Identifier Code is available.
Datatype: "Max35Text" on page 1251
16.1.14.4  MarketIdentification84
Definition: Context, or geographic environment, in which trading parties may meet in order to negotiate
and execute trades among themselves.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 884
   Type <Tp> [1..1] ± 885
Constraints
• MarketTypeAndIdentificationRule
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
16.1.14.4.1  Identification <Id>
Presence: [0..1]
Definition: Code allocated to places of trade, that is, stock exchanges, regulated markets, for example,
Electronic Trading Platforms (ECN), and unregulated markets, for example, Automated Trading
Systems (ATS), as sources of prices and related information, in order to facilitate automated
processing.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 884 February 2026
```

