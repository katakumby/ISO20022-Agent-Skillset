---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.26 ReturnReasonInformation <RtrRsnInf>", "4.4.3.26.2 Reason <Rsn>"]
file_pages: [350, 351, 352, 353, 354, 355, 356, 357, 358, 359]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.26.2 Reason <Rsn>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 350 to 359.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 350

```text
4.4.3.26.2  Reason <Rsn>
Presence: [0..1]
Definition: Specifies the reason for the return.
Reason <Rsn> contains one of the following ReturnReason5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 350
Or}   Proprietary <Prtry> [1..1] Text 350
4.4.3.26.2.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the return, as published in an external reason code list.
Datatype: "ExternalReturnReason1Code" on page 1233
4.4.3.26.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the return, in a proprietary form.
Datatype: "Max35Text" on page 1246
4.4.3.26.3  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Further details on the return reason.
Datatype: "Max105Text" on page 1244
4.4.3.27  OriginalTransactionReference <OrgnlTxRef>
Presence: [0..1]
Definition: Key elements used to identify the original transaction that is being referred to.
Impacted by: C81 "UnderlyingCustomerCreditTransferRule", C82
"UnderlyingFinancialInstitutionCreditTransferRule"
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
350 March 2026
```

## File page 351

```text
OriginalTransactionReference <OrgnlTxRef> contains the following
OriginalTransactionReference45 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InterbankSettlementAmount <IntrBkSttlmAmt> [0..1] Amount C2, C12 364
   Amount <Amt> [0..1] ± 365
   InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 365
   RequestedCollectionDate <ReqdColltnDt> [0..1] Date 365
   RequestedExecutionDate <ReqdExctnDt> [0..1] ± 365
   CreditorSchemeIdentification <CdtrSchmeId> [0..1] ± 366
   SettlementInformation <SttlmInf> [0..1]  C24,
C26,
C63,
C64,
C65,
C66,
C69,
C70
367
     SettlementMethod <SttlmMtd> [1..1] CodeSet 369
     SettlementAccount <SttlmAcct> [0..1] ± C22,
C21
370
     ClearingSystem <ClrSys> [0..1]  370
{Or       Code <Cd> [1..1] CodeSet 371
Or}       Proprietary <Prtry> [1..1] Text 371
     InstructingReimbursementAgent
<InstgRmbrsmntAgt>
[0..1] ± 371
     InstructingReimbursementAgentAccount
<InstgRmbrsmntAgtAcct>
[0..1] ± C22,
C21
372
     InstructedReimbursementAgent <InstdRmbrsmntAgt> [0..1] ± 372
     InstructedReimbursementAgentAccount
<InstdRmbrsmntAgtAcct>
[0..1] ± C22,
C21
373
     ThirdReimbursementAgent <ThrdRmbrsmntAgt> [0..1] ± 374
     ThirdReimbursementAgentAccount
<ThrdRmbrsmntAgtAcct>
[0..1] ± C22,
C21
374
   PaymentTypeInformation <PmtTpInf> [0..1] ± 375
   PaymentMethod <PmtMtd> [0..1] CodeSet 376
   MandateRelatedInformation <MndtRltdInf> [0..1]  376
{Or     DirectDebitMandate <DrctDbtMndt> [1..1]  C3, C4 378
       MandateIdentification <MndtId> [0..1] Text 380
       DateOfSignature <DtOfSgntr> [0..1] Date 380
       AmendmentIndicator <AmdmntInd> [0..1] Indicator 380
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
351 March 2026
```

## File page 352

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AmendmentInformationDetails <AmdmntInfDtls> [0..1]  380
         OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 381
         OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 381
         OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 382
         OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> [0..1] ± C22,
C21
383
         OriginalDebtor <OrgnlDbtr> [0..1] ± 384
         OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C22,
C21
385
         OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 386
         OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C22,
