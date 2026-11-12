---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.2 Structure"]
file_pages: [1310, 1311, 1312, 1313, 1314, 1315, 1316, 1317, 1318]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1310 to 1318.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1310

```text
38.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <AcctHldgInf> [1..1]  C12,
C13,
C25,
C26,
C29
   MessageReference <MsgRef> [1..1] ± 1324
   PoolReference <PoolRef> [0..1] ± 1324
   PreviousReference <PrvsRef> [0..1] ± 1325
   RelatedReference <RltdRef> [0..1] ± 0
   BusinessFlowDirectionType <BizFlowDrctnTp> [0..1] CodeSet 0
   PrimaryIndividualInvestor <PmryIndvInvstr> [0..1] ± C41 0
   SecondaryIndividualInvestor <ScndryIndvInvstr> [0..1] ± C41 0
   OtherIndividualInvestor <OthrIndvInvstr> [0..*] ± C41 0
   PrimaryCorporateInvestor <PmryCorpInvstr> [0..1] ± 0
   SecondaryCorporateInvestor <ScndryCorpInvstr> [0..1] ± 1328
   OtherCorporateInvestor <OthrCorpInvstr> [0..*] ± 0
   TransferorAccount <TrfrAcct> [1..1] ± 0
   NomineeAccount <NmneeAcct> [0..1] ± 0
   Transferee <Trfee> [1..1] ± 0
   ProductTransfer <PdctTrf> [1..*]  0
     MasterReference <MstrRef> [0..1] Text 1341
     TransferIdentification <TrfId> [1..1] Text 1341
     TransferConfirmationIdentification <TrfConfId> [0..1] Text 1341
     Portfolio <Prtfl> [0..1]  1341
{Or       TaxEfficientProduct <TaxEffcntPdct> [1..1]  1345
         TaxEfficientProductType <TaxEffcntPdctTp> [1..1] ± 1347
         CurrentYear <CurYr> [0..1] Indicator 1347
         CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1348
         PreviousYears <PrvsYrs> [0..1]  C42 1348
           PreviousYears <PrvsYrs> [1..1]  1348
{Or             AllPreviousYears <AllPrvsYrs> [1..1] Text 1348
Or}             SpecificPreviousYears <SpcfcPrvsYrs> [1..*] Year 1349
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1310 May 2026
```

## File page 1311

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1349
         PreviousYearSubscriptionAmount <PrvsYrSbcptAmt> [0..1] Amount C1 1349
         PreviousYearsSubscriptionAmount <PrvsYrsSbcptAmt> [0..1] Amount C1 1349
         DateOfFirstSubscription <DtOfFrstSbcpt> [0..1] Date 1349
         CurrentYearSubscriptionDetails <CurYrSbcptDtls> [0..1]  C45 1350
           DateOfFirstSubscription <DtOfFrstSbcpt> [1..1] Date 1350
           EquityComponent <EqtyCmpnt> [0..1] Amount C1 1350
           CashComponent <CshCmpnt> [0..1] Amount C1 1350
           TotalAmountYearToDate <TtlAmtYrToDt> [1..1] Amount C1 1351
         BonusOrWithdrawal <BnsOrWdrwl> [0..*]  1351
           TypeOfAmount <TpOfAmt> [1..1]  1352
{Or             Code <Cd> [1..1] CodeSet 1352
Or}             Proprietary <Prtry> [1..1] ± 1352
           Amount <Amt> [0..1] Amount C2 1352
           Reason <Rsn> [0..1]  1353
{Or             Code <Cd> [1..1] CodeSet 1353
Or}             Proprietary <Prtry> [1..1] ± 1353
           UnclaimedAmount <UclmdAmt> [0..1] Amount C2 1353
           Outstanding <Outsdng> [0..1] Indicator 1354
           Reference <Ref> [0..1] Text 1354
           AdditionalInformation <AddtlInf> [0..*] ± 1354
         WithdrawalForResidentialPurchaseProgress
