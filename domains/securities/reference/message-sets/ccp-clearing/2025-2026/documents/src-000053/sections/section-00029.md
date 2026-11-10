---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["2 MX secl.001.001.05 TradeLegNotificationV05", "2.4 Message Building Blocks", "2.4.6 TradeLegDetails <TradLegDtls>", "2.4.6.1 TradeLegIdentification <TradLegId>"]
file_pages: [42]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.001.001.05"]
---

# 2.4.6.1 TradeLegIdentification <TradLegId>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 42 to 42.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 42

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}     Proprietary <Prtry> [1..1]  61
       Identification <Id> [0..1] Text 62
       Type <Tp> [1..1] ± 62
   SafekeepingAccount <SfkpgAcct> [0..1] ± 62
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
2.4.6.1  TradeLegIdentification <TradLegId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction (that is the trade leg) as known by the
instructing party.
Datatype: Max35Text on page 493
2.4.6.2  TradeIdentification <TradId>
Presence: [0..1]
Definition: Reference assigned to the trade by the investor or the trading party. This reference will be
used throughout the trade life cycle to access/update the trade details.
Datatype: Max35Text on page 493
2.4.6.3  TradeExecutionIdentification <TradExctnId>
Presence: [0..1]
Definition: Unique reference assigned by the trading venue when the trade is executed.
Datatype: Max35Text on page 493
2.4.6.4  UniqueTransactionIdentifier <UnqTxIdr>
Presence: [0..1]
Definition: Unique Transaction Identifier (UTI) as agreed with the other counterparty.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 42
```