C21
387
         OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 388
         OriginalFrequency <OrgnlFrqcy> [0..1] ± 388
         OriginalReason <OrgnlRsn> [0..1]  388
{Or           Code <Cd> [1..1] CodeSet 388
Or}           Proprietary <Prtry> [1..1] Text 388
         OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 389
       ElectronicSignature <ElctrncSgntr> [0..1] Text 389
       FirstCollectionDate <FrstColltnDt> [0..1] Date 389
       FinalCollectionDate <FnlColltnDt> [0..1] Date 389
       Frequency <Frqcy> [0..1] ± 389
       Reason <Rsn> [0..1]  389
{Or         Code <Cd> [1..1] CodeSet 390
Or}         Proprietary <Prtry> [1..1] Text 390
       TrackingDays <TrckgDays> [0..1] Text 390
Or}     CreditTransferMandate <CdtTrfMndt> [1..1] ± 390
   RemittanceInformation <RmtInf> [0..1]  391
     Unstructured <Ustrd> [0..*] Text 395
     Structured <Strd> [0..*]  395
       ReferredDocumentInformation <RfrdDocInf> [0..*]  399
         Type <Tp> [0..1]  401
           CodeOrProprietary <CdOrPrtry> [1..1]  401
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
352 March 2026
```

## File page 353

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or             Code <Cd> [1..1] CodeSet 401
Or}             Proprietary <Prtry> [1..1] Text 401
           Issuer <Issr> [0..1] Text 401
         Number <Nb> [0..1] Text 402
         RelatedDate <RltdDt> [0..1]  402
           Type <Tp> [1..1]  402
{Or             Code <Cd> [1..1] CodeSet 402
Or}             Proprietary <Prtry> [1..1] Text 402
           Date <Dt> [1..1] Date 402
         LineDetails <LineDtls> [0..*]  403
           Identification <Id> [1..*]  403
             Type <Tp> [0..1]  404
               CodeOrProprietary <CdOrPrtry> [1..1]  404
{Or                 Code <Cd> [1..1] CodeSet 404
Or}                 Proprietary <Prtry> [1..1] Text 404
               Issuer <Issr> [0..1] Text 405
             Number <Nb> [0..1] Text 405
             RelatedDate <RltdDt> [0..1] Date 405
           Description <Desc> [0..1] Text 405
           Amount <Amt> [0..1]  C59 405
             RemittanceAmountAndType <RmtAmtAndTp> [0..*]  406
               Type <Tp> [1..1]  406
{Or                 Code <Cd> [1..1] CodeSet 407
Or}                 Proprietary <Prtry> [1..1] Text 407
               Amount <Amt> [1..1] Amount C2, C12 407
             AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  407
               Amount <Amt> [1..1] Amount C2, C12 407
               CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 408
               Reason <Rsn> [0..1] Text 408
               AdditionalInformation <AddtlInf> [0..1] Text 408
       ReferredDocumentAmount <RfrdDocAmt> [0..1]  C59 408
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
353 March 2026
```

