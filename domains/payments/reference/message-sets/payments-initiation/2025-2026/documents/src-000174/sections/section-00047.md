---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.23 RegulatoryReporting <RgltryRptg>"]
file_pages: [73, 74]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.23 RegulatoryReporting <RgltryRptg>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 73 to 74.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 73

```text
2.4.2.19.23  RegulatoryReporting <RgltryRptg>
Presence: [0..10]
Definition: Information needed due to regulatory and statutory requirements.
RegulatoryReporting <RgltryRptg> contains the following elements (see "RegulatoryReporting10" on
page 579 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebitCreditReportingIndicator <DbtCdtRptgInd> [1..1] CodeSet 579
   Authority <Authrty> [0..1]  579
     Name <Nm> [0..1] Text 580
     Country <Ctry> [0..1] CodeSet C18 580
   Details <Dtls> [0..*]  C34 580
     Type <Tp> [0..1]  581
{Or       Code <Cd> [1..1] CodeSet 581
Or}       Proprietary <Prtry> [1..1] Text 581
     Date <Dt> [0..1] Date 581
     Country <Ctry> [0..1] CodeSet C18 581
     ReportingCode <RptgCd> [0..1] Text 582
     Amount <Amt> [0..1] Amount C2, C19 582
     Information <Inf> [0..*] Text 582
2.4.2.19.24  Tax <Tax>
Presence: [0..1]
Definition: Provides details on the tax.
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 73 March 2026
```

## File page 74

```text
Tax <Tax> contains the following TaxData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1] ± 75
   Debtor <Dbtr> [0..1] ± 75
   UltimateDebtor <UltmtDbtr> [0..1] ± 75
   AdministrationZone <AdmstnZone> [0..1] Text 76
   ReferenceNumber <RefNb> [0..1] Text 76
   Method <Mtd> [0..1] Text 76
   TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C19 76
   TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C19 77
   Date <Dt> [0..1] Date 77
   SequenceNumber <SeqNb> [0..1] Quantity 77
   Record <Rcrd> [0..*]  77
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
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 74 March 2026
```

