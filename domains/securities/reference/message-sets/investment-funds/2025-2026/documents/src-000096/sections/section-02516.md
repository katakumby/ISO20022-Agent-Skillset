---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.16 RedemptionLegDetails <RedLegDtls>"]
file_pages: [3544, 3545, 3546, 3547, 3548, 3549, 3550]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.16 RedemptionLegDetails <RedLegDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3544 to 3550.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3544

```text
CancellationRight <CxlRght> contains one of the following elements (see "CancellationRight1Choice"
on page 4834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4834
Or}   Proprietary <Prtry> [1..1] ± 4834
53.4.5.16  RedemptionLegDetails <RedLegDtls>
Presence: [1..*]
Definition: Part of the investment fund switch order that is a redemption.
Impacted by: C29 "PhysicalDeliveryDetails1Rule", C31 "PhysicalDeliveryDetails2Rule"
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3544 May 2026
```

## File page 3545

```text
RedemptionLegDetails <RedLegDtls> contains the following SwitchRedemptionLegOrder7
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LegIdentification <LegId> [0..1] Text 3551
   FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C20 3551
     Identification <Id> [1..1]  3553
{Or       ISIN <ISIN> [1..1] IdentifierSet 3553
Or       SEDOL <SEDOL> [1..1] IdentifierSet 3554
Or       CUSIP <CUSIP> [1..1] IdentifierSet 3554
Or       RIC <RIC> [1..1] IdentifierSet 3554
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 3554
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 3554
Or       CTA <CTA> [1..1] IdentifierSet 3554
Or       QUICK <QUICK> [1..1] IdentifierSet 3554
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 3555
Or       Dutch <Dtch> [1..1] IdentifierSet 3555
Or       Valoren <Vlrn> [1..1] IdentifierSet 3555
Or       Sicovam <SCVM> [1..1] IdentifierSet 3555
Or       Belgian <Belgn> [1..1] IdentifierSet 3555
Or       Common <Cmon> [1..1] IdentifierSet 3555
Or       DTI <DTI> [1..1] IdentifierSet 3555
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  3555
         Identification <Id> [1..1] Text 3556
         IdentificationSource <IdSrc> [1..1] ± 3556
     Name <Nm> [0..1] Text 3556
     ShortName <ShrtNm> [0..1] Text 3556
     SupplementaryIdentification <SplmtryId> [0..1] Text 3556
     ClassType <ClssTp> [0..1] Text 3556
     SecuritiesForm <SctiesForm> [0..1] CodeSet 3557
     DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 3557
     ProductGroup <PdctGrp> [0..1] Text 3557
     SeriesIdentification <SrsId> [0..1]  C35 3557
       SeriesDate <SrsDt> [0..1] ± 3558
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3545 May 2026
```

## File page 3546

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       SeriesName <SrsNm> [0..1] Text 3558
   FinancialInstrumentQuantityChoice
<FinInstrmQtyChc>
[0..1]  3558
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 3558
Or     PercentageOfTotalSubscriptionAmount
<PctgOfTtlSbcptAmt>
[1..1] Rate 3559
Or     NetAmount <NetAmt> [1..1] Amount C3, C8 3559
Or     GrossAmount <GrssAmt> [1..1] Amount C3, C8 3559
Or     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 3560
Or}     HoldingsRedemptionRate <HldgsRedRate> [1..1] Rate 3560
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
       Type <Tp> [1..1]  3568
{Or         Code <Cd> [1..1] CodeSet 3568
Or}         Proprietary <Prtry> [1..1] ± 3569
       Basis <Bsis> [0..1]  3569
{Or         Code <Cd> [1..1] CodeSet 3570
Or}         Proprietary <Prtry> [1..1] ± 3570
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3546 May 2026
```

## File page 3547

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       StandardAmount <StdAmt> [0..1] Amount C2, C7 3570
       StandardRate <StdRate> [0..1] Rate 3571
       DiscountDetails <DscntDtls> [0..1]  C14 3571
         Amount <Amt> [0..1] Amount C2, C7 3571
         Rate <Rate> [0..1] Rate 3572
         Basis <Bsis> [0..1]  3572
{Or           Code <Cd> [1..1] CodeSet 3572
Or}           Proprietary <Prtry> [1..1] ± 3573
       RequestedAmount <ReqdAmt> [0..1] Amount C2, C7 3573
       RequestedRate <ReqdRate> [0..1] Rate 3573
       NonStandardSLAReference <NonStdSLARef> [0..1] Text 3574
       RecipientIdentification <RcptId> [0..1] ± 3574
     IndividualTax <IndvTax> [0..*]  3574
       Type <Tp> [1..1]  3575
{Or         Code <Cd> [1..1] CodeSet 3575
Or}         Proprietary <Prtry> [1..1] ± 3577
       Tax <Tax> [0..1]  3577
{Or         Amount <Amt> [1..1] Amount C2, C7 3577
Or}         Rate <Rate> [1..1] Rate 3578
       Country <Ctry> [0..1] CodeSet C6 3578
       ExemptionIndicator <XmptnInd> [1..1] Indicator 3578
       ExemptionReason <XmptnRsn> [0..1]  3578
{Or         Code <Cd> [1..1] CodeSet 3578
Or}         Proprietary <Prtry> [1..1] ± 3581
       RecipientIdentification <RcptId> [0..1] ± 3581
       TaxCalculationDetails <TaxClctnDtls> [0..1]  3582
         Basis <Bsis> [1..1]  3582
{Or           Code <Cd> [1..1] CodeSet 3582
Or}           Proprietary <Prtry> [1..1] ± 3582
     DigitalNetworkFee <DgtlNtwkFee> [0..*]  3583
       FinancialInstrumentIdentification <FinInstrmId> [1..1]  C11,
C12,
C22,
3583
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3547 May 2026
```

