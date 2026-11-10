---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["24 sese.001.001.10 TransferOutInstructionV10", "24.2 Structure"]
file_pages: [435, 436, 437, 438, 439, 440]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.001.001.10"]
---

# 24.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 435 to 440.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 435

```text
24.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <TrfOutInstr> [1..1]  C31
   MessageIdentification <MsgId> [1..1] ± 0
   PoolReference <PoolRef> [0..1] ± 0
   PreviousReference <PrvsRef> [0..1] ± 0
   RelatedReference <RltdRef> [0..1] ± 445
   MasterReference <MstrRef> [0..1] Text 445
   TransferDetails <TrfDtls> [1..*]  C33 0
     TransferReference <TrfRef> [1..1] Text 449
     ClientReference <ClntRef> [0..1] ± 449
     CounterpartyReference <CtrPtyRef> [0..1] ± 450
     BusinessFlowType <BizFlowTp> [0..1] CodeSet 450
     RequestedTransferDate <ReqdTrfDt> [0..1] ± 450
     RequestedSettlementDate <ReqdSttlmDt> [0..1] Date 451
     TransferOrderDateForm <TrfOrdrDtForm> [0..1] Date 451
     TransferReason <TrfRsn> [0..1] ± 451
     HoldingsPlanType <HldgsPlanTp> [0..3] CodeSet 451
     FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C19 452
       Identification <Id> [1..1]  453
{Or         ISIN <ISIN> [1..1] IdentifierSet 453
Or         SEDOL <SEDOL> [1..1] IdentifierSet 454
Or         CUSIP <CUSIP> [1..1] IdentifierSet 454
Or         RIC <RIC> [1..1] IdentifierSet 454
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 454
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 454
Or         CTA <CTA> [1..1] IdentifierSet 454
Or         QUICK <QUICK> [1..1] IdentifierSet 454
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 455
Or         Dutch <Dtch> [1..1] IdentifierSet 455
Or         Valoren <Vlrn> [1..1] IdentifierSet 455
Or         Sicovam <SCVM> [1..1] IdentifierSet 455
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 435 May 2026
```

## File page 436

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or         Belgian <Belgn> [1..1] IdentifierSet 455
Or         Common <Cmon> [1..1] IdentifierSet 455
Or         DTI <DTI> [1..1] IdentifierSet 455
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  455
           Identification <Id> [1..1] Text 456
           IdentificationSource <IdSrc> [1..1] ± 456
       Name <Nm> [0..1] Text 456
       ShortName <ShrtNm> [0..1] Text 456
       SupplementaryIdentification <SplmtryId> [0..1] Text 456
       ClassType <ClssTp> [0..1] Text 456
       SecuritiesForm <SctiesForm> [0..1] CodeSet 457
       DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 457
       DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 457
     Quantity <Qty> [1..1]  457
{Or       TotalUnitsNumber <TtlUnitsNb> [1..1]  458
{Or         UnitsNumber <UnitsNb> [1..1] Quantity 458
Or}         DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 458
Or}       TransferRate <TrfRate> [1..1] Rate 458
     UnitsDetails <UnitsDtls> [0..*]  458
       Units <Units> [1..1]  461
{Or         UnitsNumber <UnitsNb> [1..1] Quantity 461
Or}         DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 461
       OrderDate <OrdrDt> [0..1] Date 461
       AcquisitionDate <AcqstnDt> [0..1] Date 461
       CertificateNumber <CertNb> [0..*] Text 461
       Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 461
       Reference <Ref> [0..1] Text 462
       PriceDetails <PricDtls> [0..1] ± 462
       TransactionOverhead <TxOvrhd> [0..1]  C23,
C34
462
         TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C10 464
         TotalFees <TtlFees> [0..1] Amount C1, C10 465
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 436 May 2026
```

## File page 437

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         TotalTaxes <TtlTaxs> [0..1] Amount C1, C10 465
         CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 465
         IndividualFee <IndvFee> [0..*]  C6 466
           Type <Tp> [1..1]  466
{Or             Code <Cd> [1..1] CodeSet 467
Or}             Proprietary <Prtry> [1..1] ± 468
           Basis <Bsis> [0..1]  468
{Or             Code <Cd> [1..1] CodeSet 468
Or}             Proprietary <Prtry> [1..1] ± 469
           StandardAmount <StdAmt> [0..1] Amount C1, C10 469
           StandardRate <StdRate> [0..1] Rate 469
           DiscountDetails <DscntDtls> [0..1]  C15 470
             Amount <Amt> [0..1] Amount C1, C10 470
             Rate <Rate> [0..1] Rate 471
             Basis <Bsis> [0..1]  471
{Or               Code <Cd> [1..1] CodeSet 471
Or}               Proprietary <Prtry> [1..1] ± 471
           AppliedAmount <ApldAmt> [0..1] Amount C1, C10 472
           AppliedRate <ApldRate> [0..1] Rate 472
           NonStandardSLAReference <NonStdSLARef> [0..1] Text 472
           RecipientIdentification <RcptId> [0..1] ± 472
           InformativeIndicator <InftvInd> [1..1] Indicator 473
         IndividualTax <IndvTax> [0..*] ± 473
         DigitalNetworkFee <DgtlNtwkFee> [0..2]  473
           FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C20,
C21,
C24
474
             ISIN <ISIN> [0..1] IdentifierSet 476
             OtherIdentification <OthrId> [0..*]  476
               Identification <Id> [1..1] Text 476
               Suffix <Sfx> [0..1] Text 476
               Type <Tp> [1..1]  476
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 437 May 2026
```

