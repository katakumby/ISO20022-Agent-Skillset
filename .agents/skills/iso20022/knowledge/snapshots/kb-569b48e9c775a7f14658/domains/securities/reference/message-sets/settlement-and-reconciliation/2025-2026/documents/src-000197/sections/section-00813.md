---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.2 Deletion <Deltn>", "32.4.2.2.3 TradeDetails <TradDtls>", "32.4.2.2.3.1 TradeIdentification <TradId>"]
file_pages: [1221]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.2.3.1 TradeIdentification <TradId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1221 to 1221.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1221

```text
• TradeDateGuideline
In addition to the settlement date (ISO 20022 mandatory), trade date is one of the 10 common
elements recommended by SMPG for equities and fixed income settlement instructions.
For more details, see the relevant market practice document on www.smpg.info.
• TradeDateTimeUTCRule
If Trade Date/Time is used with a time or a time + UTC indicator, then it must be the local time of the
place of trade, for example, of the stock exchange, or of the selling broker for OTC.
32.4.2.2.3.1  TradeIdentification <TradId>
Presence: [0..1]
Definition: Reference assigned to the trade by the investor or the trading party. This reference will be
used throughout the trade life cycle to access/update the trade details.
Datatype: "Max35Text" on page 2192
32.4.2.2.3.2  UniqueTransactionIdentifier <UnqTxIdr>
Presence: [0..1]
Definition: Unique Transaction Identifier (UTI) as agreed with the other counterparty.
Datatype: "UTIIdentifier" on page 2188
32.4.2.2.3.3  CollateralTransactionIdentification <CollTxId>
Presence: [0..*]
Definition: Unambiguous identification of a collateral transaction as assigned by the instructing party.
Datatype: "Max35Text" on page 2192
32.4.2.2.3.4  PlaceOfTrade <PlcOfTrad>
Presence: [0..1]
Definition: Market in which a trade transaction has been executed.
PlaceOfTrade <PlcOfTrad> contains the following elements (see "PlaceOfTradeIdentification1" on
page 1527 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MarketTypeAndIdentification <MktTpAndId> [0..1] ± C27 1527
   LEI <LEI> [0..1] IdentifierSet 1527
32.4.2.2.3.5  PlaceOfClearing <PlcOfClr>
Presence: [0..1]
Definition: Infrastructure which may be a component of a clearing house and which facilitates clearing
and settlement for its members by standing between the buyer and the seller. It may net transactions
and it substitutes itself as settlement counterparty for each position.
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1221 March 2026
```

