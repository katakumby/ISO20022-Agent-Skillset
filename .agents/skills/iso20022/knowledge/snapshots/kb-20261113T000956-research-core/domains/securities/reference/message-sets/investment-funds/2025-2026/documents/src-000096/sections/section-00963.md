---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>"]
file_pages: [1328, 1329, 1330, 1331, 1332, 1333, 1334, 1335, 1336, 1337]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1328 to 1337.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1328

```text
Constraints
• SocialSecurityNumberGuideline
The UK Insurance Number must be indicated without spaces.
38.4.9 PrimaryCorporateInvestor <PmryCorpInvstr>
Presence: [0..1]
Definition: Information identifying the primary corporate investor, for example, name and address.
PrimaryCorporateInvestor <PmryCorpInvstr> contains the following elements (see "Organisation36"
on page 4904 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 4904
   Identification <Id> [0..1] ± 4904
   Purpose <Purp> [0..1] Text 4904
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C12 4905
   RegistrationCountry <RegnCtry> [0..1] CodeSet C12 4905
   RegistrationDate <RegnDt> [0..1] Date 4905
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 4905
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 4905
   CorporateInvestorAddress <CorpInvstrAdr> [1..1] ± 4905
38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>
Presence: [0..1]
Definition: Information identifying the secondary corporate investor, for example, name and address.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1328 May 2026
```

## File page 1329

```text
SecondaryCorporateInvestor <ScndryCorpInvstr> contains the following elements (see
"Organisation36" on page 4904 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 4904
   Identification <Id> [0..1] ± 4904
   Purpose <Purp> [0..1] Text 4904
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C12 4905
   RegistrationCountry <RegnCtry> [0..1] CodeSet C12 4905
   RegistrationDate <RegnDt> [0..1] Date 4905
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 4905
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 4905
   CorporateInvestorAddress <CorpInvstrAdr> [1..1] ± 4905
38.4.11 OtherCorporateInvestor <OthrCorpInvstr>
Presence: [0..*]
Definition: Information identifying the other corporate investors, for example, name and address.
OtherCorporateInvestor <OthrCorpInvstr> contains the following elements (see "Organisation36" on
page 4904 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 4904
   Identification <Id> [0..1] ± 4904
   Purpose <Purp> [0..1] Text 4904
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C12 4905
   RegistrationCountry <RegnCtry> [0..1] CodeSet C12 4905
   RegistrationDate <RegnDt> [0..1] Date 4905
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 4905
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 4905
   CorporateInvestorAddress <CorpInvstrAdr> [1..1] ± 4905
38.4.12 TransferorAccount <TrfrAcct>
Presence: [1..1]
Definition: Identification of the account owned by the investor at the old plan manager (account
servicer).
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1329 May 2026
```

## File page 1330

```text
TransferorAccount <TrfrAcct> contains the following elements (see "InvestmentAccount69" on
page 4331 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 4331
   Designation <Dsgnt> [0..1] Text 4331
   AccountName <AcctNm> [0..1] Text 4332
   Servicer <Svcr> [0..1] ± 4332
38.4.13 NomineeAccount <NmneeAcct>
Presence: [0..1]
Definition: Account held in the name of a party that is not the name of the beneficial owner of the
shares.
NomineeAccount <NmneeAcct> contains the following elements (see "InvestmentAccount69" on
page 4331 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 4331
   Designation <Dsgnt> [0..1] Text 4331
   AccountName <AcctNm> [0..1] Text 4332
   Servicer <Svcr> [0..1] ± 4332
38.4.14 Transferee <Trfee>
Presence: [1..1]
Definition: Identification of the institution to which the financial instrument is to be transferred. This may
also be known as the new plan manager.
Transferee <Trfee> contains the following elements (see "PartyIdentification132" on page 5029 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C4 5029
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 5029
   NameAndAddress <NmAndAdr> [0..1] ± 5030
   ProprietaryIdentification <PrtryId> [0..1] ± 5031
   LEI <LEI> [0..1] IdentifierSet 5031
38.4.15 ProductTransfer <PdctTrf>
Presence: [1..*]
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1330 May 2026
```

