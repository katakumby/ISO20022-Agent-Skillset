---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>"]
file_pages: [3828, 3829, 3830, 3831, 3832, 3833, 3834, 3835, 3836, 3837]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.4 RelatedReference <RltdRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3828 to 3837.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3828

```text
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
55.4.4 RelatedReference <RltdRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously received.
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
55.4.5 SwitchExecutionDetails <SwtchExctnDtls>
Presence: [1..*]
Definition: Information related to a switch execution.
Impacted by: C19 "InvestmentAccountDetailsRule", C26 "OrderOriginatorEligibility3Rule"
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3828 May 2026
```

## File page 3829

```text
SwitchExecutionDetails <SwtchExctnDtls> contains the following SwitchExecution8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AmendmentIndicator <AmdmntInd> [0..1] Indicator 3850
   MasterReference <MstrRef> [0..1] Text 3850
   PlaceOfTrade <PlcOfTrad> [0..1] ± 3850
   OrderDateTime <OrdrDtTm> [0..1] DateTime 3851
   ReceivedDateTime <RcvdDtTm> [0..1] DateTime 3851
   DealReference <DealRef> [1..1] Text 3851
   OrderReference <OrdrRef> [1..1] Text 3851
   ClientReference <ClntRef> [0..1] Text 3851
   NonceIdentification <NonceId> [0..1] Text 3851
   InvestmentAccountDetails <InvstmtAcctDtls> [0..1]  C25 3852
     AccountIdentification <AcctId> [1..1] Text 3852
     AccountName <AcctNm> [0..1] Text 3852
     AccountDesignation <AcctDsgnt> [0..1] Text 3852
     OwnerIdentification <OwnrId> [0..*] ± 3853
     AccountServicer <AcctSvcr> [0..1] ± 3853
     OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 3853
     SubAccountDetails <SubAcctDtls> [0..1] ± 3853
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3854
   RelatedPartyDetails <RltdPtyDtls> [0..10] ± C24 3854
   CancellationRight <CxlRght> [0..1] ± 3855
   RequestedFutureTradeDate <ReqdFutrTradDt> [0..1] Date 3855
   SettlementAmount <SttlmAmt> [0..1] Amount C2, C8 3855
   CashSettlementDate <CshSttlmDt> [0..1] Date 3855
   SettlementMethod <SttlmMtd> [0..1] CodeSet 3856
   AdditionalAmount <AddtlAmt> [0..1] ± 3856
   BestExecution <BestExctn> [0..1] CodeSet 3856
   RedemptionLegDetails <RedLegDtls> [1..*]  C28,
C30
3856
     LegIdentification <LegId> [0..1] Text 3863
     LegExecutionIdentification <LegExctnId> [0..1] Text 3864
     FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C18 3864
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3829 May 2026
```

