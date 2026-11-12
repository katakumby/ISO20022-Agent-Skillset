---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.15 Tax <Tax>", "5.4.2.18.15.11 Record <Rcrd>", "5.4.2.18.15.11.1 Type <Tp>"]
file_pages: [475]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.15.11.1 Type <Tp>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 475 to 475.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 475

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 475
   Category <Ctgy> [0..1] Text 475
   CategoryDetails <CtgyDtls> [0..1] Text 475
   DebtorStatus <DbtrSts> [0..1] Text 476
   CertificateIdentification <CertId> [0..1] Text 476
   FormsCode <FrmsCd> [0..1] Text 476
   Period <Prd> [0..1]  476
     Year <Yr> [0..1] Year 476
     Type <Tp> [0..1] CodeSet 476
     FromToDate <FrToDt> [0..1] ± 477
   TaxAmount <TaxAmt> [0..1]  478
     Rate <Rate> [0..1] Rate 478
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C12 478
     TotalAmount <TtlAmt> [0..1] Amount C2, C12 478
     Details <Dtls> [0..*]  479
       Period <Prd> [0..1]  479
         Year <Yr> [0..1] Year 479
         Type <Tp> [0..1] CodeSet 480
         FromToDate <FrToDt> [0..1] ± 480
       Amount <Amt> [1..1] Amount C2, C12 481
   AdditionalInformation <AddtlInf> [0..1] Text 481
5.4.2.18.15.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 609
5.4.2.18.15.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 609
5.4.2.18.15.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 475 March 2026
```