## File page 1331

```text
Definition: Information about the portfolio and assets.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1331 May 2026
```

## File page 1332

```text
ProductTransfer <PdctTrf> contains the following PortfolioTransfer16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MasterReference <MstrRef> [0..1] Text 1341
   TransferIdentification <TrfId> [1..1] Text 1341
   TransferConfirmationIdentification <TrfConfId> [0..1] Text 1341
   Portfolio <Prtfl> [0..1]  1341
{Or     TaxEfficientProduct <TaxEffcntPdct> [1..1]  1345
       TaxEfficientProductType <TaxEffcntPdctTp> [1..1] ± 1347
       CurrentYear <CurYr> [0..1] Indicator 1347
       CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1348
       PreviousYears <PrvsYrs> [0..1]  C42 1348
         PreviousYears <PrvsYrs> [1..1]  1348
{Or           AllPreviousYears <AllPrvsYrs> [1..1] Text 1348
Or}           SpecificPreviousYears <SpcfcPrvsYrs> [1..*] Year 1349
         CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1349
       PreviousYearSubscriptionAmount
<PrvsYrSbcptAmt>
[0..1] Amount C1 1349
       PreviousYearsSubscriptionAmount
<PrvsYrsSbcptAmt>
[0..1] Amount C1 1349
       DateOfFirstSubscription <DtOfFrstSbcpt> [0..1] Date 1349
       CurrentYearSubscriptionDetails <CurYrSbcptDtls> [0..1]  C45 1350
         DateOfFirstSubscription <DtOfFrstSbcpt> [1..1] Date 1350
         EquityComponent <EqtyCmpnt> [0..1] Amount C1 1350
         CashComponent <CshCmpnt> [0..1] Amount C1 1350
         TotalAmountYearToDate <TtlAmtYrToDt> [1..1] Amount C1 1351
       BonusOrWithdrawal <BnsOrWdrwl> [0..*]  1351
         TypeOfAmount <TpOfAmt> [1..1]  1352
{Or           Code <Cd> [1..1] CodeSet 1352
Or}           Proprietary <Prtry> [1..1] ± 1352
         Amount <Amt> [0..1] Amount C2 1352
         Reason <Rsn> [0..1]  1353
{Or           Code <Cd> [1..1] CodeSet 1353
Or}           Proprietary <Prtry> [1..1] ± 1353
         UnclaimedAmount <UclmdAmt> [0..1] Amount C2 1353
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1332 May 2026
```

## File page 1333

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or           Code <Cd> [1..1] CodeSet 1356
Or}           Proprietary <Prtry> [1..1] ± 1357
         Reference <Ref> [1..1] Text 1357
       InvestmentsToFollowValue <InvstmtsToFllwVal> [0..*] ± 1357
       InnovativeFinance <InnvtvFinc> [0..*]  1357
         Type <Tp> [1..1] ± 1358
         Information <Inf> [1..1] Text 1358
       LowestInvestedAmountCurrentYear
<LwstInvstdAmtCurYr>
[0..1] Amount C1 1358
       TaxCalculationBase <TaxClctnBase> [0..1] Amount C1 1358
       UnusedTaxDeduction <UusdTaxDdctn> [0..1] Amount C1 1359
       CurrentInvestmentAmount <CurInvstmtAmt> [0..1] Amount C1 1359
       EstimatedValue <EstmtdVal> [0..1] ± 1359
       AdditionalInformation <AddtlInf> [0..*] ± 1360
