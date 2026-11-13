---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.2 Structure"]
file_pages: [3489, 3490, 3491, 3492, 3493, 3494, 3495, 3496, 3497, 3498]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3489 to 3498.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3489

```text
53.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SwtchOrdr> [1..1]  C24
   MessageIdentification <MsgId> [1..1] ± 0
   PoolReference <PoolRef> [0..1] ± 0
   PreviousReference <PrvsRef> [0..*] ± 3513
   MessagePagination <MsgPgntn> [0..1] ± 3514
   SwitchOrderDetails <SwtchOrdrDtls> [1..*]  C18,
C21,
C27
3514
     MasterReference <MstrRef> [0..1] Text 3536
     OrderDateTime <OrdrDtTm> [0..1] DateTime 3536
     PlaceOfTrade <PlcOfTrad> [0..1] ± 3536
     OrderReference <OrdrRef> [1..1] Text 3537
     ClientReference <ClntRef> [0..1] Text 3537
     NonceIdentification <NonceId> [0..1] Text 3537
     InvestmentAccountDetails <InvstmtAcctDtls> [0..1]  C26 3537
       AccountIdentification <AcctId> [1..1] Text 3538
       AccountName <AcctNm> [0..1] Text 3538
       AccountDesignation <AcctDsgnt> [0..1] Text 3538
       OwnerIdentification <OwnrId> [0..*] ± 3538
       AccountServicer <AcctSvcr> [0..1] ± 3538
       OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 3539
       SubAccountDetails <SubAcctDtls> [0..1] ± 3539
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3539
     RelatedPartyDetails <RltdPtyDtls> [0..10]  C25 3540
       Identification <Id> [1..1] ± 3540
       Account <Acct> [0..1]  3540
         Identification <Id> [1..1] Text 3541
         AccountServicer <AcctSvcr> [0..1] ± 3541
       OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 3541
       Role <Role> [0..1] ± 3542
     RequestedFutureTradeDate <ReqdFutrTradDt> [0..1] Date 3542
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3489 May 2026
```

## File page 3490

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     SettlementAmount <SttlmAmt> [0..1] Amount C2, C7 3542
     CashSettlementDate <CshSttlmDt> [0..1] Date 3542
     SettlementMethod <SttlmMtd> [0..1] CodeSet 3543
     AdditionalAmount <AddtlAmt> [0..1] ± 3543
     ExpiryDateTime <XpryDtTm> [0..1] ± 3543
     CancellationRight <CxlRght> [0..1] ± 3543
     RedemptionLegDetails <RedLegDtls> [1..*]  C29,
