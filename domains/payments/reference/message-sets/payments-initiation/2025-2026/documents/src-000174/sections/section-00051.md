---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.24 Tax <Tax>", "2.4.2.19.24.11 Record <Rcrd>", "2.4.2.19.24.11.1 Type <Tp>"]
file_pages: [78]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.24.11.1 Type <Tp>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 78 to 78.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 78

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 78
   Category <Ctgy> [0..1] Text 78
   CategoryDetails <CtgyDtls> [0..1] Text 78
   DebtorStatus <DbtrSts> [0..1] Text 79
   CertificateIdentification <CertId> [0..1] Text 79
   FormsCode <FrmsCd> [0..1] Text 79
   Period <Prd> [0..1]  79
     Year <Yr> [0..1] Year 79
     Type <Tp> [0..1] CodeSet 79
     FromToDate <FrToDt> [0..1] ± 80
   TaxAmount <TaxAmt> [0..1]  81
     Rate <Rate> [0..1] Rate 81
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C19 81
     TotalAmount <TtlAmt> [0..1] Amount C2, C19 81
     Details <Dtls> [0..*]  82
       Period <Prd> [0..1]  82
         Year <Yr> [0..1] Year 82
         Type <Tp> [0..1] CodeSet 83
         FromToDate <FrToDt> [0..1] ± 83
       Amount <Amt> [1..1] Amount C2, C19 84
   AdditionalInformation <AddtlInf> [0..1] Text 84
2.4.2.19.24.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 609
2.4.2.19.24.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 609
2.4.2.19.24.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 78 March 2026
```

