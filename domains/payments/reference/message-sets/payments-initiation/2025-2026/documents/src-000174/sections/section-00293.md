---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.1.7 ForwardingAgent <FwdgAgt>"]
file_pages: [416, 417, 418, 419, 420, 421, 422, 423, 424, 425]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.1.7 ForwardingAgent <FwdgAgt>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 416 to 425.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 416

```text
InitiatingParty <InitgPty> contains the following elements (see "PartyIdentification272" on page 554
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 555
   PostalAddress <PstlAdr> [0..1] ± 556
   Identification <Id> [0..1]  556
{Or     OrganisationIdentification <OrgId> [1..1]  557
       AnyBIC <AnyBIC> [0..1] IdentifierSet C3 558
       LEI <LEI> [0..1] IdentifierSet 558
       Other <Othr> [0..*]  558
         Identification <Id> [1..1] Text 559
         SchemeName <SchmeNm> [0..1]  559
{Or           Code <Cd> [1..1] CodeSet 559
Or}           Proprietary <Prtry> [1..1] Text 559
         Issuer <Issr> [0..1] Text 559
Or}     PrivateIdentification <PrvtId> [1..1]  559
       DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  560
         BirthDate <BirthDt> [1..1] Date 560
         ProvinceOfBirth <PrvcOfBirth> [0..1] Text 560
         CityOfBirth <CityOfBirth> [1..1] Text 561
         CountryOfBirth <CtryOfBirth> [1..1] CodeSet C18 561
       Other <Othr> [0..*]  561
         Identification <Id> [1..1] Text 561
         SchemeName <SchmeNm> [0..1]  561
{Or           Code <Cd> [1..1] CodeSet 562
Or}           Proprietary <Prtry> [1..1] Text 562
         Issuer <Issr> [0..1] Text 562
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C18 562
   ContactDetails <CtctDtls> [0..1] ± 562
5.4.1.7  ForwardingAgent <FwdgAgt>
Presence: [0..1]
Definition: Financial institution that receives the instruction from the initiating party and forwards it to the
next agent in the payment chain for execution.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 416 March 2026
```

## File page 417

```text
ForwardingAgent <FwdgAgt> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 539 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  540
     BICFI <BICFI> [0..1] IdentifierSet C4 540
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 541
     LEI <LEI> [0..1] IdentifierSet 541
     Name <Nm> [0..1] Text 541
     PostalAddress <PstlAdr> [0..1] ± 541
     Other <Othr> [0..1] ± 542
   BranchIdentification <BrnchId> [0..1]  543
     Identification <Id> [0..1] Text 543
     LEI <LEI> [0..1] IdentifierSet 543
     Name <Nm> [0..1] Text 543
     PostalAddress <PstlAdr> [0..1] ± 543
5.4.2 PaymentInformation <PmtInf>
Presence: [1..*]
Definition: Set of characteristics that apply to the credit side of the payment transactions included in the
direct debit transaction initiation.
Impacted by: C7 "ChargeBearerRule", C8 "ChargesAccountAgentRule", C9 "ChargesAccountRule",
C11 "CreditorSchemeIdentificationRule", C17 "PaymentTypeInformationRule", C24
"UltimateCreditorRule", C22 "UltimateCreditorGuideline"
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 417 March 2026
```

## File page 418

```text
PaymentInformation <PmtInf> contains the following PaymentInstruction50 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentInformationIdentification <PmtInfId> [1..1] Text 426
   PaymentMethod <PmtMtd> [1..1] CodeSet 426
   RequestedAdviceType <ReqdAdvcTp> [0..1]  426
     CreditAdvice <CdtAdvc> [0..1]  427
{Or       Code <Cd> [1..1] CodeSet 427
Or}       Proprietary <Prtry> [1..1] Text 427
     DebitAdvice <DbtAdvc> [0..1]  427
{Or       Code <Cd> [1..1] CodeSet 428
Or}       Proprietary <Prtry> [1..1] Text 428
   BatchBooking <BtchBookg> [0..1] Indicator 428
   NumberOfTransactions <NbOfTxs> [0..1] Text 428
   ControlSum <CtrlSum> [0..1] Quantity 428
   PaymentTypeInformation <PmtTpInf> [0..1] ± 429
   RequestedCollectionDate <ReqdColltnDt> [1..1] Date 429
   Creditor <Cdtr> [1..1] ± 429
   CreditorAccount <CdtrAcct> [1..1] ± C16,
C15
430
   CreditorAgent <CdtrAgt> [1..1] ± 431
   CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C16,
C15
432
   UltimateCreditor <UltmtCdtr> [0..1] ± 433
   ChargeBearer <ChrgBr> [0..1] CodeSet 434
   ChargesAccount <ChrgsAcct> [0..1] ± C16,
C15
435
   ChargesAccountAgent <ChrgsAcctAgt> [0..1] ± 436
   CreditorSchemeIdentification <CdtrSchmeId> [0..1] ± 436
   DirectDebitTransactionInformation <DrctDbtTxInf> [1..*]  C23,
C25
437
     PaymentIdentification <PmtId> [1..1] ± 444
     PaymentTypeInformation <PmtTpInf> [0..1] ± 444
     InstructedAmount <InstdAmt> [1..1] Amount C2, C12 445
     ChargeBearer <ChrgBr> [0..1] CodeSet 445
     DirectDebitTransaction <DrctDbtTx> [0..1]  446
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 418 March 2026
```