C31
3544
       LegIdentification <LegId> [0..1] Text 3551
       FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C20 3551
         Identification <Id> [1..1]  3553
{Or           ISIN <ISIN> [1..1] IdentifierSet 3553
Or           SEDOL <SEDOL> [1..1] IdentifierSet 3554
Or           CUSIP <CUSIP> [1..1] IdentifierSet 3554
Or           RIC <RIC> [1..1] IdentifierSet 3554
Or           TickerSymbol <TckrSymb> [1..1] IdentifierSet 3554
Or           Bloomberg <Blmbrg> [1..1] IdentifierSet 3554
Or           CTA <CTA> [1..1] IdentifierSet 3554
Or           QUICK <QUICK> [1..1] IdentifierSet 3554
Or           Wertpapier <Wrtppr> [1..1] IdentifierSet 3555
Or           Dutch <Dtch> [1..1] IdentifierSet 3555
Or           Valoren <Vlrn> [1..1] IdentifierSet 3555
Or           Sicovam <SCVM> [1..1] IdentifierSet 3555
Or           Belgian <Belgn> [1..1] IdentifierSet 3555
Or           Common <Cmon> [1..1] IdentifierSet 3555
Or           DTI <DTI> [1..1] IdentifierSet 3555
Or}           OtherProprietaryIdentification <OthrPrtryId> [1..1]  3555
             Identification <Id> [1..1] Text 3556
             IdentificationSource <IdSrc> [1..1] ± 3556
         Name <Nm> [0..1] Text 3556
         ShortName <ShrtNm> [0..1] Text 3556
         SupplementaryIdentification <SplmtryId> [0..1] Text 3556
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3490 May 2026
```

## File page 3491

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         ClassType <ClssTp> [0..1] Text 3556
         SecuritiesForm <SctiesForm> [0..1] CodeSet 3557
         DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 3557
         ProductGroup <PdctGrp> [0..1] Text 3557
         SeriesIdentification <SrsId> [0..1]  C35 3557
           SeriesDate <SrsDt> [0..1] ± 3558
           SeriesName <SrsNm> [0..1] Text 3558
       FinancialInstrumentQuantityChoice <FinInstrmQtyChc> [0..1]  3558
{Or         UnitsNumber <UnitsNb> [1..1] Quantity 3558
Or         PercentageOfTotalSubscriptionAmount
<PctgOfTtlSbcptAmt>
[1..1] Rate 3559
Or         NetAmount <NetAmt> [1..1] Amount C3, C8 3559
Or         GrossAmount <GrssAmt> [1..1] Amount C3, C8 3559
Or         DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 3560
Or}         HoldingsRedemptionRate <HldgsRedRate> [1..1] Rate 3560
       InvestmentAccountDetails <InvstmtAcctDtls> [0..1]  C26 3560
         AccountIdentification <AcctId> [1..1] Text 3560
         AccountName <AcctNm> [0..1] Text 3560
         AccountDesignation <AcctDsgnt> [0..1] Text 3561
         OwnerIdentification <OwnrId> [0..*] ± 3561
         AccountServicer <AcctSvcr> [0..1] ± 3561
         OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 3561
         SubAccountDetails <SubAcctDtls> [0..1] ± 3562
         BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3562
       IncomePreference <IncmPref> [0..1] CodeSet 3562
       Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 3563
       RequestedSettlementCurrency <ReqdSttlmCcy> [0..1] CodeSet C2 3563
       RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C3 3563
       TransactionOverhead <TxOvrhd> [0..1]  C17 3564
         CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 3567
         IndividualFee <IndvFee> [0..*]  C16,
C36,
C37
3567
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3491 May 2026
```

