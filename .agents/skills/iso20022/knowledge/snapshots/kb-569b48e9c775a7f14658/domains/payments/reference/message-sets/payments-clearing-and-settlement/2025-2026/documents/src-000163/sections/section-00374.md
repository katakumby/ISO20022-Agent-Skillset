---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.23 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "4.4.3.27.23.30 RemittanceInformation <RmtInf>", "4.4.3.27.23.30.2 Structured <Strd>", "4.4.3.27.23.30.2.6 TaxRemittance <TaxRmt>", "4.4.3.27.23.30.2.6.11 Record <Rcrd>", "4.4.3.27.23.30.2.6.11.1 Type <Tp>"]
file_pages: [517]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.23.30.2.6.11.1 Type <Tp>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 517 to 517.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 517

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 517
   Category <Ctgy> [0..1] Text 517
   CategoryDetails <CtgyDtls> [0..1] Text 517
   DebtorStatus <DbtrSts> [0..1] Text 518
   CertificateIdentification <CertId> [0..1] Text 518
   FormsCode <FrmsCd> [0..1] Text 518
   Period <Prd> [0..1]  518
     Year <Yr> [0..1] Year 518
     Type <Tp> [0..1] CodeSet 518
     FromToDate <FrToDt> [0..1] ± 519
   TaxAmount <TaxAmt> [0..1]  520
     Rate <Rate> [0..1] Rate 520
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C12 520
     TotalAmount <TtlAmt> [0..1] Amount C2, C12 520
     Details <Dtls> [0..*]  521
       Period <Prd> [0..1]  521
         Year <Yr> [0..1] Year 521
         Type <Tp> [0..1] CodeSet 522
         FromToDate <FrToDt> [0..1] ± 522
       Amount <Amt> [1..1] Amount C2, C12 523
   AdditionalInformation <AddtlInf> [0..1] Text 523
4.4.3.27.23.30.2.6.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 1246
4.4.3.27.23.30.2.6.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 1246
4.4.3.27.23.30.2.6.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
517 March 2026
```

