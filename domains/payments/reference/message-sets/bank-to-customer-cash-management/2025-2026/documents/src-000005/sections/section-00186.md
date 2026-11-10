---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.2 Structure"]
file_pages: [264, 265, 266, 267, 268, 269, 270, 271, 272, 273]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.2 Structure

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 264 to 273.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 264

```text
3.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <BkToCstmrStmt> [1..1]  C23,
C29
   GroupHeader <GrpHdr> [1..1]  0
     MessageIdentification <MsgId> [1..1] Text 283
     CreationDateTime <CreDtTm> [1..1] DateTime 283
     MessageRecipient <MsgRcpt> [0..1] ± 283
     MessagePagination <MsgPgntn> [0..1] ± 284
     OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 285
     AdditionalInformation <AddtlInf> [0..1] Text 285
   Statement <Stmt> [1..*]  285
     Identification <Id> [1..1] Text 301
     StatementPagination <StmtPgntn> [0..1] ± 302
     ElectronicSequenceNumber <ElctrncSeqNb> [0..1] Quantity 302
     ReportingSequence <RptgSeq> [0..1] ± 302
     LegalSequenceNumber <LglSeqNb> [0..1] Quantity 302
     CreationDateTime <CreDtTm> [0..1] DateTime 303
     FromToDate <FrToDt> [0..1] ± 303
     CopyDuplicateIndicator <CpyDplctInd> [0..1] CodeSet 303
     ReportingSource <RptgSrc> [0..1] ± 303
     Account <Acct> [1..1]  C19,
C17
304
       Identification <Id> [0..1] ± 304
       Type <Tp> [0..1] ± 305
       Currency <Ccy> [0..1] CodeSet C2 305
       Name <Nm> [0..1] Text 305
       Proxy <Prxy> [0..1] ± 305
       Owner <Ownr> [0..1] ± 306
       Servicer <Svcr> [0..1] ± 307
     RelatedAccount <RltdAcct> [0..1] ± C20,
C18
308
     Interest <Intrst> [0..*]  309
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
264 March 2026
```

## File page 265

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       Type <Tp> [0..1]  309
{Or         Code <Cd> [1..1] CodeSet 310
Or}         Proprietary <Prtry> [1..1] Text 310
       Rate <Rate> [0..*]  310
         Type <Tp> [1..1] ± 310
         ValidityRange <VldtyRg> [0..1] ± 310
       FromToDate <FrToDt> [0..1] ± 311
       Reason <Rsn> [0..1] Text 311
       Tax <Tax> [0..1]  311
         Identification <Id> [0..1] Text 311
         Rate <Rate> [0..1] Rate 312
         Amount <Amt> [0..1] Amount C2, C6 312
     Balance <Bal> [1..*] ± C15 312
     TransactionsSummary <TxsSummry> [0..1] ± 313
     Entry <Ntry> [0..*]  C26 313
       EntryReference <NtryRef> [0..1] Text 329
       Amount <Amt> [1..1] Amount C2, C6 329
       CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 330
       ReversalIndicator <RvslInd> [0..1] Indicator 330
       Status <Sts> [1..1] ± 330
       BookingDate <BookgDt> [0..1] ± 331
       ValueDate <ValDt> [0..1] ± 331
       AccountServicerReference <AcctSvcrRef> [0..1] Text 331
       Availability <Avlbty> [0..*] ± 332
       BankTransactionCode <BkTxCd> [1..1] ± C11,
