---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09", "21.2 Structure"]
file_pages: [710]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.027.001.09"]
---

# 21.2 Structure

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 710 to 710.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 710

```text
21.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesTxCxlReqStsAdvc> [1..1]  C24
   CancellationRequestReference <CxlReqRef> [1..1] Text 713
   TransactionIdentification <TxId> [0..1] ± C13 713
   ProcessingStatus <PrcgSts> [1..1]  714
{Or     PendingCancellation <PdgCxl> [1..1] ± 714
Or     Rejected <Rjctd> [1..1] ± 714
Or     Repair <Rpr> [1..1] ± 715
Or     AcknowledgedAccepted <AckdAccptd> [1..1] ± 715
Or     Proprietary <Prtry> [1..1] ± 715
Or     Denied <Dnd> [1..1] ± 716
Or}     Cancelled <Canc> [1..1] ± 716
   TransactionDetails <TxDtls> [0..1]  C19,
C21,
C23
716
     AccountOwner <AcctOwnr> [0..1] ± 718
     SafekeepingAccount <SfkpgAcct> [0..1] ± 718
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 718
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C8, C9,
C11,
C12,
C14
719
     SettlementQuantity <SttlmQty> [1..1] ± 720
     SettlementAmount <SttlmAmt> [0..1] ± 720
     DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  720
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C8, C9,
C11,
C12,
C14
721
       ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 722
       CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  722
{Or         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 722
Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C4 722
Or}         LEI <LEI> [1..1] IdentifierSet 723
     TradeDate <TradDt> [0..1] ± 723
Approved by the Securities SEG on 27 January 2026 sese.027.001.09
SecuritiesTransactionCancellationRequestStatusAd
viceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 710 March 2026
```

