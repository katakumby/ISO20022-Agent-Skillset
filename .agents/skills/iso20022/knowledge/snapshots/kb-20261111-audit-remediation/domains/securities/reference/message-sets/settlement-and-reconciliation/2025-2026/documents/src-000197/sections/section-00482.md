---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12", "22.4 Message Building Blocks", "22.4.2 SettlementTypeAndAdditionalParameters <SttlmTpAndAddtlParams>"]
file_pages: [739]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.028.001.12"]
---

# 22.4.2 SettlementTypeAndAdditionalParameters <SttlmTpAndAddtlParams>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 739 to 739.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 739

```text
Definition: Unambiguous identification of the allegement notification known by the executing/servicing
party.
Datatype: "Max35Text" on page 2192
22.4.2 SettlementTypeAndAdditionalParameters
<SttlmTpAndAddtlParams>
Presence: [1..1]
Definition: Provides settlement type and identification information.
SettlementTypeAndAdditionalParameters <SttlmTpAndAddtlParams> contains the following
elements (see "SettlementTypeAndAdditionalParameters12" on page 1632 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1632
   Payment <Pmt> [1..1] CodeSet 1632
   CommonIdentification <CmonId> [0..1] Text 1633
22.4.3 MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
22.4.4 CounterpartyMarketInfrastructureTransactionIdentific
ation <CtrPtyMktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a counterparty transaction assigned by a market infrastructure other than a
central securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
22.4.5 TradeDetails <TradDtls>
Presence: [1..1]
Definition: Details of the trade.
Impacted by: C23 "LateDeliveryDateRule", C32 "PlaceOfTradeRule", C47 "TradeDateTimeUTCRule"
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 739 March 2026
```