<WdrwlForResdtlPurchsPrgrs>
[0..1] Indicator 1354
         TransferorAlternateIdentification <TrfrAltrnId> [0..1] Text 1354
         TotalSubscriptionAmount <TtlSbcptAmt> [0..1] Amount C1, C15 1355
         OtherAmount <OthrAmt> [0..*]  1355
           Type <Tp> [1..1] ± 1355
           Amount <Amt> [1..1] Amount C1, C15 1355
         DateFirstQualifyingAddition <DtFrstQlfygAddtn> [0..1] Date 1356
         InvestorTaxReference <InvstrTaxRef> [0..1]  1356
           Type <Tp> [0..1]  1356
{Or             Code <Cd> [1..1] CodeSet 1356
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1311 May 2026
```

## File page 1312

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}             Proprietary <Prtry> [1..1] ± 1357
           Reference <Ref> [1..1] Text 1357
         InvestmentsToFollowValue <InvstmtsToFllwVal> [0..*] ± 1357
         InnovativeFinance <InnvtvFinc> [0..*]  1357
           Type <Tp> [1..1] ± 1358
           Information <Inf> [1..1] Text 1358
         LowestInvestedAmountCurrentYear <LwstInvstdAmtCurYr> [0..1] Amount C1 1358
         TaxCalculationBase <TaxClctnBase> [0..1] Amount C1 1358
         UnusedTaxDeduction <UusdTaxDdctn> [0..1] Amount C1 1359
         CurrentInvestmentAmount <CurInvstmtAmt> [0..1] Amount C1 1359
         EstimatedValue <EstmtdVal> [0..1] ± 1359
         AdditionalInformation <AddtlInf> [0..*] ± 1360
Or       GeneralInvestment <GnlInvstmt> [1..1] ± 1360
Or}       Pension <Pnsn> [1..1]  C9, C10,
C36,
C37,
C38,
C39,
C43,
C44,
C47
1360
         Identification <Id> [0..1]  1363
           Identifier <Idr> [1..1] Text 1364
           SubIdentifier <SubIdr> [0..1] Text 1364
           AdditionalInformation <AddtlInf> [0..1] ± 1364
         Type <Tp> [1..1]  1364
{Or           Code <Cd> [1..1] CodeSet 1364
Or}           Proprietary <Prtry> [1..1] ± 1365
         TransferScope <TrfScp> [0..1] ± 1366
         TaxReference <TaxRef> [0..*] ± 1366
         DrawdownTrancheIdentification <DrwdwnTrchId> [0..1] Text 1366
         DrawdownStatus <DrwdwnSts> [0..1] ± 1366
         DrawdownType <DrwdwnTp> [0..1] ± 1367
         NumberOfDrawdownTranches <NbOfDrwdwnTrnchs> [0..1] Quantity 1367
         EstimatedValue <EstmtdVal> [0..1] ± 1367
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1312 May 2026
```

## File page 1313

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         BlockTransfer <BlckTrf> [0..1] Indicator 1367
         BlockTransferReference <BlckTrfRef> [0..1] Text 1368
         TaxFreeCashProtection <TaxFreeCshPrtcn> [0..1] Indicator 1368
         TaxFreeCashAmount <TaxFreeCshAmt> [0..1] ± 1368
         ValueOfPensionPolicyOrPlanOrScheme
<ValOfPnsnPlcyOrPlanOrSchme>
[0..1] ± 1368
         RetirementAgeProtection <RtrmntAgePrtcn> [0..1] Indicator 1368
         RetirementAge <RtrmntAge> [0..1] Quantity 1369
         Sharing <Shrg> [0..1] Indicator 1369
         LumpSumType <LumpSumTp> [0..*] ± 1369
         PensionOrder <PnsnOrdr> [0..*] ± 1369
         RingFencedDrawdownAssets <RingFncdDrwdwnAssts> [0..1] Indicator 1369
         MoneyPurchaseAnnualAllowance <MnyPurchsAnlAllwnc> [0..1] ± 1370
         SafeguardBenefit <SfgrdBnft> [0..1] Indicator 1370
         NonSafeguardedGuaranteedBenefits
<NonSfgrddGrntedBnfts>
[0..1] Indicator 1370
         LifetimeAllowanceProtection <LftmAllwncPrtcn> [0..1] Indicator 1370
         ClientLifetimeAllowanceProtection <ClntLftmAllwncPrtcn> [0..1] Indicator 1370
         BenefitCrystallisationEventOccurred
<BnftCrstllstnEvtOcrd>
[0..1] Indicator 1371
         NonWrapperTransfer <NonWrpprTrf> [0..1] Indicator 1371
         AdditionalInformation <AddtlInf> [0..*] ± 1371
     PartialDiscovery <PrtlDscvry> [0..1] Indicator 1371
     ResidualCash <RsdlCsh> [0..*] ± 1371
     TaxDate <TaxDt> [0..1] Date 1372
     FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf> [0..*]  C7, C8 1372
       LineIdentification <LineId> [0..1] Text 1378
       Instrument <Instrm> [1..1]  1379
{Or         Security <Scty> [1..1]  C23 1381
           Identification <Id> [1..1]  1383
{Or             ISIN <ISIN> [1..1] IdentifierSet 1384
Or             SEDOL <SEDOL> [1..1] IdentifierSet 1384
Or             CUSIP <CUSIP> [1..1] IdentifierSet 1385
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1313 May 2026
```

## File page 1314

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or             RIC <RIC> [1..1] IdentifierSet 1385
Or             TickerSymbol <TckrSymb> [1..1] IdentifierSet 1385
Or             Bloomberg <Blmbrg> [1..1] IdentifierSet 1385
Or             CTA <CTA> [1..1] IdentifierSet 1385
Or             QUICK <QUICK> [1..1] IdentifierSet 1385
Or             Wertpapier <Wrtppr> [1..1] IdentifierSet 1385
Or             Dutch <Dtch> [1..1] IdentifierSet 1386
Or             Valoren <Vlrn> [1..1] IdentifierSet 1386
Or             Sicovam <SCVM> [1..1] IdentifierSet 1386
Or             Belgian <Belgn> [1..1] IdentifierSet 1386
Or             Common <Cmon> [1..1] IdentifierSet 1386
Or             DTI <DTI> [1..1] IdentifierSet 1386
Or}             OtherProprietaryIdentification <OthrPrtryId> [1..1]  1386
               Identification <Id> [1..1] Text 1387
               IdentificationSource <IdSrc> [1..1] ± 1387
           Name <Nm> [0..1] Text 1387
           ShortName <ShrtNm> [0..1] Text 1387
           ClassificationType <ClssfctnTp> [0..1] ± 1387
           RestrictedIndicator <RstrctdInd> [0..1] Indicator 1387
           AlternateSecurity <AltrnScty> [0..*]  C24 1388
             Identification <Id> [1..1]  1389
{Or               ISIN <ISIN> [1..1] IdentifierSet 1389
Or               SEDOL <SEDOL> [1..1] IdentifierSet 1390
Or               CUSIP <CUSIP> [1..1] IdentifierSet 1390
Or               RIC <RIC> [1..1] IdentifierSet 1390
Or               TickerSymbol <TckrSymb> [1..1] IdentifierSet 1390
Or               Bloomberg <Blmbrg> [1..1] IdentifierSet 1390
Or               CTA <CTA> [1..1] IdentifierSet 1390
Or               QUICK <QUICK> [1..1] IdentifierSet 1390
Or               Wertpapier <Wrtppr> [1..1] IdentifierSet 1391
Or               Dutch <Dtch> [1..1] IdentifierSet 1391
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1314 May 2026
```

## File page 1315

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or               Valoren <Vlrn> [1..1] IdentifierSet 1391
Or               Sicovam <SCVM> [1..1] IdentifierSet 1391
Or               Belgian <Belgn> [1..1] IdentifierSet 1391
Or               Common <Cmon> [1..1] IdentifierSet 1391
Or               DTI <DTI> [1..1] IdentifierSet 1391
Or}               OtherProprietaryIdentification <OthrPrtryId> [1..1]  1391
                 Identification <Id> [1..1] Text 1392
                 IdentificationSource <IdSrc> [1..1] ± 1392
             Name <Nm> [0..1] Text 1392
             ShortName <ShrtNm> [0..1] Text 1392
             ClassificationType <ClssfctnTp> [0..1] ± 1392
             AlternateSecurityType <AltrnSctyTp> [0..1] ± 1393
Or         CashAsset <CshAsst> [1..1] ± 1393
Or}         OtherAsset <OthrAsst> [1..1] ± 1393
       Quantity <Qty> [0..1]  1394
         Unit <Unit> [0..1]  1394
{Or           UnitsNumber <UnitsNb> [1..1] Quantity 1395
Or}           DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1395
         PercentageRate <PctgRate> [0..1] Rate 1395
         FaceAmount <FaceAmt> [0..1] Amount 1395
         AmortisedValue <AmtsdVal> [0..1] Amount 1395
         CashAmount <CshAmt> [0..1] Amount C1 1395
         OtherAsset <OthrAsst> [0..1] Text 1395
       UnitsDetails <UnitsDtls> [0..*]  1396
         Units <Units> [1..1]  1399
{Or           UnitsNumber <UnitsNb> [1..1] Quantity 1399
Or}           DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1399
         OrderDate <OrdrDt> [0..1] Date 1399
         AcquisitionDate <AcqstnDt> [0..1] Date 1399
         CertificateNumber <CertNb> [0..*] Text 1399
         Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 1399
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1315 May 2026
```

## File page 1316

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         Reference <Ref> [0..1] Text 1400
         PriceDetails <PricDtls> [0..1] ± 1400
         TransactionOverhead <TxOvrhd> [0..1]  C30,
C46
1400
           TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C15 1402
           TotalFees <TtlFees> [0..1] Amount C1, C15 1403
           TotalTaxes <TtlTaxs> [0..1] Amount C1, C15 1403
           CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 1403
           IndividualFee <IndvFee> [0..*]  C6 1404
             Type <Tp> [1..1]  1404
{Or               Code <Cd> [1..1] CodeSet 1405
Or}               Proprietary <Prtry> [1..1] ± 1406
             Basis <Bsis> [0..1]  1406
{Or               Code <Cd> [1..1] CodeSet 1406
Or}               Proprietary <Prtry> [1..1] ± 1407
             StandardAmount <StdAmt> [0..1] Amount C1, C15 1407
             StandardRate <StdRate> [0..1] Rate 1407
             DiscountDetails <DscntDtls> [0..1]  C21 1408
               Amount <Amt> [0..1] Amount C1, C15 1408
               Rate <Rate> [0..1] Rate 1409
               Basis <Bsis> [0..1]  1409
{Or                 Code <Cd> [1..1] CodeSet 1409
Or}                 Proprietary <Prtry> [1..1] ± 1409
             AppliedAmount <ApldAmt> [0..1] Amount C1, C15 1410
             AppliedRate <ApldRate> [0..1] Rate 1410
             NonStandardSLAReference <NonStdSLARef> [0..1] Text 1410
             RecipientIdentification <RcptId> [0..1] ± 1410
             InformativeIndicator <InftvInd> [1..1] Indicator 1411
           IndividualTax <IndvTax> [0..*] ± 1411
           DigitalNetworkFee <DgtlNtwkFee> [0..2]  1411
             FinancialInstrumentIdentification <FinInstrmId> [1..1]  C18,
C19,
C27,
1412
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1316 May 2026
```

## File page 1317

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
C28,
C31
               ISIN <ISIN> [0..1] IdentifierSet 1414
               OtherIdentification <OthrId> [0..*]  1414
                 Identification <Id> [1..1] Text 1414
                 Suffix <Sfx> [0..1] Text 1414
                 Type <Tp> [1..1]  1414
{Or                   Code <Cd> [1..1] CodeSet 1415
Or}                   Proprietary <Prtry> [1..1] Text 1416
               Description <Desc> [0..1] Text 1416
             Quantity <Qty> [1..1]  1417
{Or               Quantity <Qty> [1..1] ± C20 1417
Or}               ProprietaryQuantity <PrtryQty> [1..1]  1417
                 Quantity <Qty> [1..1] Quantity 1418
                 QuantityType <QtyTp> [1..1] Text 1418
                 Issuer <Issr> [1..1] Text 1418
                 SchemeName <SchmeNm> [0..1] Text 1418
             DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1418
         OtherAmount <OthrAmt> [0..*]  1418
           Type <Tp> [1..1]  1419
{Or             Code <Cd> [1..1] CodeSet 1419
Or}             ProprietaryCode <PrtryCd> [1..1] ± 1419
           Amount <Amt> [1..1] Amount C1, C15 1419
       ClientReference <ClntRef> [0..1] ± 1420
       CounterpartyReference <CtrPtyRef> [0..1] ± 1420
       BusinessFlowType <BizFlowTp> [0..1] CodeSet 1420
       AverageAcquisitionPrice <AvrgAcqstnPric> [0..1] Amount C2, C16 1421
       TransferCurrency <TrfCcy> [0..1] CodeSet C2 1421
       TotalBookValue <TtlBookVal> [0..1] ± 1421
       LatestValuation <LatstValtn> [0..1] ± 1422
       OriginalCost <OrgnlCost> [0..1] Amount C1 1422
       TransfereeAccount <TrfeeAcct> [0..1]  1422
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1317 May 2026
```

## File page 1318

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         OwnerIdentification <OwnrId> [0..1] ± 1423
         AccountIdentification <AcctId> [0..1] Text 1423
         Designation <Dsgnt> [0..1] Text 1423
         AccountName <AcctNm> [0..1] Text 1423
         Servicer <Svcr> [0..1] ± 1424
         SubAccountDetails <SubAcctDtls> [0..1] ± 1424
         BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1424
       Transferor <Trfr> [0..*]  1425
         OwnerIdentification <OwnrId> [0..1] ± 1425
         AccountIdentification <AcctId> [0..1] Text 1425
         Designation <Dsgnt> [0..1] Text 1425
         AccountName <AcctNm> [0..1] Text 1426
         Servicer <Svcr> [0..1] ± 1426
         SubAccountDetails <SubAcctDtls> [0..1] ± 1426
         BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1426
       IntermediaryInformation <IntrmyInf> [0..*] ± 1427
       CrystallisationDetails <CrstllstnDtls> [0..*] ± 1427
       TaxValuationPoint <TaxValtnPt> [0..1] ± 1427
       SettlementPartiesDetails <SttlmPtiesDtls> [0..*]  1428
         SafekeepingPlace <SfkpgPlc> [0..1] ± 1429
         TradeTransactionCondition <TradTxCond> [0..*] ± 1430
         SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1430
         SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 1430
         ReceivingSideDetails <RcvgSdDtls> [0..1]  C11,
C17,
C32,
C33,
C34,
C35,
C40
1431
           Depository <Dpstry> [0..1] ± 1432
           Party1 <Pty1> [0..1] ± 1433
           Party2 <Pty2> [0..1] ± 1433
           Party3 <Pty3> [0..1] ± 1434
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1318 May 2026
```

