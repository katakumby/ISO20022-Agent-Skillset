---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.1 Batch <Btch>", "3.4.2.15.18.1.5 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [368, 369, 370, 371, 372, 373, 374, 375, 376, 377]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.1.5 CreditDebitIndicator <CdtDbtInd>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 368 to 377.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 368

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
3.4.2.15.18.1.5  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether the batch entry is a credit or a debit entry.
Datatype: "CreditDebitCode" on page 892
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
3.4.2.15.18.2  TransactionDetails <TxDtls>
Presence: [0..*]
Definition: Provides information on the underlying transaction(s).
Impacted by: C25 "PaymentTypeOrLocalInstrumentRule"
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
368 March 2026
```

## File page 369

```text
TransactionDetails <TxDtls> contains the following EntryTransaction16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   References <Refs> [0..1]  380
     MessageIdentification <MsgId> [0..1] Text 381
     AccountServicerReference <AcctSvcrRef> [0..1] Text 381
     PaymentInformationIdentification <PmtInfId> [0..1] Text 381
     InstructionIdentification <InstrId> [0..1] Text 382
     EndToEndIdentification <EndToEndId> [0..1] Text 382
     UETR <UETR> [0..1] IdentifierSet 382
     TransactionIdentification <TxId> [0..1] Text 382
     MandateIdentification <MndtId> [0..1] Text 382
     ChequeNumber <ChqNb> [0..1] Text 383
     ClearingSystemReference <ClrSysRef> [0..1] Text 383
     AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 383
     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 383
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 383
     ProcessingIdentification <PrcgId> [0..1] Text 383
     ReturnIdentification <RtrId> [0..1] Text 383
     Proprietary <Prtry> [0..*]  384
       Type <Tp> [1..1] Text 384
       Reference <Ref> [1..1] Text 384
   Amount <Amt> [0..1] Amount C2, C6 384
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 384
   AmountDetails <AmtDtls> [0..1] ± 385
   Availability <Avlbty> [0..*] ± 385
   BankTransactionCode <BkTxCd> [0..1] ± C11,
C14
385
   Charges <Chrgs> [0..1]  386
     TotalChargesAndTaxAmount <TtlChrgsAndTaxAmt> [0..1] Amount C2, C6 387
     Record <Rcrd> [0..*]  387
       Amount <Amt> [1..1] Amount C2, C6 388
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 388
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
369 March 2026
```

## File page 370

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       ChargeIncludedIndicator <ChrgInclInd> [0..1] Indicator 389
       Type <Tp> [0..1]  389
{Or         Code <Cd> [1..1] CodeSet 389
Or}         Proprietary <Prtry> [1..1] ± 389
       Rate <Rate> [0..1] Rate 389
       Bearer <Br> [0..1] CodeSet 390
       Agent <Agt> [0..1] ± 390
       Tax <Tax> [0..1]  391
         Identification <Id> [0..1] Text 391
         Rate <Rate> [0..1] Rate 391
         Amount <Amt> [0..1] Amount C2, C6 391
   Interest <Intrst> [0..1] ± 391
   RelatedParties <RltdPties> [0..1]  392
     InitiatingParty <InitgPty> [0..1]  393
{Or       Party <Pty> [1..1] ± 394
Or}       Agent <Agt> [1..1] ± 395
     Debtor <Dbtr> [0..1]  396
{Or       Party <Pty> [1..1] ± 396
Or}       Agent <Agt> [1..1] ± 397
     DebtorAccount <DbtrAcct> [0..1] ± C20,
C18
398
     UltimateDebtor <UltmtDbtr> [0..1]  399
{Or       Party <Pty> [1..1] ± 399
Or}       Agent <Agt> [1..1] ± 400
     Creditor <Cdtr> [0..1]  401
{Or       Party <Pty> [1..1] ± 401
Or}       Agent <Agt> [1..1] ± 402
     CreditorAccount <CdtrAcct> [0..1] ± C20,
C18
403
     UltimateCreditor <UltmtCdtr> [0..1]  404
{Or       Party <Pty> [1..1] ± 404
Or}       Agent <Agt> [1..1] ± 405
     TradingParty <TradgPty> [0..1]  406
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
370 March 2026
```

