---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks", "5.4.5 NetPositionReport <NetPosRpt>", "5.4.5.16 TradeLegDetails <TradLegDtls>", "5.4.5.16.15 PlaceOfTrade <PlcOfTrad>"]
file_pages: [219]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.4.5.16.15 PlaceOfTrade <PlcOfTrad>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 219 to 219.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 219

```text
GrossAmount <GrssAmt> contains the following elements (see AmountAndDirection21 on page 377
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount   'C2,
  'C6
377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 378
5.4.5.16.15  PlaceOfTrade <PlcOfTrad>
Presence: [1..1]
Definition: Place at which the security is traded.
Impacted by: C12 MarketTypeAndIdentificationRule
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
5.4.5.16.16  PlaceOfListing <PlcOfListg>
Presence: [0..1]
Definition: Place where the referenced financial instrument is listed.
Impacted by: C13 MarketTypeAndIdentificationRule
PlaceOfListing <PlcOfListg> contains the following MarketIdentification85 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 220
   Type <Tp> [1..1] ± 220
Constraints
• MarketTypeAndIdentificationRule
(Rule)
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 219
```