C14
332
       CommissionWaiverIndicator <ComssnWvrInd> [0..1] Indicator 333
       AdditionalInformationIndicator <AddtlInfInd> [0..1]  333
         MessageNameIdentification <MsgNmId> [0..1] Text 333
         MessageIdentification <MsgId> [0..1] Text 333
       AmountDetails <AmtDtls> [0..1] ± 333
       Charges <Chrgs> [0..1]  334
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
265 March 2026
```

## File page 266

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         TotalChargesAndTaxAmount <TtlChrgsAndTaxAmt> [0..1] Amount C2, C6 334
         Record <Rcrd> [0..*]  335
           Amount <Amt> [1..1] Amount C2, C6 335
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 336
           ChargeIncludedIndicator <ChrgInclInd> [0..1] Indicator 336
           Type <Tp> [0..1]  336
{Or             Code <Cd> [1..1] CodeSet 336
Or}             Proprietary <Prtry> [1..1] ± 337
           Rate <Rate> [0..1] Rate 337
           Bearer <Br> [0..1] CodeSet 337
           Agent <Agt> [0..1] ± 337
           Tax <Tax> [0..1]  338
             Identification <Id> [0..1] Text 338
             Rate <Rate> [0..1] Rate 338
             Amount <Amt> [0..1] Amount C2, C6 339
       TechnicalInputChannel <TechInptChanl> [0..1]  339
{Or         Code <Cd> [1..1] CodeSet 339
Or}         Proprietary <Prtry> [1..1] Text 339
       Interest <Intrst> [0..1] ± 339
       CardTransaction <CardTx> [0..1]  340
         Card <Card> [0..1]  342
           PlainCardData <PlainCardData> [0..1]  343
             PAN <PAN> [1..1] Text 344
             CardSequenceNumber <CardSeqNb> [0..1] Text 344
             EffectiveDate <FctvDt> [0..1] YearMonth 344
             ExpiryDate <XpryDt> [1..1] YearMonth 344
             ServiceCode <SvcCd> [0..1] Text 344
             TrackData <TrckData> [0..*]  345
               TrackNumber <TrckNb> [0..1] Text 345
               TrackValue <TrckVal> [1..1] Text 345
             CardSecurityCode <CardSctyCd> [0..1]  345
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
266 March 2026
```

## File page 267

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
               CSCManagement <CSCMgmt> [1..1] CodeSet 345
               CSCValue <CSCVal> [0..1] Text 346
           CardCountryCode <CardCtryCd> [0..1] Text 346
           CardBrand <CardBrnd> [0..1] ± 346
           AdditionalCardData <AddtlCardData> [0..1] Text 346
         POI <POI> [0..1]  346
           Identification <Id> [1..1] ± 347
           SystemName <SysNm> [0..1] Text 348
           GroupIdentification <GrpId> [0..1] Text 348
           Capabilities <Cpblties> [0..1]  348
             CardReadingCapabilities <CardRdngCpblties> [0..*] CodeSet 348
             CardholderVerificationCapabilities
<CrdhldrVrfctnCpblties>
[0..*] CodeSet 349
             OnLineCapabilities <OnLineCpblties> [0..1] CodeSet 349
             DisplayCapabilities <DispCpblties> [0..*]  350
               DisplayType <DispTp> [1..1] CodeSet 350
               NumberOfLines <NbOfLines> [1..1] Text 350
               LineWidth <LineWidth> [1..1] Text 350
             PrintLineWidth <PrtLineWidth> [0..1] Text 350
           Component <Cmpnt> [0..*]  350
             POIComponentType <POICmpntTp> [1..1] CodeSet 351
             ManufacturerIdentification <ManfctrId> [0..1] Text 351
             Model <Mdl> [0..1] Text 351
             VersionNumber <VrsnNb> [0..1] Text 351
             SerialNumber <SrlNb> [0..1] Text 352
             ApprovalNumber <ApprvlNb> [0..*] Text 352
         AggregatedEntry <AggtdNtry> [0..1]  352
           AdditionalService <AddtlSvc> [0..1] CodeSet 352
           TransactionCategory <TxCtgy> [0..1] CodeSet 353
           SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 353
           SequenceNumberRange <SeqNbRg> [0..1]  353
             FirstTransaction <FrstTx> [0..1] Text 353
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
267 March 2026
```

## File page 268

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             LastTransaction <LastTx> [0..1] Text 353
           TransactionDateRange <TxDtRg> [0..1] ± 354
         PrePaidAccount <PrePdAcct> [0..1] ± C20,
C18
354
       EntryDetails <NtryDtls> [0..*]  354
         Batch <Btch> [0..1]  367
           MessageIdentification <MsgId> [0..1] Text 367
           PaymentInformationIdentification <PmtInfId> [0..1] Text 367
           NumberOfTransactions <NbOfTxs> [0..1] Text 367
           TotalAmount <TtlAmt> [0..1] Amount C2, C6 367
           CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 368
         TransactionDetails <TxDtls> [0..*]  C25 368
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
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
268 March 2026
```

## File page 269

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
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
               ChargeIncludedIndicator <ChrgInclInd> [0..1] Indicator 389
               Type <Tp> [0..1]  389
{Or                 Code <Cd> [1..1] CodeSet 389
Or}                 Proprietary <Prtry> [1..1] ± 389
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
{Or               Party <Pty> [1..1] ± 394
Or}               Agent <Agt> [1..1] ± 395
             Debtor <Dbtr> [0..1]  396
{Or               Party <Pty> [1..1] ± 396
Or}               Agent <Agt> [1..1] ± 397
             DebtorAccount <DbtrAcct> [0..1] ± C20,