## File page 371

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       Party <Pty> [1..1] ± 406
Or}       Agent <Agt> [1..1] ± 407
     Proprietary <Prtry> [0..*]  408
       Type <Tp> [1..1] Text 408
       Party <Pty> [1..1]  408
{Or         Party <Pty> [1..1] ± 409
Or}         Agent <Agt> [1..1] ± 410
   RelatedAgents <RltdAgts> [0..1]  411
     InstructingAgent <InstgAgt> [0..1] ± 412
     InstructedAgent <InstdAgt> [0..1] ± 413
     DebtorAgent <DbtrAgt> [0..1] ± 414
     CreditorAgent <CdtrAgt> [0..1] ± 415
     IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 415
     IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 416
     IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 417
     ReceivingAgent <RcvgAgt> [0..1] ± 418
     DeliveringAgent <DlvrgAgt> [0..1] ± 419
     IssuingAgent <IssgAgt> [0..1] ± 420
     SettlementPlace <SttlmPlc> [0..1] ± 421
     Proprietary <Prtry> [0..*]  421
       Type <Tp> [1..1] Text 421
       Agent <Agt> [1..1] ± 421
   LocalInstrument <LclInstrm> [0..1]  422
{Or     Code <Cd> [1..1] CodeSet 422
Or}     Proprietary <Prtry> [1..1] Text 422
   PaymentTypeInformation <PmtTpInf> [0..1] ± 423
   Purpose <Purp> [0..1] ± 423
   RelatedRemittanceInformation <RltdRmtInf> [0..10]  423
     RemittanceIdentification <RmtId> [0..1] Text 424
     RemittanceLocationDetails <RmtLctnDtls> [0..*]  424
       Method <Mtd> [1..1] CodeSet 424
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
371 March 2026
```

## File page 372

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       ElectronicAddress <ElctrncAdr> [0..1] Text 425
       PostalAddress <PstlAdr> [0..1]  425
         Name <Nm> [1..1] Text 425
         Address <Adr> [1..1] ± 425
   RemittanceInformation <RmtInf> [0..1]  426
     Unstructured <Ustrd> [0..*] Text 430
     Structured <Strd> [0..*]  430
       ReferredDocumentInformation <RfrdDocInf> [0..*]  434
         Type <Tp> [0..1]  436
           CodeOrProprietary <CdOrPrtry> [1..1]  436
{Or             Code <Cd> [1..1] CodeSet 436
Or}             Proprietary <Prtry> [1..1] Text 436
           Issuer <Issr> [0..1] Text 436
         Number <Nb> [0..1] Text 437
         RelatedDate <RltdDt> [0..1]  437
           Type <Tp> [1..1]  437
{Or             Code <Cd> [1..1] CodeSet 437
Or}             Proprietary <Prtry> [1..1] Text 437
           Date <Dt> [1..1] Date 437
         LineDetails <LineDtls> [0..*]  438
           Identification <Id> [1..*]  438
             Type <Tp> [0..1]  439
               CodeOrProprietary <CdOrPrtry> [1..1]  439
{Or                 Code <Cd> [1..1] CodeSet 439
Or}                 Proprietary <Prtry> [1..1] Text 439
               Issuer <Issr> [0..1] Text 440
             Number <Nb> [0..1] Text 440
             RelatedDate <RltdDt> [0..1] Date 440
           Description <Desc> [0..1] Text 440
           Amount <Amt> [0..1]  C27 440
             RemittanceAmountAndType <RmtAmtAndTp> [0..*]  441
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
372 March 2026
```

