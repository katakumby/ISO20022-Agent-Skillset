---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.26 RemittanceInformation <RmtInf>", "2.4.2.19.26.2 Structured <Strd>", "2.4.2.19.26.2.6 TaxRemittance <TaxRmt>", "2.4.2.19.26.2.6.11 Record <Rcrd>", "2.4.2.19.26.2.6.11.1 Type <Tp>"]
file_pages: [116]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.26.2.6.11.1 Type <Tp>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 116 to 116.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 116

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 116
   Category <Ctgy> [0..1] Text 116
   CategoryDetails <CtgyDtls> [0..1] Text 116
   DebtorStatus <DbtrSts> [0..1] Text 117
   CertificateIdentification <CertId> [0..1] Text 117
   FormsCode <FrmsCd> [0..1] Text 117
   Period <Prd> [0..1]  117
     Year <Yr> [0..1] Year 117
     Type <Tp> [0..1] CodeSet 117
     FromToDate <FrToDt> [0..1] ± 118
   TaxAmount <TaxAmt> [0..1]  119
     Rate <Rate> [0..1] Rate 119
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C19 119
     TotalAmount <TtlAmt> [0..1] Amount C2, C19 119
     Details <Dtls> [0..*]  120
       Period <Prd> [0..1]  120
         Year <Yr> [0..1] Year 120
         Type <Tp> [0..1] CodeSet 121
         FromToDate <FrToDt> [0..1] ± 121
       Amount <Amt> [1..1] Amount C2, C19 122
   AdditionalInformation <AddtlInf> [0..1] Text 122
2.4.2.19.26.2.6.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 609
2.4.2.19.26.2.6.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 609
2.4.2.19.26.2.6.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 116 March 2026
```