## File page 3548

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
C23,
C28
         ISIN <ISIN> [0..1] IdentifierSet 3585
         OtherIdentification <OthrId> [0..*]  3585
           Identification <Id> [1..1] Text 3585
           Suffix <Sfx> [0..1] Text 3585
           Type <Tp> [1..1]  3585
{Or             Code <Cd> [1..1] CodeSet 3586
Or}             Proprietary <Prtry> [1..1] Text 3587
         Description <Desc> [0..1] Text 3587
       Quantity <Qty> [1..1]  3588
{Or         Quantity <Qty> [1..1] ± C13 3588
Or}         ProprietaryQuantity <PrtryQty> [1..1]  3588
           Quantity <Qty> [1..1] Quantity 3589
           QuantityType <QtyTp> [1..1] Text 3589
           Issuer <Issr> [1..1] Text 3589
           SchemeName <SchmeNm> [0..1] Text 3589
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3589
   SettlementAndCustodyDetails <SttlmAndCtdyDtls> [0..1]  3589
     SettlementDate <SttlmDt> [0..1] Date 3591
     SettlementPlace <SttlmPlc> [1..1]  3591
       Party <Pty> [1..1]  3592
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C4 3592
Or         ProprietaryIdentification <PrtryId> [1..1] ± 3592
Or         NameAndAddress <NmAndAdr> [1..1] ± 3593
Or}         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3593
       LEI <LEI> [0..1] IdentifierSet 3593
     SafekeepingPlace <SfkpgPlc> [0..1] ± 3593
     SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 3594
     TradeTransactionCondition <TradTxCond> [0..*] ± 3594
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 3594
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3548 May 2026
```

## File page 3549

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     ReceivingSideDetails <RcvgSdDtls> [0..1]  C33,
C34
3595
       ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  3596
         PartyIdentification <PtyId> [1..1] ± 3596
         AccountIdentification <AcctId> [0..1] Text 3596
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3596
       ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  3597
         PartyIdentification <PtyId> [1..1] ± 3597
         AccountIdentification <AcctId> [0..1] Text 3597
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3597
       ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  3598
         PartyIdentification <PtyId> [1..1] ± 3598
         AccountIdentification <AcctId> [0..1] Text 3598
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3598
       ReceivingAgentDetails <RcvgAgtDtls> [1..1]  3599
         PartyIdentification <PtyId> [1..1] ± 3599
         AccountIdentification <AcctId> [0..1] Text 3599
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3599
     DeliveringSideDetails <DlvrgSdDtls> [1..1]  C9, C10 3600
       DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  3601
         PartyIdentification <PtyId> [1..1] ± 3601
         AccountIdentification <AcctId> [0..1] Text 3601
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3602
       DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  3602
         PartyIdentification <PtyId> [1..1] ± 3602
         AccountIdentification <AcctId> [0..1] Text 3602
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3602
       DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  3603
         PartyIdentification <PtyId> [1..1] ± 3603
         AccountIdentification <AcctId> [0..1] Text 3603
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3549 May 2026
```

## File page 3550

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3603
       DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  3604
         PartyIdentification <PtyId> [1..1] ± 3604
         AccountIdentification <AcctId> [0..1] Text 3604
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3604
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
{Or           Code <Cd> [1..1] CodeSet 3609
Or}           Proprietary <Prtry> [1..1] Text 3610
       Description <Desc> [0..1] Text 3610
     Quantity <Qty> [1..1]  3611
{Or       Quantity <Qty> [1..1] ± C13 3611
Or}       ProprietaryQuantity <PrtryQty> [1..1]  3611
         Quantity <Qty> [1..1] Quantity 3612
         QuantityType <QtyTp> [1..1] Text 3612
         Issuer <Issr> [1..1] Text 3612
         SchemeName <SchmeNm> [0..1] Text 3612
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3612
   NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 3612
   Equalisation <Equlstn> [0..1] ± 3612
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3550 May 2026
```

