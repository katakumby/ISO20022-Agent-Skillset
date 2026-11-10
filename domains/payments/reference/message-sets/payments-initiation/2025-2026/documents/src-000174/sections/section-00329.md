---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.13 Purpose <Purp>"]
file_pages: [469, 470, 471]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.13 Purpose <Purp>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 469 to 471.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 469

```text
Datatype: "Max140Text" on page 608
5.4.2.18.13  Purpose <Purp>
Presence: [0..1]
Definition: Underlying reason for the payment transaction.
Usage: Purpose is used by the end-customers, that is initiating party, (ultimate) debtor, (ultimate)
creditor to provide information concerning the nature of the payment. Purpose is a content element,
which is not used for processing by any of the agents involved in the payment chain.
Purpose <Purp> contains one of the following elements (see "Purpose2Choice" on page 554 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 554
Or}   Proprietary <Prtry> [1..1] Text 554
5.4.2.18.14  RegulatoryReporting <RgltryRptg>
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
5.4.2.18.15  Tax <Tax>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 469 March 2026
```

## File page 470

```text
Definition: Provides details on the tax.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 470 March 2026
```

## File page 471

```text
Tax <Tax> contains the following TaxData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1] ± 472
   Debtor <Dbtr> [0..1] ± 472
   UltimateDebtor <UltmtDbtr> [0..1] ± 472
   AdministrationZone <AdmstnZone> [0..1] Text 473
   ReferenceNumber <RefNb> [0..1] Text 473
   Method <Mtd> [0..1] Text 473
   TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C12 473
   TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C12 474
   Date <Dt> [0..1] Date 474
   SequenceNumber <SeqNb> [0..1] Quantity 474
   Record <Rcrd> [0..*]  474
     Type <Tp> [0..1] Text 475
     Category <Ctgy> [0..1] Text 475
     CategoryDetails <CtgyDtls> [0..1] Text 475
     DebtorStatus <DbtrSts> [0..1] Text 476
     CertificateIdentification <CertId> [0..1] Text 476
     FormsCode <FrmsCd> [0..1] Text 476
     Period <Prd> [0..1]  476
       Year <Yr> [0..1] Year 476
       Type <Tp> [0..1] CodeSet 476
       FromToDate <FrToDt> [0..1] ± 477
     TaxAmount <TaxAmt> [0..1]  478
       Rate <Rate> [0..1] Rate 478
       TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C12 478
       TotalAmount <TtlAmt> [0..1] Amount C2, C12 478
       Details <Dtls> [0..*]  479
         Period <Prd> [0..1]  479
           Year <Yr> [0..1] Year 479
           Type <Tp> [0..1] CodeSet 480
           FromToDate <FrToDt> [0..1] ± 480
         Amount <Amt> [1..1] Amount C2, C12 481
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 471 March 2026
```

