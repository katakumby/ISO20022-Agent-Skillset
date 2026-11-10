---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.12 OriginalTransactionReference <OrgnlTxRef>", "3.4.3.7.12.11 RemittanceInformation <RmtInf>", "3.4.3.7.12.11.2 Structured <Strd>", "3.4.3.7.12.11.2.6 TaxRemittance <TaxRmt>", "3.4.3.7.12.11.2.6.11 Record <Rcrd>", "3.4.3.7.12.11.2.6.11.1 Type <Tp>"]
file_pages: [244]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.12.11.2.6.11.1 Type <Tp>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 244 to 244.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 244

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 244
   Category <Ctgy> [0..1] Text 244
   CategoryDetails <CtgyDtls> [0..1] Text 244
   DebtorStatus <DbtrSts> [0..1] Text 245
   CertificateIdentification <CertId> [0..1] Text 245
   FormsCode <FrmsCd> [0..1] Text 245
   Period <Prd> [0..1]  245
     Year <Yr> [0..1] Year 245
     Type <Tp> [0..1] CodeSet 245
     FromToDate <FrToDt> [0..1] ± 246
   TaxAmount <TaxAmt> [0..1]  247
     Rate <Rate> [0..1] Rate 247
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C8 247
     TotalAmount <TtlAmt> [0..1] Amount C2, C8 247
     Details <Dtls> [0..*]  248
       Period <Prd> [0..1]  248
         Year <Yr> [0..1] Year 248
         Type <Tp> [0..1] CodeSet 249
         FromToDate <FrToDt> [0..1] ± 249
       Amount <Amt> [1..1] Amount C2, C8 250
   AdditionalInformation <AddtlInf> [0..1] Text 250
3.4.3.7.12.11.2.6.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 609
3.4.3.7.12.11.2.6.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 609
3.4.3.7.12.11.2.6.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 244 March 2026
```

