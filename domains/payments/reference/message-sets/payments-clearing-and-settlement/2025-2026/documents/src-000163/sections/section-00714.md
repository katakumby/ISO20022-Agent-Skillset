---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.40 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "7.4.2.40.30 RemittanceInformation <RmtInf>", "7.4.2.40.30.2 Structured <Strd>", "7.4.2.40.30.2.6 TaxRemittance <TaxRmt>", "7.4.2.40.30.2.6.11 Record <Rcrd>", "7.4.2.40.30.2.6.11.1 Type <Tp>"]
file_pages: [970]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.40.30.2.6.11.1 Type <Tp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 970 to 970.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 970

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 970
   Category <Ctgy> [0..1] Text 970
   CategoryDetails <CtgyDtls> [0..1] Text 970
   DebtorStatus <DbtrSts> [0..1] Text 971
   CertificateIdentification <CertId> [0..1] Text 971
   FormsCode <FrmsCd> [0..1] Text 971
   Period <Prd> [0..1]  971
     Year <Yr> [0..1] Year 971
     Type <Tp> [0..1] CodeSet 971
     FromToDate <FrToDt> [0..1] ± 972
   TaxAmount <TaxAmt> [0..1]  973
     Rate <Rate> [0..1] Rate 973
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C9 973
     TotalAmount <TtlAmt> [0..1] Amount C2, C9 973
     Details <Dtls> [0..*]  974
       Period <Prd> [0..1]  974
         Year <Yr> [0..1] Year 974
         Type <Tp> [0..1] CodeSet 975
         FromToDate <FrToDt> [0..1] ± 975
       Amount <Amt> [1..1] Amount C2, C9 976
   AdditionalInformation <AddtlInf> [0..1] Text 976
7.4.2.40.30.2.6.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 1246
7.4.2.40.30.2.6.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 1246
7.4.2.40.30.2.6.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
970 March 2026
```

