---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.4 ReturnReasonInformation <RtrRsnInf>", "4.4.2.4.2 Reason <Rsn>", "4.4.2.4.2.1 Code <Cd>"]
file_pages: [291, 292, 293, 294, 295, 296, 297, 298, 299, 300]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.2.4.2.1 Code <Cd>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 291 to 300.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 291

```text
Reason <Rsn> contains one of the following ReturnReason5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 291
Or}   Proprietary <Prtry> [1..1] Text 291
4.4.2.4.2.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the return, as published in an external reason code list.
Datatype: "ExternalReturnReason1Code" on page 1233
4.4.2.4.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the return, in a proprietary form.
Datatype: "Max35Text" on page 1246
4.4.2.4.3  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Further details on the return reason.
Datatype: "Max105Text" on page 1244
4.4.3 TransactionInformation <TxInf>
Presence: [0..*]
Definition: Information concerning the original transactions, to which the return message refers.
Impacted by: C7 "ChargesInformationAndReturnedInstructedAmountRule", C60
"ReturnedInstructedAmountAndExchangeRate1Rule", C61
"ReturnedInstructedAmountAndExchangeRate2Rule"
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
291 March 2026
```

## File page 292

```text
TransactionInformation <TxInf> contains the following PaymentTransaction168 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReturnIdentification <RtrId> [0..1] Text 309
   OriginalGroupInformation <OrgnlGrpInf> [0..1]  309
     OriginalMessageIdentification <OrgnlMsgId> [1..1] Text 309
     OriginalMessageNameIdentification
<OrgnlMsgNmId>
[1..1] Text 309
     OriginalCreationDateTime <OrgnlCreDtTm> [0..1] DateTime 310
   OriginalInstructionIdentification <OrgnlInstrId> [0..1] Text 310
   OriginalEndToEndIdentification <OrgnlEndToEndId> [0..1] Text 310
   OriginalTransactionIdentification <OrgnlTxId> [0..1] Text 310
   OriginalUETR <OrgnlUETR> [0..1] IdentifierSet 310
   OriginalClearingSystemReference <OrgnlClrSysRef> [0..1] Text 310
   OriginalInterbankSettlementAmount
<OrgnlIntrBkSttlmAmt>
[0..1] Amount C2, C12 310
   OriginalInterbankSettlementDate <OrgnlIntrBkSttlmDt> [0..1] Date 311
   PaymentTypeInformation <PmtTpInf> [0..1] ± 311
   ReturnedInterbankSettlementAmount
<RtrdIntrBkSttlmAmt>
[1..1] Amount C1, C11 312
   InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 312
   SettlementPriority <SttlmPrty> [0..1] CodeSet 312
   SettlementTimeIndication <SttlmTmIndctn> [0..1]  313
     DebitDateTime <DbtDtTm> [0..1] DateTime 313
     CreditDateTime <CdtDtTm> [0..1] DateTime 313
   SettlementTimeRequest <SttlmTmReq> [0..1] ± 313
   ReturnedInstructedAmount <RtrdInstdAmt> [0..1] Amount C2, C12 313
   ExchangeRate <XchgRate> [0..1] Rate 314
   AgreedRate <AgrdRate> [0..1]  314
     UnitCurrency <UnitCcy> [0..1] CodeSet C2 314
     QuotedCurrency <QtdCcy> [0..1] CodeSet C2 315
     PreAgreedExchangeRate <PreAgrdXchgRate> [1..1] Rate 315
     QuotationDateTime <QtnDtTm> [0..1] DateTime 315
     QuoteIdentification <QtId> [0..1] IdentifierSet 315
     ForeignExchangeAgent <FXAgt> [0..1] ± 316
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
292 March 2026
```

## File page 293

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CompensationAmount <CompstnAmt> [0..1] Amount C2, C12 316
   ChargeBearer <ChrgBr> [0..1] CodeSet 317
   ChargesInformation <ChrgsInf> [0..*]  317
     Amount <Amt> [1..1] Amount C2, C12 317
     Agent <Agt> [1..1] ± 318
     Type <Tp> [0..1]  318
{Or       Code <Cd> [1..1] CodeSet 319
Or}       Proprietary <Prtry> [1..1] ± 319
   ClearingSystemReference <ClrSysRef> [0..1] Text 319
   InstructingAgent <InstgAgt> [0..1] ± 319
   InstructedAgent <InstdAgt> [0..1] ± 320
   ReturnChain <RtrChain> [0..1]  C27,
