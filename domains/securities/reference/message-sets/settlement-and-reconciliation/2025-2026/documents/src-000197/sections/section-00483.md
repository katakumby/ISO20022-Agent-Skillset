---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12", "22.4 Message Building Blocks", "22.4.4 CounterpartyMarketInfrastructureTransactionIdentification <CtrPtyMktInfrstrctrTxId>", "22.4.5.1 TradeIdentification <TradId>"]
file_pages: [740]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.028.001.12"]
---

# 22.4.5.1 TradeIdentification <TradId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 740 to 740.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 740

```text
TradeDetails <TradDtls> contains the following SecuritiesTradeDetails151 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeIdentification <TradId> [0..*] Text 740
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 740
   CollateralTransactionIdentification <CollTxId> [0..*] Text 741
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..*] Text 741
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 741
   PlaceOfTrade <PlcOfTrad> [0..1] ± 741
   PlaceOfClearing <PlcOfClr> [0..1] ± 741
   TradeDate <TradDt> [0..1] ± 742
   SettlementDate <SttlmDt> [1..1] ± 742
   DealPrice <DealPric> [0..1] ± 742
   NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C25 743
   TradeTransactionCondition <TradTxCond> [0..*] ± 743
   TypeOfPrice <TpOfPric> [0..1] ± 743
Constraints
• LateDeliveryDateRule
If LateDeliveryDate is used, then the transaction must be a pool trade that results from the original
TBA (To Be Announced). The original TBA would be offset by an opposite transaction and replaced
by buys or sells of individual pools. It is a date greater than the settlement date stated in the trade,
for pools designed as settling late.
• PlaceOfTradeRule
If PlaceOfTrade is used and an ISO 10383 MIC exists for the market to be identified, then the ISO
10383 Market Identifier Code (MIC) must be used.
• TradeDateTimeUTCRule
If Trade Date/Time is used with a time or a time + UTC indicator, then it must be the local time of the
place of trade, for example, of the stock exchange, or of the selling broker for OTC.
22.4.5.1  TradeIdentification <TradId>
Presence: [0..*]
Definition: Reference assigned to the trade by the investor or the trading party. This reference will be
used throughout the trade life cycle to access/update the trade details.
Datatype: "Max35Text" on page 2192
22.4.5.2  UniqueTransactionIdentifier <UnqTxIdr>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 740 March 2026
```