## File page 438

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or                 Code <Cd> [1..1] CodeSet 477
Or}                 Proprietary <Prtry> [1..1] Text 478
             Description <Desc> [0..1] Text 478
           Quantity <Qty> [1..1]  479
{Or             Quantity <Qty> [1..1] ± C14 479
Or}             ProprietaryQuantity <PrtryQty> [1..1]  479
               Quantity <Qty> [1..1] Quantity 480
               QuantityType <QtyTp> [1..1] Text 480
               Issuer <Issr> [1..1] Text 480
               SchemeName <SchmeNm> [0..1] Text 480
           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 480
       OtherAmount <OthrAmt> [0..*]  480
         Type <Tp> [1..1]  481
{Or           Code <Cd> [1..1] CodeSet 481
Or}           ProprietaryCode <PrtryCd> [1..1] ± 481
         Amount <Amt> [1..1] Amount C1, C10 481
     Rounding <Rndg> [0..1] CodeSet 482
     OriginalCost <OrgnlCost> [0..1] Amount C1 482
     AveragePrice <AvrgPric> [0..1] Amount C2 482
     TransferCurrency <TrfCcy> [0..1] CodeSet C2 483
     OwnAccountTransferIndicator <OwnAcctTrfInd> [0..1] Indicator 483
     NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 483
     TransferExpensesPaymentType <TrfExpnssPmtTp> [0..1] ± 483
   AccountDetails <AcctDtls> [1..1]  484
     OwnerIdentification <OwnrId> [0..*] ± 485
     AccountIdentification <AcctId> [1..1] Text 486
     AccountName <AcctNm> [0..1] Text 486
     AccountDesignation <AcctDsgnt> [0..1] Text 486
     AccountServicer <AcctSvcr> [0..1] ± 486
     SubAccountDetails <SubAcctDtls> [0..1] ± 486
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 487
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 438 May 2026
```

## File page 439

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     IntermediaryInformation <IntrmyInf> [0..*] ± 487
     SecuritiesForm <SctiesForm> [0..1] CodeSet 487
     DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 488
     IncomePreference <IncmPref> [0..1] CodeSet 488
     BeneficiaryCertificationCompletion <BnfcryCertfctnCmpltn> [0..1] CodeSet 488
     SafekeepingPlace <SfkpgPlc> [0..1] ± 488
     SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  489
       TradeTransactionCondition <TradTxCond> [0..*] ± 489
       SettlementTransactionCondition <SttlmTxCond> [0..*] ± 490
       SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 490
       DeliveringSideDetails <DlvrgSdDtls> [0..1]  C7, C11,
C25,
C26,
C27,
C28,
C32
490
         Depository <Dpstry> [0..1] ± 492
         Party1 <Pty1> [0..1] ± 493
         Party2 <Pty2> [0..1] ± 493
         Party3 <Pty3> [0..1] ± 493
         Party4 <Pty4> [0..1] ± 494
         Party5 <Pty5> [0..1] ± 494
   SettlementDetails <SttlmDtls> [0..1]  C29,
C30
0
     Transferee <Trfee> [0..1] ± 497
     TransfereeRegisteredAccount <TrfeeRegdAcct> [0..1]  497
       Identification <Id> [0..1] Text 498
       AccountName <AcctNm> [0..1] Text 498
       Designation <Dsgnt> [0..1] Text 498
       Servicer <Svcr> [0..1] ± 498
       SubAccountDetails <SubAcctDtls> [0..1] ± 498
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 499
     IntermediaryInformation <IntrmyInf> [0..*] ± 499
     SecuritiesForm <SctiesForm> [0..1] CodeSet 499
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 439 May 2026
```

## File page 440

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 500
     IncomePreference <IncmPref> [0..1] CodeSet 500
     BeneficiaryCertificationCompletion <BnfcryCertfctnCmpltn> [0..1] CodeSet 500
     RequestedTradeDate <ReqdTradDt> [0..1] Date 500
     RequestedSettlementDate <ReqdSttlmDt> [0..1] Date 501
     SettlementAmount <SttlmAmt> [0..1] Amount C1, C10 501
     StampDuty <StmpDty> [0..1] CodeSet 501
     NetAmount <NetAmt> [0..1] Amount C1, C10 501
     Fees <Fees> [0..*] ± C18 502
     IndividualTax <IndvTax> [0..*] ± 503
     ForeignExchangeDetails <FXDtls> [0..*] ± 503
     SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  504
       TradeTransactionCondition <TradTxCond> [0..*] ± 505
       SettlementTransactionCondition <SttlmTxCond> [0..*] ± 505
       SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 506
       ReceivingSideDetails <RcvgSdDtls> [0..1]  C7, C11,
C25,
C26,
C27,
C28,
C32
506
         Depository <Dpstry> [0..1] ± 507
         Party1 <Pty1> [0..1] ± 508
         Party2 <Pty2> [0..1] ± 508
         Party3 <Pty3> [0..1] ± 509
         Party4 <Pty4> [0..1] ± 509
         Party5 <Pty5> [0..1] ± 510
     PhysicalTransfer <PhysTrf> [0..1] CodeSet 510
     PhysicalTransferDetails <PhysTrfDtls> [0..1] ± C22 510
     ClientReference <ClntRef> [0..1] ± 511
   MarketPracticeVersion <MktPrctcVrsn> [0..1] ± 0
   CopyDetails <CpyDtls> [0..1] ± 0
   Extension <Xtnsn> [0..*] ± C17 0
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 440 May 2026
```

