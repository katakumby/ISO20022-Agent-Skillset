---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.17 RemittanceInformation <RmtInf>", "5.4.2.18.17.1 Unstructured <Ustrd>"]
file_pages: [488, 489, 490, 491]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.17.1 Unstructured <Ustrd>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 488 to 491.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 488

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] Text 521
         Issuer <Issr> [0..1] Text 521
       Garnishee <Grnshee> [0..1] ± 521
       GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 522
       ReferenceNumber <RefNb> [0..1] Text 523
       Date <Dt> [0..1] Date 524
       RemittedAmount <RmtdAmt> [0..1] Amount C2, C12 524
       FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 524
       EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 524
     SecuritiesData <SctiesData> [0..*]  524
       UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 525
       Amount <Amt> [0..1] Amount C1, C13 525
     AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 525
5.4.2.18.17.1  Unstructured <Ustrd>
Presence: [0..*]
Definition: Information supplied to enable the matching/reconciliation of an entry with the items that the
payment is intended to settle, such as commercial invoices in an accounts' receivable system, in an
unstructured form.
Datatype: "Max140Text" on page 608
5.4.2.18.17.2  Structured <Strd>
Presence: [0..*]
Definition: Information supplied to enable the matching/reconciliation of an entry with the items that the
payment is intended to settle, such as commercial invoices in an accounts' receivable system, in a
structured form.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 488 March 2026
```

## File page 489

```text
Structured <Strd> contains the following StructuredRemittanceInformation22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReferredDocumentInformation <RfrdDocInf> [0..*]  492
     Type <Tp> [0..1]  494
       CodeOrProprietary <CdOrPrtry> [1..1]  494
{Or         Code <Cd> [1..1] CodeSet 494
Or}         Proprietary <Prtry> [1..1] Text 494
       Issuer <Issr> [0..1] Text 494
     Number <Nb> [0..1] Text 495
     RelatedDate <RltdDt> [0..1]  495
       Type <Tp> [1..1]  495
{Or         Code <Cd> [1..1] CodeSet 495
Or}         Proprietary <Prtry> [1..1] Text 495
       Date <Dt> [1..1] Date 495
     LineDetails <LineDtls> [0..*]  496
       Identification <Id> [1..*]  496
         Type <Tp> [0..1]  497
           CodeOrProprietary <CdOrPrtry> [1..1]  497
{Or             Code <Cd> [1..1] CodeSet 497
Or}             Proprietary <Prtry> [1..1] Text 497
           Issuer <Issr> [0..1] Text 498
         Number <Nb> [0..1] Text 498
         RelatedDate <RltdDt> [0..1] Date 498
       Description <Desc> [0..1] Text 498
       Amount <Amt> [0..1]  C18 498
         RemittanceAmountAndType <RmtAmtAndTp> [0..*]  499
           Type <Tp> [1..1]  499
{Or             Code <Cd> [1..1] CodeSet 500
Or}             Proprietary <Prtry> [1..1] Text 500
           Amount <Amt> [1..1] Amount C2, C12 500
         AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  500
           Amount <Amt> [1..1] Amount C2, C12 500
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 489 March 2026
```

## File page 490

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 501
           Reason <Rsn> [0..1] Text 501
           AdditionalInformation <AddtlInf> [0..1] Text 501
   ReferredDocumentAmount <RfrdDocAmt> [0..1]  C18 501
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  502
       Type <Tp> [1..1]  502
{Or         Code <Cd> [1..1] CodeSet 503
Or}         Proprietary <Prtry> [1..1] Text 503
       Amount <Amt> [1..1] Amount C2, C12 503
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  503
       Amount <Amt> [1..1] Amount C2, C12 503
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 504
       Reason <Rsn> [0..1] Text 504
       AdditionalInformation <AddtlInf> [0..1] Text 504
   CreditorReferenceInformation <CdtrRefInf> [0..1]  504
     Type <Tp> [0..1]  505
       CodeOrProprietary <CdOrPrtry> [1..1]  505
{Or         Code <Cd> [1..1] CodeSet 505
Or}         Proprietary <Prtry> [1..1] Text 505
       Issuer <Issr> [0..1] Text 506
     Reference <Ref> [0..1] Text 506
   Invoicer <Invcr> [0..1] ± 506
   Invoicee <Invcee> [0..1] ± 507
   TaxRemittance <TaxRmt> [0..1]  508
     Creditor <Cdtr> [0..1] ± 510
     Debtor <Dbtr> [0..1] ± 510
     UltimateDebtor <UltmtDbtr> [0..1] ± 510
     AdministrationZone <AdmstnZone> [0..1] Text 511
     ReferenceNumber <RefNb> [0..1] Text 511
     Method <Mtd> [0..1] Text 511
     TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C12 511
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 490 March 2026
```

## File page 491

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C12 512
     Date <Dt> [0..1] Date 512
     SequenceNumber <SeqNb> [0..1] Quantity 512
     Record <Rcrd> [0..*]  512
       Type <Tp> [0..1] Text 513
       Category <Ctgy> [0..1] Text 513
       CategoryDetails <CtgyDtls> [0..1] Text 513
       DebtorStatus <DbtrSts> [0..1] Text 514
       CertificateIdentification <CertId> [0..1] Text 514
       FormsCode <FrmsCd> [0..1] Text 514
       Period <Prd> [0..1]  514
         Year <Yr> [0..1] Year 514
         Type <Tp> [0..1] CodeSet 514
         FromToDate <FrToDt> [0..1] ± 515
       TaxAmount <TaxAmt> [0..1]  516
         Rate <Rate> [0..1] Rate 516
         TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C12 516
         TotalAmount <TtlAmt> [0..1] Amount C2, C12 516
         Details <Dtls> [0..*]  517
           Period <Prd> [0..1]  517
             Year <Yr> [0..1] Year 517
             Type <Tp> [0..1] CodeSet 518
             FromToDate <FrToDt> [0..1] ± 518
           Amount <Amt> [1..1] Amount C2, C12 519
       AdditionalInformation <AddtlInf> [0..1] Text 519
   GarnishmentRemittance <GrnshmtRmt> [0..1]  519
     Type <Tp> [1..1]  520
       CodeOrProprietary <CdOrPrtry> [1..1]  520
{Or         Code <Cd> [1..1] CodeSet 521
Or}         Proprietary <Prtry> [1..1] Text 521
       Issuer <Issr> [0..1] Text 521
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 491 March 2026
```