## File page 3830

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Identification <Id> [1..1]  3866
{Or         ISIN <ISIN> [1..1] IdentifierSet 3866
Or         SEDOL <SEDOL> [1..1] IdentifierSet 3867
Or         CUSIP <CUSIP> [1..1] IdentifierSet 3867
Or         RIC <RIC> [1..1] IdentifierSet 3867
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 3867
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 3867
Or         CTA <CTA> [1..1] IdentifierSet 3867
Or         QUICK <QUICK> [1..1] IdentifierSet 3867
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 3868
Or         Dutch <Dtch> [1..1] IdentifierSet 3868
Or         Valoren <Vlrn> [1..1] IdentifierSet 3868
Or         Sicovam <SCVM> [1..1] IdentifierSet 3868
Or         Belgian <Belgn> [1..1] IdentifierSet 3868
Or         Common <Cmon> [1..1] IdentifierSet 3868
Or         DTI <DTI> [1..1] IdentifierSet 3868
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  3868
           Identification <Id> [1..1] Text 3869
           IdentificationSource <IdSrc> [1..1] ± 3869
       Name <Nm> [0..1] Text 3869
       ShortName <ShrtNm> [0..1] Text 3869
       SupplementaryIdentification <SplmtryId> [0..1] Text 3869
       ClassType <ClssTp> [0..1] Text 3869
       SecuritiesForm <SctiesForm> [0..1] CodeSet 3870
       DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 3870
       ProductGroup <PdctGrp> [0..1] Text 3870
       SeriesIdentification <SrsId> [0..1]  C34 3870
         SeriesDate <SrsDt> [0..1] ± 3871
         SeriesName <SrsNm> [0..1] Text 3871
     Units <Units> [1..1]  3871
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 3871
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3830 May 2026
```

## File page 3831

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 3871
     HoldingsRedemptionRate <HldgsRedRate> [0..1] Rate 3872
     NetAmount <NetAmt> [0..1] Amount C2, C8 3872
     GrossAmount <GrssAmt> [0..1] Amount C2, C8 3872
     InvestmentAccountDetails <InvstmtAcctDtls> [0..1]  C25 3873
       AccountIdentification <AcctId> [1..1] Text 3873
       AccountName <AcctNm> [0..1] Text 3873
       AccountDesignation <AcctDsgnt> [0..1] Text 3873
       OwnerIdentification <OwnrId> [0..*] ± 3874
       AccountServicer <AcctSvcr> [0..1] ± 3874
       OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 3874
       SubAccountDetails <SubAcctDtls> [0..1] ± 3874
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3875
     TradeDateTime <TradDtTm> [1..1] ± 3875
     PriceDetails <PricDtls> [1..1] ± 3875
     InformativePriceDetails <InftvPricDtls> [0..2] ± 3876
     CumDividendIndicator <CumDvddInd> [1..1] Indicator 3876
     InterimProfitAmount <IntrmPrftAmt> [0..1] ± 3877
     IncomePreference <IncmPref> [0..1] CodeSet 3877
     Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 3877
     RequestedSettlementCurrency <ReqdSttlmCcy> [0..1] CodeSet C2 3877
     RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C3 3878
     TransactionOverhead <TxOvrhd> [0..1]  C23,
C36
3878
       TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C2, C8 3880
       TotalFees <TtlFees> [0..1] Amount C2, C8 3881
       TotalTaxes <TtlTaxs> [0..1] Amount C2, C8 3881
       CommercialAgreementReference
<ComrclAgrmtRef>
[0..1] Text 3881
       IndividualFee <IndvFee> [0..*]  C5 3882
         Type <Tp> [1..1]  3882
{Or           Code <Cd> [1..1] CodeSet 3883
Or}           Proprietary <Prtry> [1..1] ± 3884
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3831 May 2026
```

## File page 3832

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Basis <Bsis> [0..1]  3884
{Or           Code <Cd> [1..1] CodeSet 3884
Or}           Proprietary <Prtry> [1..1] ± 3885
         StandardAmount <StdAmt> [0..1] Amount C2, C8 3885
         StandardRate <StdRate> [0..1] Rate 3885
         DiscountDetails <DscntDtls> [0..1]  C15 3886
           Amount <Amt> [0..1] Amount C2, C8 3886
           Rate <Rate> [0..1] Rate 3887
           Basis <Bsis> [0..1]  3887
{Or             Code <Cd> [1..1] CodeSet 3887
Or}             Proprietary <Prtry> [1..1] ± 3887
         AppliedAmount <ApldAmt> [0..1] Amount C2, C8 3888
         AppliedRate <ApldRate> [0..1] Rate 3888
         NonStandardSLAReference <NonStdSLARef> [0..1] Text 3888
         RecipientIdentification <RcptId> [0..1] ± 3888
         InformativeIndicator <InftvInd> [1..1] Indicator 3889
       IndividualTax <IndvTax> [0..*] ± 3889
       DigitalNetworkFee <DgtlNtwkFee> [0..2]  3889
         FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C20,
C21,
C27
3890
           ISIN <ISIN> [0..1] IdentifierSet 3892
           OtherIdentification <OthrId> [0..*]  3892
             Identification <Id> [1..1] Text 3892
             Suffix <Sfx> [0..1] Text 3892
             Type <Tp> [1..1]  3892
{Or               Code <Cd> [1..1] CodeSet 3893
Or}               Proprietary <Prtry> [1..1] Text 3894
           Description <Desc> [0..1] Text 3894
         Quantity <Qty> [1..1]  3895
{Or           Quantity <Qty> [1..1] ± C14 3895
Or}           ProprietaryQuantity <PrtryQty> [1..1]  3895
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3832 May 2026
```

## File page 3833

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Quantity <Qty> [1..1] Quantity 3896
             QuantityType <QtyTp> [1..1] Text 3896
             Issuer <Issr> [1..1] Text 3896
             SchemeName <SchmeNm> [0..1] Text 3896
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3896
     InformativeTaxDetails <InftvTaxDtls> [0..1] ± C35 3896
     SettlementAndCustodyDetails <SttlmAndCtdyDtls> [0..1]  3898
       SettlementDate <SttlmDt> [0..1] Date 3900
       SettlementPlace <SttlmPlc> [1..1]  3900
         Party <Pty> [1..1]  3901
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C4 3901
Or           ProprietaryIdentification <PrtryId> [1..1] ± 3901
Or           NameAndAddress <NmAndAdr> [1..1] ± 3902
Or}           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3902
         LEI <LEI> [0..1] IdentifierSet 3902
       SafekeepingPlace <SfkpgPlc> [0..1] ± 3902
       SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 3903
       TradeTransactionCondition <TradTxCond> [0..*] ± 3903
       SettlementTransactionCondition <SttlmTxCond> [0..*] ± 3903
       ReceivingSideDetails <RcvgSdDtls> [1..1]  C32,
C33
3904
         ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  3905
           PartyIdentification <PtyId> [1..1] ± 3905
           AccountIdentification <AcctId> [0..1] Text 3905
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3905
         ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  3906
           PartyIdentification <PtyId> [1..1] ± 3906
           AccountIdentification <AcctId> [0..1] Text 3906
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3906
         ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  3907
           PartyIdentification <PtyId> [1..1] ± 3907
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3833 May 2026
```

## File page 3834

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           AccountIdentification <AcctId> [0..1] Text 3907
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3907
         ReceivingAgentDetails <RcvgAgtDtls> [1..1]  3908
           PartyIdentification <PtyId> [1..1] ± 3908
           AccountIdentification <AcctId> [0..1] Text 3908
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3908
       DeliveringSideDetails <DlvrgSdDtls> [0..1]  C10,
C11
3909
         DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  3910
           PartyIdentification <PtyId> [1..1] ± 3910
           AccountIdentification <AcctId> [0..1] Text 3910
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3911
         DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  3911
           PartyIdentification <PtyId> [1..1] ± 3911
           AccountIdentification <AcctId> [0..1] Text 3911
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3911
         DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  3912
           PartyIdentification <PtyId> [1..1] ± 3912
           AccountIdentification <AcctId> [0..1] Text 3912
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3912
         DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  3913
           PartyIdentification <PtyId> [1..1] ± 3913
           AccountIdentification <AcctId> [0..1] Text 3913
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3913
     PhysicalDeliveryIndicator <PhysDlvryInd> [1..1] Indicator 3914
     PhysicalDeliveryDetails <PhysDlvryDtls> [0..1] ± 3914
     DigitalAssetSettlement <DgtlAsstSttlm> [0..1]  3914
       FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C20,
C21,
C27
3915
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3834 May 2026
```

## File page 3835

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         ISIN <ISIN> [0..1] IdentifierSet 3917
         OtherIdentification <OthrId> [0..*]  3917
           Identification <Id> [1..1] Text 3917
           Suffix <Sfx> [0..1] Text 3917
           Type <Tp> [1..1]  3917
{Or             Code <Cd> [1..1] CodeSet 3918
Or}             Proprietary <Prtry> [1..1] Text 3919
         Description <Desc> [0..1] Text 3919
       Quantity <Qty> [1..1]  3920
{Or         Quantity <Qty> [1..1] ± C14 3920
Or}         ProprietaryQuantity <PrtryQty> [1..1]  3920
           Quantity <Qty> [1..1] Quantity 3921
           QuantityType <QtyTp> [1..1] Text 3921
           Issuer <Issr> [1..1] Text 3921
           SchemeName <SchmeNm> [0..1] Text 3921
       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3921
     NonStandardSettlementInformation
<NonStdSttlmInf>
[0..1] Text 3921
     Equalisation <Equlstn> [0..1] ± 3921
     GatingOrHoldBackDetails <GtgOrHldBckDtls> [0..1]  3922
       Type <Tp> [1..1] CodeSet 3923
       Amount <Amt> [0..1] Amount C2, C8 3924
       ExpectedReleaseDate <XpctdRlsDt> [0..1] Date 3924
       FinancialInstrumentIdentification <FinInstrmId> [0..1]  3924
{Or         ISIN <ISIN> [1..1] IdentifierSet 3925
Or         SEDOL <SEDOL> [1..1] IdentifierSet 3925
Or         CUSIP <CUSIP> [1..1] IdentifierSet 3926
Or         RIC <RIC> [1..1] IdentifierSet 3926
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 3926
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 3926
Or         CTA <CTA> [1..1] IdentifierSet 3926
Or         QUICK <QUICK> [1..1] IdentifierSet 3926
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3835 May 2026
```

## File page 3836

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 3926
Or         Dutch <Dtch> [1..1] IdentifierSet 3927
Or         Valoren <Vlrn> [1..1] IdentifierSet 3927
Or         Sicovam <SCVM> [1..1] IdentifierSet 3927
Or         Belgian <Belgn> [1..1] IdentifierSet 3927
Or         Common <Cmon> [1..1] IdentifierSet 3927
Or         DTI <DTI> [1..1] IdentifierSet 3927
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  3927
           Identification <Id> [1..1] Text 3928
           IdentificationSource <IdSrc> [1..1] ± 3928
       FinancialInstrumentName <FinInstrmNm> [0..1] Text 3928
       RedemptionCompletion <RedCmpltn> [0..1] CodeSet 3928
       FinalConfirmation <FnlConf> [0..1] Indicator 3928
   SubscriptionLegDetails <SbcptLegDtls> [1..*]  C29,
C31
3929
     LegIdentification <LegId> [0..1] Text 3936
     LegExecutionIdentification <LegExctnId> [0..1] Text 3936
     FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C18 3936
       Identification <Id> [1..1]  3938
{Or         ISIN <ISIN> [1..1] IdentifierSet 3938
Or         SEDOL <SEDOL> [1..1] IdentifierSet 3939
Or         CUSIP <CUSIP> [1..1] IdentifierSet 3939
Or         RIC <RIC> [1..1] IdentifierSet 3939
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 3939
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 3939
Or         CTA <CTA> [1..1] IdentifierSet 3939
Or         QUICK <QUICK> [1..1] IdentifierSet 3939
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 3940
Or         Dutch <Dtch> [1..1] IdentifierSet 3940
Or         Valoren <Vlrn> [1..1] IdentifierSet 3940
Or         Sicovam <SCVM> [1..1] IdentifierSet 3940
Or         Belgian <Belgn> [1..1] IdentifierSet 3940
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3836 May 2026
```

## File page 3837

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         Common <Cmon> [1..1] IdentifierSet 3940
Or         DTI <DTI> [1..1] IdentifierSet 3940
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  3940
           Identification <Id> [1..1] Text 3941
           IdentificationSource <IdSrc> [1..1] ± 3941
       Name <Nm> [0..1] Text 3941
       ShortName <ShrtNm> [0..1] Text 3941
       SupplementaryIdentification <SplmtryId> [0..1] Text 3941
       ClassType <ClssTp> [0..1] Text 3941
       SecuritiesForm <SctiesForm> [0..1] CodeSet 3942
       DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 3942
       ProductGroup <PdctGrp> [0..1] Text 3942
       SeriesIdentification <SrsId> [0..1]  C34 3942
         SeriesDate <SrsDt> [0..1] ± 3943
         SeriesName <SrsNm> [0..1] Text 3943
     Units <Units> [1..1]  3943
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 3943
Or}       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 3943
     NetAmount <NetAmt> [0..1] Amount C2, C8 3944
     GrossAmount <GrssAmt> [0..1] Amount C2, C8 3944
     InvestmentAccountDetails <InvstmtAcctDtls> [0..1]  C25 3944
       AccountIdentification <AcctId> [1..1] Text 3945
       AccountName <AcctNm> [0..1] Text 3945
       AccountDesignation <AcctDsgnt> [0..1] Text 3945
       OwnerIdentification <OwnrId> [0..*] ± 3945
       AccountServicer <AcctSvcr> [0..1] ± 3946
       OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 3946
       SubAccountDetails <SubAcctDtls> [0..1] ± 3946
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3947
     TradeDateTime <TradDtTm> [1..1] ± 3947
     PriceDetails <PricDtls> [1..1] ± 3947
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3837 May 2026
```

