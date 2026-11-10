---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.17 SubscriptionLegDetails <SbcptLegDtls>"]
file_pages: [3613, 3614, 3615, 3616, 3617, 3618, 3619]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.17 SubscriptionLegDetails <SbcptLegDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3613 to 3619.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3613

```text
Definition: Part of an investor's retained subscription amount that is returned by the fund in order to
reimburse preliminary incentive/performance fees.
Equalisation <Equlstn> contains the following elements (see "Equalisation1" on page 4775 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [0..1] Amount C2, C10 4775
   Rate <Rate> [0..1] Rate 4776
53.4.5.17  SubscriptionLegDetails <SbcptLegDtls>
Presence: [1..*]
Definition: Part of the investment fund switch order that is a subscription.
Impacted by: C30 "PhysicalDeliveryDetails1Rule", C32 "PhysicalDeliveryDetails2Rule"
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3613 May 2026
```

## File page 3614

```text
SubscriptionLegDetails <SbcptLegDtls> contains the following SwitchSubscriptionLegOrder7
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LegIdentification <LegId> [0..1] Text 3620
   FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C20 3620
     Identification <Id> [1..1]  3622
{Or       ISIN <ISIN> [1..1] IdentifierSet 3622
Or       SEDOL <SEDOL> [1..1] IdentifierSet 3623
Or       CUSIP <CUSIP> [1..1] IdentifierSet 3623
Or       RIC <RIC> [1..1] IdentifierSet 3623
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 3623
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 3623
Or       CTA <CTA> [1..1] IdentifierSet 3623
Or       QUICK <QUICK> [1..1] IdentifierSet 3623
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 3624
Or       Dutch <Dtch> [1..1] IdentifierSet 3624
Or       Valoren <Vlrn> [1..1] IdentifierSet 3624
Or       Sicovam <SCVM> [1..1] IdentifierSet 3624
Or       Belgian <Belgn> [1..1] IdentifierSet 3624
Or       Common <Cmon> [1..1] IdentifierSet 3624
Or       DTI <DTI> [1..1] IdentifierSet 3624
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  3624
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
Investment Funds - Maintenance 2025 - 2026 3614 May 2026
```

## File page 3615

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       SeriesName <SrsNm> [0..1] Text 3627
   FinancialInstrumentQuantityChoice
<FinInstrmQtyChc>
[0..1]  3627
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 3627
Or     PercentageOfTotalRedemptionAmount
<PctgOfTtlRedAmt>
[1..1] Rate 3628
Or     NetAmount <NetAmt> [1..1] Amount C3, C8 3628
Or     GrossAmount <GrssAmt> [1..1] Amount C3, C8 3628
Or}     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 3629
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
{Or         Code <Cd> [1..1] CodeSet 3636
Or}         Proprietary <Prtry> [1..1] ± 3637
       Basis <Bsis> [0..1]  3637
{Or         Code <Cd> [1..1] CodeSet 3638
Or}         Proprietary <Prtry> [1..1] ± 3638
       StandardAmount <StdAmt> [0..1] Amount C2, C7 3638
       StandardRate <StdRate> [0..1] Rate 3639
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3615 May 2026
```

## File page 3616

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       DiscountDetails <DscntDtls> [0..1]  C14 3639
         Amount <Amt> [0..1] Amount C2, C7 3639
         Rate <Rate> [0..1] Rate 3640
         Basis <Bsis> [0..1]  3640
{Or           Code <Cd> [1..1] CodeSet 3640
Or}           Proprietary <Prtry> [1..1] ± 3641
       RequestedAmount <ReqdAmt> [0..1] Amount C2, C7 3641
       RequestedRate <ReqdRate> [0..1] Rate 3641
       NonStandardSLAReference <NonStdSLARef> [0..1] Text 3642
       RecipientIdentification <RcptId> [0..1] ± 3642
     IndividualTax <IndvTax> [0..*]  3642
       Type <Tp> [1..1]  3643
{Or         Code <Cd> [1..1] CodeSet 3643
Or}         Proprietary <Prtry> [1..1] ± 3645
       Tax <Tax> [0..1]  3645
{Or         Amount <Amt> [1..1] Amount C2, C7 3645
Or}         Rate <Rate> [1..1] Rate 3646
       Country <Ctry> [0..1] CodeSet C6 3646
       ExemptionIndicator <XmptnInd> [1..1] Indicator 3646
       ExemptionReason <XmptnRsn> [0..1]  3646
{Or         Code <Cd> [1..1] CodeSet 3646
Or}         Proprietary <Prtry> [1..1] ± 3649
       RecipientIdentification <RcptId> [0..1] ± 3649
       TaxCalculationDetails <TaxClctnDtls> [0..1]  3650
         Basis <Bsis> [1..1]  3650
{Or           Code <Cd> [1..1] CodeSet 3650
Or}           Proprietary <Prtry> [1..1] ± 3650
     DigitalNetworkFee <DgtlNtwkFee> [0..*]  3651
       FinancialInstrumentIdentification <FinInstrmId> [1..1]  C11,
C12,
C22,
C23,
C28
3651
         ISIN <ISIN> [0..1] IdentifierSet 3653
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3616 May 2026
```