## File page 419

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       MandateRelatedInformation <MndtRltdInf> [0..1]  C3, C4 448
         MandateIdentification <MndtId> [0..1] Text 450
         DateOfSignature <DtOfSgntr> [0..1] Date 450
         AmendmentIndicator <AmdmntInd> [0..1] Indicator 450
         AmendmentInformationDetails <AmdmntInfDtls> [0..1]  450
           OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 451
           OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 451
           OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 452
           OriginalCreditorAgentAccount
<OrgnlCdtrAgtAcct>
[0..1] ± C16,
C15
453
           OriginalDebtor <OrgnlDbtr> [0..1] ± 454
           OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C16,
C15
455
           OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 456
           OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C16,
C15
457
           OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 458
           OriginalFrequency <OrgnlFrqcy> [0..1] ± 458
           OriginalReason <OrgnlRsn> [0..1]  458
{Or             Code <Cd> [1..1] CodeSet 458
Or}             Proprietary <Prtry> [1..1] Text 458
           OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 459
         ElectronicSignature <ElctrncSgntr> [0..1] Text 459
         FirstCollectionDate <FrstColltnDt> [0..1] Date 459
         FinalCollectionDate <FnlColltnDt> [0..1] Date 459
         Frequency <Frqcy> [0..1] ± 459
         Reason <Rsn> [0..1]  459
{Or           Code <Cd> [1..1] CodeSet 460
Or}           Proprietary <Prtry> [1..1] Text 460
         TrackingDays <TrckgDays> [0..1] Text 460
       CreditorSchemeIdentification <CdtrSchmeId> [0..1] ± 460
       PreNotificationIdentification <PreNtfctnId> [0..1] Text 461
       PreNotificationDate <PreNtfctnDt> [0..1] Date 462
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 419 March 2026
```

## File page 420

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     UltimateCreditor <UltmtCdtr> [0..1] ± 462
     DebtorAgent <DbtrAgt> [1..1] ± 463
     DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C16,
C15
464
     Debtor <Dbtr> [1..1] ± 465
     DebtorAccount <DbtrAcct> [1..1] ± C16,
C15
466
     UltimateDebtor <UltmtDbtr> [0..1] ± 467
     InstructionForCreditorAgent <InstrForCdtrAgt> [0..1] Text 468
     Purpose <Purp> [0..1] ± 469
     RegulatoryReporting <RgltryRptg> [0..10] ± 469
     Tax <Tax> [0..1]  469
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
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 420 March 2026
```