Or     GeneralInvestment <GnlInvstmt> [1..1] ± 1360
Or}     Pension <Pnsn> [1..1]  C9, C10,
C36,
C37,
C38,
C39,
C43,
C44,
C47
1360
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1333 May 2026
```

## File page 1334

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Identification <Id> [0..1]  1363
         Identifier <Idr> [1..1] Text 1364
         SubIdentifier <SubIdr> [0..1] Text 1364
         AdditionalInformation <AddtlInf> [0..1] ± 1364
       Type <Tp> [1..1]  1364
{Or         Code <Cd> [1..1] CodeSet 1364
Or}         Proprietary <Prtry> [1..1] ± 1365
       TransferScope <TrfScp> [0..1] ± 1366
       TaxReference <TaxRef> [0..*] ± 1366
       DrawdownTrancheIdentification <DrwdwnTrchId> [0..1] Text 1366
       DrawdownStatus <DrwdwnSts> [0..1] ± 1366
       DrawdownType <DrwdwnTp> [0..1] ± 1367
       NumberOfDrawdownTranches
<NbOfDrwdwnTrnchs>
[0..1] Quantity 1367
       EstimatedValue <EstmtdVal> [0..1] ± 1367
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
       RingFencedDrawdownAssets
<RingFncdDrwdwnAssts>
[0..1] Indicator 1369
       MoneyPurchaseAnnualAllowance
<MnyPurchsAnlAllwnc>
[0..1] ± 1370
       SafeguardBenefit <SfgrdBnft> [0..1] Indicator 1370
       NonSafeguardedGuaranteedBenefits
<NonSfgrddGrntedBnfts>
[0..1] Indicator 1370
       LifetimeAllowanceProtection <LftmAllwncPrtcn> [0..1] Indicator 1370
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1334 May 2026
```

## File page 1335

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       ClientLifetimeAllowanceProtection
<ClntLftmAllwncPrtcn>
[0..1] Indicator 1370
       BenefitCrystallisationEventOccurred
<BnftCrstllstnEvtOcrd>
[0..1] Indicator 1371
       NonWrapperTransfer <NonWrpprTrf> [0..1] Indicator 1371
       AdditionalInformation <AddtlInf> [0..*] ± 1371
   PartialDiscovery <PrtlDscvry> [0..1] Indicator 1371
   ResidualCash <RsdlCsh> [0..*] ± 1371
   TaxDate <TaxDt> [0..1] Date 1372
   FinancialInstrumentAssetForTransfer
