---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["3 MX secl.002.001.05 TradeLegNotificationCancellationV05", "3.4 Message Building Blocks", "3.4.6 TradeLegDetails <TradLegDtls>", "3.4.6.17 AccruedInterestAmount <AcrdIntrstAmt>"]
file_pages: [107]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.002.001.05"]
---

# 3.4.6.17 AccruedInterestAmount <AcrdIntrstAmt>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 107 to 107.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 107

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
3.4.6.17  AccruedInterestAmount <AcrdIntrstAmt>
Presence: [0..1]
Definition: Interest that has accumulated on a bond since the last interest payment up to, but not
including, the settlement date.
AccruedInterestAmount <AcrdIntrstAmt> contains the following elements (see
AmountAndDirection21 on page 377 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount   'C2,
  'C6
377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 378
3.4.6.18  PlaceOfTrade <PlcOfTrad>
Presence: [1..1]
Definition: Place at which the security is traded.
Impacted by: C15 MarketTypeAndIdentificationRule
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
3.4.6.19  PlaceOfListing <PlcOfListg>
Presence: [0..1]
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 107
```