## File page 373

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
               Type <Tp> [1..1]  441
{Or                 Code <Cd> [1..1] CodeSet 442
Or}                 Proprietary <Prtry> [1..1] Text 442
               Amount <Amt> [1..1] Amount C2, C6 442
             AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  442
               Amount <Amt> [1..1] Amount C2, C6 442
               CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 443
               Reason <Rsn> [0..1] Text 443
               AdditionalInformation <AddtlInf> [0..1] Text 443
       ReferredDocumentAmount <RfrdDocAmt> [0..1]  C27 443
         RemittanceAmountAndType <RmtAmtAndTp> [0..*]  444
           Type <Tp> [1..1]  444
{Or             Code <Cd> [1..1] CodeSet 445
Or}             Proprietary <Prtry> [1..1] Text 445
           Amount <Amt> [1..1] Amount C2, C6 445
         AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  445
           Amount <Amt> [1..1] Amount C2, C6 445
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 446
           Reason <Rsn> [0..1] Text 446
           AdditionalInformation <AddtlInf> [0..1] Text 446
       CreditorReferenceInformation <CdtrRefInf> [0..1]  446
         Type <Tp> [0..1]  447
           CodeOrProprietary <CdOrPrtry> [1..1]  447
{Or             Code <Cd> [1..1] CodeSet 447
Or}             Proprietary <Prtry> [1..1] Text 447
           Issuer <Issr> [0..1] Text 448
         Reference <Ref> [0..1] Text 448
       Invoicer <Invcr> [0..1] ± 448
       Invoicee <Invcee> [0..1] ± 449
       TaxRemittance <TaxRmt> [0..1]  450
         Creditor <Cdtr> [0..1] ± 452
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
373 March 2026
```

## File page 374

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Debtor <Dbtr> [0..1] ± 452
         UltimateDebtor <UltmtDbtr> [0..1] ± 452
         AdministrationZone <AdmstnZone> [0..1] Text 453
         ReferenceNumber <RefNb> [0..1] Text 453
         Method <Mtd> [0..1] Text 453
         TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C6 453
         TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C6 454
         Date <Dt> [0..1] Date 454
         SequenceNumber <SeqNb> [0..1] Quantity 454
         Record <Rcrd> [0..*]  454
           Type <Tp> [0..1] Text 455
           Category <Ctgy> [0..1] Text 455
           CategoryDetails <CtgyDtls> [0..1] Text 455
           DebtorStatus <DbtrSts> [0..1] Text 456
           CertificateIdentification <CertId> [0..1] Text 456
           FormsCode <FrmsCd> [0..1] Text 456
           Period <Prd> [0..1]  456
             Year <Yr> [0..1] Year 456
             Type <Tp> [0..1] CodeSet 456
             FromToDate <FrToDt> [0..1] ± 457
           TaxAmount <TaxAmt> [0..1]  458
             Rate <Rate> [0..1] Rate 458
             TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 458
             TotalAmount <TtlAmt> [0..1] Amount C2, C6 458
             Details <Dtls> [0..*]  459
               Period <Prd> [0..1]  459
                 Year <Yr> [0..1] Year 459
                 Type <Tp> [0..1] CodeSet 460
                 FromToDate <FrToDt> [0..1] ± 460
               Amount <Amt> [1..1] Amount C2, C6 461
           AdditionalInformation <AddtlInf> [0..1] Text 461
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
374 March 2026
```

## File page 375

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       GarnishmentRemittance <GrnshmtRmt> [0..1]  461
         Type <Tp> [1..1]  462
           CodeOrProprietary <CdOrPrtry> [1..1]  462
{Or             Code <Cd> [1..1] CodeSet 463
Or}             Proprietary <Prtry> [1..1] Text 463
           Issuer <Issr> [0..1] Text 463
         Garnishee <Grnshee> [0..1] ± 463
         GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 464
         ReferenceNumber <RefNb> [0..1] Text 465
         Date <Dt> [0..1] Date 466
         RemittedAmount <RmtdAmt> [0..1] Amount C2, C6 466
         FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 466
         EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 466
       SecuritiesData <SctiesData> [0..*]  466
         UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 467
         Amount <Amt> [0..1] Amount C1, C7 467
       AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 467
   RelatedDates <RltdDts> [0..1]  467
     AcceptanceDateTime <AccptncDtTm> [0..1] DateTime 468
     TradeActivityContractualSettlementDate
