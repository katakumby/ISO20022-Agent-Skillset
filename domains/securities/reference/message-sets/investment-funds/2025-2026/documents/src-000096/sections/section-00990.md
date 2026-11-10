---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.7 TaxDate <TaxDt>"]
file_pages: [1372, 1373, 1374, 1375, 1376, 1377]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.7 TaxDate <TaxDt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1372 to 1377.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1372

```text
ResidualCash <RsdlCsh> contains the following elements (see "ResidualCash1" on page 4872 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ResidualCashIndicator <RsdlCshInd> [1..1] Indicator 4872
   Currency <Ccy> [0..1] CodeSet C1 4872
38.4.15.7  TaxDate <TaxDt>
Presence: [0..1]
Definition: Tax date applicable to all the assets.
Datatype: "ISODate" on page 5388
38.4.15.8  FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>
Presence: [0..*]
Definition: Asset to be transferred.
Impacted by: C7 "AssetQuantity1Guideline", C8 "AssetQuantity2Guideline"
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1372 May 2026
```

## File page 1373

```text
FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf> contains the following
FinancialInstrument110 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LineIdentification <LineId> [0..1] Text 1378
   Instrument <Instrm> [1..1]  1379
{Or     Security <Scty> [1..1]  C23 1381
       Identification <Id> [1..1]  1383
{Or         ISIN <ISIN> [1..1] IdentifierSet 1384
Or         SEDOL <SEDOL> [1..1] IdentifierSet 1384
Or         CUSIP <CUSIP> [1..1] IdentifierSet 1385
Or         RIC <RIC> [1..1] IdentifierSet 1385
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 1385
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 1385
Or         CTA <CTA> [1..1] IdentifierSet 1385
Or         QUICK <QUICK> [1..1] IdentifierSet 1385
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 1385
Or         Dutch <Dtch> [1..1] IdentifierSet 1386
Or         Valoren <Vlrn> [1..1] IdentifierSet 1386
Or         Sicovam <SCVM> [1..1] IdentifierSet 1386
Or         Belgian <Belgn> [1..1] IdentifierSet 1386
Or         Common <Cmon> [1..1] IdentifierSet 1386
Or         DTI <DTI> [1..1] IdentifierSet 1386
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  1386
           Identification <Id> [1..1] Text 1387
           IdentificationSource <IdSrc> [1..1] ± 1387
       Name <Nm> [0..1] Text 1387
       ShortName <ShrtNm> [0..1] Text 1387
       ClassificationType <ClssfctnTp> [0..1] ± 1387
       RestrictedIndicator <RstrctdInd> [0..1] Indicator 1387
       AlternateSecurity <AltrnScty> [0..*]  C24 1388
         Identification <Id> [1..1]  1389
{Or           ISIN <ISIN> [1..1] IdentifierSet 1389
Or           SEDOL <SEDOL> [1..1] IdentifierSet 1390
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1373 May 2026
```

## File page 1374

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or           CUSIP <CUSIP> [1..1] IdentifierSet 1390
Or           RIC <RIC> [1..1] IdentifierSet 1390
Or           TickerSymbol <TckrSymb> [1..1] IdentifierSet 1390
Or           Bloomberg <Blmbrg> [1..1] IdentifierSet 1390
Or           CTA <CTA> [1..1] IdentifierSet 1390
Or           QUICK <QUICK> [1..1] IdentifierSet 1390
Or           Wertpapier <Wrtppr> [1..1] IdentifierSet 1391
Or           Dutch <Dtch> [1..1] IdentifierSet 1391
Or           Valoren <Vlrn> [1..1] IdentifierSet 1391
Or           Sicovam <SCVM> [1..1] IdentifierSet 1391
Or           Belgian <Belgn> [1..1] IdentifierSet 1391
Or           Common <Cmon> [1..1] IdentifierSet 1391
Or           DTI <DTI> [1..1] IdentifierSet 1391
Or}           OtherProprietaryIdentification <OthrPrtryId> [1..1]  1391
             Identification <Id> [1..1] Text 1392
             IdentificationSource <IdSrc> [1..1] ± 1392
         Name <Nm> [0..1] Text 1392
         ShortName <ShrtNm> [0..1] Text 1392
         ClassificationType <ClssfctnTp> [0..1] ± 1392
         AlternateSecurityType <AltrnSctyTp> [0..1] ± 1393