## File page 421

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
         AdditionalInformation <AddtlInf> [0..1] Text 481
     RelatedRemittanceInformation <RltdRmtInf> [0..10]  481
       RemittanceIdentification <RmtId> [0..1] Text 482
       RemittanceLocationDetails <RmtLctnDtls> [0..*]  482
         Method <Mtd> [1..1] CodeSet 482
         ElectronicAddress <ElctrncAdr> [0..1] Text 483
         PostalAddress <PstlAdr> [0..1]  483
           Name <Nm> [1..1] Text 483
           Address <Adr> [1..1] ± 483
     RemittanceInformation <RmtInf> [0..1]  484
       Unstructured <Ustrd> [0..*] Text 488
       Structured <Strd> [0..*]  488
         ReferredDocumentInformation <RfrdDocInf> [0..*]  492
           Type <Tp> [0..1]  494
             CodeOrProprietary <CdOrPrtry> [1..1]  494
{Or               Code <Cd> [1..1] CodeSet 494
Or}               Proprietary <Prtry> [1..1] Text 494
             Issuer <Issr> [0..1] Text 494
           Number <Nb> [0..1] Text 495
           RelatedDate <RltdDt> [0..1]  495
             Type <Tp> [1..1]  495
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 421 March 2026
```

## File page 422

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or               Code <Cd> [1..1] CodeSet 495
Or}               Proprietary <Prtry> [1..1] Text 495
             Date <Dt> [1..1] Date 495
           LineDetails <LineDtls> [0..*]  496
             Identification <Id> [1..*]  496
               Type <Tp> [0..1]  497
                 CodeOrProprietary <CdOrPrtry> [1..1]  497
{Or                   Code <Cd> [1..1] CodeSet 497
Or}                   Proprietary <Prtry> [1..1] Text 497
                 Issuer <Issr> [0..1] Text 498
               Number <Nb> [0..1] Text 498
               RelatedDate <RltdDt> [0..1] Date 498
             Description <Desc> [0..1] Text 498
             Amount <Amt> [0..1]  C18 498
               RemittanceAmountAndType <RmtAmtAndTp> [0..*]  499
                 Type <Tp> [1..1]  499
{Or                   Code <Cd> [1..1] CodeSet 500
Or}                   Proprietary <Prtry> [1..1] Text 500
                 Amount <Amt> [1..1] Amount C2, C12 500
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
{Or               Code <Cd> [1..1] CodeSet 503
Or}               Proprietary <Prtry> [1..1] Text 503
             Amount <Amt> [1..1] Amount C2, C12 503
           AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  503
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 422 March 2026
```

## File page 423

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Amount <Amt> [1..1] Amount C2, C12 503
             CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 504
             Reason <Rsn> [0..1] Text 504
             AdditionalInformation <AddtlInf> [0..1] Text 504
         CreditorReferenceInformation <CdtrRefInf> [0..1]  504
           Type <Tp> [0..1]  505
             CodeOrProprietary <CdOrPrtry> [1..1]  505
{Or               Code <Cd> [1..1] CodeSet 505
Or}               Proprietary <Prtry> [1..1] Text 505
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
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 423 March 2026
```

## File page 424

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or               Code <Cd> [1..1] CodeSet 521
Or}               Proprietary <Prtry> [1..1] Text 521
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
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 424 March 2026
```

## File page 425

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 525
     SupplementaryData <SplmtryData> [0..*] ± C21 525
Constraints
• ChargeBearerRule
If ChargeBearer is present, then DirectDebitTransactionInformation/ChargeBearer is not allowed.
If DirectDebitTransactionInformation/ChargeBearer is present, then ChargeBearer is not allowed.
DirectDebitTransactionInformation/ChargeBearer and ChargeBearer may both be absent.
Following Must be True
    /ChargeBearer Must be absent
 Or    /DirectDebitTransactionInformation[*]/ChargeBearer Must be absent
• ChargesAccountAgentRule
If ChargesAccountAgent is present, then it must contain a branch of the CreditorAgent. It must not
contain a completely different agent.
On Condition
    /ChargesAccountAgent is present
Following Must be True
    /ChargesAccountAgent/FinancialInstitutionIdentification/Name Must be equal to 
value 'Branch of DebtorAgent'
• ChargesAccountRule
If ChargesAccountAgent is present, then ChargesAccount must be present.
On Condition
    /ChargesAccountAgent is present
Following Must be True
    /ChargesAccount Must be present
• CreditorSchemeIdentificationRule
If CreditorSchemeIdentification is present, then DirectDebitTransactionInformation/
CreditorSchemeIdentification is not allowed.
If DirectDebitTransactionInformation/CreditorSchemeIdentification is present, then
CreditorSchemeIdentification is not allowed.
DirectDebitTransactionInformation/CreditorSchemeIdentification and CreditorSchemeIdentification
may both be absent.
Following Must be True
    /CreditorSchemeIdentification Must be absent
 Or    /DirectDebitTransactionInformation[*]/DirectDebitTransaction/
CreditorSchemeIdentification Must be absent
• PaymentTypeInformationRule
If PaymentTypeInformation is present, then DirectDebitTransactionInformation/
PaymentTypeInformation is not allowed.
On Condition
    /PaymentTypeInformation is present
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 425 March 2026
```

