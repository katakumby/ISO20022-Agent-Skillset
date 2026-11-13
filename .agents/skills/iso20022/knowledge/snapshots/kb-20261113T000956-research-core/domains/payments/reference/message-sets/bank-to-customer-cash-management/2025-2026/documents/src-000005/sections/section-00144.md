---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.20 Tax <Tax>", "2.4.2.15.18.2.20.11 Record <Rcrd>", "2.4.2.15.18.2.20.11.1 Type <Tp>"]
file_pages: [218]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.20.11.1 Type <Tp>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 218 to 218.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 218

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 218
   Category <Ctgy> [0..1] Text 218
   CategoryDetails <CtgyDtls> [0..1] Text 218
   DebtorStatus <DbtrSts> [0..1] Text 219
   CertificateIdentification <CertId> [0..1] Text 219
   FormsCode <FrmsCd> [0..1] Text 219
   Period <Prd> [0..1]  219
     Year <Yr> [0..1] Year 219
     Type <Tp> [0..1] CodeSet 219
     FromToDate <FrToDt> [0..1] ± 220
   TaxAmount <TaxAmt> [0..1]  221
     Rate <Rate> [0..1] Rate 221
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 221
     TotalAmount <TtlAmt> [0..1] Amount C2, C6 221
     Details <Dtls> [0..*]  222
       Period <Prd> [0..1]  222
         Year <Yr> [0..1] Year 222
         Type <Tp> [0..1] CodeSet 223
         FromToDate <FrToDt> [0..1] ± 223
       Amount <Amt> [1..1] Amount C2, C6 224
   AdditionalInformation <AddtlInf> [0..1] Text 224
2.4.2.15.18.2.20.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.20.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.20.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
218 March 2026
```