C18
398
             UltimateDebtor <UltmtDbtr> [0..1]  399
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
269 March 2026
```

## File page 270

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or               Party <Pty> [1..1] ± 399
Or}               Agent <Agt> [1..1] ± 400
             Creditor <Cdtr> [0..1]  401
{Or               Party <Pty> [1..1] ± 401
Or}               Agent <Agt> [1..1] ± 402
             CreditorAccount <CdtrAcct> [0..1] ± C20,
C18
403
             UltimateCreditor <UltmtCdtr> [0..1]  404
{Or               Party <Pty> [1..1] ± 404
Or}               Agent <Agt> [1..1] ± 405
             TradingParty <TradgPty> [0..1]  406
{Or               Party <Pty> [1..1] ± 406
Or}               Agent <Agt> [1..1] ± 407
             Proprietary <Prtry> [0..*]  408
               Type <Tp> [1..1] Text 408
               Party <Pty> [1..1]  408
{Or                 Party <Pty> [1..1] ± 409
Or}                 Agent <Agt> [1..1] ± 410
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
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
270 March 2026
```

## File page 271

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
               Agent <Agt> [1..1] ± 421
           LocalInstrument <LclInstrm> [0..1]  422
{Or             Code <Cd> [1..1] CodeSet 422
Or}             Proprietary <Prtry> [1..1] Text 422
           PaymentTypeInformation <PmtTpInf> [0..1] ± 423
           Purpose <Purp> [0..1] ± 423
           RelatedRemittanceInformation <RltdRmtInf> [0..10]  423
             RemittanceIdentification <RmtId> [0..1] Text 424
             RemittanceLocationDetails <RmtLctnDtls> [0..*]  424
               Method <Mtd> [1..1] CodeSet 424
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
{Or                     Code <Cd> [1..1] CodeSet 436
Or}                     Proprietary <Prtry> [1..1] Text 436
                   Issuer <Issr> [0..1] Text 436
                 Number <Nb> [0..1] Text 437
                 RelatedDate <RltdDt> [0..1]  437
                   Type <Tp> [1..1]  437
{Or                     Code <Cd> [1..1] CodeSet 437
Or}                     Proprietary <Prtry> [1..1] Text 437
                   Date <Dt> [1..1] Date 437
                 LineDetails <LineDtls> [0..*]  438
                   Identification <Id> [1..*]  438
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
271 March 2026
```

## File page 272

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
                     Type <Tp> [0..1]  439
                       CodeOrProprietary <CdOrPrtry> [1..1]  439
{Or                         Code <Cd> [1..1] CodeSet 439
Or}                         Proprietary <Prtry> [1..1] Text 439
                       Issuer <Issr> [0..1] Text 440
                     Number <Nb> [0..1] Text 440
                     RelatedDate <RltdDt> [0..1] Date 440
                   Description <Desc> [0..1] Text 440
                   Amount <Amt> [0..1]  C27 440
                     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  441
                       Type <Tp> [1..1]  441
{Or                         Code <Cd> [1..1] CodeSet 442
Or}                         Proprietary <Prtry> [1..1] Text 442
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
{Or                     Code <Cd> [1..1] CodeSet 445
Or}                     Proprietary <Prtry> [1..1] Text 445
                   Amount <Amt> [1..1] Amount C2, C6 445
                 AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  445
                   Amount <Amt> [1..1] Amount C2, C6 445
                   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 446
                   Reason <Rsn> [0..1] Text 446
                   AdditionalInformation <AddtlInf> [0..1] Text 446
               CreditorReferenceInformation <CdtrRefInf> [0..1]  446
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
272 March 2026
```

## File page 273

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
                 Type <Tp> [0..1]  447
                   CodeOrProprietary <CdOrPrtry> [1..1]  447
{Or                     Code <Cd> [1..1] CodeSet 447
Or}                     Proprietary <Prtry> [1..1] Text 447
                   Issuer <Issr> [0..1] Text 448
                 Reference <Ref> [0..1] Text 448
               Invoicer <Invcr> [0..1] ± 448
               Invoicee <Invcee> [0..1] ± 449
               TaxRemittance <TaxRmt> [0..1]  450
                 Creditor <Cdtr> [0..1] ± 452
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
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
273 March 2026
```

