---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks", "4.4.5 StatementDetails <StmtDtls>", "4.4.5.4 TradeLegsDetails <TradLegsDtls>", "4.4.5.4.20 PlaceOfListing <PlcOfListg>"]
file_pages: [154]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.4.5.4.20 PlaceOfListing <PlcOfListg>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 154 to 154.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 154

```text
PlaceOfTrade <PlcOfTrad> contains the following elements (see MarketIdentification84 on page 436
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 436
   Type <Tp> [1..1] ± 437
Constraints
• MarketTypeAndIdentificationRule
(Rule)
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
4.4.5.4.20  PlaceOfListing <PlcOfListg>
Presence: [0..1]
Definition: Place at which the security is listed.
Impacted by: C16 MarketTypeAndIdentificationRule
PlaceOfListing <PlcOfListg> contains the following MarketIdentification85 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 154
   Type <Tp> [1..1] ± 155
Constraints
• MarketTypeAndIdentificationRule
(Rule)
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
4.4.5.4.20.1  Identification <Id>
Presence: [0..1]
Definition: Code allocated to places of trade, ie, stock exchanges, regulated markets, eg, Electronic
Trading Platforms (ECN), and unregulated markets, eg, Automated Trading Systems (ATS), as sources
of prices and related information, in order to facilitate automated processing.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 154
```

