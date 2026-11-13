---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: []
file_pages: [1338, 1339, 1340]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# Continuation at file page 1338

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1338 to 1340.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1338

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           StandardRate <StdRate> [0..1] Rate 1407
           DiscountDetails <DscntDtls> [0..1]  C21 1408
             Amount <Amt> [0..1] Amount C1, C15 1408
             Rate <Rate> [0..1] Rate 1409
             Basis <Bsis> [0..1]  1409
{Or               Code <Cd> [1..1] CodeSet 1409
Or}               Proprietary <Prtry> [1..1] ± 1409
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
C28,
C31
1412
             ISIN <ISIN> [0..1] IdentifierSet 1414
             OtherIdentification <OthrId> [0..*]  1414
               Identification <Id> [1..1] Text 1414
               Suffix <Sfx> [0..1] Text 1414
               Type <Tp> [1..1]  1414
{Or                 Code <Cd> [1..1] CodeSet 1415
Or}                 Proprietary <Prtry> [1..1] Text 1416
             Description <Desc> [0..1] Text 1416
           Quantity <Qty> [1..1]  1417
{Or             Quantity <Qty> [1..1] ± C20 1417
Or}             ProprietaryQuantity <PrtryQty> [1..1]  1417
               Quantity <Qty> [1..1] Quantity 1418
               QuantityType <QtyTp> [1..1] Text 1418
               Issuer <Issr> [1..1] Text 1418
               SchemeName <SchmeNm> [0..1] Text 1418
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1338 May 2026
```

## File page 1339

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1418
       OtherAmount <OthrAmt> [0..*]  1418
         Type <Tp> [1..1]  1419
{Or           Code <Cd> [1..1] CodeSet 1419
Or}           ProprietaryCode <PrtryCd> [1..1] ± 1419
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
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1339 May 2026
```

## File page 1340

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
         Party4 <Pty4> [0..1] ± 1434
         Party5 <Pty5> [0..1] ± 1435
       DeliveringSideDetails <DlvrgSdDtls> [0..1]  C11,
C17,
C32,
C33,
C34,
C35,
C40
1435
         Depository <Dpstry> [0..1] ± 1437
         Party1 <Pty1> [0..1] ± 1438
         Party2 <Pty2> [0..1] ± 1438
         Party3 <Pty3> [0..1] ± 1438
         Party4 <Pty4> [0..1] ± 1439
         Party5 <Pty5> [0..1] ± 1439
     AssetsHeldInOwnName <AsstsHeldInOwnNm> [0..1] Indicator 1440
     TransferResultsInChangeOfBeneficialOwner
<TrfRsltsInChngOfBnfclOwnr>
[0..1] Indicator 1440
     AdditionalInformation <AddtlInf> [0..*] ± 1440
   AdditionalInformation <AddtlInf> [0..*] ± 1440
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1340 May 2026
```

