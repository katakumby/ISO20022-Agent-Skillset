---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: []
file_pages: [295, 296, 297, 298, 299, 300]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# Continuation at file page 295

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 295 to 300.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 295

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
295 March 2026
```

## File page 296

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             GarnishmentRemittance <GrnshmtRmt> [0..1]  461
               Type <Tp> [1..1]  462
                 CodeOrProprietary <CdOrPrtry> [1..1]  462
{Or                   Code <Cd> [1..1] CodeSet 463
Or}                   Proprietary <Prtry> [1..1] Text 463
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
{Or           DealPrice <DealPric> [1..1] ± 470
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
296 March 2026
```

## File page 297

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..*]  470
             Type <Tp> [1..1] Text 470
             Price <Pric> [1..1] Amount C2, C6 470
         RelatedQuantities <RltdQties> [0..*]  471
{Or           Quantity <Qty> [1..1] ± C10 471
Or           OriginalAndCurrentFaceAmount
<OrgnlAndCurFaceAmt>
[1..1] ± 472
Or}           Proprietary <Prtry> [1..1]  472
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
297 March 2026
```

## File page 298

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
{Or             Code <Cd> [1..1] CodeSet 488
Or}             Proprietary <Prtry> [1..1] Text 488
           AdditionalInformation <AddtlInf> [0..*] Text 488
         RelatedCorporateAction <RltdCorpActn> [0..1]  488
           EventType <EvtTp> [1..1] ± C12 488
           CorporateActionEventIdentification
<CorpActnEvtId>
[1..1] Text 489
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
298 March 2026
```

## File page 299

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Reference <Ref> [1..1] Text 492
           RelatedReferences <RltdRefs> [0..*] ± 492
         CashDeposit <CshDpst> [0..*] ± 492
         CardTransaction <CardTx> [0..1]  493
           Card <Card> [0..1]  496
             PlainCardData <PlainCardData> [0..1]  497
               PAN <PAN> [1..1] Text 498
               CardSequenceNumber <CardSeqNb> [0..1] Text 498
               EffectiveDate <FctvDt> [0..1] YearMonth 498
               ExpiryDate <XpryDt> [1..1] YearMonth 498
               ServiceCode <SvcCd> [0..1] Text 498
               TrackData <TrckData> [0..*]  499
                 TrackNumber <TrckNb> [0..1] Text 499
                 TrackValue <TrckVal> [1..1] Text 499
               CardSecurityCode <CardSctyCd> [0..1]  499
                 CSCManagement <CSCMgmt> [1..1] CodeSet 499
                 CSCValue <CSCVal> [0..1] Text 500
             CardCountryCode <CardCtryCd> [0..1] Text 500
             CardBrand <CardBrnd> [0..1] ± 500
             AdditionalCardData <AddtlCardData> [0..1] Text 500
           POI <POI> [0..1]  500
             Identification <Id> [1..1] ± 501
             SystemName <SysNm> [0..1] Text 502
             GroupIdentification <GrpId> [0..1] Text 502
             Capabilities <Cpblties> [0..1]  502
               CardReadingCapabilities <CardRdngCpblties> [0..*] CodeSet 502
               CardholderVerificationCapabilities
<CrdhldrVrfctnCpblties>
[0..*] CodeSet 503
               OnLineCapabilities <OnLineCpblties> [0..1] CodeSet 503
               DisplayCapabilities <DispCpblties> [0..*]  504
                 DisplayType <DispTp> [1..1] CodeSet 504
                 NumberOfLines <NbOfLines> [1..1] Text 504
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
299 March 2026
```

## File page 300

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
                 LineWidth <LineWidth> [1..1] Text 504
               PrintLineWidth <PrtLineWidth> [0..1] Text 504
             Component <Cmpnt> [0..*]  504
               POIComponentType <POICmpntTp> [1..1] CodeSet 505
               ManufacturerIdentification <ManfctrId> [0..1] Text 505
               Model <Mdl> [0..1] Text 505
               VersionNumber <VrsnNb> [0..1] Text 505
               SerialNumber <SrlNb> [0..1] Text 506
               ApprovalNumber <ApprvlNb> [0..*] Text 506
           Transaction <Tx> [0..1]  506
{Or             Aggregated <Aggtd> [1..1]  508
               AdditionalService <AddtlSvc> [0..1] CodeSet 508
               TransactionCategory <TxCtgy> [0..1] CodeSet 509
               SaleReconciliationIdentification
<SaleRcncltnId>
[0..1] Text 509
               SequenceNumberRange <SeqNbRg> [0..1]  509
                 FirstTransaction <FrstTx> [0..1] Text 509
                 LastTransaction <LastTx> [0..1] Text 509
               TransactionDateRange <TxDtRg> [0..1] ± 510
Or}             Individual <Indv> [1..1]  510
               ICCRelatedData <ICCRltdData> [0..1] Text 512
               PaymentContext <PmtCntxt> [0..1]  512
                 CardPresent <CardPres> [0..1] Indicator 512
                 CardholderPresent <CrdhldrPres> [0..1] Indicator 512
                 OnLineContext <OnLineCntxt> [0..1] Indicator 513
                 AttendanceContext <AttndncCntxt> [0..1] CodeSet 513
                 TransactionEnvironment <TxEnvt> [0..1] CodeSet 513
                 TransactionChannel <TxChanl> [0..1] CodeSet 513
                 AttendantMessageCapable <AttndntMsgCpbl> [0..1] Indicator 514
                 AttendantLanguage <AttndntLang> [0..1] CodeSet 514
                 CardDataEntryMode <CardDataNtryMd> [1..1] CodeSet 514
                 FallbackIndicator <FllbckInd> [0..1] Indicator 514
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
300 March 2026
```

