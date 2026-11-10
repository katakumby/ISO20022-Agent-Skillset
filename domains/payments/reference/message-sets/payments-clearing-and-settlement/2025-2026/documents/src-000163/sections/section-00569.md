---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.44 RegulatoryReporting <RgltryRptg>"]
file_pages: [773, 774]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.44 RegulatoryReporting <RgltryRptg>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 773 to 774.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 773

```text
Definition: Underlying reason for the payment transaction.
Usage: Purpose is used by the end-customers, that is initiating party, (ultimate) debtor, (ultimate)
creditor to provide information concerning the nature of the payment. Purpose is a content element,
which is not used for processing by any of the agents involved in the payment chain.
Purpose <Purp> contains one of the following elements (see "Purpose2Choice" on page 1191 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1191
Or}   Proprietary <Prtry> [1..1] Text 1191
6.4.2.44  RegulatoryReporting <RgltryRptg>
Presence: [0..10]
Definition: Information needed due to regulatory and statutory requirements.
RegulatoryReporting <RgltryRptg> contains the following elements (see "RegulatoryReporting10" on
page 1216 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebitCreditReportingIndicator <DbtCdtRptgInd> [1..1] CodeSet 1217
   Authority <Authrty> [0..1]  1217
     Name <Nm> [0..1] Text 1218
     Country <Ctry> [0..1] CodeSet C10 1218
   Details <Dtls> [0..*]  C40 1218
     Type <Tp> [0..1]  1219
{Or       Code <Cd> [1..1] CodeSet 1219
Or}       Proprietary <Prtry> [1..1] Text 1219
     Date <Dt> [0..1] Date 1219
     Country <Ctry> [0..1] CodeSet C10 1219
     ReportingCode <RptgCd> [0..1] Text 1219
     Amount <Amt> [0..1] Amount C2, C12 1220
     Information <Inf> [0..*] Text 1220
6.4.2.45  Tax <Tax>
Presence: [0..1]
Definition: Provides details on the tax.
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
773 March 2026
```

## File page 774

```text
Tax <Tax> contains the following TaxData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1] ± 775
   Debtor <Dbtr> [0..1] ± 775
   UltimateDebtor <UltmtDbtr> [0..1] ± 775
   AdministrationZone <AdmstnZone> [0..1] Text 776
   ReferenceNumber <RefNb> [0..1] Text 776
   Method <Mtd> [0..1] Text 776
   TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C12 776
   TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C12 777
   Date <Dt> [0..1] Date 777
   SequenceNumber <SeqNb> [0..1] Quantity 777
   Record <Rcrd> [0..*]  777
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
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
774 March 2026
```