## File page 3492

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           Type <Tp> [1..1]  3568
{Or             Code <Cd> [1..1] CodeSet 3568
Or}             Proprietary <Prtry> [1..1] ± 3569
           Basis <Bsis> [0..1]  3569
{Or             Code <Cd> [1..1] CodeSet 3570
Or}             Proprietary <Prtry> [1..1] ± 3570
           StandardAmount <StdAmt> [0..1] Amount C2, C7 3570
           StandardRate <StdRate> [0..1] Rate 3571
           DiscountDetails <DscntDtls> [0..1]  C14 3571
             Amount <Amt> [0..1] Amount C2, C7 3571
             Rate <Rate> [0..1] Rate 3572
             Basis <Bsis> [0..1]  3572
{Or               Code <Cd> [1..1] CodeSet 3572
Or}               Proprietary <Prtry> [1..1] ± 3573
           RequestedAmount <ReqdAmt> [0..1] Amount C2, C7 3573
           RequestedRate <ReqdRate> [0..1] Rate 3573
           NonStandardSLAReference <NonStdSLARef> [0..1] Text 3574
           RecipientIdentification <RcptId> [0..1] ± 3574
         IndividualTax <IndvTax> [0..*]  3574
           Type <Tp> [1..1]  3575
{Or             Code <Cd> [1..1] CodeSet 3575
Or}             Proprietary <Prtry> [1..1] ± 3577
           Tax <Tax> [0..1]  3577
{Or             Amount <Amt> [1..1] Amount C2, C7 3577
Or}             Rate <Rate> [1..1] Rate 3578
           Country <Ctry> [0..1] CodeSet C6 3578
           ExemptionIndicator <XmptnInd> [1..1] Indicator 3578
           ExemptionReason <XmptnRsn> [0..1]  3578
{Or             Code <Cd> [1..1] CodeSet 3578
Or}             Proprietary <Prtry> [1..1] ± 3581
           RecipientIdentification <RcptId> [0..1] ± 3581
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3492 May 2026
```

## File page 3493

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           TaxCalculationDetails <TaxClctnDtls> [0..1]  3582
             Basis <Bsis> [1..1]  3582
{Or               Code <Cd> [1..1] CodeSet 3582
Or}               Proprietary <Prtry> [1..1] ± 3582
         DigitalNetworkFee <DgtlNtwkFee> [0..*]  3583
           FinancialInstrumentIdentification <FinInstrmId> [1..1]  C11,
C12,
C22,
C23,
C28
3583
             ISIN <ISIN> [0..1] IdentifierSet 3585
             OtherIdentification <OthrId> [0..*]  3585
               Identification <Id> [1..1] Text 3585
               Suffix <Sfx> [0..1] Text 3585
               Type <Tp> [1..1]  3585
{Or                 Code <Cd> [1..1] CodeSet 3586
Or}                 Proprietary <Prtry> [1..1] Text 3587
             Description <Desc> [0..1] Text 3587
           Quantity <Qty> [1..1]  3588
{Or             Quantity <Qty> [1..1] ± C13 3588
Or}             ProprietaryQuantity <PrtryQty> [1..1]  3588
               Quantity <Qty> [1..1] Quantity 3589
               QuantityType <QtyTp> [1..1] Text 3589
               Issuer <Issr> [1..1] Text 3589
               SchemeName <SchmeNm> [0..1] Text 3589
           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3589
       SettlementAndCustodyDetails <SttlmAndCtdyDtls> [0..1]  3589
         SettlementDate <SttlmDt> [0..1] Date 3591
         SettlementPlace <SttlmPlc> [1..1]  3591
           Party <Pty> [1..1]  3592
{Or             AnyBIC <AnyBIC> [1..1] IdentifierSet C4 3592
Or             ProprietaryIdentification <PrtryId> [1..1] ± 3592
Or             NameAndAddress <NmAndAdr> [1..1] ± 3593
Or}             DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3593
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3493 May 2026
```

## File page 3494

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           LEI <LEI> [0..1] IdentifierSet 3593
         SafekeepingPlace <SfkpgPlc> [0..1] ± 3593
         SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 3594
         TradeTransactionCondition <TradTxCond> [0..*] ± 3594
         SettlementTransactionCondition <SttlmTxCond> [0..*] ± 3594
         ReceivingSideDetails <RcvgSdDtls> [0..1]  C33,
