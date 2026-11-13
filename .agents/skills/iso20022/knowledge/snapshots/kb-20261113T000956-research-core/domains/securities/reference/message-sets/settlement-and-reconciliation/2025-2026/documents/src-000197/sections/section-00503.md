---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["23 sese.029.001.08 SecuritiesSettlementAllegementRemovalAdviceV08", "23.2 Structure"]
file_pages: [769]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.029.001.08"]
---

# 23.2 Structure

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 769 to 769.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 769

```text
23.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesSttlmAllgmtRmvlAdvc> [1..1]  C17,
C19,
C21
   AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] ± 772
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 772
   CounterpartyMarketInfrastructureTransactionIdentification
<CtrPtyMktInfrstrctrTxId>
[0..1] Text 772
   AccountOwner <AcctOwnr> [0..1] ± 772
   SafekeepingAccount <SfkpgAcct> [0..1] ± 773
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 773
   TransactionDetails <TxDtls> [0..1]  773
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C7, C8,
C10,
C11,
C12
774
     TradeDate <TradDt> [0..1] ± 775
     SettlementDate <SttlmDt> [1..1] ± 776
     SettlementQuantity <SttlmQty> [1..1] ± 776
     SettlementAmount <SttlmAmt> [0..1] ± 776
     DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  777
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C7, C8,
C10,
C11,
C12
777
       ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 778
       CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  779
{Or         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 779
Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 779
Or}         LEI <LEI> [1..1] IdentifierSet 779
     DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C13,
C14,
C15,
C16
779
     ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C13,
C14,
C15,
C16
780
Approved by the Securities SEG on 27 January 2026 sese.029.001.08
SecuritiesSettlementAllegementRemovalAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 769 March 2026
```