## File page 354

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         RemittanceAmountAndType <RmtAmtAndTp> [0..*]  409
           Type <Tp> [1..1]  409
{Or             Code <Cd> [1..1] CodeSet 410
Or}             Proprietary <Prtry> [1..1] Text 410
           Amount <Amt> [1..1] Amount C2, C12 410
         AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  410
           Amount <Amt> [1..1] Amount C2, C12 410
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 411
           Reason <Rsn> [0..1] Text 411
           AdditionalInformation <AddtlInf> [0..1] Text 411
       CreditorReferenceInformation <CdtrRefInf> [0..1]  411
         Type <Tp> [0..1]  412
           CodeOrProprietary <CdOrPrtry> [1..1]  412
{Or             Code <Cd> [1..1] CodeSet 412
Or}             Proprietary <Prtry> [1..1] Text 412
           Issuer <Issr> [0..1] Text 413
         Reference <Ref> [0..1] Text 413
       Invoicer <Invcr> [0..1] ± 413
       Invoicee <Invcee> [0..1] ± 414
       TaxRemittance <TaxRmt> [0..1]  415
         Creditor <Cdtr> [0..1] ± 417
         Debtor <Dbtr> [0..1] ± 417
         UltimateDebtor <UltmtDbtr> [0..1] ± 417
         AdministrationZone <AdmstnZone> [0..1] Text 418
         ReferenceNumber <RefNb> [0..1] Text 418
         Method <Mtd> [0..1] Text 418
         TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C12 418
         TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C12 419
         Date <Dt> [0..1] Date 419
         SequenceNumber <SeqNb> [0..1] Quantity 419
         Record <Rcrd> [0..*]  419
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
354 March 2026
```

## File page 355

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Type <Tp> [0..1] Text 420
           Category <Ctgy> [0..1] Text 420
           CategoryDetails <CtgyDtls> [0..1] Text 420
           DebtorStatus <DbtrSts> [0..1] Text 421
           CertificateIdentification <CertId> [0..1] Text 421
           FormsCode <FrmsCd> [0..1] Text 421
           Period <Prd> [0..1]  421
             Year <Yr> [0..1] Year 421
             Type <Tp> [0..1] CodeSet 421
             FromToDate <FrToDt> [0..1] ± 422
           TaxAmount <TaxAmt> [0..1]  423
             Rate <Rate> [0..1] Rate 423
             TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C12 423
             TotalAmount <TtlAmt> [0..1] Amount C2, C12 423
             Details <Dtls> [0..*]  424
               Period <Prd> [0..1]  424
                 Year <Yr> [0..1] Year 424
                 Type <Tp> [0..1] CodeSet 425
                 FromToDate <FrToDt> [0..1] ± 425
               Amount <Amt> [1..1] Amount C2, C12 426
           AdditionalInformation <AddtlInf> [0..1] Text 426
       GarnishmentRemittance <GrnshmtRmt> [0..1]  426
         Type <Tp> [1..1]  427
           CodeOrProprietary <CdOrPrtry> [1..1]  427
{Or             Code <Cd> [1..1] CodeSet 428
Or}             Proprietary <Prtry> [1..1] Text 428
           Issuer <Issr> [0..1] Text 428
         Garnishee <Grnshee> [0..1] ± 428
         GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 429
         ReferenceNumber <RefNb> [0..1] Text 430
         Date <Dt> [0..1] Date 431
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
355 March 2026
```

## File page 356

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         RemittedAmount <RmtdAmt> [0..1] Amount C2, C12 431
         FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 431
         EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 431
       SecuritiesData <SctiesData> [0..*]  431
         UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 432
         Amount <Amt> [0..1] Amount C1, C11 432
       AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 432
   UltimateDebtor <UltmtDbtr> [0..1]  432
{Or     Party <Pty> [1..1] ± 433
Or}     Agent <Agt> [1..1] ± 434
   Debtor <Dbtr> [0..1]  435
{Or     Party <Pty> [1..1] ± 435
Or}     Agent <Agt> [1..1] ± 436
   DebtorAccount <DbtrAcct> [0..1] ± C22,
C21
437
   DebtorAgent <DbtrAgt> [0..1] ± 438
   DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C22,
C21
438
   CreditorAgent <CdtrAgt> [0..1] ± 439
   CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C22,
C21
440
   Creditor <Cdtr> [0..1]  441
{Or     Party <Pty> [1..1] ± 441
Or}     Agent <Agt> [1..1] ± 442
   CreditorAccount <CdtrAcct> [0..1] ± C22,
C21
443
   UltimateCreditor <UltmtCdtr> [0..1]  444
{Or     Party <Pty> [1..1] ± 444
Or}     Agent <Agt> [1..1] ± 445
   Purpose <Purp> [0..1] ± 446
   UnderlyingCustomerCreditTransfer
