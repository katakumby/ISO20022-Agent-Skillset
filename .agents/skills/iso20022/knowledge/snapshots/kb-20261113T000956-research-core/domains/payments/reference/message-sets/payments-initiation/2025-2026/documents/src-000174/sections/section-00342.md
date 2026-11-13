---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.17 RemittanceInformation <RmtInf>"]
file_pages: [484, 485, 486, 487]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.17 RemittanceInformation <RmtInf>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 484 to 487.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 484

```text
Address <Adr> contains the following elements (see "PostalAddress27" on page 575 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  575
{Or     Code <Cd> [1..1] CodeSet 576
Or}     Proprietary <Prtry> [1..1] ± 576
   CareOf <CareOf> [0..1] Text 576
   Department <Dept> [0..1] Text 576
   SubDepartment <SubDept> [0..1] Text 577
   StreetName <StrtNm> [0..1] Text 577
   BuildingNumber <BldgNb> [0..1] Text 577
   BuildingName <BldgNm> [0..1] Text 577
   Floor <Flr> [0..1] Text 577
   UnitNumber <UnitNb> [0..1] Text 577
   PostBox <PstBx> [0..1] Text 577
   Room <Room> [0..1] Text 577
   PostCode <PstCd> [0..1] Text 578
   TownName <TwnNm> [0..1] Text 578
   TownLocationName <TwnLctnNm> [0..1] Text 578
   DistrictName <DstrctNm> [0..1] Text 578
   CountrySubDivision <CtrySubDvsn> [0..1] Text 578
   Country <Ctry> [0..1] CodeSet C18 578
   AddressLine <AdrLine> [0..7] Text 578
5.4.2.18.17  RemittanceInformation <RmtInf>
Presence: [0..1]
Definition: Information supplied to enable the matching of an entry with the items that the transfer is
intended to settle, such as commercial invoices in an accounts' receivable system.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 484 March 2026
```

## File page 485

```text
RemittanceInformation <RmtInf> contains the following RemittanceInformation26 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unstructured <Ustrd> [0..*] Text 488
   Structured <Strd> [0..*]  488
     ReferredDocumentInformation <RfrdDocInf> [0..*]  492
       Type <Tp> [0..1]  494
         CodeOrProprietary <CdOrPrtry> [1..1]  494
{Or           Code <Cd> [1..1] CodeSet 494
Or}           Proprietary <Prtry> [1..1] Text 494
         Issuer <Issr> [0..1] Text 494
       Number <Nb> [0..1] Text 495
       RelatedDate <RltdDt> [0..1]  495
         Type <Tp> [1..1]  495
{Or           Code <Cd> [1..1] CodeSet 495
Or}           Proprietary <Prtry> [1..1] Text 495
         Date <Dt> [1..1] Date 495
       LineDetails <LineDtls> [0..*]  496
         Identification <Id> [1..*]  496
           Type <Tp> [0..1]  497
             CodeOrProprietary <CdOrPrtry> [1..1]  497
{Or               Code <Cd> [1..1] CodeSet 497
Or}               Proprietary <Prtry> [1..1] Text 497
             Issuer <Issr> [0..1] Text 498
           Number <Nb> [0..1] Text 498
           RelatedDate <RltdDt> [0..1] Date 498
         Description <Desc> [0..1] Text 498
         Amount <Amt> [0..1]  C18 498
           RemittanceAmountAndType <RmtAmtAndTp> [0..*]  499
             Type <Tp> [1..1]  499
{Or               Code <Cd> [1..1] CodeSet 500
Or}               Proprietary <Prtry> [1..1] Text 500
             Amount <Amt> [1..1] Amount C2, C12 500
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 485 March 2026
```

## File page 486

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  500
             Amount <Amt> [1..1] Amount C2, C12 500
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 501
             Reason <Rsn> [0..1] Text 501
             AdditionalInformation <AddtlInf> [0..1] Text 501
     ReferredDocumentAmount <RfrdDocAmt> [0..1]  C18 501
       RemittanceAmountAndType <RmtAmtAndTp> [0..*]  502
         Type <Tp> [1..1]  502
{Or           Code <Cd> [1..1] CodeSet 503
Or}           Proprietary <Prtry> [1..1] Text 503
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
{Or           Code <Cd> [1..1] CodeSet 505
Or}           Proprietary <Prtry> [1..1] Text 505
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
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 486 March 2026
```

## File page 487

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Method <Mtd> [0..1] Text 511
       TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C12 511
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
{Or           Code <Cd> [1..1] CodeSet 521
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 487 March 2026
```