C34
3595
           ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  3596
             PartyIdentification <PtyId> [1..1] ± 3596
             AccountIdentification <AcctId> [0..1] Text 3596
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3596
           ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  3597
             PartyIdentification <PtyId> [1..1] ± 3597
             AccountIdentification <AcctId> [0..1] Text 3597
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3597
           ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  3598
             PartyIdentification <PtyId> [1..1] ± 3598
             AccountIdentification <AcctId> [0..1] Text 3598
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3598
           ReceivingAgentDetails <RcvgAgtDtls> [1..1]  3599
             PartyIdentification <PtyId> [1..1] ± 3599
             AccountIdentification <AcctId> [0..1] Text 3599
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3599
         DeliveringSideDetails <DlvrgSdDtls> [1..1]  C9, C10 3600
           DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  3601
             PartyIdentification <PtyId> [1..1] ± 3601
             AccountIdentification <AcctId> [0..1] Text 3601
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3602
           DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  3602
             PartyIdentification <PtyId> [1..1] ± 3602
             AccountIdentification <AcctId> [0..1] Text 3602
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3602
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3494 May 2026
```

## File page 3495

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  3603
             PartyIdentification <PtyId> [1..1] ± 3603
             AccountIdentification <AcctId> [0..1] Text 3603
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3603
           DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  3604
             PartyIdentification <PtyId> [1..1] ± 3604
             AccountIdentification <AcctId> [0..1] Text 3604
             BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3604
       PhysicalDeliveryIndicator <PhysDlvryInd> [1..1] Indicator 3605
       PhysicalDeliveryDetails <PhysDlvryDtls> [0..1] ± 3605
       DigitalAssetSettlement <DgtlAsstSttlm> [0..1]  3605
         FinancialInstrumentIdentification <FinInstrmId> [1..1]  C11,
C12,
C22,
C23,
C28
3606
           ISIN <ISIN> [0..1] IdentifierSet 3608
           OtherIdentification <OthrId> [0..*]  3608
             Identification <Id> [1..1] Text 3608
             Suffix <Sfx> [0..1] Text 3608
             Type <Tp> [1..1]  3608
{Or               Code <Cd> [1..1] CodeSet 3609
Or}               Proprietary <Prtry> [1..1] Text 3610
           Description <Desc> [0..1] Text 3610
         Quantity <Qty> [1..1]  3611
{Or           Quantity <Qty> [1..1] ± C13 3611
Or}           ProprietaryQuantity <PrtryQty> [1..1]  3611
             Quantity <Qty> [1..1] Quantity 3612
             QuantityType <QtyTp> [1..1] Text 3612
             Issuer <Issr> [1..1] Text 3612
             SchemeName <SchmeNm> [0..1] Text 3612
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3612
       NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 3612
       Equalisation <Equlstn> [0..1] ± 3612
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3495 May 2026
```

## File page 3496

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     SubscriptionLegDetails <SbcptLegDtls> [1..*]  C30,
C32
3613
       LegIdentification <LegId> [0..1] Text 3620
       FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C20 3620
         Identification <Id> [1..1]  3622
{Or           ISIN <ISIN> [1..1] IdentifierSet 3622
Or           SEDOL <SEDOL> [1..1] IdentifierSet 3623
Or           CUSIP <CUSIP> [1..1] IdentifierSet 3623
Or           RIC <RIC> [1..1] IdentifierSet 3623
Or           TickerSymbol <TckrSymb> [1..1] IdentifierSet 3623
Or           Bloomberg <Blmbrg> [1..1] IdentifierSet 3623
Or           CTA <CTA> [1..1] IdentifierSet 3623
Or           QUICK <QUICK> [1..1] IdentifierSet 3623
Or           Wertpapier <Wrtppr> [1..1] IdentifierSet 3624
Or           Dutch <Dtch> [1..1] IdentifierSet 3624
Or           Valoren <Vlrn> [1..1] IdentifierSet 3624
Or           Sicovam <SCVM> [1..1] IdentifierSet 3624
Or           Belgian <Belgn> [1..1] IdentifierSet 3624
Or           Common <Cmon> [1..1] IdentifierSet 3624
Or           DTI <DTI> [1..1] IdentifierSet 3624
Or}           OtherProprietaryIdentification <OthrPrtryId> [1..1]  3624
             Identification <Id> [1..1] Text 3625
             IdentificationSource <IdSrc> [1..1] ± 3625
         Name <Nm> [0..1] Text 3625
         ShortName <ShrtNm> [0..1] Text 3625
         SupplementaryIdentification <SplmtryId> [0..1] Text 3625
         ClassType <ClssTp> [0..1] Text 3625
         SecuritiesForm <SctiesForm> [0..1] CodeSet 3626
         DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 3626
         ProductGroup <PdctGrp> [0..1] Text 3626
         SeriesIdentification <SrsId> [0..1]  C35 3626
           SeriesDate <SrsDt> [0..1] ± 3627
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3496 May 2026
```

## File page 3497

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           SeriesName <SrsNm> [0..1] Text 3627
       FinancialInstrumentQuantityChoice <FinInstrmQtyChc> [0..1]  3627
{Or         UnitsNumber <UnitsNb> [1..1] Quantity 3627
Or         PercentageOfTotalRedemptionAmount
<PctgOfTtlRedAmt>
[1..1] Rate 3628
Or         NetAmount <NetAmt> [1..1] Amount C3, C8 3628
Or         GrossAmount <GrssAmt> [1..1] Amount C3, C8 3628
Or}         DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 3629
       InvestmentAccountDetails <InvstmtAcctDtls> [0..1]  C26 3629
         AccountIdentification <AcctId> [1..1] Text 3629
         AccountName <AcctNm> [0..1] Text 3629
         AccountDesignation <AcctDsgnt> [0..1] Text 3630
         OwnerIdentification <OwnrId> [0..*] ± 3630
         AccountServicer <AcctSvcr> [0..1] ± 3630
         OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 3630
         SubAccountDetails <SubAcctDtls> [0..1] ± 3631
         BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3631
       IncomePreference <IncmPref> [0..1] CodeSet 3631
       RequestedSettlementCurrency <ReqdSttlmCcy> [0..1] CodeSet C2 3632
       RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C3 3632
       TransactionOverhead <TxOvrhd> [0..1]  C17 3632
         CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 3635
         IndividualFee <IndvFee> [0..*]  C16,
C36,
C37
3635
           Type <Tp> [1..1]  3636
{Or             Code <Cd> [1..1] CodeSet 3636
Or}             Proprietary <Prtry> [1..1] ± 3637
           Basis <Bsis> [0..1]  3637
{Or             Code <Cd> [1..1] CodeSet 3638
Or}             Proprietary <Prtry> [1..1] ± 3638
           StandardAmount <StdAmt> [0..1] Amount C2, C7 3638
           StandardRate <StdRate> [0..1] Rate 3639
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3497 May 2026
```

