---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.1 EntryReference <NtryRef>"]
file_pages: [587]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.1 EntryReference <NtryRef>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 587 to 587.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 587

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             AdditionalService <AddtlSvc> [0..1] CodeSet 774
             TransactionCategory <TxCtgy> [0..1] CodeSet 774
             SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 774
             SaleReferenceNumber <SaleRefNb> [0..1] Text 775
             RePresentmentReason <RePresntmntRsn> [0..1] CodeSet 775
             SequenceNumber <SeqNb> [0..1] Text 775
             TransactionIdentification <TxId> [0..1] ± 775
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
         PrePaidAccount <PrePdAcct> [0..1] ± C19,
C17
778
       InstructionCopy <InstrCpy> [0..1] Text 779
       AdditionalTransactionInformation <AddtlTxInf> [0..1] Text 779
       SupplementaryData <SplmtryData> [0..*] ± C29 779
   AdditionalEntryInformation <AddtlNtryInf> [0..1] Text 779
Constraints
• ReferenceGuideline
At least one reference should be present to identify the underlying transaction(s).
4.4.2.14.1  EntryReference <NtryRef>
Presence: [0..1]
Definition: Unique reference for the entry.
Datatype: "Max35Text" on page 916
4.4.2.14.2  Amount <Amt>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
587 March 2026
```

