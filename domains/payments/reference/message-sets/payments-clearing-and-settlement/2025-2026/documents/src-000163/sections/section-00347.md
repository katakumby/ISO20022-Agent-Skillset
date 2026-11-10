---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.23 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "4.4.3.27.23.29 Tax <Tax>", "4.4.3.27.23.29.11 Record <Rcrd>", "4.4.3.27.23.29.11.1 Type <Tp>"]
file_pages: [482]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.23.29.11.1 Type <Tp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 482 to 482.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 482

```text
Record <Rcrd> contains the following TaxRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] Text 482
   Category <Ctgy> [0..1] Text 482
   CategoryDetails <CtgyDtls> [0..1] Text 482
   DebtorStatus <DbtrSts> [0..1] Text 483
   CertificateIdentification <CertId> [0..1] Text 483
   FormsCode <FrmsCd> [0..1] Text 483
   Period <Prd> [0..1]  483
     Year <Yr> [0..1] Year 483
     Type <Tp> [0..1] CodeSet 483
     FromToDate <FrToDt> [0..1] ± 484
   TaxAmount <TaxAmt> [0..1]  485
     Rate <Rate> [0..1] Rate 485
     TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C12 485
     TotalAmount <TtlAmt> [0..1] Amount C2, C12 485
     Details <Dtls> [0..*]  486
       Period <Prd> [0..1]  486
         Year <Yr> [0..1] Year 486
         Type <Tp> [0..1] CodeSet 487
         FromToDate <FrToDt> [0..1] ± 487
       Amount <Amt> [1..1] Amount C2, C12 488
   AdditionalInformation <AddtlInf> [0..1] Text 488
4.4.3.27.23.29.11.1  Type <Tp>
Presence: [0..1]
Definition: High level code to identify the type of tax details.
Datatype: "Max35Text" on page 1246
4.4.3.27.23.29.11.2  Category <Ctgy>
Presence: [0..1]
Definition: Specifies the tax code as published by the tax authority.
Datatype: "Max35Text" on page 1246
4.4.3.27.23.29.11.3  CategoryDetails <CtgyDtls>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
482 March 2026
```

