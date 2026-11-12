---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["2 MX secl.001.001.05 TradeLegNotificationV05", "2.4 Message Building Blocks", "2.4.6 TradeLegDetails <TradLegDtls>", "2.4.6.19 PlaceOfListing <PlcOfListg>", "2.4.6.19.1 Identification <Id>"]
file_pages: [50]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.001.001.05"]
---

# 2.4.6.19.1 Identification <Id>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 50 to 50.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 50

```text
Definition: Place at which the security is listed.
Impacted by: C16 MarketTypeAndIdentificationRule
PlaceOfListing <PlcOfListg> contains the following MarketIdentification85 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 50
   Type <Tp> [1..1] ± 50
Constraints
• MarketTypeAndIdentificationRule
(Rule)
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
2.4.6.19.1  Identification <Id>
Presence: [0..1]
Definition: Code allocated to places of trade, ie, stock exchanges, regulated markets, eg, Electronic
Trading Platforms (ECN), and unregulated markets, eg, Automated Trading Systems (ATS), as sources
of prices and related information, in order to facilitate automated processing.
Identification <Id> contains one of the following elements (see MarketIdentification1Choice on
page 435 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 435
Or}   Description <Desc> [1..1] Text 435
2.4.6.19.2  Type <Tp>
Presence: [1..1]
Definition: Nature of a market in which transactions take place.
Type <Tp> contains one of the following elements (see MarketType9Choice on page 437 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 437
Or}   Proprietary <Prtry> [1..1] ± 437
2.4.6.20  TradeType <TradTp>
Presence: [1..1]
Definition: Identifies the type of trade transaction.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 50
```

