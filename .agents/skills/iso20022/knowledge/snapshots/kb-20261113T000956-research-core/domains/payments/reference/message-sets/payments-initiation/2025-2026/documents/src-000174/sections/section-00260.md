---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.8.9.11 RemittanceInformation <RmtInf>", "4.4.3.8.9.11.2 Structured <Strd>", "4.4.3.8.9.11.2.6 TaxRemittance <TaxRmt>", "4.4.3.8.9.11.2.6.11 Record <Rcrd>", "4.4.3.8.9.11.2.6.11.1 Type <Tp>"]
file_pages: [375]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.9.11.2.6.11.1 Type <Tp>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 375 to 375.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 375

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 375
   Category <Ctgy> [0..1] Text 375
   CategoryDetails <CtgyDtls> [0..1] Text 375
   DebtorStatus <DbtrSts> [0..1] Text 376
   CertificateIdentification <CertId> [0..1] Text 376
   FormsCode <FrmsCd> [0..1] Text 376
   Period <Prd> [0..1]  376
     Year <Yr> [0..1] Year 376
     Type <Tp> [0..1] CodeSet 376
     FromToDate <FrToDt> [0..1] ± 377
   TaxAmount <TaxAmt> [0..1]  378
     Rate <Rate> [0..1] Rate 378
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C9 378
     TotalAmount <TtlAmt> [0..1] Amount C2, C9 378
     Details <Dtls> [0..*]  379
       Period <Prd> [0..1]  379
         Year <Yr> [0..1] Year 379
         Type <Tp> [0..1] CodeSet 380
         FromToDate <FrToDt> [0..1] ± 380
       Amount <Amt> [1..1] Amount C2, C9 381
   AdditionalInformation <AddtlInf> [0..1] Text 381
4.4.3.8.9.11.2.6.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 609
4.4.3.8.9.11.2.6.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 609
4.4.3.8.9.11.2.6.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 375 March 2026
```

