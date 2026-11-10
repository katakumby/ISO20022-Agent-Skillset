---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.2 DirectDebitTransactionInformation <DrctDbtTxInf>", "3.4.2.35 RemittanceInformation <RmtInf>", "3.4.2.35.2 Structured <Strd>", "3.4.2.35.2.6 TaxRemittance <TaxRmt>", "3.4.2.35.2.6.11 Record <Rcrd>", "3.4.2.35.2.6.11.1 Type <Tp>"]
file_pages: [232]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.2.35.2.6.11.1 Type <Tp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 232 to 232.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 232

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 232
   Category <Ctgy> [0..1] Text 232
   CategoryDetails <CtgyDtls> [0..1] Text 232
   DebtorStatus <DbtrSts> [0..1] Text 233
   CertificateIdentification <CertId> [0..1] Text 233
   FormsCode <FrmsCd> [0..1] Text 233
   Period <Prd> [0..1]  233
     Year <Yr> [0..1] Year 233
     Type <Tp> [0..1] CodeSet 233
     FromToDate <FrToDt> [0..1] ± 234
   TaxAmount <TaxAmt> [0..1]  235
     Rate <Rate> [0..1] Rate 235
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C11 235
     TotalAmount <TtlAmt> [0..1] Amount C2, C11 235
     Details <Dtls> [0..*]  236
       Period <Prd> [0..1]  236
         Year <Yr> [0..1] Year 236
         Type <Tp> [0..1] CodeSet 237
         FromToDate <FrToDt> [0..1] ± 237
       Amount <Amt> [1..1] Amount C2, C11 238
   AdditionalInformation <AddtlInf> [0..1] Text 238
3.4.2.35.2.6.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 1246
3.4.2.35.2.6.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 1246
3.4.2.35.2.6.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
232 March 2026
```

