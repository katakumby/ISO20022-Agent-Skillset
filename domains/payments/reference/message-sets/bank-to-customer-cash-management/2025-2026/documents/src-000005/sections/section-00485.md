---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.15 RemittanceInformation <RmtInf>", "4.4.2.14.18.2.15.2 Structured <Strd>", "4.4.2.14.18.2.15.2.6 TaxRemittance <TaxRmt>", "4.4.2.14.18.2.15.2.6.11 Record <Rcrd>", "4.4.2.14.18.2.15.2.6.11.1 Type <Tp>"]
file_pages: [713]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.15.2.6.11.1 Type <Tp>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 713 to 713.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 713

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 713
   Category <Ctgy> [0..1] Text 713
   CategoryDetails <CtgyDtls> [0..1] Text 713
   DebtorStatus <DbtrSts> [0..1] Text 714
   CertificateIdentification <CertId> [0..1] Text 714
   FormsCode <FrmsCd> [0..1] Text 714
   Period <Prd> [0..1]  714
     Year <Yr> [0..1] Year 714
     Type <Tp> [0..1] CodeSet 714
     FromToDate <FrToDt> [0..1] ± 715
   TaxAmount <TaxAmt> [0..1]  716
     Rate <Rate> [0..1] Rate 716
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 716
     TotalAmount <TtlAmt> [0..1] Amount C2, C6 716
     Details <Dtls> [0..*]  717
       Period <Prd> [0..1]  717
         Year <Yr> [0..1] Year 717
         Type <Tp> [0..1] CodeSet 718
         FromToDate <FrToDt> [0..1] ± 718
       Amount <Amt> [1..1] Amount C2, C6 719
   AdditionalInformation <AddtlInf> [0..1] Text 719
4.4.2.14.18.2.15.2.6.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.15.2.6.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.15.2.6.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
713 March 2026
```

