---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "9.4 Message Building Blocks", "9.4.1 GroupHeader <GrpHdr>", "9.4.3.11 OriginalTransactionReference <OrgnlTxRef>", "9.4.3.11.11 RemittanceInformation <RmtInf>", "9.4.3.11.11.2 Structured <Strd>", "9.4.3.11.11.2.6 TaxRemittance <TaxRmt>", "9.4.3.11.11.2.6.11 Record <Rcrd>", "9.4.3.11.11.2.6.11.1 Type <Tp>"]
file_pages: [1133]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.028.001.07"]
---

# 9.4.3.11.11.2.6.11.1 Type <Tp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1133 to 1133.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1133

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 1133
   Category <Ctgy> [0..1] Text 1133
   CategoryDetails <CtgyDtls> [0..1] Text 1133
   DebtorStatus <DbtrSts> [0..1] Text 1134
   CertificateIdentification <CertId> [0..1] Text 1134
   FormsCode <FrmsCd> [0..1] Text 1134
   Period <Prd> [0..1]  1134
     Year <Yr> [0..1] Year 1134
     Type <Tp> [0..1] CodeSet 1134
     FromToDate <FrToDt> [0..1] ± 1135
   TaxAmount <TaxAmt> [0..1]  1136
     Rate <Rate> [0..1] Rate 1136
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C8 1136
     TotalAmount <TtlAmt> [0..1] Amount C2, C8 1136
     Details <Dtls> [0..*]  1137
       Period <Prd> [0..1]  1137
         Year <Yr> [0..1] Year 1137
         Type <Tp> [0..1] CodeSet 1138
         FromToDate <FrToDt> [0..1] ± 1138
       Amount <Amt> [1..1] Amount C2, C8 1139
   AdditionalInformation <AddtlInf> [0..1] Text 1139
9.4.3.11.11.2.6.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 1246
9.4.3.11.11.2.6.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 1246
9.4.3.11.11.2.6.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1133 March 2026
```

