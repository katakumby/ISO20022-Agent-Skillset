---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.17 CardTransaction <CardTx>", "2.4.2.15.17.1 Card <Card>"]
file_pages: [82]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.17.1 Card <Card>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 82 to 82.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 82

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       POIComponentType <POICmpntTp> [1..1] CodeSet 91
       ManufacturerIdentification <ManfctrId> [0..1] Text 91
       Model <Mdl> [0..1] Text 91
       VersionNumber <VrsnNb> [0..1] Text 91
       SerialNumber <SrlNb> [0..1] Text 92
       ApprovalNumber <ApprvlNb> [0..*] Text 92
   AggregatedEntry <AggtdNtry> [0..1]  92
     AdditionalService <AddtlSvc> [0..1] CodeSet 92
     TransactionCategory <TxCtgy> [0..1] CodeSet 93
     SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 93
     SequenceNumberRange <SeqNbRg> [0..1]  93
       FirstTransaction <FrstTx> [0..1] Text 93
       LastTransaction <LastTx> [0..1] Text 93
     TransactionDateRange <TxDtRg> [0..1] ± 94
   PrePaidAccount <PrePdAcct> [0..1] ± C20,
C18
94
2.4.2.15.17.1  Card <Card>
Presence: [0..1]
Definition: Electronic money product that provides the cardholder with a portable and specialised
computer device, which typically contains a microprocessor.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
82 March 2026
```