<FinInstrmAsstForTrf>
[0..*]  C7, C8 1372
     LineIdentification <LineId> [0..1] Text 1378
     Instrument <Instrm> [1..1]  1379
{Or       Security <Scty> [1..1]  C23 1381
         Identification <Id> [1..1]  1383
{Or           ISIN <ISIN> [1..1] IdentifierSet 1384
Or           SEDOL <SEDOL> [1..1] IdentifierSet 1384
Or           CUSIP <CUSIP> [1..1] IdentifierSet 1385
Or           RIC <RIC> [1..1] IdentifierSet 1385
Or           TickerSymbol <TckrSymb> [1..1] IdentifierSet 1385
Or           Bloomberg <Blmbrg> [1..1] IdentifierSet 1385
Or           CTA <CTA> [1..1] IdentifierSet 1385
Or           QUICK <QUICK> [1..1] IdentifierSet 1385
Or           Wertpapier <Wrtppr> [1..1] IdentifierSet 1385
Or           Dutch <Dtch> [1..1] IdentifierSet 1386
Or           Valoren <Vlrn> [1..1] IdentifierSet 1386
Or           Sicovam <SCVM> [1..1] IdentifierSet 1386
Or           Belgian <Belgn> [1..1] IdentifierSet 1386
Or           Common <Cmon> [1..1] IdentifierSet 1386
Or           DTI <DTI> [1..1] IdentifierSet 1386
Or}           OtherProprietaryIdentification <OthrPrtryId> [1..1]  1386
             Identification <Id> [1..1] Text 1387
             IdentificationSource <IdSrc> [1..1] ± 1387
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1335 May 2026
```

## File page 1336

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Name <Nm> [0..1] Text 1387
         ShortName <ShrtNm> [0..1] Text 1387
         ClassificationType <ClssfctnTp> [0..1] ± 1387
         RestrictedIndicator <RstrctdInd> [0..1] Indicator 1387
         AlternateSecurity <AltrnScty> [0..*]  C24 1388
           Identification <Id> [1..1]  1389
{Or             ISIN <ISIN> [1..1] IdentifierSet 1389
Or             SEDOL <SEDOL> [1..1] IdentifierSet 1390
Or             CUSIP <CUSIP> [1..1] IdentifierSet 1390
Or             RIC <RIC> [1..1] IdentifierSet 1390
Or             TickerSymbol <TckrSymb> [1..1] IdentifierSet 1390
Or             Bloomberg <Blmbrg> [1..1] IdentifierSet 1390
Or             CTA <CTA> [1..1] IdentifierSet 1390
Or             QUICK <QUICK> [1..1] IdentifierSet 1390
Or             Wertpapier <Wrtppr> [1..1] IdentifierSet 1391
Or             Dutch <Dtch> [1..1] IdentifierSet 1391
Or             Valoren <Vlrn> [1..1] IdentifierSet 1391
Or             Sicovam <SCVM> [1..1] IdentifierSet 1391
Or             Belgian <Belgn> [1..1] IdentifierSet 1391
Or             Common <Cmon> [1..1] IdentifierSet 1391
Or             DTI <DTI> [1..1] IdentifierSet 1391
Or}             OtherProprietaryIdentification <OthrPrtryId> [1..1]  1391
               Identification <Id> [1..1] Text 1392
               IdentificationSource <IdSrc> [1..1] ± 1392
           Name <Nm> [0..1] Text 1392
           ShortName <ShrtNm> [0..1] Text 1392
           ClassificationType <ClssfctnTp> [0..1] ± 1392
           AlternateSecurityType <AltrnSctyTp> [0..1] ± 1393
Or       CashAsset <CshAsst> [1..1] ± 1393
Or}       OtherAsset <OthrAsst> [1..1] ± 1393
     Quantity <Qty> [0..1]  1394
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1336 May 2026
```

## File page 1337

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Unit <Unit> [0..1]  1394
{Or         UnitsNumber <UnitsNb> [1..1] Quantity 1395
Or}         DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1395
       PercentageRate <PctgRate> [0..1] Rate 1395
       FaceAmount <FaceAmt> [0..1] Amount 1395
       AmortisedValue <AmtsdVal> [0..1] Amount 1395
       CashAmount <CshAmt> [0..1] Amount C1 1395
       OtherAsset <OthrAsst> [0..1] Text 1395
     UnitsDetails <UnitsDtls> [0..*]  1396
       Units <Units> [1..1]  1399
{Or         UnitsNumber <UnitsNb> [1..1] Quantity 1399
Or}         DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1399
       OrderDate <OrdrDt> [0..1] Date 1399
       AcquisitionDate <AcqstnDt> [0..1] Date 1399
       CertificateNumber <CertNb> [0..*] Text 1399
       Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 1399
       Reference <Ref> [0..1] Text 1400
       PriceDetails <PricDtls> [0..1] ± 1400
       TransactionOverhead <TxOvrhd> [0..1]  C30,
C46
1400
         TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C15 1402
         TotalFees <TtlFees> [0..1] Amount C1, C15 1403
         TotalTaxes <TtlTaxs> [0..1] Amount C1, C15 1403
         CommercialAgreementReference
<ComrclAgrmtRef>
[0..1] Text 1403
         IndividualFee <IndvFee> [0..*]  C6 1404
           Type <Tp> [1..1]  1404
{Or             Code <Cd> [1..1] CodeSet 1405
Or}             Proprietary <Prtry> [1..1] ± 1406
           Basis <Bsis> [0..1]  1406
{Or             Code <Cd> [1..1] CodeSet 1406
Or}             Proprietary <Prtry> [1..1] ± 1407
           StandardAmount <StdAmt> [0..1] Amount C1, C15 1407
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1337 May 2026
```

