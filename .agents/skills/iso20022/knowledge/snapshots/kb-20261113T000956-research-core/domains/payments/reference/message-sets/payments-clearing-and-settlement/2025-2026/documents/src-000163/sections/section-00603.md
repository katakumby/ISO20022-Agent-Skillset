---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.47 RemittanceInformation <RmtInf>", "6.4.2.47.2 Structured <Strd>", "6.4.2.47.2.6 TaxRemittance <TaxRmt>", "6.4.2.47.2.6.11 Record <Rcrd>", "6.4.2.47.2.6.11.1 Type <Tp>"]
file_pages: [816]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.47.2.6.11.1 Type <Tp>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 816 to 816.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 816

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 816
   Category <Ctgy> [0..1] Text 816
   CategoryDetails <CtgyDtls> [0..1] Text 816
   DebtorStatus <DbtrSts> [0..1] Text 817
   CertificateIdentification <CertId> [0..1] Text 817
   FormsCode <FrmsCd> [0..1] Text 817
   Period <Prd> [0..1]  817
     Year <Yr> [0..1] Year 817
     Type <Tp> [0..1] CodeSet 817
     FromToDate <FrToDt> [0..1] ± 818
   TaxAmount <TaxAmt> [0..1]  819
     Rate <Rate> [0..1] Rate 819
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C12 819
     TotalAmount <TtlAmt> [0..1] Amount C2, C12 819
     Details <Dtls> [0..*]  820
       Period <Prd> [0..1]  820
         Year <Yr> [0..1] Year 820
         Type <Tp> [0..1] CodeSet 821
         FromToDate <FrToDt> [0..1] ± 821
       Amount <Amt> [1..1] Amount C2, C12 822
   AdditionalInformation <AddtlInf> [0..1] Text 822
6.4.2.47.2.6.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 1246
6.4.2.47.2.6.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 1246
6.4.2.47.2.6.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
816 March 2026
```