## File page 3617

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         OtherIdentification <OthrId> [0..*]  3653
           Identification <Id> [1..1] Text 3653
           Suffix <Sfx> [0..1] Text 3653
           Type <Tp> [1..1]  3653
{Or             Code <Cd> [1..1] CodeSet 3654
Or}             Proprietary <Prtry> [1..1] Text 3655
         Description <Desc> [0..1] Text 3655
       Quantity <Qty> [1..1]  3656
{Or         Quantity <Qty> [1..1] ± C13 3656
Or}         ProprietaryQuantity <PrtryQty> [1..1]  3656
           Quantity <Qty> [1..1] Quantity 3657
           QuantityType <QtyTp> [1..1] Text 3657
           Issuer <Issr> [1..1] Text 3657
           SchemeName <SchmeNm> [0..1] Text 3657
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3657
   SettlementAndCustodyDetails <SttlmAndCtdyDtls> [0..1]  3657
     SettlementDate <SttlmDt> [0..1] Date 3659
     SettlementPlace <SttlmPlc> [1..1]  3659
       Party <Pty> [1..1]  3660
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C4 3660
Or         ProprietaryIdentification <PrtryId> [1..1] ± 3660
Or         NameAndAddress <NmAndAdr> [1..1] ± 3661
Or}         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3661
       LEI <LEI> [0..1] IdentifierSet 3661
     SafekeepingPlace <SfkpgPlc> [0..1] ± 3661
     SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 3662
     TradeTransactionCondition <TradTxCond> [0..*] ± 3662
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 3662
     ReceivingSideDetails <RcvgSdDtls> [1..1]  C33,
C34
3663
       ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  3664
         PartyIdentification <PtyId> [1..1] ± 3664
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3617 May 2026
```

## File page 3618

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         AccountIdentification <AcctId> [0..1] Text 3664
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3664
       ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  3665
         PartyIdentification <PtyId> [1..1] ± 3665
         AccountIdentification <AcctId> [0..1] Text 3665
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3665
       ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  3666
         PartyIdentification <PtyId> [1..1] ± 3666
         AccountIdentification <AcctId> [0..1] Text 3666
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3666
       ReceivingAgentDetails <RcvgAgtDtls> [1..1]  3667
         PartyIdentification <PtyId> [1..1] ± 3667
         AccountIdentification <AcctId> [0..1] Text 3667
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3667
     DeliveringSideDetails <DlvrgSdDtls> [0..1]  C9, C10 3668
       DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  3669
         PartyIdentification <PtyId> [1..1] ± 3669
         AccountIdentification <AcctId> [0..1] Text 3669
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3670
       DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  3670
         PartyIdentification <PtyId> [1..1] ± 3670
         AccountIdentification <AcctId> [0..1] Text 3670
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3670
       DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  3671
         PartyIdentification <PtyId> [1..1] ± 3671
         AccountIdentification <AcctId> [0..1] Text 3671
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3671
       DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  3672
         PartyIdentification <PtyId> [1..1] ± 3672
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3618 May 2026
```

## File page 3619

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         AccountIdentification <AcctId> [0..1] Text 3672
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3672
   PhysicalDeliveryIndicator <PhysDlvryInd> [1..1] Indicator 3673
   PhysicalDeliveryDetails <PhysDlvryDtls> [0..1] ± 3673
   DigitalAssetSettlement <DgtlAsstSttlm> [0..1]  3673
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C11,
C12,
C22,
C23,
C28
3674
       ISIN <ISIN> [0..1] IdentifierSet 3676
       OtherIdentification <OthrId> [0..*]  3676
         Identification <Id> [1..1] Text 3676
         Suffix <Sfx> [0..1] Text 3676
         Type <Tp> [1..1]  3676
{Or           Code <Cd> [1..1] CodeSet 3677
Or}           Proprietary <Prtry> [1..1] Text 3678
       Description <Desc> [0..1] Text 3678
     Quantity <Qty> [1..1]  3679
{Or       Quantity <Qty> [1..1] ± C13 3679
Or}       ProprietaryQuantity <PrtryQty> [1..1]  3679
         Quantity <Qty> [1..1] Quantity 3680
         QuantityType <QtyTp> [1..1] Text 3680
         Issuer <Issr> [1..1] Text 3680
         SchemeName <SchmeNm> [0..1] Text 3680
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3680
   NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 3680
   Equalisation <Equlstn> [0..1] ± 3680
Constraints
• PhysicalDeliveryDetails1Rule
If PhysicalDeliveryIndicator is "false" or "0" (No), then PhysicalDeliveryDetails is not allowed.
On Condition
    /PhysicalDeliveryIndicator is equal to value 'false'
 Or    /PhysicalDeliveryIndicator is equal to value '0'
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3619 May 2026
```

