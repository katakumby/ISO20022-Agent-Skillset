---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.40 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "7.4.2.40.29 Tax <Tax>", "7.4.2.40.29.11 Record <Rcrd>", "7.4.2.40.29.11.1 Type <Tp>"]
file_pages: [935]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.40.29.11.1 Type <Tp>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 935 to 935.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 935

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 935
   Category <Ctgy> [0..1] Text 935
   CategoryDetails <CtgyDtls> [0..1] Text 935
   DebtorStatus <DbtrSts> [0..1] Text 936
   CertificateIdentification <CertId> [0..1] Text 936
   FormsCode <FrmsCd> [0..1] Text 936
   Period <Prd> [0..1]  936
     Year <Yr> [0..1] Year 936
     Type <Tp> [0..1] CodeSet 936
     FromToDate <FrToDt> [0..1] ± 937
   TaxAmount <TaxAmt> [0..1]  938
     Rate <Rate> [0..1] Rate 938
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C9 938
     TotalAmount <TtlAmt> [0..1] Amount C2, C9 938
     Details <Dtls> [0..*]  939
       Period <Prd> [0..1]  939
         Year <Yr> [0..1] Year 939
         Type <Tp> [0..1] CodeSet 940
         FromToDate <FrToDt> [0..1] ± 940
       Amount <Amt> [1..1] Amount C2, C9 941
   AdditionalInformation <AddtlInf> [0..1] Text 941
7.4.2.40.29.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 1246
7.4.2.40.29.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 1246
7.4.2.40.29.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
935 March 2026
```

