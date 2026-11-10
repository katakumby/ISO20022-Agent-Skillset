---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.17 CardTransaction <CardTx>", "4.4.2.14.17.1 Card <Card>"]
file_pages: [600]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.17.1 Card <Card>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 600 to 600.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 600

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       POIComponentType <POICmpntTp> [1..1] CodeSet 609
       ManufacturerIdentification <ManfctrId> [0..1] Text 609
       Model <Mdl> [0..1] Text 609
       VersionNumber <VrsnNb> [0..1] Text 609
       SerialNumber <SrlNb> [0..1] Text 610
       ApprovalNumber <ApprvlNb> [0..*] Text 610
   AggregatedEntry <AggtdNtry> [0..1]  610
     AdditionalService <AddtlSvc> [0..1] CodeSet 610
     TransactionCategory <TxCtgy> [0..1] CodeSet 611
     SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 611
     SequenceNumberRange <SeqNbRg> [0..1]  611
       FirstTransaction <FrstTx> [0..1] Text 611
       LastTransaction <LastTx> [0..1] Text 611
     TransactionDateRange <TxDtRg> [0..1] ± 612
   PrePaidAccount <PrePdAcct> [0..1] ± C19,
C17
612
4.4.2.14.17.1  Card <Card>
Presence: [0..1]
Definition: Electronic money product that provides the cardholder with a portable and specialised
computer device, which typically contains a microprocessor.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
600 March 2026
```