C31,
C36,
C44,
C49,
C54
321
     UltimateDebtor <UltmtDbtr> [0..1]  324
{Or       Party <Pty> [1..1] ± 324
Or}       Agent <Agt> [1..1] ± 325
     Debtor <Dbtr> [1..1]  326
{Or       Party <Pty> [1..1] ± 326
Or}       Agent <Agt> [1..1] ± 327
     DebtorAccount <DbtrAcct> [0..1] ± C22,
C21
328
     InitiatingParty <InitgPty> [0..1]  329
{Or       Party <Pty> [1..1] ± 329
Or}       Agent <Agt> [1..1] ± 330
     DebtorAgent <DbtrAgt> [0..1] ± 331
     DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C22,
C21
332
     PreviousInstructingAgent1 <PrvsInstgAgt1> [0..1] ± 332
     PreviousInstructingAgent1Account
<PrvsInstgAgt1Acct>
[0..1] ± C22,
C21
333
     PreviousInstructingAgent2 <PrvsInstgAgt2> [0..1] ± 334
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
293 March 2026
```

## File page 294

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     PreviousInstructingAgent2Account
<PrvsInstgAgt2Acct>
[0..1] ± C22,
C21
334
     PreviousInstructingAgent3 <PrvsInstgAgt3> [0..1] ± 335
     PreviousInstructingAgent3Account
<PrvsInstgAgt3Acct>
[0..1] ± C22,
C21
336
     IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 337
     IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1] ± C22,
C21
337
     IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 338
     IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1] ± C22,
C21
339
     IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 340
     IntermediaryAgent3Account <IntrmyAgt3Acct> [0..1] ± C22,
C21
340
     CreditorAgent <CdtrAgt> [0..1] ± 341
     CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C22,
C21
342
     Creditor <Cdtr> [1..1]  343
{Or       Party <Pty> [1..1] ± 343
Or}       Agent <Agt> [1..1] ± 344
     CreditorAccount <CdtrAcct> [0..1] ± C22,
C21
345
     UltimateCreditor <UltmtCdtr> [0..1]  346
{Or       Party <Pty> [1..1] ± 346
Or}       Agent <Agt> [1..1] ± 347
   ReturnReasonInformation <RtrRsnInf> [0..*]  C62 348
     Originator <Orgtr> [0..1] ± 349
     Reason <Rsn> [0..1]  350
{Or       Code <Cd> [1..1] CodeSet 350
Or}       Proprietary <Prtry> [1..1] Text 350
     AdditionalInformation <AddtlInf> [0..*] Text 350
   OriginalTransactionReference <OrgnlTxRef> [0..1]  C81,
C82
350
     InterbankSettlementAmount <IntrBkSttlmAmt> [0..1] Amount C2, C12 364
     Amount <Amt> [0..1] ± 365
     InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 365
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
294 March 2026
```

## File page 295

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or         Code <Cd> [1..1] CodeSet 371
Or}         Proprietary <Prtry> [1..1] Text 371
       InstructingReimbursementAgent
<InstgRmbrsmntAgt>
[0..1] ± 371
       InstructingReimbursementAgentAccount
<InstgRmbrsmntAgtAcct>
[0..1] ± C22,
C21
372
       InstructedReimbursementAgent
