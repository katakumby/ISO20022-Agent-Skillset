---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks", "5.4.5 NetPositionReport <NetPosRpt>", "5.4.5.16 TradeLegDetails <TradLegDtls>", "5.4.5.16.6 AllocationIdentification <AllcnId>"]
file_pages: [215]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.4.5.16.6 AllocationIdentification <AllcnId>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 215 to 215.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 215

```text
5.4.5.16.6  AllocationIdentification <AllcnId>
Presence: [0..1]
Definition: Identifies the portion of assets within a determined trade that shall be allocated to different
clients.
Datatype: Max35Text on page 493
5.4.5.16.7  TradeDate <TradDt>
Presence: [1..1]
Definition: Provides the date and time of trade transaction.
Datatype: ISODate on page 487
5.4.5.16.8  TransactionDateAndTime <TxDtAndTm>
Presence: [0..1]
Definition: Date and time used to determine the price applicable to a trade. If the trade is registered
"after market" hours, the trading price will the price of the day but the actual trade date will be the next
working day.
Datatype: ISODateTime on page 487
5.4.5.16.9  SettlementDate <SttlmDt>
Presence: [1..1]
Definition: Provides the contractual settlement date.
SettlementDate <SttlmDt> contains one of the following DateFormat66Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 215
Or}   DateCode <DtCd> [1..1]  215
{Or     Code <Cd> [1..1] CodeSet 216
Or}     Proprietary <Prtry> [1..1] ± 216
5.4.5.16.9.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as a calendar date.
Datatype: ISODate on page 487
5.4.5.16.9.2  DateCode <DtCd>
Presence: [1..1]
Definition: Date is expressed using a code.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 215
```

