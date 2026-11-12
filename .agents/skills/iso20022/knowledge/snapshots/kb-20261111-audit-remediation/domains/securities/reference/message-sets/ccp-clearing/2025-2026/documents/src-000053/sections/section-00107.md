---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks", "4.4.5 StatementDetails <StmtDtls>", "4.4.5.4 TradeLegsDetails <TradLegsDtls>", "4.4.5.4.1 MarginAccount <MrgnAcct>"]
file_pages: [146]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.4.5.4.1 MarginAccount <MrgnAcct>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 146 to 146.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 146

```text
Constraints
• DepositoryOrPlaceOfListingPresenceRule
(Rule)
Depository or PlaceOfListing must be present.
Following Must be True
    /PlaceOfListing Must be present
 Or    /SettlementDetails/Depository Must be present
Error handling:
– Error severity: Fatal
– Error Code: X00200
– Error Text: Either Depository or PlaceOfListing must be present
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
4.4.5.4.1  MarginAccount <MrgnAcct>
Presence: [0..1]
Definition: Margin account where the negotiation and liquidation risks will be calculated.
MarginAccount <MrgnAcct> contains the following elements (see SecuritiesAccount19 on page 375
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 375
   Type <Tp> [0..1] ± 375
   Name <Nm> [0..1] Text 375
4.4.5.4.2  DeliveryAccount <DlvryAcct>
Presence: [0..1]
Definition: Account opened by the central counterparty in the name of the clearing member or its
settlement agent within the account structure, for settlement purposes (gives information about the
clearing member/its settlement agent account at the central securities depository).
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 146
```

