---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks", "11.4.6 ReportDetails <RptDtls>", "11.4.6.2 SettlementObligationDetails <SttlmOblgtnDtls>", "11.4.6.2.7 TradeDate <TradDt>"]
file_pages: [338]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4.6.2.7 TradeDate <TradDt>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 338 to 338.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 338

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
11.4.6.2.7  TradeDate <TradDt>
Presence: [0..1]
Definition: Provides the trade date.
TradeDate <TradDt> contains one of the following TradeDate3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 338
Or}   DateCode <DtCd> [1..1] CodeSet 338
11.4.6.2.7.1  Date <Dt>
Presence: [1..1]
Definition: Trade date expressed as an ISO 20022 code.
Datatype: ISODate on page 487
11.4.6.2.7.2  DateCode <DtCd>
Presence: [1..1]
Definition: Date expressed as a code.
Datatype: DateType1Code on page 476
CodeName Name Definition
UKWN Unknown Date is unknown by the sender or has
not been established.
11.4.6.2.8  TradingCapacity <TradgCpcty>
Presence: [0..1]
Definition: Identifies the trading capacity of seller.
Datatype: TradingCapacity5Code on page 486
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 338
```