Or     CashAsset <CshAsst> [1..1] ± 1393
Or}     OtherAsset <OthrAsst> [1..1] ± 1393
   Quantity <Qty> [0..1]  1394
     Unit <Unit> [0..1]  1394
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 1395
Or}       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1395
     PercentageRate <PctgRate> [0..1] Rate 1395
     FaceAmount <FaceAmt> [0..1] Amount 1395
     AmortisedValue <AmtsdVal> [0..1] Amount 1395
     CashAmount <CshAmt> [0..1] Amount C1 1395
     OtherAsset <OthrAsst> [0..1] Text 1395
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1374 May 2026
```

## File page 1375

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitsDetails <UnitsDtls> [0..*]  1396
     Units <Units> [1..1]  1399
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 1399
Or}       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1399
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
{Or           Code <Cd> [1..1] CodeSet 1405
Or}           Proprietary <Prtry> [1..1] ± 1406
         Basis <Bsis> [0..1]  1406
{Or           Code <Cd> [1..1] CodeSet 1406
Or}           Proprietary <Prtry> [1..1] ± 1407
         StandardAmount <StdAmt> [0..1] Amount C1, C15 1407
         StandardRate <StdRate> [0..1] Rate 1407
         DiscountDetails <DscntDtls> [0..1]  C21 1408
           Amount <Amt> [0..1] Amount C1, C15 1408
           Rate <Rate> [0..1] Rate 1409
           Basis <Bsis> [0..1]  1409
{Or             Code <Cd> [1..1] CodeSet 1409
Or}             Proprietary <Prtry> [1..1] ± 1409
         AppliedAmount <ApldAmt> [0..1] Amount C1, C15 1410
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1375 May 2026
```

## File page 1376

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         AppliedRate <ApldRate> [0..1] Rate 1410
         NonStandardSLAReference <NonStdSLARef> [0..1] Text 1410
         RecipientIdentification <RcptId> [0..1] ± 1410
         InformativeIndicator <InftvInd> [1..1] Indicator 1411
       IndividualTax <IndvTax> [0..*] ± 1411
       DigitalNetworkFee <DgtlNtwkFee> [0..2]  1411
         FinancialInstrumentIdentification <FinInstrmId> [1..1]  C18,
C19,
C27,
C28,
C31
1412
           ISIN <ISIN> [0..1] IdentifierSet 1414
           OtherIdentification <OthrId> [0..*]  1414
             Identification <Id> [1..1] Text 1414
             Suffix <Sfx> [0..1] Text 1414
             Type <Tp> [1..1]  1414
{Or               Code <Cd> [1..1] CodeSet 1415
Or}               Proprietary <Prtry> [1..1] Text 1416
           Description <Desc> [0..1] Text 1416
         Quantity <Qty> [1..1]  1417
{Or           Quantity <Qty> [1..1] ± C20 1417
Or}           ProprietaryQuantity <PrtryQty> [1..1]  1417
             Quantity <Qty> [1..1] Quantity 1418
             QuantityType <QtyTp> [1..1] Text 1418
             Issuer <Issr> [1..1] Text 1418
             SchemeName <SchmeNm> [0..1] Text 1418
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1418
     OtherAmount <OthrAmt> [0..*]  1418
       Type <Tp> [1..1]  1419
{Or         Code <Cd> [1..1] CodeSet 1419
Or}         ProprietaryCode <PrtryCd> [1..1] ± 1419
       Amount <Amt> [1..1] Amount C1, C15 1419
   ClientReference <ClntRef> [0..1] ± 1420
   CounterpartyReference <CtrPtyRef> [0..1] ± 1420
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1376 May 2026
```

## File page 1377

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BusinessFlowType <BizFlowTp> [0..1] CodeSet 1420
   AverageAcquisitionPrice <AvrgAcqstnPric> [0..1] Amount C2, C16 1421
   TransferCurrency <TrfCcy> [0..1] CodeSet C2 1421
   TotalBookValue <TtlBookVal> [0..1] ± 1421
   LatestValuation <LatstValtn> [0..1] ± 1422
   OriginalCost <OrgnlCost> [0..1] Amount C1 1422
   TransfereeAccount <TrfeeAcct> [0..1]  1422
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
1431
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1377 May 2026
```

