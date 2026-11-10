---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks", "11.4.6 ReportDetails <RptDtls>", "11.4.6.2 SettlementObligationDetails <SttlmOblgtnDtls>", "11.4.6.2.15 AdditionalSettlementObligationDetails <AddtlSttlmOblgtnDtls>", "11.4.6.2.15.2 ObligationType <OblgtnTp>", "11.4.6.2.15.2.1 Code <Cd>"]
file_pages: [364]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4.6.2.15.2.1 Code <Cd>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 364 to 364.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 364

```text
11.4.6.2.15.2.1  Code <Cd>
Presence: [1..1]
Definition: Indicates the type of the obligation using a code.
Datatype: ObligationType1Code on page 480
CodeName Name Definition
FAIL Fails Specifies that the obligation is related to
a failed trade.
NEW1 New Specifies that the obligation is related to
new a trade.
COEV CorporateEvent Specifies that the obligation is related to
a corporate event.
11.4.6.2.15.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Indicates the type of the obligation using a proprietary format.
Proprietary <Prtry> contains the following elements (see GenericIdentification30 on page 400 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 400
   Issuer <Issr> [1..1] Text 401
   SchemeName <SchmeNm> [0..1] Text 401
11.4.6.2.15.3  Description <Desc>
Presence: [0..1]
Definition: Provides additional information related to the linked obligation.
Datatype: Max35Text on page 493
11.4.6.2.15.4  TradeDate <TradDt>
Presence: [0..1]
Definition: Provides the original trade date.
Datatype: ISODate on page 487
11.4.6.2.15.5  Quantity <Qty>
Presence: [1..1]
Definition: Specifies the quantity related to the settlement obligation.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 364
```

