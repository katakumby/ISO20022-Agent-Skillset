---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.1 EntryReference <NtryRef>"]
file_pages: [329]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.1 EntryReference <NtryRef>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 329 to 329.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 329

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
   AdditionalEntryInformation <AddtlNtryInf> [0..1] Text 521
Constraints
• ReferenceGuideline
At least one reference should be present to identify the underlying transaction(s).
3.4.2.15.1  EntryReference <NtryRef>
Presence: [0..1]
Definition: Unique reference for the entry.
Datatype: "Max35Text" on page 916
3.4.2.15.2  Amount <Amt>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
329 March 2026
```

