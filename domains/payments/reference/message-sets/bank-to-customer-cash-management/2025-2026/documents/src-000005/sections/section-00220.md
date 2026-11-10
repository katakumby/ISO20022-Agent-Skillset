---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.17 CardTransaction <CardTx>", "3.4.2.15.17.1 Card <Card>"]
file_pages: [342]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.17.1 Card <Card>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 342 to 342.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 342

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       POIComponentType <POICmpntTp> [1..1] CodeSet 351
       ManufacturerIdentification <ManfctrId> [0..1] Text 351
       Model <Mdl> [0..1] Text 351
       VersionNumber <VrsnNb> [0..1] Text 351
       SerialNumber <SrlNb> [0..1] Text 352
       ApprovalNumber <ApprvlNb> [0..*] Text 352
   AggregatedEntry <AggtdNtry> [0..1]  352
     AdditionalService <AddtlSvc> [0..1] CodeSet 352
     TransactionCategory <TxCtgy> [0..1] CodeSet 353
     SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 353
     SequenceNumberRange <SeqNbRg> [0..1]  353
       FirstTransaction <FrstTx> [0..1] Text 353
       LastTransaction <LastTx> [0..1] Text 353
     TransactionDateRange <TxDtRg> [0..1] ± 354
   PrePaidAccount <PrePdAcct> [0..1] ± C20,
C18
354
3.4.2.15.17.1  Card <Card>
Presence: [0..1]
Definition: Electronic money product that provides the cardholder with a portable and specialised
computer device, which typically contains a microprocessor.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
342 March 2026
```