<InstdRmbrsmntAgt>
[0..1] ± 372
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
{Or       DirectDebitMandate <DrctDbtMndt> [1..1]  C3, C4 378
         MandateIdentification <MndtId> [0..1] Text 380
         DateOfSignature <DtOfSgntr> [0..1] Date 380
         AmendmentIndicator <AmdmntInd> [0..1] Indicator 380
         AmendmentInformationDetails <AmdmntInfDtls> [0..1]  380
           OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 381
           OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 381
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
295 March 2026
```

## File page 296

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 382
           OriginalCreditorAgentAccount
<OrgnlCdtrAgtAcct>
[0..1] ± C22,
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
{Or             Code <Cd> [1..1] CodeSet 388
Or}             Proprietary <Prtry> [1..1] Text 388
           OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 389
         ElectronicSignature <ElctrncSgntr> [0..1] Text 389
         FirstCollectionDate <FrstColltnDt> [0..1] Date 389
         FinalCollectionDate <FnlColltnDt> [0..1] Date 389
         Frequency <Frqcy> [0..1] ± 389
         Reason <Rsn> [0..1]  389
{Or           Code <Cd> [1..1] CodeSet 390
Or}           Proprietary <Prtry> [1..1] Text 390
         TrackingDays <TrckgDays> [0..1] Text 390
Or}       CreditTransferMandate <CdtTrfMndt> [1..1] ± 390
     RemittanceInformation <RmtInf> [0..1]  391
       Unstructured <Ustrd> [0..*] Text 395
       Structured <Strd> [0..*]  395
         ReferredDocumentInformation <RfrdDocInf> [0..*]  399
           Type <Tp> [0..1]  401
             CodeOrProprietary <CdOrPrtry> [1..1]  401
{Or               Code <Cd> [1..1] CodeSet 401
Or}               Proprietary <Prtry> [1..1] Text 401
             Issuer <Issr> [0..1] Text 401
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
296 March 2026
```

## File page 297

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Number <Nb> [0..1] Text 402
           RelatedDate <RltdDt> [0..1]  402
             Type <Tp> [1..1]  402
{Or               Code <Cd> [1..1] CodeSet 402
Or}               Proprietary <Prtry> [1..1] Text 402
             Date <Dt> [1..1] Date 402
           LineDetails <LineDtls> [0..*]  403
             Identification <Id> [1..*]  403
               Type <Tp> [0..1]  404
                 CodeOrProprietary <CdOrPrtry> [1..1]  404
{Or                   Code <Cd> [1..1] CodeSet 404
Or}                   Proprietary <Prtry> [1..1] Text 404
                 Issuer <Issr> [0..1] Text 405
               Number <Nb> [0..1] Text 405
               RelatedDate <RltdDt> [0..1] Date 405
             Description <Desc> [0..1] Text 405
             Amount <Amt> [0..1]  C59 405
               RemittanceAmountAndType <RmtAmtAndTp> [0..*]  406
                 Type <Tp> [1..1]  406
{Or                   Code <Cd> [1..1] CodeSet 407
Or}                   Proprietary <Prtry> [1..1] Text 407
                 Amount <Amt> [1..1] Amount C2, C12 407
               AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  407
                 Amount <Amt> [1..1] Amount C2, C12 407
                 CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 408
                 Reason <Rsn> [0..1] Text 408
                 AdditionalInformation <AddtlInf> [0..1] Text 408
         ReferredDocumentAmount <RfrdDocAmt> [0..1]  C59 408
           RemittanceAmountAndType <RmtAmtAndTp> [0..*]  409
             Type <Tp> [1..1]  409
{Or               Code <Cd> [1..1] CodeSet 410
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
297 March 2026
```

## File page 298

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}               Proprietary <Prtry> [1..1] Text 410
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
{Or               Code <Cd> [1..1] CodeSet 412
Or}               Proprietary <Prtry> [1..1] Text 412
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
             Type <Tp> [0..1] Text 420
             Category <Ctgy> [0..1] Text 420
             CategoryDetails <CtgyDtls> [0..1] Text 420
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
298 March 2026
```

## File page 299

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or               Code <Cd> [1..1] CodeSet 428
Or}               Proprietary <Prtry> [1..1] Text 428
             Issuer <Issr> [0..1] Text 428
           Garnishee <Grnshee> [0..1] ± 428
           GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 429
           ReferenceNumber <RefNb> [0..1] Text 430
           Date <Dt> [0..1] Date 431
           RemittedAmount <RmtdAmt> [0..1] Amount C2, C12 431
           FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 431
           EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 431
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
299 March 2026
```

## File page 300

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         SecuritiesData <SctiesData> [0..*]  431
           UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 432
           Amount <Amt> [0..1] Amount C1, C11 432
         AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 432
     UltimateDebtor <UltmtDbtr> [0..1]  432
{Or       Party <Pty> [1..1] ± 433
Or}       Agent <Agt> [1..1] ± 434
     Debtor <Dbtr> [0..1]  435
{Or       Party <Pty> [1..1] ± 435
Or}       Agent <Agt> [1..1] ± 436
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
{Or       Party <Pty> [1..1] ± 441
Or}       Agent <Agt> [1..1] ± 442
     CreditorAccount <CdtrAcct> [0..1] ± C22,
C21
443
     UltimateCreditor <UltmtCdtr> [0..1]  444
{Or       Party <Pty> [1..1] ± 444
Or}       Agent <Agt> [1..1] ± 445
     Purpose <Purp> [0..1] ± 446
     UnderlyingCustomerCreditTransfer
<UndrlygCstmrCdtTrf>
[0..1]  C28,
C32,
C34,
C37,
C39,
C45,
C50,
C52,
C55,
C57,
C47,
C76,
C78
446
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
300 March 2026
```

