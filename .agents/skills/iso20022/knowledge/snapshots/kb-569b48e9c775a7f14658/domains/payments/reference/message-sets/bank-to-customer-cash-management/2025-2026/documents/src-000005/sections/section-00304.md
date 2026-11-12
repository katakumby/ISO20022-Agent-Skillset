---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.15 RemittanceInformation <RmtInf>", "3.4.2.15.18.2.15.2 Structured <Strd>", "3.4.2.15.18.2.15.2.6 TaxRemittance <TaxRmt>", "3.4.2.15.18.2.15.2.6.11 Record <Rcrd>", "3.4.2.15.18.2.15.2.6.11.1 Type <Tp>"]
file_pages: [455]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.15.2.6.11.1 Type <Tp>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 455 to 455.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 455

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 455
   Category <Ctgy> [0..1] Text 455
   CategoryDetails <CtgyDtls> [0..1] Text 455
   DebtorStatus <DbtrSts> [0..1] Text 456
   CertificateIdentification <CertId> [0..1] Text 456
   FormsCode <FrmsCd> [0..1] Text 456
   Period <Prd> [0..1]  456
     Year <Yr> [0..1] Year 456
     Type <Tp> [0..1] CodeSet 456
     FromToDate <FrToDt> [0..1] ± 457
   TaxAmount <TaxAmt> [0..1]  458
     Rate <Rate> [0..1] Rate 458
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 458
     TotalAmount <TtlAmt> [0..1] Amount C2, C6 458
     Details <Dtls> [0..*]  459
       Period <Prd> [0..1]  459
         Year <Yr> [0..1] Year 459
         Type <Tp> [0..1] CodeSet 460
         FromToDate <FrToDt> [0..1] ± 460
       Amount <Amt> [1..1] Amount C2, C6 461
   AdditionalInformation <AddtlInf> [0..1] Text 461
3.4.2.15.18.2.15.2.6.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.15.2.6.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.15.2.6.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
455 March 2026
```