## File page 3498

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           DiscountDetails <DscntDtls> [0..1]  C14 3639
             Amount <Amt> [0..1] Amount C2, C7 3639
             Rate <Rate> [0..1] Rate 3640
             Basis <Bsis> [0..1]  3640
{Or               Code <Cd> [1..1] CodeSet 3640
Or}               Proprietary <Prtry> [1..1] ± 3641
           RequestedAmount <ReqdAmt> [0..1] Amount C2, C7 3641
           RequestedRate <ReqdRate> [0..1] Rate 3641
           NonStandardSLAReference <NonStdSLARef> [0..1] Text 3642
           RecipientIdentification <RcptId> [0..1] ± 3642
         IndividualTax <IndvTax> [0..*]  3642
           Type <Tp> [1..1]  3643
{Or             Code <Cd> [1..1] CodeSet 3643
Or}             Proprietary <Prtry> [1..1] ± 3645
           Tax <Tax> [0..1]  3645
{Or             Amount <Amt> [1..1] Amount C2, C7 3645
Or}             Rate <Rate> [1..1] Rate 3646
           Country <Ctry> [0..1] CodeSet C6 3646
           ExemptionIndicator <XmptnInd> [1..1] Indicator 3646
           ExemptionReason <XmptnRsn> [0..1]  3646
{Or             Code <Cd> [1..1] CodeSet 3646
Or}             Proprietary <Prtry> [1..1] ± 3649
           RecipientIdentification <RcptId> [0..1] ± 3649
           TaxCalculationDetails <TaxClctnDtls> [0..1]  3650
             Basis <Bsis> [1..1]  3650
{Or               Code <Cd> [1..1] CodeSet 3650
Or}               Proprietary <Prtry> [1..1] ± 3650
         DigitalNetworkFee <DgtlNtwkFee> [0..*]  3651
           FinancialInstrumentIdentification <FinInstrmId> [1..1]  C11,
C12,
C22,
C23,
C28
3651
             ISIN <ISIN> [0..1] IdentifierSet 3653
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3498 May 2026
```

