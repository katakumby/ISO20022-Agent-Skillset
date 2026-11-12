---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.26 CardTransaction <CardTx>", "4.4.2.14.18.2.26.3 Transaction <Tx>", "4.4.2.14.18.2.26.3.1 Aggregated <Aggtd>"]
file_pages: [766]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.26.3.1 Aggregated <Aggtd>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 766 to 766.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 766

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Product <Pdct> [0..1]  775
       ProductCode <PdctCd> [1..1] Text 776
       UnitOfMeasure <UnitOfMeasr> [0..1] CodeSet 776
       ProductQuantity <PdctQty> [0..1] Quantity 777
       UnitPrice <UnitPric> [0..1] Amount 777
       ProductAmount <PdctAmt> [0..1] Amount 777
       TaxType <TaxTp> [0..1] Text 778
       AdditionalProductInformation <AddtlPdctInf> [0..1] Text 778
     ValidationDate <VldtnDt> [0..1] Date 778
     ValidationSequenceNumber <VldtnSeqNb> [0..1] Text 778
4.4.2.14.18.2.26.3.1  Aggregated <Aggtd>
Presence: [1..1]
Definition: Card transaction details, based on card transaction aggregated data performed by the card
acquirer.
Aggregated <Aggtd> contains the following CardAggregated2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalService <AddtlSvc> [0..1] CodeSet 766
   TransactionCategory <TxCtgy> [0..1] CodeSet 767
   SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 767
   SequenceNumberRange <SeqNbRg> [0..1]  767
     FirstTransaction <FrstTx> [0..1] Text 767
     LastTransaction <LastTx> [0..1] Text 767
   TransactionDateRange <TxDtRg> [0..1] ± 768
4.4.2.14.18.2.26.3.1.1  AdditionalService <AddtlSvc>
Presence: [0..1]
Definition: Service in addition to the main service.
Datatype: "CardPaymentServiceType2Code" on page 890
CodeName Name Definition
AGGR Aggregation Aggregation of low payments.
DCCV DCC Dynamic currency conversion (DCC).
GRTT Gratuity Card payment with gratuity.
INSP Instalment Instalment payment.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
766 March 2026
```

