---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.15 RemittanceInformation <RmtInf>", "2.4.2.15.18.2.15.2 Structured <Strd>", "2.4.2.15.18.2.15.2.6 TaxRemittance <TaxRmt>", "2.4.2.15.18.2.15.2.6.11 Record <Rcrd>", "2.4.2.15.18.2.15.2.6.11.1 Type <Tp>"]
file_pages: [195]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.15.2.6.11.1 Type <Tp>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 195 to 195.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 195

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 195
   Category <Ctgy> [0..1] Text 195
   CategoryDetails <CtgyDtls> [0..1] Text 195
   DebtorStatus <DbtrSts> [0..1] Text 196
   CertificateIdentification <CertId> [0..1] Text 196
   FormsCode <FrmsCd> [0..1] Text 196
   Period <Prd> [0..1]  196
     Year <Yr> [0..1] Year 196
     Type <Tp> [0..1] CodeSet 196
     FromToDate <FrToDt> [0..1] ± 197
   TaxAmount <TaxAmt> [0..1]  198
     Rate <Rate> [0..1] Rate 198
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 198
     TotalAmount <TtlAmt> [0..1] Amount C2, C6 198
     Details <Dtls> [0..*]  199
       Period <Prd> [0..1]  199
         Year <Yr> [0..1] Year 199
         Type <Tp> [0..1] CodeSet 200
         FromToDate <FrToDt> [0..1] ± 200
       Amount <Amt> [1..1] Amount C2, C6 201
   AdditionalInformation <AddtlInf> [0..1] Text 201
2.4.2.15.18.2.15.2.6.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.15.2.6.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.15.2.6.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
195 March 2026
```

