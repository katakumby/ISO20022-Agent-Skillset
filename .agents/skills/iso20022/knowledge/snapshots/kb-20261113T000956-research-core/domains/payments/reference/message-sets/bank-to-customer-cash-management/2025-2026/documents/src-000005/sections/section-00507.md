---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.20 Tax <Tax>", "4.4.2.14.18.2.20.11 Record <Rcrd>", "4.4.2.14.18.2.20.11.1 Type <Tp>"]
file_pages: [736]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.20.11.1 Type <Tp>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 736 to 736.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 736

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 736
   Category <Ctgy> [0..1] Text 736
   CategoryDetails <CtgyDtls> [0..1] Text 736
   DebtorStatus <DbtrSts> [0..1] Text 737
   CertificateIdentification <CertId> [0..1] Text 737
   FormsCode <FrmsCd> [0..1] Text 737
   Period <Prd> [0..1]  737
     Year <Yr> [0..1] Year 737
     Type <Tp> [0..1] CodeSet 737
     FromToDate <FrToDt> [0..1] ± 738
   TaxAmount <TaxAmt> [0..1]  739
     Rate <Rate> [0..1] Rate 739
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 739
     TotalAmount <TtlAmt> [0..1] Amount C2, C6 739
     Details <Dtls> [0..*]  740
       Period <Prd> [0..1]  740
         Year <Yr> [0..1] Year 740
         Type <Tp> [0..1] CodeSet 741
         FromToDate <FrToDt> [0..1] ± 741
       Amount <Amt> [1..1] Amount C2, C6 742
   AdditionalInformation <AddtlInf> [0..1] Text 742
4.4.2.14.18.2.20.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.20.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.20.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
736 March 2026
```

