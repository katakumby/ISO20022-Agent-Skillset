---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.12 Market", "12.1.12.3 MarketIdentification20", "12.1.12.3.2 Type <Tp>"]
file_pages: [436]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.12.3.2 Type <Tp>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 436 to 436.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 436

```text
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
12.1.12.3.2  Type <Tp>
Presence: [1..1]
Definition: Nature of a market in which transactions take place.
Type <Tp> contains one of the following elements (see MarketType8Choice on page 434 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 434
Or}   Proprietary <Prtry> [1..1] ± 434
12.1.12.4  MarketIdentification84
Definition: Context, or geographic environment, in which trading parties may meet in order to negotiate
and execute trades among themselves.
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
12.1.12.4.1  Identification <Id>
Presence: [0..1]
Definition: Code allocated to places of trade, that is, stock exchanges, regulated markets, for example,
Electronic Trading Platforms (ECN), and unregulated markets, for example, Automated Trading
Systems (ATS), as sources of prices and related information, in order to facilitate automated
processing.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 436
```

