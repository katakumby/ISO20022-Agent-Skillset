---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.1 References <Refs>"]
file_pages: [380]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.1 References <Refs>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 380 to 380.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 380

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           AuthenticationMethod <AuthntcnMtd> [0..1]  515
             AuthenticationMethod <AuthntcnMtd> [1..1] CodeSet 515
             AuthenticationEntity <AuthntcnNtty> [1..1] CodeSet 515
         AdditionalService <AddtlSvc> [0..1] CodeSet 516
         TransactionCategory <TxCtgy> [0..1] CodeSet 516
         SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 516
         SaleReferenceNumber <SaleRefNb> [0..1] Text 517
         RePresentmentReason <RePresntmntRsn> [0..1] CodeSet 517
         SequenceNumber <SeqNb> [0..1] Text 517
         TransactionIdentification <TxId> [0..1] ± 517
         Product <Pdct> [0..1]  517
           ProductCode <PdctCd> [1..1] Text 518
           UnitOfMeasure <UnitOfMeasr> [0..1] CodeSet 518
           ProductQuantity <PdctQty> [0..1] Quantity 519
           UnitPrice <UnitPric> [0..1] Amount 519
           ProductAmount <PdctAmt> [0..1] Amount 519
           TaxType <TaxTp> [0..1] Text 520
           AdditionalProductInformation <AddtlPdctInf> [0..1] Text 520
         ValidationDate <VldtnDt> [0..1] Date 520
         ValidationSequenceNumber <VldtnSeqNb> [0..1] Text 520
     PrePaidAccount <PrePdAcct> [0..1] ± C20,
C18
520
   InstructionCopy <InstrCpy> [0..1] Text 521
   AdditionalTransactionInformation <AddtlTxInf> [0..1] Text 521
   SupplementaryData <SplmtryData> [0..*] ± C30 521
Constraints
• PaymentTypeOrLocalInstrumentRule
PaymentTypeInformation or LocalInstrument must be absent, both can be absent.
Following Must be True
    /PaymentTypeInformation Must be absent
 Or    /LocalInstrument Must be absent
3.4.2.15.18.2.1  References <Refs>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
380 March 2026
```

