---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "26.4 Message Building Blocks", "26.4.3 Linkages <Lnkgs>", "26.4.4.1 TradeIdentification <TradId>"]
file_pages: [839]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.032.001.13"]
---

# 26.4.4.1 TradeIdentification <TradId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 839 to 839.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 839

```text
For more details, see the relevant market practice document on www.smpg.info.
• TradeDateTimeUTCRule
If Trade Date/Time is present with a time or a time + UTC indicator, then it must be the local time of
the place of trade, for example, of the stock exchange, or of the selling broker for OTC.
26.4.4.1  TradeIdentification <TradId>
Presence: [0..*]
Definition: Reference assigned to the trade by the investor or the trading party. This reference will be
used throughout the trade life cycle to access/update the trade details.
Datatype: "Max35Text" on page 2192
26.4.4.2  UniqueTransactionIdentifier <UnqTxIdr>
Presence: [0..1]
Definition: Unique Transaction Identifier (UTI) as agreed with the other counterparty.
Datatype: "UTIIdentifier" on page 2188
26.4.4.3  CollateralTransactionIdentification <CollTxId>
Presence: [0..*]
Definition: Unambiguous identification of a collateral transaction as assigned by the instructing party.
Datatype: "Max35Text" on page 2192
26.4.4.4  PlaceOfTrade <PlcOfTrad>
Presence: [0..1]
Definition: Market in which a trade transaction has been executed.
PlaceOfTrade <PlcOfTrad> contains the following elements (see "PlaceOfTradeIdentification1" on
page 1527 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MarketTypeAndIdentification <MktTpAndId> [0..1] ± C27 1527
   LEI <LEI> [0..1] IdentifierSet 1527
26.4.4.5  PlaceOfClearing <PlcOfClr>
Presence: [0..1]
Definition: Infrastructure which may be a component of a clearing house and which facilitates clearing
and settlement for its members by standing between the buyer and the seller. It may net transactions
and it substitutes itself as settlement counterparty for each position.
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 839 March 2026
```

