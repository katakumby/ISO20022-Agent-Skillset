---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.26 CardTransaction <CardTx>", "2.4.2.15.18.2.26.3 Transaction <Tx>", "2.4.2.15.18.2.26.3.1 Aggregated <Aggtd>"]
file_pages: [248]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.26.3.1 Aggregated <Aggtd>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 248 to 248.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 248

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Product <Pdct> [0..1]  257
       ProductCode <PdctCd> [1..1] Text 258
       UnitOfMeasure <UnitOfMeasr> [0..1] CodeSet 258
       ProductQuantity <PdctQty> [0..1] Quantity 259
       UnitPrice <UnitPric> [0..1] Amount 259
       ProductAmount <PdctAmt> [0..1] Amount 259
       TaxType <TaxTp> [0..1] Text 260
       AdditionalProductInformation <AddtlPdctInf> [0..1] Text 260
     ValidationDate <VldtnDt> [0..1] Date 260
     ValidationSequenceNumber <VldtnSeqNb> [0..1] Text 260
2.4.2.15.18.2.26.3.1  Aggregated <Aggtd>
Presence: [1..1]
Definition: Card transaction details, based on card transaction aggregated data performed by the card
acquirer.
Aggregated <Aggtd> contains the following CardAggregated2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalService <AddtlSvc> [0..1] CodeSet 248
   TransactionCategory <TxCtgy> [0..1] CodeSet 249
   SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 249
   SequenceNumberRange <SeqNbRg> [0..1]  249
     FirstTransaction <FrstTx> [0..1] Text 249
     LastTransaction <LastTx> [0..1] Text 249
   TransactionDateRange <TxDtRg> [0..1] ± 250
2.4.2.15.18.2.26.3.1.1  AdditionalService <AddtlSvc>
Presence: [0..1]
Definition: Service in addition to the main service.
Datatype: "CardPaymentServiceType2Code" on page 890
CodeName Name Definition
AGGR Aggregation Aggregation of low payments.
DCCV DCC Dynamic currency conversion (DCC).
GRTT Gratuity Card payment with gratuity.
INSP Instalment Instalment payment.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
248 March 2026
```

