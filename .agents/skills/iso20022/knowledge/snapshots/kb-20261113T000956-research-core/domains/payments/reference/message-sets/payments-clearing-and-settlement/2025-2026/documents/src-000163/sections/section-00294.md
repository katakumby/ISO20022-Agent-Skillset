---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.11 RemittanceInformation <RmtInf>", "4.4.3.27.11.2 Structured <Strd>", "4.4.3.27.11.2.6 TaxRemittance <TaxRmt>", "4.4.3.27.11.2.6.11 Record <Rcrd>", "4.4.3.27.11.2.6.11.1 Type <Tp>"]
file_pages: [420]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.11.2.6.11.1 Type <Tp>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 420 to 420.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 420

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 420
   Category <Ctgy> [0..1] Text 420
   CategoryDetails <CtgyDtls> [0..1] Text 420
   DebtorStatus <DbtrSts> [0..1] Text 421
   CertificateIdentification <CertId> [0..1] Text 421
   FormsCode <FrmsCd> [0..1] Text 421
   Period <Prd> [0..1]  421
     Year <Yr> [0..1] Year 421
     Type <Tp> [0..1] CodeSet 421
     FromToDate <FrToDt> [0..1] ± 422
   TaxAmount <TaxAmt> [0..1]  423
     Rate <Rate> [0..1] Rate 423
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C12 423
     TotalAmount <TtlAmt> [0..1] Amount C2, C12 423
     Details <Dtls> [0..*]  424
       Period <Prd> [0..1]  424
         Year <Yr> [0..1] Year 424
         Type <Tp> [0..1] CodeSet 425
         FromToDate <FrToDt> [0..1] ± 425
       Amount <Amt> [1..1] Amount C2, C12 426
   AdditionalInformation <AddtlInf> [0..1] Text 426
4.4.3.27.11.2.6.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 1246
4.4.3.27.11.2.6.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 1246
4.4.3.27.11.2.6.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
420 March 2026
```

