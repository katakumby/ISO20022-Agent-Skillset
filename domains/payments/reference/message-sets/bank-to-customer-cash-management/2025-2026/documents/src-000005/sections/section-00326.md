---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.20 Tax <Tax>", "3.4.2.15.18.2.20.11 Record <Rcrd>", "3.4.2.15.18.2.20.11.1 Type <Tp>"]
file_pages: [478]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.20.11.1 Type <Tp>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 478 to 478.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 478

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 478
   Category <Ctgy> [0..1] Text 478
   CategoryDetails <CtgyDtls> [0..1] Text 478
   DebtorStatus <DbtrSts> [0..1] Text 479
   CertificateIdentification <CertId> [0..1] Text 479
   FormsCode <FrmsCd> [0..1] Text 479
   Period <Prd> [0..1]  479
     Year <Yr> [0..1] Year 479
     Type <Tp> [0..1] CodeSet 479
     FromToDate <FrToDt> [0..1] ± 480
   TaxAmount <TaxAmt> [0..1]  481
     Rate <Rate> [0..1] Rate 481
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 481
     TotalAmount <TtlAmt> [0..1] Amount C2, C6 481
     Details <Dtls> [0..*]  482
       Period <Prd> [0..1]  482
         Year <Yr> [0..1] Year 482
         Type <Tp> [0..1] CodeSet 483
         FromToDate <FrToDt> [0..1] ± 483
       Amount <Amt> [1..1] Amount C2, C6 484
   AdditionalInformation <AddtlInf> [0..1] Text 484
3.4.2.15.18.2.20.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.20.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.20.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
478 March 2026
```

