---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.3 TransactionInformationAndStatus <TxInfAndSts>", "2.4.3.18 OriginalTransactionReference <OrgnlTxRef>", "2.4.3.18.11 RemittanceInformation <RmtInf>", "2.4.3.18.11.2 Structured <Strd>", "2.4.3.18.11.2.6 TaxRemittance <TaxRmt>", "2.4.3.18.11.2.6.11 Record <Rcrd>", "2.4.3.18.11.2.6.11.1 Type <Tp>"]
file_pages: [104]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.3.18.11.2.6.11.1 Type <Tp>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 104 to 104.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 104

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 104
   Category <Ctgy> [0..1] Text 104
   CategoryDetails <CtgyDtls> [0..1] Text 104
   DebtorStatus <DbtrSts> [0..1] Text 105
   CertificateIdentification <CertId> [0..1] Text 105
   FormsCode <FrmsCd> [0..1] Text 105
   Period <Prd> [0..1]  105
     Year <Yr> [0..1] Year 105
     Type <Tp> [0..1] CodeSet 105
     FromToDate <FrToDt> [0..1] ± 106
   TaxAmount <TaxAmt> [0..1]  107
     Rate <Rate> [0..1] Rate 107
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C8 107
     TotalAmount <TtlAmt> [0..1] Amount C2, C8 107
     Details <Dtls> [0..*]  108
       Period <Prd> [0..1]  108
         Year <Yr> [0..1] Year 108
         Type <Tp> [0..1] CodeSet 109
         FromToDate <FrToDt> [0..1] ± 109
       Amount <Amt> [1..1] Amount C2, C8 110
   AdditionalInformation <AddtlInf> [0..1] Text 110
2.4.3.18.11.2.6.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 1246
2.4.3.18.11.2.6.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 1246
2.4.3.18.11.2.6.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
104 March 2026
```

