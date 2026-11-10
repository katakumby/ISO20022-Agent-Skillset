---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.16 SettlementMethod <SttlmMtd>"]
file_pages: [3856, 3857, 3858, 3859, 3860, 3861, 3862]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.16 SettlementMethod <SttlmMtd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3856 to 3862.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3856

```text
Definition: Date on which cash is available.
Datatype: "ISODate" on page 5388
55.4.5.16  SettlementMethod <SttlmMtd>
Presence: [0..1]
Definition: Method by which the transaction is settled.
Datatype: "DeliveryReceiptType2Code" on page 5294
CodeName Name Definition
FREE SeparateSettlement Settlement of the financial instrument
and cash is separate.
APMT AgainstPaymentSettlement Settlement of the financial instrument
and cash takes place in a delivery
versus payment (DVP) environment, that
is, through an International Central
Securities Depository (ICSD) or Central
Securities Depository (CSD).
55.4.5.17  AdditionalAmount <AddtlAmt>
Presence: [0..1]
Definition: Choice between additional cash in or resulting cash out.
AdditionalAmount <AddtlAmt> contains one of the following elements (see
"AdditionalAmount1Choice" on page 4774 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AdditionalCashIn <AddtlCshIn> [1..1] Amount C2, C10 4774
Or}   ResultingCashOut <RsltgCshOut> [1..1] Amount C2, C10 4775
55.4.5.18  BestExecution <BestExctn>
Presence: [0..1]
Definition: Specifies that the execution was subject to best execution rules as defined by MiFID.
Datatype: "BestExecution1Code" on page 5278
CodeName Name Definition
BTEX Best Best execution rules were followed.
55.4.5.19  RedemptionLegDetails <RedLegDtls>
Presence: [1..*]
Definition: Redemption leg of a switch order execution.
Impacted by: C28 "PhysicalDeliveryDetails1Rule", C30 "PhysicalDeliveryDetails2Rule"
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3856 May 2026
```

## File page 3857

```text
RedemptionLegDetails <RedLegDtls> contains the following SwitchRedemptionLegExecution5
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LegIdentification <LegId> [0..1] Text 3863
   LegExecutionIdentification <LegExctnId> [0..1] Text 3864
   FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C18 3864
     Identification <Id> [1..1]  3866
{Or       ISIN <ISIN> [1..1] IdentifierSet 3866
Or       SEDOL <SEDOL> [1..1] IdentifierSet 3867
Or       CUSIP <CUSIP> [1..1] IdentifierSet 3867
Or       RIC <RIC> [1..1] IdentifierSet 3867
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 3867
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 3867
Or       CTA <CTA> [1..1] IdentifierSet 3867
Or       QUICK <QUICK> [1..1] IdentifierSet 3867
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 3868
Or       Dutch <Dtch> [1..1] IdentifierSet 3868
Or       Valoren <Vlrn> [1..1] IdentifierSet 3868
Or       Sicovam <SCVM> [1..1] IdentifierSet 3868
Or       Belgian <Belgn> [1..1] IdentifierSet 3868
Or       Common <Cmon> [1..1] IdentifierSet 3868
Or       DTI <DTI> [1..1] IdentifierSet 3868
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  3868
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
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3857 May 2026
```

## File page 3858

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       SeriesDate <SrsDt> [0..1] ± 3871
       SeriesName <SrsNm> [0..1] Text 3871
   Units <Units> [1..1]  3871
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 3871
Or}     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 3871
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
     CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 3881
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3858 May 2026
```

## File page 3859

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     IndividualFee <IndvFee> [0..*]  C5 3882
       Type <Tp> [1..1]  3882
{Or         Code <Cd> [1..1] CodeSet 3883
Or}         Proprietary <Prtry> [1..1] ± 3884
       Basis <Bsis> [0..1]  3884
{Or         Code <Cd> [1..1] CodeSet 3884
Or}         Proprietary <Prtry> [1..1] ± 3885
       StandardAmount <StdAmt> [0..1] Amount C2, C8 3885
       StandardRate <StdRate> [0..1] Rate 3885
       DiscountDetails <DscntDtls> [0..1]  C15 3886
         Amount <Amt> [0..1] Amount C2, C8 3886
         Rate <Rate> [0..1] Rate 3887
         Basis <Bsis> [0..1]  3887
{Or           Code <Cd> [1..1] CodeSet 3887
Or}           Proprietary <Prtry> [1..1] ± 3887
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
{Or             Code <Cd> [1..1] CodeSet 3893
Or}             Proprietary <Prtry> [1..1] Text 3894
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3859 May 2026
```

## File page 3860

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Description <Desc> [0..1] Text 3894
       Quantity <Qty> [1..1]  3895
{Or         Quantity <Qty> [1..1] ± C14 3895
Or}         ProprietaryQuantity <PrtryQty> [1..1]  3895
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
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C4 3901
Or         ProprietaryIdentification <PrtryId> [1..1] ± 3901
Or         NameAndAddress <NmAndAdr> [1..1] ± 3902
Or}         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3902
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
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3860 May 2026
```

## File page 3861

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         AccountIdentification <AcctId> [0..1] Text 3906
         BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3906
       ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  3907
         PartyIdentification <PtyId> [1..1] ± 3907
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
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3861 May 2026
```

## File page 3862

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PhysicalDeliveryDetails <PhysDlvryDtls> [0..1] ± 3914
   DigitalAssetSettlement <DgtlAsstSttlm> [0..1]  3914
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C20,
C21,
C27
3915
       ISIN <ISIN> [0..1] IdentifierSet 3917
       OtherIdentification <OthrId> [0..*]  3917
         Identification <Id> [1..1] Text 3917
         Suffix <Sfx> [0..1] Text 3917
         Type <Tp> [1..1]  3917
{Or           Code <Cd> [1..1] CodeSet 3918
Or}           Proprietary <Prtry> [1..1] Text 3919
       Description <Desc> [0..1] Text 3919
     Quantity <Qty> [1..1]  3920
{Or       Quantity <Qty> [1..1] ± C14 3920
Or}       ProprietaryQuantity <PrtryQty> [1..1]  3920
         Quantity <Qty> [1..1] Quantity 3921
         QuantityType <QtyTp> [1..1] Text 3921
         Issuer <Issr> [1..1] Text 3921
         SchemeName <SchmeNm> [0..1] Text 3921
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3921
   NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 3921
   Equalisation <Equlstn> [0..1] ± 3921
   GatingOrHoldBackDetails <GtgOrHldBckDtls> [0..1]  3922
     Type <Tp> [1..1] CodeSet 3923
     Amount <Amt> [0..1] Amount C2, C8 3924
     ExpectedReleaseDate <XpctdRlsDt> [0..1] Date 3924
     FinancialInstrumentIdentification <FinInstrmId> [0..1]  3924
{Or       ISIN <ISIN> [1..1] IdentifierSet 3925
Or       SEDOL <SEDOL> [1..1] IdentifierSet 3925
Or       CUSIP <CUSIP> [1..1] IdentifierSet 3926
Or       RIC <RIC> [1..1] IdentifierSet 3926
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3862 May 2026
```