<TradActvtyCtrctlSttlmDt>
[0..1] Date 468
     TradeDate <TradDt> [0..1] Date 468
     InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 468
     StartDate <StartDt> [0..1] Date 468
     EndDate <EndDt> [0..1] Date 469
     TransactionDateTime <TxDtTm> [0..1] DateTime 469
     Proprietary <Prtry> [0..*]  469
       Type <Tp> [1..1] Text 469
       Date <Dt> [1..1] ± 469
   RelatedPrice <RltdPric> [0..1]  469
{Or     DealPrice <DealPric> [1..1] ± 470
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
375 March 2026
```

## File page 376

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}     Proprietary <Prtry> [1..*]  470
       Type <Tp> [1..1] Text 470
       Price <Pric> [1..1] Amount C2, C6 470
   RelatedQuantities <RltdQties> [0..*]  471
{Or     Quantity <Qty> [1..1] ± C10 471
Or     OriginalAndCurrentFaceAmount
<OrgnlAndCurFaceAmt>
[1..1] ± 472
Or}     Proprietary <Prtry> [1..1]  472
       Type <Tp> [1..1] Text 472
       Quantity <Qty> [1..1] Text 472
   FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C8, C9,
C21,
C22,
C24
472
   Tax <Tax> [0..1]  473
     Creditor <Cdtr> [0..1] ± 475
     Debtor <Dbtr> [0..1] ± 475
     UltimateDebtor <UltmtDbtr> [0..1] ± 475
     AdministrationZone <AdmstnZone> [0..1] Text 476
     ReferenceNumber <RefNb> [0..1] Text 476
     Method <Mtd> [0..1] Text 476
     TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C6 476
     TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C6 477
     Date <Dt> [0..1] Date 477
     SequenceNumber <SeqNb> [0..1] Quantity 477
     Record <Rcrd> [0..*]  477
       Type <Tp> [0..1] Text 478
       Category <Ctgy> [0..1] Text 478
       CategoryDetails <CtgyDtls> [0..1] Text 478
       DebtorStatus <DbtrSts> [0..1] Text 479
       CertificateIdentification <CertId> [0..1] Text 479
       FormsCode <FrmsCd> [0..1] Text 479
       Period <Prd> [0..1]  479
         Year <Yr> [0..1] Year 479
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
376 March 2026
```

## File page 377

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Type <Tp> [0..1] CodeSet 479
         FromToDate <FrToDt> [0..1] ± 480
       TaxAmount <TaxAmt> [0..1]  481
         Rate <Rate> [0..1] Rate 481
         TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 481
         TotalAmount <TtlAmt> [0..1] Amount C2, C6 481
         Details <Dtls> [0..*]  482
           Period <Prd> [0..1]  482
             Year <Yr> [0..1] Year 482
             Type <Tp> [0..1] CodeSet 483
             FromToDate <FrToDt> [0..1] ± 483
           Amount <Amt> [1..1] Amount C2, C6 484
       AdditionalInformation <AddtlInf> [0..1] Text 484
   ReturnInformation <RtrInf> [0..1]  C28 484
     OriginalBankTransactionCode <OrgnlBkTxCd> [0..1] ± C11,
C14
485
     Originator <Orgtr> [0..1] ± 486
     Reason <Rsn> [0..1]  487
{Or       Code <Cd> [1..1] CodeSet 488
Or}       Proprietary <Prtry> [1..1] Text 488
     AdditionalInformation <AddtlInf> [0..*] Text 488
   RelatedCorporateAction <RltdCorpActn> [0..1]  488
     EventType <EvtTp> [1..1] ± C12 488
     CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 489
     OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 489
   SafekeepingAccount <SfkpgAcct> [0..1] ± 489
   UnderlyingAllocation <UndrlygAllcn> [0..*]  C31 490
     Amount <Amt> [1..1] Amount C2, C6 490
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 490
     Account <Acct> [1..1] ± C20,
C18
491
     Purpose <Purp> [1..1] ± 491
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
377 March 2026
```

