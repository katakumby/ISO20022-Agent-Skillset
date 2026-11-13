---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["14 sese.020.001.09 SecuritiesTransactionCancellationRequestV09", "14.2 Structure"]
file_pages: [460]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.020.001.09"]
---

# 14.2 Structure

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 460 to 460.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 460

```text
14.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesTxCxlReq> [1..1]  C12,
C18,
C20,
C22,
C25
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] ± 463
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 464
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 464
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 464
   NonceIdentification <NonceId> [0..1] Text 464
   AccountOwner <AcctOwnr> [0..1] ± 464
   SafekeepingAccount <SfkpgAcct> [0..1] ± 465
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 465
   TransactionDetails <TxDtls> [0..1]  465
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C7, C8,
C10,
C11,
C13
466
     TradeDate <TradDt> [0..1] ± 467
     SettlementDate <SttlmDt> [1..1] ± 468
     SettlementQuantity <SttlmQty> [1..1] ± 468
     SettlementAmount <SttlmAmt> [0..1] ± 468
     DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  469
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C7, C8,
C10,
C11,
C13
469
       ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 470
       CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  471
{Or         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 471
Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 471
Or}         LEI <LEI> [1..1] IdentifierSet 471
     DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C14,
C15,
C16,
C17
471
Approved by the Securities SEG on 27 January 2026 sese.020.001.09
SecuritiesTransactionCancellationRequestV09
Settlement And Reconciliation - Maintenance 2025 - 2026 460 March 2026
```

