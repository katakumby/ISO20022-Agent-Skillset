---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.3 TransactionInformation <TxInf>", "5.4.3.21 OriginalTransactionReference <OrgnlTxRef>", "5.4.3.21.11 RemittanceInformation <RmtInf>", "5.4.3.21.11.2 Structured <Strd>", "5.4.3.21.11.2.6 TaxRemittance <TaxRmt>", "5.4.3.21.11.2.6.11 Record <Rcrd>", "5.4.3.21.11.2.6.11.1 Type <Tp>"]
file_pages: [674]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.3.21.11.2.6.11.1 Type <Tp>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 674 to 674.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 674

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 674
   Category <Ctgy> [0..1] Text 674
   CategoryDetails <CtgyDtls> [0..1] Text 674
   DebtorStatus <DbtrSts> [0..1] Text 675
   CertificateIdentification <CertId> [0..1] Text 675
   FormsCode <FrmsCd> [0..1] Text 675
   Period <Prd> [0..1]  675
     Year <Yr> [0..1] Year 675
     Type <Tp> [0..1] CodeSet 675
     FromToDate <FrToDt> [0..1] ± 676
   TaxAmount <TaxAmt> [0..1]  677
     Rate <Rate> [0..1] Rate 677
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C11 677
     TotalAmount <TtlAmt> [0..1] Amount C2, C11 677
     Details <Dtls> [0..*]  678
       Period <Prd> [0..1]  678
         Year <Yr> [0..1] Year 678
         Type <Tp> [0..1] CodeSet 679
         FromToDate <FrToDt> [0..1] ± 679
       Amount <Amt> [1..1] Amount C2, C11 680
   AdditionalInformation <AddtlInf> [0..1] Text 680
5.4.3.21.11.2.6.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 1246
5.4.3.21.11.2.6.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 1246
5.4.3.21.11.2.6.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
674 March 2026
```

