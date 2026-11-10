---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["9 MX secl.008.001.03 BuyInResponseV03", "9.4 Message Building Blocks", "9.4.3 OriginalSettlementObligationDetails <OrgnlSttlmOblgtnDtls>", "9.4.3.11 TradeDate <TradDt>"]
file_pages: [290]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.008.001.03"]
---

# 9.4.3.11 TradeDate <TradDt>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 290 to 290.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 290

```text
Error handling:
– Error severity: Fatal
– Error Code: X00194
– Error Text: At least one identification must be present.
• OtherIdentificationPresenceRule
(Rule)
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
Error handling:
– Error severity: Fatal
– Error Code: X00193
– Error Text: At least one identification must be present.
9.4.3.11  TradeDate <TradDt>
Presence: [0..1]
Definition: Provides the trade date.
Datatype: ISODate on page 487
9.4.3.12  DealPrice <DealPric>
Presence: [0..1]
Definition: Provides the price of the trade.
DealPrice <DealPric> contains the following elements (see Price4 on page 465 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 465
   Type <Tp> [0..1] CodeSet 466
9.4.3.13  Quantity <Qty>
Presence: [1..1]
Definition: Provides the quantity of the trade.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.008.001.03 BuyInResponseV03
March 2026 290
```

