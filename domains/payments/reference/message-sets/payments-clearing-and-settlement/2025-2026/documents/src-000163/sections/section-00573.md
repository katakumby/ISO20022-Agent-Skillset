---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.45 Tax <Tax>", "6.4.2.45.11 Record <Rcrd>", "6.4.2.45.11.1 Type <Tp>"]
file_pages: [778]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.45.11.1 Type <Tp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 778 to 778.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 778

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 778
   Category <Ctgy> [0..1] Text 778
   CategoryDetails <CtgyDtls> [0..1] Text 778
   DebtorStatus <DbtrSts> [0..1] Text 779
   CertificateIdentification <CertId> [0..1] Text 779
   FormsCode <FrmsCd> [0..1] Text 779
   Period <Prd> [0..1]  779
     Year <Yr> [0..1] Year 779
     Type <Tp> [0..1] CodeSet 779
     FromToDate <FrToDt> [0..1] ± 780
   TaxAmount <TaxAmt> [0..1]  781
     Rate <Rate> [0..1] Rate 781
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C12 781
     TotalAmount <TtlAmt> [0..1] Amount C2, C12 781
     Details <Dtls> [0..*]  782
       Period <Prd> [0..1]  782
         Year <Yr> [0..1] Year 782
         Type <Tp> [0..1] CodeSet 783
         FromToDate <FrToDt> [0..1] ± 783
       Amount <Amt> [1..1] Amount C2, C12 784
   AdditionalInformation <AddtlInf> [0..1] Text 784
6.4.2.45.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 1246
6.4.2.45.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 1246
6.4.2.45.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
778 March 2026
```

