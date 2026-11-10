---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks", "5.4.5 NetPositionReport <NetPosRpt>", "5.4.5.16 TradeLegDetails <TradLegDtls>", "5.4.5.16.1 TradeLegIdentification <TradLegId>"]
file_pages: [214]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.4.5.16.1 TradeLegIdentification <TradLegId>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 214 to 214.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 214

```text
Constraints
• TradeIdentificationPresenceRule
(Rule)
TradeIdentification Or TradeExecutionIdentification Or UniqueTransactionIdentifier Must be present.
Following Must be True
    /TradeIdentification Must be present
 Or    /TradeExecutionIdentification Must be present
 Or    /UniqueTransactionIdentifier Must be present
Error handling:
– Error severity: Fatal
– Error Code: X00658
– Error Text: TradeIdentification Or TradeExecutionIdentification Or UniqueTradeIdentifier Must be
present.
5.4.5.16.1  TradeLegIdentification <TradLegId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction (that is the trade leg) as know by the instructing
party.
Datatype: Max35Text on page 493
5.4.5.16.2  TradeIdentification <TradId>
Presence: [0..1]
Definition: Reference assigned to the trade by the investor or the trading party. This reference will be
used throughout the trade life cycle to access/update the trade details.
Datatype: Max35Text on page 493
5.4.5.16.3  TradeExecutionIdentification <TradExctnId>
Presence: [0..1]
Definition: Unique reference assigned by the trading venue when the trade is executed.
Datatype: Max35Text on page 493
5.4.5.16.4  UniqueTransactionIdentifier <UnqTxIdr>
Presence: [0..1]
Definition: Unique Transaction Identifier (UTI) as agreed with the other counterparty.
Datatype: UTIIdentifier on page 490
5.4.5.16.5  OrderIdentification <OrdrId>
Presence: [0..1]
Definition: Identifies the order sent by the final investor to an intermediary in order to initiate a trade in
the former's name. This identification is then matched with the equivalent trade by the clearing.
Datatype: Max35Text on page 493
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 214
```

