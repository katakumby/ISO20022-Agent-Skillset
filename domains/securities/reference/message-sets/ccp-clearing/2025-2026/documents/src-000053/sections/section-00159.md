---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks", "5.4.5 NetPositionReport <NetPosRpt>", "5.4.5.14 TradeDate <TradDt>"]
file_pages: [210]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.4.5.14 TradeDate <TradDt>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 210 to 210.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 210

```text
PlaceOfTrade <PlcOfTrad> contains the following elements (see MarketIdentification20 on page 435
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 435
   Type <Tp> [1..1] ± 436
Constraints
• MarketTypeAndIdentificationRule
(Rule)
If MarketType is OverTheCounter (OTCO), then Identification/Description must specify a system. If
MarketType is Exchange (EXCH), then Identification/MarketIdentificationCode must be present.
5.4.5.14  TradeDate <TradDt>
Presence: [0..1]
Definition: Provides the date of the trade.
Datatype: ISODate on page 487
5.4.5.15  SettlementDate <SttlmDt>
Presence: [0..1]
Definition: Provides the contractual settlement date.
SettlementDate <SttlmDt> contains one of the following DateFormat66Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 210
Or}   DateCode <DtCd> [1..1]  210
{Or     Code <Cd> [1..1] CodeSet 211
Or}     Proprietary <Prtry> [1..1] ± 211
5.4.5.15.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as a calendar date.
Datatype: ISODate on page 487
5.4.5.15.2  DateCode <DtCd>
Presence: [1..1]
Definition: Date is expressed using a code.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 210
```

