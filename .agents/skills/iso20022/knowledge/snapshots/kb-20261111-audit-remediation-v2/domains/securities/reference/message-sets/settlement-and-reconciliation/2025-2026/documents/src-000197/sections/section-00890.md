---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06", "34.2 Structure"]
file_pages: [1324]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.040.001.06"]
---

# 34.2 Structure

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1324 to 1324.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1324

```text
34.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesSttlmTxCtrPtyRspn> [1..1]  
   TransactionIdentification <TxId> [1..1]  1327
     AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 1327
     AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1327
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 1327
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 1327
   ResponseStatus <RspnSts> [1..1] ± 1327
   TransactionDetails <TxDtls> [0..1]  C17,
C19,
C21
1328
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C7, C8,
C10,
C11,
C12
1330
     SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1331
     Payment <Pmt> [1..1] CodeSet 1331
     SettlementQuantity <SttlmQty> [1..1] ± 1331
     SafekeepingAccount <SfkpgAcct> [0..1] ± 1332
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1332
     SettlementAmount <SttlmAmt> [0..1] ± 1332
     DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  1333
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C7, C8,
C10,
C11,
C12
1333
       ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 1334
       CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  1335
{Or         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1335
Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 1335
Or}         LEI <LEI> [1..1] IdentifierSet 1335
     SettlementDate <SttlmDt> [1..1] ± 1335
     TradeDate <TradDt> [0..1] ± 1336
     DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C13,
C14,
1336
Approved by the Securities SEG on 27 January 2026 sese.040.001.06
SecuritiesSettlementTransactionCounterpartyRespo
nseV06
Settlement And Reconciliation - Maintenance 2025 - 2026 1324 March 2026
```