<UndrlygCstmrCdtTrf>
[0..1]  C28,
C32,
C34,
C37,
C39,
C45,
446
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
356 March 2026
```

## File page 357

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
C50,
C52,
C55,
C57,
C47,
C76,
C78
     PaymentIdentification <PmtId> [0..1] ± C74 455
     PaymentTypeInformation <PmtTpInf> [0..1] ± 455
     UltimateDebtor <UltmtDbtr> [0..1] ± 456
     InitiatingParty <InitgPty> [0..1] ± 457
     Debtor <Dbtr> [1..1] ± 458
     DebtorAccount <DbtrAcct> [0..1] ± C22,
C21
459
     DebtorAgent <DbtrAgt> [1..1] ± 460
     DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C22,
C21
461
     PreviousInstructingAgent1 <PrvsInstgAgt1> [0..1] ± 462
     PreviousInstructingAgent1Account
<PrvsInstgAgt1Acct>
[0..1] ± C22,
C21
462
     PreviousInstructingAgent2 <PrvsInstgAgt2> [0..1] ± 463
     PreviousInstructingAgent2Account
<PrvsInstgAgt2Acct>
[0..1] ± C22,
C21
464
     PreviousInstructingAgent3 <PrvsInstgAgt3> [0..1] ± 465
     PreviousInstructingAgent3Account
<PrvsInstgAgt3Acct>
[0..1] ± C22,
C21
465
     IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 466
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1] ± C22,
C21
467
     IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 468
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1] ± C22,
C21
468
     IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 469
     IntermediaryAgent3Account <IntrmyAgt3Acct> [0..1] ± C22,
C21
470
     CreditorAgent <CdtrAgt> [1..1] ± 471
     CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C22,
C21
471
     Creditor <Cdtr> [1..1] ± 472
     CreditorAccount <CdtrAcct> [0..1] ± C22,
C21
473
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
357 March 2026
```

## File page 358

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     UltimateCreditor <UltmtCdtr> [0..1] ± 474
     InstructionForCreditorAgent <InstrForCdtrAgt> [0..*] ± 475
     InstructionForNextAgent <InstrForNxtAgt> [0..*]  476
       Code <Cd> [0..1] CodeSet 476
       InstructionInformation <InstrInf> [0..1] Text 476
     Purpose <Purp> [0..1] ± 476
     Tax <Tax> [0..1]  477
       Creditor <Cdtr> [0..1] ± 479
       Debtor <Dbtr> [0..1] ± 479
       UltimateDebtor <UltmtDbtr> [0..1] ± 479
       AdministrationZone <AdmstnZone> [0..1] Text 480
       ReferenceNumber <RefNb> [0..1] Text 480
       Method <Mtd> [0..1] Text 480
       TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C12 480
       TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C12 481
       Date <Dt> [0..1] Date 481
       SequenceNumber <SeqNb> [0..1] Quantity 481
       Record <Rcrd> [0..*]  481
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
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
358 March 2026
```

## File page 359

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           TotalAmount <TtlAmt> [0..1] Amount C2, C12 485
           Details <Dtls> [0..*]  486
             Period <Prd> [0..1]  486
               Year <Yr> [0..1] Year 486
               Type <Tp> [0..1] CodeSet 487
               FromToDate <FrToDt> [0..1] ± 487
             Amount <Amt> [1..1] Amount C2, C12 488
         AdditionalInformation <AddtlInf> [0..1] Text 488
     RemittanceInformation <RmtInf> [0..1]  488
       Unstructured <Ustrd> [0..*] Text 492
       Structured <Strd> [0..*]  492
         ReferredDocumentInformation <RfrdDocInf> [0..*]  496
           Type <Tp> [0..1]  498
             CodeOrProprietary <CdOrPrtry> [1..1]  498
{Or               Code <Cd> [1..1] CodeSet 498
Or}               Proprietary <Prtry> [1..1] Text 498
             Issuer <Issr> [0..1] Text 498
           Number <Nb> [0..1] Text 499
           RelatedDate <RltdDt> [0..1]  499
             Type <Tp> [1..1]  499
{Or               Code <Cd> [1..1] CodeSet 499
Or}               Proprietary <Prtry> [1..1] Text 499
             Date <Dt> [1..1] Date 499
           LineDetails <LineDtls> [0..*]  500
             Identification <Id> [1..*]  500
               Type <Tp> [0..1]  501
                 CodeOrProprietary <CdOrPrtry> [1..1]  501
{Or                   Code <Cd> [1..1] CodeSet 501
Or}                   Proprietary <Prtry> [1..1] Text 501
                 Issuer <Issr> [0..1] Text 502
               Number <Nb> [0..1] Text 502
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
359 March 2026
```

